# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 06:55:00 |
| 运行耗时 | 344.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99726 |
| 去重后节点 | 27907 |
| TCP 可达 | 3000 |
| 真实可用 | 505 |
| Verified 输出 | 39 |
| Global 输出 | 300 |
| All 输出 | 27907 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.5 |
| tcp | 84.8 |
| probe | 115.1 |
| real_test | 97.1 |
| china_check | 23.4 |
| write_verified | 0.0 |
| generate | 14.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58862 |
| vmess | 16436 |
| shadowsocks | 11812 |
| trojan | 10390 |
| hysteria2 | 1211 |
| http | 740 |
| shadowsocksr | 168 |
| socks | 59 |
| anytls | 25 |
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
| 94.41 | shadowsocks | 256.6 | 1.8 | 21.84 | 14.93 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 37.19.198.243 |
| 94.28 | shadowsocks | 255.4 | 6.2 | 21.87 | 14.77 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 37.19.198.160 |
| 93.75 | hysteria2 | 259.9 | 0.2 | 21.76 | 14.99 | 10.0 | 14.06 | 17.74 | Au1rxx-base64 | 179.255.104.98 |
| 92.19 | shadowsocks | 325.8 | 5.0 | 20.24 | 14.81 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 15.204.233.41 |
| 91.49 | shadowsocks | 277.7 | 0.9 | 21.35 | 14.97 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 156.146.38.168 |
| 91.36 | shadowsocks | 282.7 | 0.3 | 21.23 | 14.99 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 156.146.38.170 |
| 91.31 | shadowsocks | 258.8 | 3.2 | 21.79 | 14.88 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 37.19.198.236 |
| 90.33 | vless | 344.5 | 4.4 | 19.8 | 14.83 | 9.66 | 8.69 | 17.74 | Au1rxx-base64 | 169.40.42.173 |
| 90.15 | vless | 304.0 | 0.6 | 20.74 | 14.98 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 147.45.60.160 |
| 90.01 | vless | 230.3 | 1.7 | 22.45 | 14.94 | 6.19 | 8.69 | 17.74 | Au1rxx-base64 | 195.123.235.183 |
| 89.98 | vless | 308.2 | 2.4 | 20.64 | 14.91 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 169.40.42.232 |
| 89.93 | vless | 393.5 | 4.6 | 18.67 | 14.83 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 169.40.42.90 |
| 89.68 | shadowsocks | 342.6 | 1.5 | 19.85 | 14.95 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 156.146.38.167 |
| 89.59 | vless | 311.0 | 5.8 | 20.58 | 14.78 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 169.40.42.225 |
| 89.51 | vless | 304.1 | 8.5 | 20.74 | 14.68 | 9.66 | 8.69 | 17.74 | Au1rxx-base64 | 137.184.218.169 |
| 89.43 | vless | 316.0 | 11.0 | 20.46 | 14.59 | 10.0 | 8.69 | 17.74 | Au1rxx-base64 | 169.40.42.163 |
| 89.32 | shadowsocks | 257.1 | 4.1 | 21.83 | 14.85 | 10.0 | 13.9 | 17.74 | Au1rxx-base64 | 37.19.198.244 |
| 89.11 | vless | 290.2 | 22.1 | 21.06 | 14.17 | 7.45 | 8.69 | 17.74 | Au1rxx-base64 | 167.17.69.171 |
| 88.95 | vless | 260.8 | 0.5 | 21.74 | 14.98 | 5.8 | 8.69 | 17.74 | Au1rxx-base64 | 195.211.98.43 |
| 88.42 | vless | 285.8 | 0.1 | 21.16 | 15.0 | 5.83 | 8.69 | 17.74 | Au1rxx-base64 | 66.70.179.198 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.941 | 0.922 | 90 | 693 | prefer |
| Au1rxx-base64 | 0.89 | 0.812 | 478 | 1992 | prefer |
| mheidari-all | 0.58 | 0.5 | 20 | 23985 | observe |
| Surfboard-tg-mixed | 0.529 | 0.447 | 47 | 7054 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 5147 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1992 | observe |
| Epodonios-all | 0.255 | None | 0 | 7651 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10060 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5573 | observe |
| barry-far-vless | 0.255 | None | 0 | 5882 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 64 |
| speed | ClientOSError | - | 22 |
| geo | ClientOSError | - | 14 |
| cn-block | ClientOSError | - | 10 |
| 204 | TimeoutError | - | 8 |
| speed | ProxyError | - | 5 |
| cn-block | ProxyError | - | 4 |
| cn-block | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 34 | 39 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
