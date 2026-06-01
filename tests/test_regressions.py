import asyncio
import base64
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.generator import node_to_clash, node_to_url, write_outputs
from core.geo import _is_public_ip, geo_flag_map
from core.parser import Node, parse_content
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

    def test_min_latency_can_be_disabled(self):
        with tempfile.NamedTemporaryFile() as f:
            tester = SingBoxTester(sb_path=f.name, min_latency_ms=0)
        self.assertEqual(tester.min_latency_ms, 0)


if __name__ == "__main__":
    unittest.main()
