# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-01 16:27:51 |
| 运行耗时 | 298.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 83812 |
| 去重后节点 | 24692 |
| TCP 可达 | 3000 |
| 真实可用 | 657 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24692 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.4 |
| tcp | 40.4 |
| probe | 89.4 |
| real_test | 125.8 |
| generate | 35.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52365 |
| vmess | 11789 |
| shadowsocks | 10254 |
| trojan | 7631 |
| hysteria2 | 1392 |
| http | 145 |
| shadowsocksr | 130 |
| socks | 83 |
| hysteria | 9 |
| tuic | 9 |
| anytls | 5 |

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
| 82.12 | vless | 244.6 | 653.0 | 22.12 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 204.48.20.223 |
| 81.72 | vless | 261.8 | 656.5 | 21.72 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 172.105.104.54 |
| 81.63 | vless | 265.6 | 645.8 | 21.63 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.202 |
| 81.61 | vless | 266.6 | 641.7 | 21.61 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 195.211.99.45 |
| 81.29 | vless | 272.6 | 636.4 | 21.47 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 195.211.99.49 |
| 81.18 | vless | 285.2 | 694.6 | 21.18 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 2.24.124.64 |
| 81.14 | vless | 286.8 | 701.8 | 21.14 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.89 |
| 80.91 | vless | 296.8 | 784.1 | 20.91 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.225 |
| 80.4 | shadowsocks | 232.9 | 639.5 | 22.39 | 0.0 | 10.0 | 13.65 | 18.36 | Au1rxx-base64 | 37.19.198.243 |
| 80.18 | vless | 328.4 | 879.0 | 20.18 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 167.17.69.171 |
| 80.05 | vless | 333.9 | 902.9 | 20.05 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.173 |
| 79.98 | vless | 336.9 | 921.8 | 19.98 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 185.95.231.156 |
| 79.97 | vless | 288.4 | 638.3 | 21.1 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.232 |
| 79.63 | vless | 352.1 | 819.2 | 19.63 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.223 |
| 79.62 | vless | 352.4 | 825.2 | 19.62 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.212 |
| 79.54 | vless | 356.0 | 841.6 | 19.54 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.74 |
| 79.37 | vless | 311.1 | 779.7 | 20.58 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 66.70.179.198 |
| 79.33 | vless | 365.0 | 928.4 | 19.33 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 169.40.42.182 |
| 79.1 | shadowsocks | 232.9 | 639.8 | 22.39 | 0.0 | 10.0 | 13.65 | 17.06 | mheidari-all | 37.19.198.236 |
| 78.84 | vless | 338.8 | 954.3 | 19.94 | 0.0 | 10.0 | 11.64 | 18.36 | Au1rxx-base64 | 45.138.100.226 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.984 | 0.91 | 144 | 17557 | prefer |
| Au1rxx-base64 | 0.98 | 0.912 | 398 | 1760 | prefer |
| zhangkai | 0.875 | 0.905 | 21 | 144 | prefer |
| Surfboard-tg-mixed | 0.835 | 0.758 | 186 | 6964 | prefer |
| DeltaKronecker-all | 0.3 | 0.4 | 5 | 7294 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4708 | observe |
| Epodonios-all | 0.255 | None | 0 | 7367 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7657 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5838 | observe |
| barry-far-vless | 0.255 | None | 0 | 6013 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4013 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1760 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 19 |
| cn-block | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyError | - | 11 |
| 204 | ProxyConnectionError | - | 10 |
| geo | ClientOSError | - | 9 |
| speed | ClientOSError | - | 6 |
| speed | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
