# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-20 14:25:44 |
| 运行耗时 | 374.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 102 |
| 原始节点 | 85546 |
| 去重后节点 | 24077 |
| TCP 可达 | 3000 |
| 真实可用 | 379 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24077 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 0.6 |
| tcp | 33.1 |
| probe | 84.4 |
| real_test | 223.1 |
| generate | 27.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50795 |
| trojan | 12995 |
| vmess | 11010 |
| shadowsocks | 10178 |
| hysteria2 | 385 |
| shadowsocksr | 71 |
| http | 52 |
| socks | 36 |
| hysteria | 16 |
| tuic | 7 |
| anytls | 1 |

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
| 79.7 | shadowsocks | 225.4 | 624.4 | 22.56 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 37.19.198.160 |
| 79.61 | shadowsocks | 229.4 | 631.5 | 22.47 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 37.19.198.244 |
| 79.51 | shadowsocks | 233.6 | 634.4 | 22.37 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 37.19.198.236 |
| 78.74 | shadowsocks | 245.4 | 654.4 | 22.1 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 108.181.57.93 |
| 78.36 | shadowsocks | 239.6 | 652.1 | 22.23 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 147.90.234.133 |
| 76.12 | shadowsocks | 286.5 | 663.6 | 21.15 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 156.146.38.168 |
| 76.1 | shadowsocks | 286.2 | 651.8 | 21.15 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 156.146.38.170 |
| 75.89 | shadowsocks | 288.0 | 651.5 | 21.11 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 156.146.38.167 |
| 75.66 | shadowsocks | 290.9 | 656.2 | 21.04 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 156.146.38.169 |
| 74.91 | shadowsocks | 357.6 | 868.0 | 19.5 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 185.196.61.82 |
| 72.56 | shadowsocks | 308.9 | 597.0 | 20.63 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 173.244.56.6 |
| 71.88 | shadowsocks | 322.7 | 578.2 | 20.31 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 173.244.56.9 |
| 70.64 | shadowsocks | 351.5 | 665.7 | 19.64 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 149.22.95.183 |
| 70.41 | trojan | 406.8 | 773.8 | 18.36 | 0.0 | 10.0 | 12.7 | 18.22 | Au1rxx-base64 | 52.212.156.233 |
| 70.07 | hysteria2 | 498.0 | 1053.9 | 16.25 | 0.0 | 10.0 | 12.0 | 18.22 | Au1rxx-base64 | 5.255.102.165 |
| 69.42 | shadowsocks | 391.8 | 724.8 | 18.71 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 158.173.24.73 |
| 69.39 | trojan | 406.6 | 777.2 | 18.37 | 0.0 | 8.77 | 12.7 | 18.22 | Au1rxx-base64 | fit-calf.rooster465.autos |
| 69.17 | shadowsocks | 403.9 | 807.0 | 18.43 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 108.181.0.177 |
| 68.92 | shadowsocks | 384.5 | 722.5 | 18.88 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | 172.245.235.84 |
| 68.23 | shadowsocks | 351.8 | 990.3 | 19.63 | 0.0 | 10.0 | 12.92 | 18.22 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.927 | 0.892 | 240 | 969 | prefer |
| Surfboard-tg-mixed | 0.658 | 0.581 | 43 | 5287 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 5035 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4714 | observe |
| Epodonios-all | 0.255 | None | 0 | 6550 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6894 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4082 | observe |
| barry-far-vless | 0.255 | None | 0 | 4908 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5193 | observe |
| nscl5-all | 0.255 | None | 0 | 2118 | observe |
| mheidari-all | 0.251 | 0.152 | 33 | 19893 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 799 |
| speed | ClientOSError | - | 122 |
| geo | ClientOSError | - | 31 |
| cn-block | TimeoutError | - | 29 |
| speed | TimeoutError | - | 10 |
| 204 | ProxyError | - | 8 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 5 |
| speed | ProxyError | - | 3 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
