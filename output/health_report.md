# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 06:06:53 |
| 运行耗时 | 341.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99583 |
| 去重后节点 | 27920 |
| TCP 可达 | 3000 |
| 真实可用 | 507 |
| Verified 输出 | 21 |
| Global 输出 | 300 |
| All 输出 | 27920 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.5 |
| tcp | 85.3 |
| probe | 95.3 |
| real_test | 109.2 |
| china_check | 28.2 |
| write_verified | 0.0 |
| generate | 14.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58788 |
| vmess | 16421 |
| shadowsocks | 11784 |
| trojan | 10369 |
| hysteria2 | 1206 |
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
| 93.49 | shadowsocks | 251.8 | 0.6 | 21.95 | 14.98 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 37.19.198.243 |
| 92.33 | shadowsocks | 257.1 | 1.5 | 21.83 | 14.94 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 37.19.198.236 |
| 90.52 | shadowsocks | 356.8 | 1.5 | 19.52 | 14.94 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 51.222.136.236 |
| 90.08 | shadowsocks | 287.8 | 9.7 | 21.12 | 14.64 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 156.146.38.167 |
| 89.93 | shadowsocks | 290.1 | 17.0 | 21.06 | 14.36 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 156.146.38.168 |
| 89.78 | vless | 260.1 | 1.5 | 21.76 | 14.94 | 9.24 | 7.76 | 16.08 | Au1rxx-base64 | 167.17.69.171 |
| 89.48 | vless | 304.7 | 2.1 | 20.72 | 14.92 | 10.0 | 7.76 | 16.08 | Au1rxx-base64 | 169.40.42.15 |
| 89.42 | shadowsocks | 309.6 | 6.7 | 20.61 | 14.75 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 15.204.233.41 |
| 88.48 | vless | 348.5 | 1.8 | 19.71 | 14.93 | 10.0 | 7.76 | 16.08 | Au1rxx-base64 | 169.40.42.163 |
| 88.12 | hysteria2 | 260.1 | 0.6 | 21.76 | 14.98 | 10.0 | 14.21 | 16.08 | Au1rxx-base64 | 179.255.104.98 |
| 87.95 | vless | 339.5 | 1.3 | 19.92 | 14.95 | 9.24 | 7.76 | 16.08 | Au1rxx-base64 | 185.95.231.156 |
| 87.86 | vless | 371.1 | 4.6 | 19.19 | 14.83 | 10.0 | 7.76 | 16.08 | Au1rxx-base64 | 169.40.42.90 |
| 87.73 | shadowsocks | 284.5 | 3.5 | 21.19 | 14.87 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 156.146.38.169 |
| 87.36 | vless | 259.1 | 7.0 | 21.78 | 14.74 | 10.0 | 7.76 | 16.08 | Au1rxx-base64 | 159.89.87.21 |
| 87.25 | vless | 255.1 | 0.8 | 21.87 | 14.97 | 6.57 | 7.76 | 16.08 | Au1rxx-base64 | 195.211.98.43 |
| 87.04 | shadowsocks | 256.7 | 2.7 | 21.84 | 14.9 | 10.0 | 14.48 | 16.08 | Au1rxx-base64 | 37.19.198.160 |
| 86.69 | http | 326.8 | 0.3 | 20.21 | 14.99 | 0.0 | 14.33 | 19.66 | ermaozi | 172.64.68.89 |
| 85.97 | vless | 222.5 | 1.5 | 22.63 | 14.95 | 9.37 | 7.76 | 16.08 | Au1rxx-base64 | 195.123.235.177 |
| 85.81 | vless | 233.7 | 0.3 | 22.37 | 14.99 | 6.61 | 7.76 | 16.08 | Au1rxx-base64 | 195.123.235.183 |
| 85.68 | hysteria2 | 245.6 | 5.4 | 22.09 | 14.8 | 0.0 | 14.21 | 16.08 | Au1rxx-base64 | 129.213.91.185 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.989 | 89 | 693 | prefer |
| Au1rxx-base64 | 0.883 | 0.804 | 490 | 1992 | prefer |
| Surfboard-tg-mixed | 0.515 | 0.636 | 11 | 7054 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1992 | observe |
| Epodonios-all | 0.255 | None | 0 | 7651 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9906 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5573 | observe |
| barry-far-vless | 0.255 | None | 0 | 5882 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| mheidari-all | 0.233 | 0.147 | 109 | 23985 | downweight |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 140 |
| geo | ClientOSError | - | 20 |
| speed | ClientOSError | - | 16 |
| cn-block | ClientOSError | - | 11 |
| 204 | TimeoutError | - | 5 |
| 204 | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| geo | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 99 | 21 | - |
| global | False | 106 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
