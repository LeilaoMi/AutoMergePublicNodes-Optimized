# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-10 04:14:36 |
| 运行耗时 | 650.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 87394 |
| 去重后节点 | 23410 |
| TCP 可达 | 3000 |
| 真实可用 | 489 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23410 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 39.7 |
| probe | 239.7 |
| real_test | 326.9 |
| generate | 36.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53235 |
| vmess | 12572 |
| shadowsocks | 10684 |
| trojan | 8372 |
| hysteria2 | 1683 |
| http | 641 |
| shadowsocksr | 124 |
| socks | 56 |
| hysteria | 12 |
| tuic | 9 |
| anytls | 6 |

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
| 83.48 | vless | 249.5 | 705.5 | 22.0 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 47.253.226.114 |
| 83.45 | vless | 250.7 | 655.3 | 21.97 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 137.184.218.169 |
| 82.92 | vless | 273.7 | 721.5 | 21.44 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.184 |
| 82.91 | vless | 274.4 | 671.8 | 21.43 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.235 |
| 82.75 | vless | 281.2 | 744.8 | 21.27 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.74 |
| 82.68 | vless | 284.3 | 747.3 | 21.2 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.229 |
| 82.56 | vless | 289.5 | 727.4 | 21.08 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.225 |
| 82.5 | vless | 291.9 | 726.3 | 21.02 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.212 |
| 82.46 | vless | 293.5 | 669.4 | 20.98 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.90 |
| 82.45 | vless | 294.0 | 732.4 | 20.97 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.224 |
| 82.38 | vless | 297.0 | 760.0 | 20.9 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 66.70.179.198 |
| 82.14 | vless | 307.5 | 822.5 | 20.66 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.52 |
| 82.08 | vless | 310.2 | 829.0 | 20.6 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.223 |
| 82.04 | vless | 249.6 | 655.5 | 22.0 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.168 |
| 81.54 | vless | 333.3 | 845.6 | 20.06 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.75 |
| 81.45 | shadowsocks | 239.9 | 665.1 | 22.22 | 0.0 | 10.0 | 13.79 | 19.44 | Au1rxx-base64 | 37.19.198.244 |
| 81.44 | shadowsocks | 240.4 | 670.9 | 22.21 | 0.0 | 10.0 | 13.79 | 19.44 | Au1rxx-base64 | 37.19.198.243 |
| 81.36 | vless | 341.1 | 813.9 | 19.88 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.16 |
| 81.24 | shadowsocks | 249.1 | 690.7 | 22.01 | 0.0 | 10.0 | 13.79 | 19.44 | Au1rxx-base64 | 37.19.198.160 |
| 81.07 | vless | 353.8 | 839.3 | 19.59 | 0.0 | 10.0 | 12.04 | 19.44 | Au1rxx-base64 | 169.40.42.104 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.984 | 0.923 | 297 | 1598 | prefer |
| Surfboard-tg-mixed | 0.894 | 0.829 | 41 | 7448 | prefer |
| ermaozi | 0.704 | 0.697 | 33 | 449 | prefer |
| mheidari-all | 0.611 | 0.532 | 141 | 16259 | observe |
| ermaozi-get_subscribe | 0.541 | 0.588 | 17 | 469 | observe |
| DeltaKronecker-all | 0.507 | 0.426 | 148 | 5187 | observe |
| xiaoji235-airport-v2ray-all | 0.492 | 0.538 | 13 | 3508 | observe |
| tg-oneclickvpnkeys | 0.317 | 1.0 | 2 | 147 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| Epodonios-all | 0.255 | None | 0 | 7910 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8706 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6108 | observe |
| barry-far-vless | 0.255 | None | 0 | 6333 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4247 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 47 |
| speed | TimeoutError | - | 42 |
| geo | ClientOSError | - | 35 |
| speed | ClientOSError | - | 26 |
| 204 | ProxyError | - | 24 |
| cn-block | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 9 |
| 204 | TimeoutError | - | 7 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
