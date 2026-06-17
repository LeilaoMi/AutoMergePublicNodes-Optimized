# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-17 18:47:52 |
| 运行耗时 | 161.9s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 43687 |
| 去重后节点 | 18013 |
| TCP 可达 | 1500 |
| 真实可用 | 102 |
| Verified 输出 | 102 |
| Global 输出 | 112 |
| All 输出 | 18013 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 1.9 |
| geo | 1.2 |
| tcp | 21.8 |
| probe | 37.6 |
| real_test | 60.4 |
| generate | 38.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 22475 |
| shadowsocks | 8338 |
| trojan | 7003 |
| vmess | 5446 |
| hysteria2 | 198 |
| http | 95 |
| shadowsocksr | 87 |
| socks | 38 |
| hysteria | 6 |
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
| 61.95 | vmess | 191.4 | 489.2 | 23.35 | 0.0 | 10.0 | 12.86 | 5.24 | Barabama-yudou | 82.198.246.233 |
| 58.93 | vless | 199.4 | 494.4 | 23.16 | 0.0 | 10.0 | 3.67 | 7.1 | DeltaKronecker-all | 172.252.125.77 |
| 58.09 | vless | 231.6 | 506.2 | 22.42 | 0.0 | 10.0 | 3.67 | 7.1 | DeltaKronecker-all | 64.23.143.23 |
| 56.39 | shadowsocks | 208.5 | 481.8 | 22.95 | 0.0 | 10.0 | 7.26 | 5.18 | Au1rxx-base64 | 173.244.56.9 |
| 55.33 | trojan | 320.2 | 737.0 | 20.37 | 0.0 | 10.0 | 5.36 | 7.1 | DeltaKronecker-all | 45.61.58.89 |
| 54.8 | vless | 183.4 | 464.9 | 23.53 | 0.0 | 10.0 | 3.67 | 7.1 | DeltaKronecker-all | 141.193.154.182 |
| 54.22 | shadowsocks | 280.6 | 764.0 | 21.28 | 0.0 | 10.0 | 7.26 | 5.18 | Au1rxx-base64 | 108.181.0.177 |
| 54.07 | shadowsocks | 287.1 | 747.4 | 21.13 | 0.0 | 10.0 | 7.26 | 5.18 | Au1rxx-base64 | 108.181.118.10 |
| 51.58 | trojan | 341.1 | 753.0 | 19.88 | 0.0 | 10.0 | 5.36 | 7.1 | DeltaKronecker-all | 45.61.52.243 |
| 50.38 | hysteria2 | 439.1 | 751.0 | 17.61 | 0.0 | 9.59 | 11.25 | 5.18 | Au1rxx-base64 | 62.210.124.146 |
| 47.88 | shadowsocks | 356.9 | 349.8 | 19.52 | 1.88 | 9.56 | 7.26 | 7.1 | DeltaKronecker-all | 36.230.59.142 |
| 47.51 | shadowsocks | 358.7 | 352.8 | 19.48 | 1.77 | 9.43 | 7.26 | 7.1 | DeltaKronecker-all | 61.231.11.137 |
| 47.07 | trojan | 445.0 | 972.6 | 17.48 | 0.0 | 10.0 | 5.36 | 7.1 | DeltaKronecker-all | 172.238.163.242 |
| 46.91 | shadowsocks | 458.5 | 286.4 | 17.16 | 4.26 | 9.17 | 7.26 | 7.1 | DeltaKronecker-all | 103.149.182.79 |
| 46.62 | shadowsocks | 382.0 | 752.7 | 18.94 | 0.0 | 10.0 | 7.26 | 7.1 | DeltaKronecker-all | 108.181.57.93 |
| 46.35 | vmess | 638.2 | 995.3 | 13.01 | 0.0 | 9.51 | 12.86 | 7.1 | DeltaKronecker-all | 159.223.13.109 |
| 45.16 | vless | 483.9 | 683.7 | 16.58 | 0.0 | 10.0 | 3.67 | 7.1 | DeltaKronecker-all | 154.17.8.84 |
| 45.15 | shadowsocks | 387.3 | 804.3 | 18.81 | 0.0 | 10.0 | 7.26 | 7.1 | DeltaKronecker-all | 147.90.234.133 |
| 45.03 | trojan | 496.9 | 879.4 | 16.27 | 0.0 | 10.0 | 5.36 | 7.1 | DeltaKronecker-all | 198.52.244.10 |
| 44.87 | http | 808.2 | 1120.5 | 9.07 | 0.0 | 9.09 | 14.42 | 9.18 | snakem982 | 84.239.49.238 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.884 | 0.895 | 57 | 73 | prefer |
| Au1rxx-base64 | 0.404 | 1.0 | 4 | 108 | observe |
| DeltaKronecker-all | 0.377 | 0.295 | 146 | 7763 | observe |
| Surfboard-tg-mixed | 0.349 | 0.667 | 3 | 4729 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 2000 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3741 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4541 | observe |
| mheidari-all | 0.255 | None | 0 | 2000 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 55 |
| 204 | TimeoutError | - | 18 |
| 204 | ProxyError | - | 10 |
| cn-block | TimeoutError | - | 9 |
| geo | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 3 |
| geo | TimeoutError | - | 3 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 190 | 102 | - |
| global | False | 199 | 112 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
