# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-28 23:12:41 |
| 运行耗时 | 390.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97528 |
| 去重后节点 | 27021 |
| TCP 可达 | 3000 |
| 真实可用 | 410 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27021 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.2 |
| geo | 1.5 |
| tcp | 44.3 |
| probe | 170.7 |
| real_test | 132.9 |
| generate | 32.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59920 |
| vmess | 14922 |
| shadowsocks | 11416 |
| trojan | 8882 |
| hysteria2 | 1459 |
| http | 635 |
| shadowsocksr | 170 |
| socks | 77 |
| anytls | 24 |
| hysteria | 15 |
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
| 82.73 | vless | 235.0 | 594.8 | 22.34 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 195.123.235.177 |
| 82.1 | vless | 262.3 | 716.4 | 21.71 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 47.90.153.88 |
| 81.58 | vless | 284.6 | 786.6 | 21.19 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 47.253.226.114 |
| 81.51 | vless | 287.6 | 684.3 | 21.12 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.16 |
| 81.48 | vless | 288.9 | 688.4 | 21.09 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.90 |
| 81.35 | vless | 294.7 | 713.8 | 20.96 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.232 |
| 81.11 | vless | 274.1 | 646.5 | 21.43 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 195.211.98.43 |
| 81.05 | vless | 282.3 | 719.7 | 21.24 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.168 |
| 80.98 | vless | 310.3 | 764.4 | 20.59 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 66.70.179.198 |
| 80.58 | vless | 327.9 | 890.1 | 20.19 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 159.89.87.21 |
| 80.57 | vless | 328.3 | 857.0 | 20.18 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.104 |
| 80.47 | vless | 332.4 | 892.2 | 20.08 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 137.184.218.169 |
| 80.1 | vless | 311.9 | 749.6 | 20.56 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 158.69.112.254 |
| 79.97 | vless | 354.0 | 957.7 | 19.58 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 185.95.231.156 |
| 79.9 | vless | 300.6 | 710.9 | 20.82 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.179 |
| 79.75 | vless | 363.7 | 953.0 | 19.36 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.224 |
| 79.66 | vless | 247.4 | 690.7 | 22.05 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 79.141.172.154 |
| 79.37 | vless | 354.9 | 946.4 | 19.56 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.89 |
| 79.2 | vless | 387.5 | 913.3 | 18.81 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 169.40.42.74 |
| 79.13 | vless | 390.5 | 1038.0 | 18.74 | 0.0 | 10.0 | 11.85 | 18.54 | Au1rxx-base64 | 185.95.231.233 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.931 | 0.866 | 343 | 1674 | prefer |
| mheidari-all | 0.903 | 0.83 | 94 | 22856 | prefer |
| Surfboard-tg-mixed | 0.749 | 0.923 | 13 | 7142 | prefer |
| ermaozi | 0.562 | 0.552 | 29 | 344 | observe |
| DeltaKronecker-all | 0.446 | 0.625 | 8 | 5428 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 121 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5326 | observe |
| Epodonios-all | 0.255 | None | 0 | 7535 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9706 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5799 | observe |
| barry-far-vless | 0.255 | None | 0 | 6027 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4237 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 30 |
| 204 | ProxyError | - | 25 |
| cn-block | TimeoutError | - | 8 |
| speed | TimeoutError | - | 5 |
| geo | TimeoutError | - | 5 |
| 204 | TimeoutError | - | 4 |
| 204 | ProxyConnectionError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
