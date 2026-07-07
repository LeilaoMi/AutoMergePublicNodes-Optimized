# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-07 03:58:53 |
| 运行耗时 | 178.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 84264 |
| 去重后节点 | 24819 |
| TCP 可达 | 3000 |
| 真实可用 | 422 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24819 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.3 |
| tcp | 31.8 |
| probe | 45.2 |
| real_test | 73.7 |
| generate | 21.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50069 |
| trojan | 12911 |
| vmess | 10584 |
| shadowsocks | 9610 |
| hysteria2 | 732 |
| shadowsocksr | 148 |
| http | 140 |
| socks | 54 |
| hysteria | 8 |
| tuic | 6 |
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
| 76.25 | shadowsocks | 244.1 | 654.2 | 22.13 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 37.19.198.160 |
| 76.1 | shadowsocks | 250.6 | 675.4 | 21.98 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 37.19.198.243 |
| 75.52 | shadowsocks | 254.0 | 651.3 | 21.9 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 108.181.57.93 |
| 72.48 | shadowsocks | 278.6 | 633.5 | 21.33 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 156.146.38.167 |
| 72.47 | vmess | 342.7 | 959.2 | 19.84 | 0.0 | 10.0 | 11.25 | 15.88 | Surfboard-tg-mixed | 67.220.95.3 |
| 72.23 | trojan | 320.4 | 752.7 | 20.36 | 0.0 | 10.0 | 10.89 | 15.86 | DeltaKronecker-all | 45.32.198.247 |
| 71.9 | shadowsocks | 283.8 | 764.4 | 21.21 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 198.98.53.130 |
| 71.76 | shadowsocks | 283.4 | 642.3 | 21.22 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 156.146.38.170 |
| 71.22 | shadowsocks | 245.2 | 660.2 | 22.1 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 37.19.198.244 |
| 71.0 | shadowsocks | 364.4 | 902.7 | 19.34 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 185.196.61.82 |
| 70.58 | trojan | 414.9 | 1045.5 | 18.17 | 0.0 | 10.0 | 10.89 | 15.86 | DeltaKronecker-all | 45.32.195.168 |
| 70.36 | shadowsocks | 279.6 | 641.8 | 21.3 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 156.146.38.168 |
| 70.2 | hysteria2 | 429.9 | 893.1 | 17.83 | 0.0 | 10.0 | 12.5 | 16.1 | Au1rxx-base64 | 5.255.102.165 |
| 70.07 | shadowsocks | 294.9 | 812.6 | 20.95 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 37.19.198.236 |
| 69.78 | shadowsocks | 435.7 | 1113.3 | 17.69 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 156.146.38.169 |
| 69.5 | shadowsocks | 245.6 | 637.4 | 22.09 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 69.44 | hysteria2 | 405.8 | 776.9 | 18.38 | 0.0 | 9.76 | 12.5 | 15.88 | Surfboard-tg-mixed | 130.49.161.70 |
| 68.9 | shadowsocks | 337.8 | 567.6 | 19.96 | 0.0 | 10.0 | 12.02 | 16.1 | Au1rxx-base64 | 173.244.56.6 |
| 68.75 | trojan | 327.8 | 785.0 | 20.19 | 0.0 | 10.0 | 10.89 | 13.22 | mheidari-all | 149.28.241.235 |
| 68.66 | trojan | 373.7 | 874.9 | 19.13 | 0.0 | 10.0 | 10.89 | 15.88 | Surfboard-tg-mixed | 45.80.111.7 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.953 | 0.879 | 132 | 6047 | prefer |
| Au1rxx-base64 | 0.846 | 0.852 | 61 | 111 | prefer |
| mheidari-all | 0.772 | 0.695 | 128 | 18366 | prefer |
| DeltaKronecker-all | 0.741 | 0.663 | 190 | 8330 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 3626 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7041 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7168 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4526 | observe |
| barry-far-vless | 0.255 | None | 0 | 5184 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5338 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| nscl5-all | 0.234 | None | 0 | 1478 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 55 |
| speed | ClientOSError | - | 28 |
| geo | ClientOSError | - | 13 |
| 204 | ClientOSError | - | 11 |
| speed | TimeoutError | - | 9 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 284 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
