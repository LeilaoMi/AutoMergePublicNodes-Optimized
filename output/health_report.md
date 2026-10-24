# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-24 21:03:17 |
| 运行耗时 | 285.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 97014 |
| 去重后节点 | 27063 |
| TCP 可达 | 3000 |
| 真实可用 | 330 |
| Verified 输出 | 81 |
| Global 输出 | 300 |
| All 输出 | 27063 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.5 |
| tcp | 80.3 |
| probe | 93.7 |
| real_test | 68.3 |
| china_check | 19.6 |
| write_verified | 0.0 |
| generate | 14.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57819 |
| vmess | 17242 |
| shadowsocks | 12474 |
| trojan | 7619 |
| hysteria2 | 1371 |
| http | 218 |
| shadowsocksr | 163 |
| socks | 61 |
| anytls | 24 |
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
| 95.84 | hysteria2 | 242.2 | 0.5 | 22.17 | 14.98 | 8.97 | 13.64 | 17.58 | Au1rxx-base64 | 129.213.91.185 |
| 94.18 | shadowsocks | 248.4 | 2.2 | 22.03 | 14.92 | 10.0 | 13.65 | 17.58 | Au1rxx-base64 | 37.19.198.236 |
| 93.87 | shadowsocks | 251.6 | 8.4 | 21.95 | 14.69 | 10.0 | 13.65 | 17.58 | Au1rxx-base64 | 37.19.198.243 |
| 93.74 | shadowsocks | 243.2 | 3.6 | 22.15 | 14.86 | 10.0 | 13.65 | 17.58 | Au1rxx-base64 | 185.230.230.18 |
| 92.99 | shadowsocks | 265.5 | 2.6 | 21.63 | 14.9 | 9.23 | 13.65 | 17.58 | Au1rxx-base64 | 37.19.198.160 |
| 92.82 | vless | 311.0 | 2.3 | 20.58 | 14.91 | 9.01 | 10.74 | 17.58 | Au1rxx-base64 | 169.40.42.231 |
| 92.67 | shadowsocks | 255.8 | 3.8 | 21.86 | 14.86 | 9.22 | 13.65 | 17.58 | Au1rxx-base64 | 193.151.163.18 |
| 92.07 | vless | 344.8 | 28.0 | 19.8 | 13.95 | 10.0 | 10.74 | 17.58 | Au1rxx-base64 | 169.40.42.35 |
| 91.9 | vless | 353.3 | 2.4 | 19.6 | 14.91 | 9.07 | 10.74 | 17.58 | Au1rxx-base64 | 169.40.42.224 |
| 91.89 | vless | 359.1 | 23.9 | 19.47 | 14.1 | 10.0 | 10.74 | 17.58 | Au1rxx-base64 | 169.40.42.225 |
| 91.88 | vless | 308.1 | 26.7 | 20.65 | 14.0 | 8.91 | 10.74 | 17.58 | Au1rxx-base64 | 66.70.179.198 |
| 91.81 | vless | 250.3 | 3.8 | 21.98 | 14.86 | 6.65 | 10.74 | 17.58 | Au1rxx-base64 | 195.123.235.177 |
| 91.65 | vless | 361.2 | 3.1 | 19.42 | 14.88 | 9.24 | 10.74 | 17.58 | Au1rxx-base64 | 169.40.42.74 |
| 91.57 | vless | 269.9 | 60.2 | 21.53 | 12.74 | 8.98 | 10.74 | 17.58 | Au1rxx-base64 | 195.123.235.183 |
| 91.45 | vless | 375.2 | 5.4 | 19.09 | 14.8 | 9.24 | 10.74 | 17.58 | Au1rxx-base64 | 169.40.42.168 |
| 91.43 | shadowsocks | 308.0 | 1.0 | 20.65 | 14.96 | 9.09 | 13.65 | 17.58 | Au1rxx-base64 | 45.86.51.18 |
| 90.93 | shadowsocks | 280.9 | 0.8 | 21.28 | 14.97 | 10.0 | 13.65 | 17.58 | Au1rxx-base64 | 156.146.38.170 |
| 90.67 | shadowsocks | 281.6 | 2.0 | 21.26 | 14.92 | 10.0 | 13.65 | 17.58 | Au1rxx-base64 | 156.146.38.169 |
| 90.47 | shadowsocks | 248.1 | 2.6 | 22.03 | 14.9 | 6.31 | 13.65 | 17.58 | Au1rxx-base64 | 37.19.198.244 |
| 90.45 | vless | 323.7 | 59.1 | 20.28 | 12.78 | 9.07 | 10.74 | 17.58 | Au1rxx-base64 | 169.40.42.235 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.939 | 0.935 | 46 | 567 | prefer |
| Au1rxx-base64 | 0.854 | 0.791 | 296 | 1623 | prefer |
| mheidari-all | 0.83 | 0.758 | 62 | 24512 | prefer |
| Surfboard-tg-mixed | 0.352 | 0.364 | 11 | 7114 | observe |
| tg-oneclickvpnkeys | 0.324 | 0.75 | 4 | 107 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 52 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4911 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3780 | observe |
| Epodonios-all | 0.255 | None | 0 | 7708 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5485 | observe |
| barry-far-vless | 0.255 | None | 0 | 5771 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 58 |
| 204 | TimeoutError | - | 9 |
| cn-block | TimeoutError | - | 6 |
| geo | ClientOSError | - | 5 |
| 204 | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 65 | 81 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
