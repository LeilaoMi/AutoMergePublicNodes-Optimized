# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-11 03:20:20 |
| 运行耗时 | 195.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 75798 |
| 去重后节点 | 24018 |
| TCP 可达 | 3000 |
| 真实可用 | 517 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24018 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.4 |
| tcp | 31.9 |
| probe | 44.0 |
| real_test | 91.5 |
| generate | 22.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43053 |
| trojan | 12059 |
| vmess | 10604 |
| shadowsocks | 9428 |
| hysteria2 | 285 |
| shadowsocksr | 141 |
| http | 135 |
| socks | 82 |
| hysteria | 8 |
| anytls | 2 |
| tuic | 1 |

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
| 79.04 | shadowsocks | 254.3 | 679.3 | 21.89 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 37.19.198.243 |
| 78.3 | shadowsocks | 286.5 | 786.3 | 21.15 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 37.19.198.244 |
| 78.03 | shadowsocks | 298.1 | 821.1 | 20.88 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 37.19.198.236 |
| 76.63 | shadowsocks | 277.1 | 631.4 | 21.36 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 156.146.38.169 |
| 75.9 | shadowsocks | 281.2 | 641.0 | 21.27 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 156.146.38.168 |
| 75.02 | shadowsocks | 316.8 | 746.3 | 20.44 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 156.146.38.170 |
| 74.24 | shadowsocks | 241.3 | 633.6 | 22.19 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 73.81 | vless | 268.0 | 736.4 | 21.57 | 0.0 | 10.0 | 6.12 | 16.12 | Surfboard-tg-mixed | 47.253.226.114 |
| 73.81 | shadowsocks | 275.4 | 637.0 | 21.4 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 156.146.38.167 |
| 72.84 | shadowsocks | 225.7 | 591.7 | 22.55 | 0.0 | 10.0 | 13.25 | 11.04 | mheidari-all | 198.98.53.130 |
| 72.61 | vless | 320.1 | 854.9 | 20.37 | 0.0 | 10.0 | 6.12 | 16.12 | Surfboard-tg-mixed | 137.184.218.169 |
| 72.04 | shadowsocks | 324.2 | 557.9 | 20.27 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 173.244.56.9 |
| 71.96 | shadowsocks | 307.1 | 574.9 | 20.67 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 108.181.118.10 |
| 71.75 | shadowsocks | 341.9 | 595.5 | 19.86 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 173.244.56.6 |
| 71.69 | hysteria2 | 361.7 | 699.8 | 19.41 | 0.0 | 10.0 | 11.25 | 17.9 | Au1rxx-base64 | 62.210.124.146 |
| 71.63 | shadowsocks | 256.5 | 659.5 | 21.84 | 0.0 | 10.0 | 13.25 | 11.04 | mheidari-all | 108.181.57.93 |
| 71.44 | shadowsocks | 329.3 | 593.9 | 20.16 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 108.181.0.177 |
| 71.08 | vless | 247.2 | 641.7 | 22.06 | 0.0 | 10.0 | 6.12 | 17.9 | Au1rxx-base64 | 159.89.87.21 |
| 70.63 | shadowsocks | 315.2 | 616.3 | 20.48 | 0.0 | 10.0 | 13.25 | 17.9 | Au1rxx-base64 | 216.105.168.18 |
| 69.71 | trojan | 395.9 | 990.4 | 18.61 | 0.0 | 10.0 | 7.94 | 17.9 | Au1rxx-base64 | 149.28.241.235 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.863 | 0.865 | 89 | 136 | prefer |
| DeltaKronecker-all | 0.814 | 0.736 | 242 | 7600 | prefer |
| mheidari-all | 0.72 | 0.646 | 48 | 16392 | prefer |
| Surfboard-tg-mixed | 0.714 | 0.635 | 304 | 5480 | prefer |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4165 | observe |
| Epodonios-all | 0.255 | None | 0 | 6288 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3971 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6402 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4087 | observe |
| barry-far-vless | 0.255 | None | 0 | 4570 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5415 | observe |
| xiaoji235-airport-v2ray-all | 0.229 | None | 0 | 1340 | observe |
| nscl5-all | 0.223 | None | 0 | 1207 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 81 |
| geo | TimeoutError | - | 68 |
| speed | TimeoutError | - | 18 |
| geo | ClientOSError | - | 16 |
| cn-block | ClientOSError | - | 6 |
| cn-block | TimeoutError | - | 6 |
| 204 | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 280 | 300 | - |
| global | False | 294 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
