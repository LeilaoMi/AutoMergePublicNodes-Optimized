# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-17 04:45:13 |
| 运行耗时 | 328.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99687 |
| 去重后节点 | 27779 |
| TCP 可达 | 3000 |
| 真实可用 | 536 |
| Verified 输出 | 145 |
| Global 输出 | 300 |
| All 输出 | 27779 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.8 |
| geo | 1.5 |
| tcp | 85.4 |
| probe | 92.8 |
| real_test | 99.9 |
| china_check | 26.8 |
| write_verified | 0.1 |
| generate | 14.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58437 |
| vmess | 16612 |
| shadowsocks | 12100 |
| trojan | 10198 |
| hysteria2 | 1344 |
| http | 717 |
| shadowsocksr | 168 |
| socks | 62 |
| anytls | 26 |
| hysteria | 17 |
| tuic | 6 |

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
| 94.7 | vless | 248.6 | 1.3 | 22.02 | 14.95 | 9.24 | 10.65 | 17.84 | Au1rxx-base64 | 147.45.60.160 |
| 94.46 | vless | 256.0 | 4.8 | 21.85 | 14.82 | 9.3 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.16 |
| 94.0 | vless | 273.5 | 6.4 | 21.45 | 14.76 | 9.3 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.89 |
| 93.98 | shadowsocks | 252.6 | 0.7 | 21.93 | 14.97 | 9.39 | 13.85 | 17.84 | Au1rxx-base64 | 37.19.198.160 |
| 93.87 | shadowsocks | 257.4 | 0.9 | 21.82 | 14.97 | 9.39 | 13.85 | 17.84 | Au1rxx-base64 | 37.19.198.244 |
| 93.62 | vless | 288.2 | 6.7 | 21.11 | 14.75 | 9.27 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.235 |
| 93.39 | shadowsocks | 254.4 | 0.3 | 21.89 | 14.99 | 9.32 | 13.85 | 17.84 | Au1rxx-base64 | 15.204.233.41 |
| 92.6 | trojan | 332.3 | 12.3 | 20.08 | 14.54 | 9.29 | 13.85 | 17.84 | Au1rxx-base64 | 69.164.240.85 |
| 92.45 | vless | 260.8 | 13.0 | 21.74 | 14.51 | 7.71 | 10.65 | 17.84 | Au1rxx-base64 | 195.211.98.43 |
| 92.13 | vless | 292.1 | 5.1 | 21.02 | 14.81 | 7.81 | 10.65 | 17.84 | Au1rxx-base64 | 185.95.231.156 |
| 92.03 | vless | 273.5 | 5.5 | 21.45 | 14.79 | 9.3 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.232 |
| 91.82 | vless | 307.0 | 5.9 | 20.67 | 14.78 | 7.88 | 10.65 | 17.84 | Au1rxx-base64 | 137.184.218.169 |
| 91.71 | shadowsocks | 279.9 | 0.5 | 21.3 | 14.98 | 9.38 | 13.85 | 17.84 | Au1rxx-base64 | 156.146.38.167 |
| 91.69 | vless | 318.6 | 0.4 | 20.4 | 14.98 | 7.82 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.173 |
| 91.59 | vless | 383.3 | 2.8 | 18.9 | 14.9 | 9.3 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.225 |
| 91.56 | vless | 317.0 | 5.1 | 20.44 | 14.81 | 7.82 | 10.65 | 17.84 | Au1rxx-base64 | 167.17.69.171 |
| 91.53 | hysteria2 | 249.3 | 0.5 | 22.01 | 14.98 | 6.53 | 11.67 | 17.84 | Au1rxx-base64 | 129.213.91.185 |
| 91.51 | vless | 382.6 | 4.9 | 18.92 | 14.82 | 9.28 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.231 |
| 91.37 | vless | 335.6 | 0.4 | 20.01 | 14.99 | 7.88 | 10.65 | 17.84 | Au1rxx-base64 | 169.40.42.35 |
| 90.54 | shadowsocks | 281.2 | 0.5 | 21.27 | 14.98 | 9.39 | 13.85 | 17.84 | Au1rxx-base64 | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | 0.98 | 100 | 702 | prefer |
| Au1rxx-base64 | 0.916 | 0.838 | 488 | 1993 | prefer |
| Surfboard-tg-mixed | 0.446 | 0.625 | 8 | 7128 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 4946 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| peasoft-NoMoreWalls | 0.261 | 1.0 | 1 | 139 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1993 | observe |
| Epodonios-all | 0.255 | None | 0 | 7630 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10040 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5602 | observe |
| barry-far-vless | 0.255 | None | 0 | 5847 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 124 |
| geo | ClientOSError | - | 31 |
| speed | ClientOSError | - | 17 |
| 204 | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 91 | 145 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
