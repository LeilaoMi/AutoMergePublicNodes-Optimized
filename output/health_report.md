# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-29 20:49:51 |
| 运行耗时 | 276.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 79290 |
| 去重后节点 | 21340 |
| TCP 可达 | 3000 |
| 真实可用 | 659 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21340 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.4 |
| tcp | 34.4 |
| probe | 59.2 |
| real_test | 142.1 |
| generate | 33.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49800 |
| vmess | 10940 |
| shadowsocks | 10529 |
| trojan | 6094 |
| hysteria2 | 1547 |
| http | 173 |
| shadowsocksr | 133 |
| socks | 57 |
| tuic | 8 |
| hysteria | 7 |
| anytls | 2 |

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
| 84.88 | hysteria2 | 228.2 | 627.3 | 22.5 | 0.0 | 10.0 | 14.38 | 19.1 | Surfboard-tg-mixed | 159.223.157.129 |
| 84.85 | vless | 240.3 | 646.0 | 22.21 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 204.48.20.223 |
| 84.65 | vless | 249.1 | 693.7 | 22.01 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 47.89.186.170 |
| 84.35 | vless | 262.2 | 632.6 | 21.71 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 195.211.99.49 |
| 84.25 | vless | 266.4 | 702.3 | 21.61 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.232 |
| 84.19 | vless | 269.2 | 714.0 | 21.55 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.231 |
| 83.91 | vless | 281.3 | 624.4 | 21.27 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.179 |
| 83.75 | vless | 287.9 | 636.9 | 21.11 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.202 |
| 83.67 | vless | 243.9 | 677.6 | 22.13 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 45.138.100.226 |
| 83.57 | vless | 295.8 | 730.7 | 20.93 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.52 |
| 83.51 | vless | 298.3 | 822.1 | 20.87 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 137.184.218.169 |
| 83.25 | vless | 309.8 | 829.4 | 20.61 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.235 |
| 83.22 | vless | 311.1 | 710.0 | 20.58 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.225 |
| 83.16 | vless | 313.5 | 785.7 | 20.52 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.182 |
| 83.09 | vless | 244.8 | 672.1 | 22.11 | 0.0 | 9.44 | 12.74 | 19.9 | Au1rxx-base64 | using.neobo-tooth.ru |
| 83.06 | vless | 318.0 | 798.2 | 20.42 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.104 |
| 82.99 | vless | 320.8 | 805.4 | 20.35 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.163 |
| 82.96 | vless | 322.0 | 893.9 | 20.32 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 79.127.243.217 |
| 82.94 | vless | 323.1 | 818.1 | 20.3 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 169.40.42.212 |
| 82.6 | vless | 251.4 | 662.1 | 21.96 | 0.0 | 10.0 | 12.74 | 19.9 | Au1rxx-base64 | 38.77.133.141 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.945 | 362 | 1753 | prefer |
| zhangkai | 0.926 | 0.957 | 23 | 144 | prefer |
| mheidari-all | 0.872 | 0.798 | 104 | 14908 | prefer |
| Surfboard-tg-mixed | 0.835 | 0.758 | 157 | 6924 | prefer |
| DeltaKronecker-all | 0.798 | 0.721 | 122 | 4926 | prefer |
| tg-oneclickvpnkeys | 0.406 | 1.0 | 4 | 155 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 178 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4635 | observe |
| Epodonios-all | 0.255 | None | 0 | 7291 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7802 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5706 | observe |
| barry-far-vless | 0.255 | None | 0 | 5901 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4012 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 30 |
| 204 | TimeoutError | - | 28 |
| geo | ClientOSError | - | 18 |
| speed | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 9 |
| speed | TimeoutError | - | 6 |
| geo | TimeoutError | - | 5 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
