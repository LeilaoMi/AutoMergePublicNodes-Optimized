# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-13 00:46:27 |
| 运行耗时 | 1245.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 100924 |
| 去重后节点 | 27887 |
| TCP 可达 | 3000 |
| 真实可用 | 486 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27887 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.6 |
| tcp | 47.8 |
| probe | 414.4 |
| real_test | 703.0 |
| generate | 73.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59339 |
| vmess | 15946 |
| shadowsocks | 12150 |
| trojan | 11093 |
| hysteria2 | 1450 |
| http | 655 |
| shadowsocksr | 176 |
| socks | 66 |
| anytls | 26 |
| hysteria | 17 |
| tuic | 6 |

## 评分权重

| 因子 | 权重 |
| --- | --- |
| latency | 25.0 |
| jitter | 15.0 |
| tcp | 10.0 |
| speed | 10.0 |
| fingerprint_resistance | 5.0 |
| protocol_history | 15.0 |
| source_history | 20.0 |

## Top 节点评分

| 评分 | 协议 | 延迟(ms) | 抖动(ms) | 延迟分 | 抖动分 | TCP分 | 协议历史分 | 来源历史分 | 来源 | 服务器 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 83.06 | vless | 226.5 | 548.8 | 22.53 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 154.29.145.196 |
| 83.02 | hysteria2 | 245.7 | 582.5 | 22.09 | 0.0 | 9.66 | 12.86 | 19.6 | Au1rxx-base64 | 66.94.121.46 |
| 82.69 | vless | 242.7 | 513.7 | 22.16 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 154.12.38.159 |
| 82.37 | vless | 256.7 | 492.3 | 21.84 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 195.123.240.65 |
| 81.47 | shadowsocks | 232.4 | 530.1 | 22.4 | 0.0 | 10.0 | 13.47 | 19.6 | Au1rxx-base64 | 173.244.56.9 |
| 80.83 | shadowsocks | 232.4 | 526.9 | 22.4 | 0.0 | 10.0 | 13.47 | 19.6 | Au1rxx-base64 | 173.244.56.6 |
| 80.8 | shadowsocks | 261.4 | 639.4 | 21.73 | 0.0 | 10.0 | 13.47 | 19.6 | Au1rxx-base64 | 156.146.38.170 |
| 80.78 | shadowsocks | 262.0 | 639.4 | 21.71 | 0.0 | 10.0 | 13.47 | 19.6 | Au1rxx-base64 | 156.146.38.169 |
| 80.29 | vless | 297.8 | 598.6 | 20.88 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 95.111.212.241 |
| 79.72 | vless | 322.3 | 770.0 | 20.32 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 23.95.222.127 |
| 79.14 | hysteria2 | 321.4 | 743.3 | 20.34 | 0.0 | 10.0 | 12.86 | 19.6 | Au1rxx-base64 | 129.213.91.185 |
| 79.13 | vless | 244.1 | 502.4 | 22.13 | 0.0 | 10.0 | 10.93 | 19.22 | mheidari-all | 47.251.108.158 |
| 78.62 | vless | 237.4 | 516.0 | 22.28 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 154.12.38.202 |
| 77.9 | shadowsocks | 348.7 | 611.5 | 19.71 | 0.0 | 10.0 | 13.47 | 19.22 | mheidari-all | 103.11.76.248 |
| 77.67 | vless | 285.7 | 676.6 | 21.16 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 147.45.60.160 |
| 77.13 | shadowsocks | 292.2 | 627.5 | 21.01 | 0.0 | 10.0 | 13.47 | 19.6 | Au1rxx-base64 | 149.22.95.183 |
| 77.08 | shadowsocks | 258.8 | 625.6 | 21.79 | 0.0 | 10.0 | 13.47 | 19.6 | Au1rxx-base64 | 156.146.38.167 |
| 76.98 | vless | 297.6 | 578.9 | 20.89 | 0.0 | 10.0 | 10.93 | 19.6 | Au1rxx-base64 | 154.29.149.140 |
| 76.39 | shadowsocks | 219.5 | 514.0 | 22.7 | 0.0 | 10.0 | 13.47 | 19.22 | mheidari-all | 216.105.168.18 |
| 75.21 | vless | 336.4 | 340.3 | 19.99 | 2.24 | 9.9 | 10.93 | 19.6 | Au1rxx-base64 | 142.91.108.25 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.991 | 0.92 | 348 | 1847 | prefer |
| Surfboard-tg-mixed | 0.593 | 1.0 | 7 | 7208 | observe |
| ermaozi | 0.471 | 0.44 | 25 | 675 | observe |
| mheidari-all | 0.351 | 0.27 | 529 | 23897 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5028 | observe |
| Epodonios-all | 0.255 | None | 0 | 7736 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10536 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5678 | observe |
| barry-far-vless | 0.255 | None | 0 | 6023 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4314 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.249 | None | 0 | 1847 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 217 |
| speed | TimeoutError | - | 111 |
| geo | ClientOSError | - | 37 |
| speed | ClientOSError | - | 34 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 4 |
| cn-block | ProxyError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
