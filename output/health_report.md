# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-11 21:54:16 |
| 运行耗时 | 724.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99284 |
| 去重后节点 | 27441 |
| TCP 可达 | 3000 |
| 真实可用 | 505 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27441 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.3 |
| tcp | 45.4 |
| probe | 280.6 |
| real_test | 317.5 |
| generate | 73.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58285 |
| vmess | 15938 |
| shadowsocks | 11720 |
| trojan | 11000 |
| hysteria2 | 1485 |
| http | 568 |
| shadowsocksr | 166 |
| socks | 66 |
| anytls | 30 |
| hysteria | 16 |
| tuic | 10 |

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
| 84.13 | hysteria2 | 239.6 | 695.4 | 22.23 | 0.0 | 10.0 | 13.64 | 19.76 | Au1rxx-base64 | 129.213.91.185 |
| 83.31 | vless | 231.8 | 657.7 | 22.41 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 136.107.170.196 |
| 82.85 | vless | 251.9 | 654.2 | 21.95 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.231 |
| 82.6 | vless | 262.7 | 632.7 | 21.7 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.235 |
| 82.55 | vless | 264.9 | 718.4 | 21.65 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 185.95.231.156 |
| 82.26 | vless | 276.7 | 685.3 | 21.37 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.184 |
| 82.2 | vless | 279.7 | 698.2 | 21.3 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 66.70.179.198 |
| 81.79 | vless | 297.4 | 674.3 | 20.89 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.224 |
| 81.66 | vless | 303.0 | 833.0 | 20.76 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 159.89.87.21 |
| 81.5 | vless | 310.1 | 710.5 | 20.6 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.212 |
| 81.18 | vless | 323.7 | 871.7 | 20.28 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 137.184.218.169 |
| 81.06 | vless | 329.3 | 883.4 | 20.16 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.179 |
| 80.64 | vless | 281.3 | 639.2 | 21.27 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.74 |
| 80.32 | vless | 278.1 | 706.5 | 21.34 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.35 |
| 80.1 | shadowsocks | 254.1 | 699.1 | 21.9 | 0.0 | 10.0 | 12.44 | 19.76 | Au1rxx-base64 | 37.19.198.243 |
| 80.06 | vless | 252.6 | 663.4 | 21.93 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.232 |
| 80.04 | shadowsocks | 256.6 | 714.2 | 21.84 | 0.0 | 10.0 | 12.44 | 19.76 | Au1rxx-base64 | 37.19.198.160 |
| 80.02 | vless | 288.3 | 758.0 | 21.1 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.16 |
| 80.01 | vless | 374.4 | 955.5 | 19.11 | 0.0 | 10.0 | 11.14 | 19.76 | Au1rxx-base64 | 169.40.42.15 |
| 79.99 | shadowsocks | 237.2 | 586.3 | 22.29 | 0.0 | 10.0 | 12.44 | 19.76 | Au1rxx-base64 | 66.23.205.83 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.93 | 388 | 1858 | prefer |
| DeltaKronecker-all | 0.943 | 0.878 | 49 | 5372 | prefer |
| mheidari-all | 0.915 | 0.844 | 77 | 23882 | prefer |
| ermaozi | 0.635 | 0.615 | 39 | 635 | observe |
| Surfboard-tg-mixed | 0.586 | 0.8 | 10 | 7031 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 104 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5099 | observe |
| Epodonios-all | 0.255 | None | 0 | 7711 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9704 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5590 | observe |
| barry-far-vless | 0.255 | None | 0 | 5966 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4284 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| 204 | TimeoutError | - | 10 |
| speed | ClientOSError | - | 7 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| geo | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
