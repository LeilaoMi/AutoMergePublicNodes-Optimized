import asyncio
import base64
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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


if __name__ == "__main__":
    unittest.main()
