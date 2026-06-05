import asyncio
import base64
import json
import sys
import tempfile
import unittest
from pathlib import Path
import os
import subprocess
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.fetcher import Source, fetch_all
from core.generator import node_to_clash, node_to_url, write_outputs
from core.geo import _is_public_ip, geo_flag_map
from core.parser import Node, parse_content
from tools.audit_sources import load_previous_audit
from tools.health_report import build_health_report
from core.tester import SingBoxTester


class RegressionTests(unittest.TestCase):
    def test_http_node_to_url_and_clash(self):
        n = Node("http", "http-test", "example.com", 8080, {"username": "u", "password": "p"})
        self.assertEqual(node_to_url(n), "http://u:p@example.com:8080#http-test")
        self.assertEqual(node_to_clash(n)["type"], "http")

    def test_write_outputs_does_not_mutate_or_duplicate_clamped_tags(self):
        n1 = Node("vless", "A" * 48 + "X", "s1.example", 443, {"uuid": "u1"})
        n2 = Node("vless", "A" * 48 + "Y", "s2.example", 443, {"uuid": "u2"})
        original = [n1.tag, n2.tag]
        with tempfile.TemporaryDirectory() as d:
            count = write_outputs([n1, n2], d, prefix="nodes", repo_path="owner/repo")
        self.assertEqual(count, 2)
        self.assertEqual([n1.tag, n2.tag], original)

    def test_parse_content_extracts_multiple_urls_per_line(self):
        nodes = parse_content("vless://id@example.com:443?type=tcp#one trojan://p@host.com:443#two")
        self.assertEqual([(n.type, n.tag) for n in nodes], [("vless", "one"), ("trojan", "two")])

    def test_parse_content_decodes_base64_after_comment(self):
        b64 = base64.b64encode(b"vless://id@example.com:443?type=tcp#one").decode()
        nodes = parse_content("# comment\n" + b64)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].type, "vless")


    def test_ssr_url_uses_standard_base64(self):
        n = Node("shadowsocksr", "备注", "example.com", 1234, {
            "password": "密码含+/",
            "method": "aes-256-cfb",
            "protocol": "origin",
            "obfs": "plain",
        })
        payload = node_to_url(n).removeprefix("ssr://")
        base64.b64decode(payload + "=" * ((4 - len(payload) % 4) % 4), validate=True)
        self.assertNotIn("-", payload)
        self.assertNotIn("_", payload)

    def test_geo_flag_map_keeps_domain_keys(self):
        nodes = [Node("vless", "domain", "localhost", 443, {"uuid": "u"})]
        flags = asyncio.run(geo_flag_map(nodes))
        self.assertIsInstance(flags, dict)
        self.assertNotIn("127.0.0.1", flags)
        self.assertFalse(_is_public_ip("127.0.0.1"))
        self.assertFalse(_is_public_ip("10.0.0.1"))



    def test_source_audit_history_accepts_new_payload_format(self):
        payload = {
            "sources": [
                {"name": "dead", "consecutive_dead": 2},
                {"name": "ok", "consecutive_dead": 0},
            ]
        }
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "source_audit.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            previous = load_previous_audit(str(path))
        self.assertEqual(previous["dead"], 2)
        self.assertEqual(previous["ok"], 0)

    def test_health_report_detects_generated_outputs(self):
        n = Node("http", "http-test", "example.com", 8080, {})
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            write_outputs([n], d, prefix="verified", repo_path="owner/repo")
            write_outputs([n], d, prefix="all", repo_path="owner/repo")
            (out / "stats.json").write_text("{}", encoding="utf-8")
            report = build_health_report(d, "verified")
        self.assertTrue(report["ok"])
        self.assertEqual(report["prefixes"]["verified"]["json_node_count"], 1)

    def test_min_latency_can_be_disabled(self):
        with tempfile.NamedTemporaryFile() as f:
            tester = SingBoxTester(sb_path=f.name, min_latency_ms=0)
        self.assertEqual(tester.min_latency_ms, 0)

    def test_singbox_config_compatible_with_1_13(self):
        """§1.6 紧急修复 — sing-box 1.11+ 移除了 inbound 上的 sniff 字段
        build_singbox_config 输出必须不含 inbound.sniff, 否则 sing-box 1.13+ 启动失败
        """
        from core.tester import build_singbox_config
        from core.parser import Node
        n = Node("vless", "t", "1.2.3.4", 443, {"uuid": "u"})
        cfg = build_singbox_config(n, 11080)
        inb = cfg["inbounds"][0]
        self.assertNotIn("sniff", inb, "inbound 不应再含 sniff (sing-box 1.13+ 已移除)")
        self.assertNotIn("domain_strategy", inb, "inbound 不应再含 domain_strategy (已移除)")

    def test_health_report_exits_2_when_verified_empty(self):
        """§1.5 — verified 0 节点时 health_report.main exit 2, 触发 CI ::error"""
        import subprocess, sys, tempfile, json
        from pathlib import Path
        from core.generator import write_outputs
        from core.parser import Node
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            # 写一个 0 节点的 verified + 1 节点 all, 模拟"真测全挂"但订阅源还活着
            write_outputs([], d, prefix="verified", repo_path="o/r")
            write_outputs([Node("http", "t", "1.2.3.4", 80, {})], d, prefix="all", repo_path="o/r")
            (out / "stats.json").write_text(json.dumps({}), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/health_report.py",
                    "--output-dir", str(out),
                    "--output", str(out / "health_report.json"),
                ],
                capture_output=True, text=True,
                cwd=str(Path(__file__).resolve().parent.parent),
            )
        self.assertEqual(result.returncode, 2, f"expected exit 2, got {result.returncode}: {result.stderr}")
        self.assertIn("verified 输出为 0", result.stderr)

    def test_fetch_all_overall_timeout_returns_partial_results(self):
        """P0 — overall timeout 时返回已完成源, 不因 coroutine.done() AttributeError 二次失败"""
        async def fake_fetch_source(session, src, timeout):
            if src.name == "slow":
                await asyncio.sleep(1)
            return type("Result", (), {"source": src})()

        sources = [
            Source(url="https://fast.example", name="fast"),
            Source(url="https://slow.example", name="slow"),
        ]
        with patch("core.fetcher.fetch_source", fake_fetch_source):
            results = asyncio.run(fetch_all(sources, concurrency=2, timeout=1, overall_timeout=0.05))
        self.assertEqual([r.source.name for r in results], ["fast"])

    # ===== v2.1 新增回归测试 =====

    def test_main_version_constant(self):
        """§4.5 — main.__version__ 存在且是字符串"""
        import main as m
        self.assertIsInstance(m.__version__, str)
        self.assertGreaterEqual(m.__version__.count("."), 2)

    def test_write_outputs_branch_passed_through(self):
        """§1.5 — write_outputs 把 branch 写进 sub_url, 不写死 main"""
        n = Node("vless", "test", "example.com", 443, {"uuid": "u1"})
        with tempfile.TemporaryDirectory() as d:
            write_outputs([n], d, prefix="n", repo_path="o/r", branch="dev")
            conv = (Path(d) / "n.converter.md").read_text(encoding="utf-8")
            self.assertIn("@dev/", conv)
            self.assertNotIn("@main/", conv)

    def test_max_per_server_default_zero_means_unlimited(self):
        """§2.2 — 默认 max_per_server=0 不再误杀同 server 多节点
        9 个同 server 不同 type: (server,type) 强去重后剩 3 个, 不再额外限流
        对比
        """
        from main import quality_prefilter
        nodes = [
            Node("vless", f"n{i}", "1.1.1.1", 443, {"uuid": f"u{i}"}) for i in range(3)
        ] + [
            Node("trojan", f"t{i}", "1.1.1.1", 443, {"password": f"p{i}"}) for i in range(3)
        ] + [
            Node("vmess", f"v{i}", "1.1.1.1", 443, {"uuid": f"u{i}"}) for i in range(3)
        ]
        out = quality_prefilter(nodes, max_per_server=0)
        self.assertEqual(len(out), 3)  # 3 type x 3 节点, 不限数量全部保留

    def test_max_per_server_two_keeps_top_two_per_type(self):
        """§2.2 — max_per_server=2 时同 server 保留 2 个
        5 vless + 5 trojan 同 server, (server,type) 去重后剩 2 个, max_per_server=2 留 2
        """
        from main import quality_prefilter
        nodes = [
            Node("vless", f"n{i}", "1.1.1.1", 443, {"uuid": f"u{i}"}) for i in range(5)
        ] + [
            Node("trojan", f"t{i}", "1.1.1.1", 443, {"password": f"p{i}"}) for i in range(5)
        ]
        out = quality_prefilter(nodes, max_per_server=2)
        self.assertEqual(len(out), 2)

    def test_quality_prefilter_dedupes_same_server_type(self):
        """§2.2 — 同一个 (server, type) 组合已经在 quality_prefilter 内去重
        所以 max_per_server=5 也不应该出现 5 个 vless@1.1.1.1
        """
        from main import quality_prefilter
        nodes = [
            Node("vless", f"n{i}", "1.1.1.1", 443, {"uuid": f"u{i}"}) for i in range(5)
        ]
        out = quality_prefilter(nodes, max_per_server=10)
        self.assertEqual(len(out), 1)  # 5 个同 (server, type) 被去重成 1

    def test_test_targets_include_cn_block(self):
        """§1.2 — TEST_TARGETS 必须包含 baidu 和 ipinfo, 不再只用 1.1.1.1/cdn-cgi/trace"""
        from core.tester import TEST_TARGETS
        kinds = {kind for _, kind in TEST_TARGETS}
        self.assertIn("cn-block", kinds, "必须包含 cn-block (baidu) 检测")
        self.assertIn("geo", kinds, "必须包含 geo (ipinfo) 检测")
        # 旧的对 CF 永通过的 1.1.1.1/cdn-cgi/trace 必须移除
        for url, _ in TEST_TARGETS:
            self.assertNotIn("1.1.1.1/cdn-cgi/trace", url, "1.1.1.1/cdn-cgi/trace 对 CF 反代永通过, 已废弃")

    def test_audit_disable_dead_sources_atomic_write(self):
        """§2.4 — disable_dead_sources 用临时文件 + rename 原子写, 不直接覆写 sources.yaml"""
        from tools.audit_sources import disable_dead_sources
        with tempfile.TemporaryDirectory() as d:
            src = Path(d) / "sources.yaml"
            src.write_text("sources:\n  - url: https://a.com\n    enabled: true\n  - url: https://b.com\n    enabled: true\n", encoding="utf-8")
            n = disable_dead_sources(str(src), {"https://a.com"})
            self.assertEqual(n, 1)
            # 读回检查
            import yaml
            data = yaml.safe_load(src.read_text(encoding="utf-8"))
            enabled_map = {s["url"]: s["enabled"] for s in data["sources"]}
            self.assertFalse(enabled_map["https://a.com"])
            self.assertTrue(enabled_map["https://b.com"])
            # 临时文件应该被清理
            self.assertFalse((Path(d) / "sources.yaml.tmp").exists())

    def test_health_report_alerts_field(self):
        """§4.1 — health_report.json 含 alerts 字段, pass_rate < 0.1 触发报警"""
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            n = Node("vless", "n", "1.2.3.4", 443, {"uuid": "u"})
            write_outputs([n], d, prefix="verified", repo_path="o/r")
            write_outputs([n], d, prefix="all", repo_path="o/r")
            (out / "stats.json").write_text('{"protocol_pass_rate": {"vless": {"pass": 0, "fail": 100}}}', encoding="utf-8")
            report = build_health_report(d, "verified")
        self.assertIn("alerts", report)
        # alerts.low_pass_protocols 是 [{protocol, pass_rate}, ...] 格式
        flagged = [p["protocol"] for p in report["alerts"]["low_pass_protocols"]]
        self.assertIn("vless", flagged)

    def test_health_report_status_warning_when_alerts_exist(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            n = Node("vless", "n", "1.2.3.4", 443, {"uuid": "u"})
            write_outputs([n], d, prefix="verified", repo_path="o/r")
            write_outputs([n], d, prefix="all", repo_path="o/r")
            (out / "stats.json").write_text('{"real_test_errors": {"204": 1}}', encoding="utf-8")
            report = build_health_report(d, "verified")
        self.assertTrue(report["ok"])
        self.assertEqual(report["status"], "warning")

    def test_health_report_status_critical_when_verified_empty(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            write_outputs([], d, prefix="verified", repo_path="o/r")
            write_outputs([Node("http", "t", "1.2.3.4", 80, {})], d, prefix="all", repo_path="o/r")
            (out / "stats.json").write_text("{}", encoding="utf-8")
            report = build_health_report(d, "verified")
        self.assertTrue(report["ok"])
        self.assertEqual(report["status"], "critical")

    def test_write_outputs_singbox_inbound_compatible_with_1_13(self):
        n = Node("vless", "test", "example.com", 443, {"uuid": "u1"})
        with tempfile.TemporaryDirectory() as d:
            write_outputs([n], d, prefix="n", repo_path="o/r")
            cfg = json.loads((Path(d) / "n.json").read_text(encoding="utf-8"))
        inb = cfg["inbounds"][0]
        self.assertNotIn("sniff", inb)
        self.assertNotIn("sniff_override_destination", inb)

    def test_tcp_check_batch_uses_worker_queue_and_sorts_results(self):
        import main as m

        class FakeWriter:
            def close(self):
                pass

            async def wait_closed(self):
                pass

        async def fake_open_connection(host, port):
            await asyncio.sleep(0.02 if host == "slow.example" else 0.01)
            if host == "bad.example":
                raise OSError("connection failed")
            return object(), FakeWriter()

        nodes = [
            Node("http", "slow", "slow.example", 80, {}),
            Node("http", "bad", "bad.example", 80, {}),
            Node("http", "fast", "fast.example", 80, {}),
        ]
        with patch("asyncio.open_connection", fake_open_connection):
            results = asyncio.run(m.tcp_check_batch(nodes, concurrency=2, timeout=1))
        self.assertEqual([n.tag for n, _ in results], ["fast", "slow"])

    def test_main_stats_include_stage_durations_and_error_details(self):
        import main as m

        class Args:
            sources = "config/sources.yaml"
            output_dir = ""
            repo = "o/r"
            branch = "main"
            fetch_concurrency = 1
            fetch_timeout = 1
            quality_filter = False
            max_per_server = 0
            tcp_check = False
            tcp_concurrency = 1
            tcp_timeout = 0.1
            test_limit = 0
            real_test = False
            top_n = 10
            global_output = False
            min_retain_ratio = 0.7
            all_output_mode = "full"

        source = Source(url="https://example.com/sub.txt", name="mock-source")
        node = Node("http", "mock", "127.0.0.1", 8080, {})
        fetch_result = type("FetchResult", (), {
            "source": source,
            "success": True,
            "nodes": [node],
        })()

        async def fake_fetch_all(sources, concurrency=30, timeout=15):
            return [fetch_result]

        async def fake_geo_flag_map(nodes):
            return {}

        with tempfile.TemporaryDirectory() as d:
            args = Args()
            args.output_dir = d
            with patch("main.load_sources", return_value=[source]), \
                 patch("main.fetch_all", fake_fetch_all), \
                 patch("main.geo_flag_map", fake_geo_flag_map):
                asyncio.run(m.run(args))
            stats = json.loads((Path(d) / "stats.json").read_text(encoding="utf-8"))
        self.assertIn("stage_durations", stats)
        self.assertIn("fetch", stats["stage_durations"])
        self.assertIn("geo", stats["stage_durations"])
        self.assertIn("tcp", stats["stage_durations"])
        self.assertIn("real_test", stats["stage_durations"])
        self.assertIn("generate", stats["stage_durations"])
        self.assertIn("real_test_error_details", stats)

    def test_global_output_adds_cn_block_retry_successes(self):
        import main as m

        class Args:
            sources = "config/sources.yaml"
            output_dir = ""
            repo = "o/r"
            branch = "main"
            fetch_concurrency = 1
            fetch_timeout = 1
            quality_filter = False
            max_per_server = 0
            tcp_check = False
            tcp_concurrency = 1
            tcp_timeout = 0.1
            test_limit = 0
            real_test = True
            top_n = 10
            global_output = True
            min_retain_ratio = 0.7
            all_output_mode = "light"
            singbox = __file__
            test_concurrency = 1
            startup_wait = 0
            test_timeout = 0.1
            min_latency = 0

        source = Source(url="https://example.com/sub.txt", name="mock-source")
        strict_node = Node("http", "strict", "127.0.0.1", 8080, {})
        global_node = Node("http", "global", "127.0.0.2", 8080, {})
        fetch_result = type("FetchResult", (), {
            "source": source,
            "success": True,
            "nodes": [strict_node, global_node],
        })()

        async def fake_fetch_all(sources, concurrency=30, timeout=15):
            return [fetch_result]

        async def fake_geo_flag_map(nodes):
            return {}

        class FakeTester:
            def __init__(self, *args, skip_target_kinds=None, **kwargs):
                self.skip_target_kinds = set(skip_target_kinds or [])

            async def test_all(self, nodes):
                from core.tester import TestResult
                if "cn-block" in self.skip_target_kinds:
                    return [TestResult(node=nodes[0], success=True, latency_ms=80, jitter_ms=0)]
                return [
                    TestResult(node=strict_node, success=True, latency_ms=50, jitter_ms=0),
                    TestResult(node=global_node, success=False, error="cn-block:status=403"),
                ]

        with tempfile.TemporaryDirectory() as d:
            args = Args()
            args.output_dir = d
            with patch("main.load_sources", return_value=[source]), \
                 patch("main.fetch_all", fake_fetch_all), \
                 patch("main.geo_flag_map", fake_geo_flag_map), \
                 patch("core.tester.SingBoxTester", FakeTester):
                asyncio.run(m.run(args))
            stats = json.loads((Path(d) / "stats.json").read_text(encoding="utf-8"))
            global_urls = (Path(d) / "global.urls").read_text(encoding="utf-8")
            verified_urls = (Path(d) / "verified.urls").read_text(encoding="utf-8")
        self.assertEqual(stats["nodes_verified_output"], 1)
        self.assertEqual(stats["nodes_global_output"], 2)
        self.assertEqual(stats["nodes_global_extra_from_cn_block"], 1)
        self.assertEqual(stats["global_skip_target_kinds"], ["cn-block"])
        self.assertIn("strict", global_urls)
        self.assertIn("global", global_urls)
        self.assertNotIn("global", verified_urls)

    def test_singbox_tester_records_skipped_target_kinds(self):
        with tempfile.NamedTemporaryFile() as f:
            tester = SingBoxTester(sb_path=f.name, skip_target_kinds={"cn-block"})
        self.assertEqual(tester.skip_target_kinds, {"cn-block"})

    def test_sample_for_real_test_balances_protocols_and_fills_by_latency(self):
        import main as m
        nodes = [
            Node("vless", "v1", "1.1.1.1", 443, {"uuid": "1"}),
            Node("vless", "v2", "1.1.1.2", 443, {"uuid": "2"}),
            Node("trojan", "t1", "1.1.1.3", 443, {"password": "p1"}),
            Node("vmess", "m1", "1.1.1.4", 443, {"uuid": "3"}),
        ]
        lat = {nodes[0].fingerprint(): 40, nodes[1].fingerprint(): 10, nodes[2].fingerprint(): 20, nodes[3].fingerprint(): 30}
        sampled = m.sample_for_real_test(nodes, lat, 3)
        self.assertEqual(len(sampled), 3)
        self.assertEqual({n.type for n in sampled}, {"vless", "trojan", "vmess"})
        self.assertIn("v2", [n.tag for n in sampled])

    def test_load_historical_pass_rates_uses_smoothed_rates(self):
        import main as m
        with tempfile.TemporaryDirectory() as d:
            Path(d, "stats.json").write_text(json.dumps({
                "protocol_pass_rate": {"trojan": {"pass": 8, "fail": 2}},
                "source_pass_rate": {"good": {"pass": 9, "fail": 1}},
            }), encoding="utf-8")
            protocol_rates, source_rates = m.load_historical_pass_rates(d)
        self.assertAlmostEqual(protocol_rates["trojan"], 9 / 12)
        self.assertAlmostEqual(source_rates["good"], 10 / 12)

    def test_weighted_sample_prefers_historical_success_after_exploration_quota(self):
        import main as m
        good = Node("trojan", "good", "1.1.1.1", 443, {"password": "p"})
        bad_fast = Node("vmess", "bad-fast", "1.1.1.2", 443, {"uuid": "u"})
        bad_slow = Node("vmess", "bad-slow", "1.1.1.3", 443, {"uuid": "u2"})
        nodes = [bad_fast, bad_slow, good]
        lat = {
            good.fingerprint(): 100,
            bad_fast.fingerprint(): 1,
            bad_slow.fingerprint(): 2,
        }
        source_map = {
            good.fingerprint(): "good-source",
            bad_fast.fingerprint(): "bad-source",
            bad_slow.fingerprint(): "bad-source",
        }
        sampled = m.sample_for_real_test_weighted(
            nodes, lat, 2, source_map,
            protocol_rates={"trojan": 0.8, "vmess": 0.1},
            source_rates={"good-source": 0.9, "bad-source": 0.1},
        )
        self.assertIn("good", [n.tag for n in sampled])

    def test_update_trend_history_keeps_recent_runs(self):
        import main as m
        with tempfile.TemporaryDirectory() as d:
            for i in range(32):
                payload = m.update_trend_history(d, {
                    "timestamp": f"run-{i}",
                    "duration_sec": i,
                    "nodes_tcp_ok": 100 + i,
                    "nodes_real_ok": 10 + i,
                    "nodes_verified_output": i,
                    "nodes_global_output": i + 1,
                    "nodes_global_extra_from_cn_block": 1,
                    "real_test_errors": {"204": i},
                    "output_guard": {"verified": {"preserved": False}},
                })
            path = Path(d) / "trend_history.json"
            saved = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(payload["updated_at"], "run-31")
        self.assertEqual(len(saved["runs"]), 30)
        self.assertEqual(saved["runs"][0]["timestamp"], "run-2")
        self.assertEqual(saved["runs"][-1]["nodes_global_output"], 32)

    def test_output_shrink_guard_helpers(self):
        import main as m
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "verified.urls"
            path.write_text("a\n\n b \n", encoding="utf-8")
            self.assertEqual(m.count_existing_urls(d, "verified"), 2)
        self.assertTrue(m.should_preserve_previous_output(60, 100, 0.7))
        self.assertFalse(m.should_preserve_previous_output(70, 100, 0.7))
        self.assertFalse(m.should_preserve_previous_output(1, 0, 0.7))
        self.assertFalse(m.should_preserve_previous_output(1, 100, 0))

    def test_write_outputs_light_mode_skips_large_json_yaml(self):
        n = Node("http", "http-test", "example.com", 8080, {})
        with tempfile.TemporaryDirectory() as d:
            count = write_outputs([n], d, prefix="all", repo_path="o/r", mode="light")
            out = Path(d)
            self.assertEqual(count, 1)
            self.assertTrue((out / "all.urls").exists())
            self.assertTrue((out / "all.txt").exists())
            self.assertTrue((out / "all.converter.md").exists())
            self.assertFalse((out / "all.json").exists())
            self.assertFalse((out / "all.yaml").exists())

    def test_protocol_fixture_corpus_parse_and_generate(self):
        fixture_dir = Path(__file__).parent / "fixtures" / "protocols"
        for path in sorted(fixture_dir.iterdir()):
            content = path.read_text(encoding="utf-8")
            nodes = parse_content(content)
            self.assertGreater(len(nodes), 0, path.name)
            with tempfile.TemporaryDirectory() as d:
                count = write_outputs(nodes, d, prefix="fixture", repo_path="o/r")
                self.assertGreater(count, 0, path.name)
                self.assertTrue((Path(d) / "fixture.json").exists(), path.name)
                self.assertTrue((Path(d) / "fixture.yaml").exists(), path.name)

    def test_prepare_artifact_output_copies_expected_files(self):
        import tools.prepare_artifact_output as prep
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            output = root / "output"
            dest = root / "artifact"
            output.mkdir()
            for name in ("verified.txt", "verified.yaml", "global.txt", "global.yaml", "all.txt", "all.json", "stats.json", "health_report.json"):
                (output / name).write_text(name, encoding="utf-8")
            old_argv = sys.argv
            try:
                sys.argv = ["prepare_artifact_output.py", "--output-dir", str(output), "--dest-dir", str(dest)]
                prep.main()
            finally:
                sys.argv = old_argv
            self.assertTrue((dest / "verified.txt").exists())
            self.assertTrue((dest / "verified.yaml").exists())
            self.assertTrue((dest / "global.txt").exists())
            self.assertTrue((dest / "global.yaml").exists())
            self.assertTrue((dest / "all.txt").exists())
            self.assertFalse((dest / "all.json").exists())
            self.assertTrue((dest / "MANIFEST.txt").exists())


if __name__ == "__main__":
    unittest.main()
