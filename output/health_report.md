# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-24 11:37:41 |
| 运行耗时 | 620.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 96310 |
| 去重后节点 | 26222 |
| TCP 可达 | 3000 |
| 真实可用 | 380 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26222 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.4 |
| tcp | 42.9 |
| probe | 306.1 |
| real_test | 171.7 |
| generate | 91.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58606 |
| vmess | 14916 |
| shadowsocks | 11191 |
| trojan | 9059 |
| hysteria2 | 1611 |
| http | 622 |
| shadowsocksr | 168 |
| socks | 86 |
| anytls | 24 |
| hysteria | 19 |
| tuic | 8 |

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
| 80.72 | shadowsocks | 253.5 | 708.5 | 21.91 | 0.0 | 9.3 | 14.13 | 19.38 | Au1rxx-base64 | 37.19.198.160 |
| 80.7 | shadowsocks | 256.5 | 704.9 | 21.84 | 0.0 | 9.35 | 14.13 | 19.38 | Au1rxx-base64 | 37.19.198.236 |
| 80.61 | shadowsocks | 255.9 | 716.9 | 21.85 | 0.0 | 9.25 | 14.13 | 19.38 | Au1rxx-base64 | 37.19.198.244 |
| 80.5 | shadowsocks | 216.4 | 584.1 | 22.77 | 0.0 | 9.22 | 14.13 | 19.38 | Au1rxx-base64 | 198.98.53.130 |
| 80.31 | shadowsocks | 247.3 | 704.5 | 22.05 | 0.0 | 9.25 | 14.13 | 19.38 | Au1rxx-base64 | 15.204.233.41 |
| 78.9 | shadowsocks | 312.5 | 880.8 | 20.54 | 0.0 | 9.35 | 14.13 | 19.38 | Au1rxx-base64 | 15.204.246.132 |
| 78.09 | shadowsocks | 280.6 | 650.0 | 21.28 | 0.0 | 9.3 | 14.13 | 19.38 | Au1rxx-base64 | 156.146.38.170 |
| 77.83 | shadowsocks | 294.5 | 734.4 | 20.96 | 0.0 | 10.0 | 14.13 | 17.24 | Surfboard-tg-mixed | 185.156.47.97 |
| 77.8 | shadowsocks | 283.6 | 649.5 | 21.21 | 0.0 | 9.36 | 14.13 | 19.38 | Au1rxx-base64 | 156.146.38.167 |
| 77.33 | shadowsocks | 253.1 | 708.6 | 21.92 | 0.0 | 9.35 | 14.13 | 19.38 | Au1rxx-base64 | 37.19.198.243 |
| 76.99 | shadowsocks | 300.5 | 676.6 | 20.82 | 0.0 | 10.0 | 14.13 | 19.38 | Au1rxx-base64 | 23.150.248.20 |
| 76.51 | shadowsocks | 428.3 | 1195.9 | 17.86 | 0.0 | 9.14 | 14.13 | 19.38 | Au1rxx-base64 | 142.4.216.225 |
| 75.6 | shadowsocks | 369.4 | 907.2 | 19.23 | 0.0 | 9.24 | 14.13 | 19.38 | Au1rxx-base64 | 156.146.38.168 |
| 75.28 | vless | 300.8 | 691.5 | 20.82 | 0.0 | 9.2 | 5.88 | 19.38 | Au1rxx-base64 | 169.40.42.133 |
| 75.15 | vless | 306.2 | 809.1 | 20.69 | 0.0 | 9.2 | 5.88 | 19.38 | Au1rxx-base64 | 169.40.42.182 |
| 74.33 | vless | 347.7 | 907.6 | 19.73 | 0.0 | 9.34 | 5.88 | 19.38 | Au1rxx-base64 | 66.70.179.198 |
| 74.28 | vless | 322.6 | 830.5 | 20.31 | 0.0 | 9.28 | 5.88 | 19.38 | Au1rxx-base64 | 195.211.98.43 |
| 74.21 | shadowsocks | 373.7 | 895.2 | 19.13 | 0.0 | 9.11 | 14.13 | 19.38 | Au1rxx-base64 | 108.181.57.93 |
| 74.13 | shadowsocks | 516.6 | 1425.4 | 15.82 | 0.0 | 9.3 | 14.13 | 19.38 | Au1rxx-base64 | 38.180.135.156 |
| 74.05 | vless | 306.4 | 696.2 | 20.69 | 0.0 | 9.28 | 5.88 | 19.38 | Au1rxx-base64 | 198.251.78.29 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.922 | 0.848 | 99 | 7027 | prefer |
| Au1rxx-base64 | 0.916 | 0.853 | 218 | 1658 | prefer |
| ermaozi | 0.625 | 0.615 | 52 | 339 | observe |
| mheidari-all | 0.617 | 0.537 | 121 | 22399 | observe |
| ermaozi-get_subscribe | 0.49 | 0.529 | 17 | 373 | observe |
| DeltaKronecker-all | 0.401 | 0.571 | 7 | 5845 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5307 | observe |
| Epodonios-all | 0.255 | None | 0 | 7495 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8857 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5676 | observe |
| barry-far-vless | 0.255 | None | 0 | 5899 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4305 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 26 |
| 204 | TimeoutError | - | 23 |
| cn-block | ClientOSError | - | 21 |
| cn-block | TimeoutError | - | 18 |
| speed | TimeoutError | - | 16 |
| geo | TimeoutError | - | 16 |
| geo | ClientOSError | - | 9 |
| 204 | ProxyConnectionError | - | 3 |
| 204 | ClientOSError | - | 2 |
| speed | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
