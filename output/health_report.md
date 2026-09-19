# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-19 10:49:09 |
| 运行耗时 | 603.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 87584 |
| 去重后节点 | 25146 |
| TCP 可达 | 3000 |
| 真实可用 | 480 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25146 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.4 |
| tcp | 40.9 |
| probe | 214.3 |
| real_test | 246.3 |
| generate | 95.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52416 |
| vmess | 13840 |
| shadowsocks | 10527 |
| trojan | 8672 |
| hysteria2 | 1262 |
| http | 656 |
| shadowsocksr | 127 |
| socks | 67 |
| hysteria | 9 |
| tuic | 4 |
| anytls | 4 |

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
| 81.68 | shadowsocks | 236.9 | 661.9 | 22.29 | 0.0 | 10.0 | 14.47 | 18.92 | Au1rxx-base64 | 37.19.198.160 |
| 81.6 | shadowsocks | 240.6 | 653.4 | 22.21 | 0.0 | 10.0 | 14.47 | 18.92 | Au1rxx-base64 | 37.19.198.243 |
| 80.08 | shadowsocks | 219.6 | 593.4 | 22.69 | 0.0 | 10.0 | 14.47 | 18.92 | Au1rxx-base64 | 198.98.53.130 |
| 79.72 | shadowsocks | 300.2 | 836.2 | 20.83 | 0.0 | 10.0 | 14.47 | 18.92 | Au1rxx-base64 | 38.180.135.156 |
| 79.57 | vless | 239.5 | 676.6 | 22.23 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 79.141.172.154 |
| 79.3 | vless | 251.5 | 664.4 | 21.96 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.173 |
| 79.26 | vless | 252.9 | 667.9 | 21.92 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.15 |
| 78.53 | shadowsocks | 351.8 | 1014.1 | 19.64 | 0.0 | 10.0 | 14.47 | 18.92 | Au1rxx-base64 | 15.204.247.206 |
| 78.47 | hysteria2 | 300.1 | 597.2 | 20.83 | 0.0 | 10.0 | 14.06 | 18.92 | Au1rxx-base64 | 66.94.121.46 |
| 78.31 | vless | 294.0 | 734.5 | 20.97 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.212 |
| 78.3 | vless | 294.3 | 719.9 | 20.96 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.231 |
| 78.19 | vless | 299.5 | 743.4 | 20.85 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.225 |
| 78.15 | vless | 300.9 | 831.2 | 20.81 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 137.184.218.169 |
| 78.04 | vless | 305.7 | 704.4 | 20.7 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.74 |
| 77.86 | vless | 313.5 | 869.1 | 20.52 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 185.95.231.156 |
| 77.4 | vless | 333.6 | 848.2 | 20.06 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.232 |
| 77.24 | vless | 340.2 | 914.4 | 19.9 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.229 |
| 76.97 | vless | 352.1 | 897.7 | 19.63 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.184 |
| 76.84 | vless | 357.8 | 914.9 | 19.5 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.75 |
| 76.76 | vless | 361.2 | 877.7 | 19.42 | 0.0 | 10.0 | 8.42 | 18.92 | Au1rxx-base64 | 169.40.42.95 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.909 | 0.848 | 310 | 1569 | prefer |
| ermaozi | 0.745 | 0.74 | 50 | 358 | prefer |
| Surfboard-tg-mixed | 0.67 | 0.591 | 225 | 7474 | observe |
| mheidari-all | 0.512 | 0.43 | 93 | 19088 | observe |
| DeltaKronecker-all | 0.352 | 0.364 | 11 | 6421 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4251 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| ermaozi-get_subscribe | 0.27 | 1.0 | 1 | 387 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5174 | observe |
| Epodonios-all | 0.255 | None | 0 | 7699 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8837 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6006 | observe |
| barry-far-vless | 0.255 | None | 0 | 5996 | observe |
| Au1rxx-clash | 0.238 | None | 0 | 1569 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 42 |
| cn-block | ClientOSError | - | 34 |
| 204 | TimeoutError | - | 32 |
| geo | TimeoutError | - | 26 |
| cn-block | TimeoutError | - | 21 |
| speed | TimeoutError | - | 21 |
| 204 | ProxyError | - | 17 |
| speed | ClientOSError | - | 14 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
