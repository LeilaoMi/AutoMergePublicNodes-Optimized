# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-28 10:52:20 |
| 运行耗时 | 228.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 76338 |
| 去重后节点 | 21064 |
| TCP 可达 | 3000 |
| 真实可用 | 435 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21064 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.4 |
| tcp | 34.8 |
| probe | 50.0 |
| real_test | 98.8 |
| generate | 37.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46278 |
| vmess | 10643 |
| shadowsocks | 10537 |
| trojan | 6906 |
| hysteria2 | 1598 |
| http | 173 |
| shadowsocksr | 133 |
| socks | 57 |
| hysteria | 10 |
| tuic | 3 |

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
| 83.4 | vless | 233.0 | 629.4 | 22.38 | 0.0 | 9.32 | 11.7 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 83.38 | hysteria2 | 267.8 | 745.9 | 21.58 | 0.0 | 9.57 | 13.33 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 83.12 | vless | 243.9 | 642.2 | 22.13 | 0.0 | 9.29 | 11.7 | 20.0 | Au1rxx-base64 | 167.17.69.171 |
| 82.7 | vless | 275.4 | 770.0 | 21.4 | 0.0 | 9.6 | 11.7 | 20.0 | Au1rxx-base64 | 47.89.186.170 |
| 82.64 | vless | 252.8 | 635.8 | 21.93 | 0.0 | 9.01 | 11.7 | 20.0 | Au1rxx-base64 | ql6k-m23nix.logicara.top |
| 82.02 | vless | 264.7 | 646.8 | 21.65 | 0.0 | 9.27 | 11.7 | 20.0 | Au1rxx-base64 | 195.211.99.49 |
| 81.96 | vless | 295.6 | 786.7 | 20.93 | 0.0 | 9.33 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.173 |
| 81.77 | vless | 302.4 | 839.8 | 20.78 | 0.0 | 9.29 | 11.7 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 81.75 | vless | 256.8 | 597.0 | 21.83 | 0.0 | 9.22 | 11.7 | 20.0 | Au1rxx-base64 | 216.227.161.95 |
| 81.54 | vless | 314.1 | 857.9 | 20.51 | 0.0 | 9.33 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.232 |
| 81.5 | vless | 314.1 | 873.8 | 20.51 | 0.0 | 9.29 | 11.7 | 20.0 | Au1rxx-base64 | 79.127.243.217 |
| 81.3 | shadowsocks | 226.3 | 625.3 | 22.54 | 0.0 | 9.37 | 13.39 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.29 | vless | 324.2 | 816.8 | 20.27 | 0.0 | 9.32 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.104 |
| 81.27 | vless | 325.9 | 877.3 | 20.23 | 0.0 | 9.34 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.16 |
| 81.17 | vless | 333.6 | 847.4 | 20.06 | 0.0 | 9.41 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.223 |
| 80.93 | vless | 338.3 | 855.1 | 19.95 | 0.0 | 9.28 | 11.7 | 20.0 | Au1rxx-base64 | 216.152.147.28 |
| 80.78 | vless | 345.1 | 822.5 | 19.79 | 0.0 | 9.29 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.235 |
| 80.67 | vless | 352.5 | 883.0 | 19.62 | 0.0 | 9.35 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.52 |
| 80.51 | vless | 359.0 | 914.4 | 19.47 | 0.0 | 9.34 | 11.7 | 20.0 | Au1rxx-base64 | 66.70.179.198 |
| 80.48 | vless | 289.5 | 718.2 | 21.08 | 0.0 | 9.29 | 11.7 | 20.0 | Au1rxx-base64 | 169.40.42.184 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.966 | 0.896 | 307 | 1823 | prefer |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| Surfboard-tg-mixed | 0.839 | 0.763 | 114 | 6512 | prefer |
| mheidari-all | 0.79 | 0.717 | 60 | 14456 | prefer |
| DeltaKronecker-all | 0.37 | 0.312 | 16 | 4318 | observe |
| tg-oneclickvpnkeys | 0.362 | 1.0 | 3 | 101 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4783 | observe |
| Epodonios-all | 0.255 | None | 0 | 6791 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3990 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7458 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5314 | observe |
| barry-far-vless | 0.255 | None | 0 | 5416 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4061 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1823 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 28 |
| cn-block | TimeoutError | - | 14 |
| geo | ClientOSError | - | 12 |
| 204 | ProxyError | - | 11 |
| speed | TimeoutError | - | 7 |
| geo | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| speed | ClientOSError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
