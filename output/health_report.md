# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-25 21:55:16 |
| 运行耗时 | 303.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 78555 |
| 去重后节点 | 27517 |
| TCP 可达 | 3000 |
| 真实可用 | 360 |
| Verified 输出 | 81 |
| Global 输出 | 300 |
| All 输出 | 27517 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.7 |
| tcp | 80.9 |
| probe | 108.3 |
| real_test | 59.7 |
| china_check | 28.0 |
| write_verified | 0.1 |
| generate | 17.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46797 |
| vmess | 15012 |
| shadowsocks | 9217 |
| trojan | 5440 |
| hysteria2 | 1616 |
| shadowsocksr | 150 |
| http | 145 |
| socks | 96 |
| anytls | 39 |
| hysteria | 31 |
| tuic | 12 |

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
| 92.46 | shadowsocks | 242.5 | 3.2 | 22.16 | 14.88 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 37.19.198.160 |
| 92.3 | shadowsocks | 247.7 | 2.5 | 22.04 | 14.91 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 37.19.198.236 |
| 92.26 | shadowsocks | 252.5 | 2.3 | 21.93 | 14.91 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 37.19.198.244 |
| 92.2 | shadowsocks | 256.0 | 1.8 | 21.85 | 14.93 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 37.19.198.243 |
| 91.36 | shadowsocks | 257.3 | 10.2 | 21.82 | 14.62 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 45.86.51.18 |
| 88.98 | vless | 333.8 | 6.6 | 20.05 | 14.75 | 9.48 | 8.84 | 15.86 | Au1rxx-base64 | 169.40.42.202 |
| 88.75 | shadowsocks | 383.9 | 1.7 | 18.89 | 14.94 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 193.151.160.9 |
| 88.59 | vless | 369.3 | 9.0 | 19.23 | 14.66 | 10.0 | 8.84 | 15.86 | Au1rxx-base64 | 169.40.42.35 |
| 87.76 | shadowsocks | 384.8 | 0.8 | 18.87 | 14.97 | 9.0 | 13.56 | 15.86 | Au1rxx-base64 | 193.151.160.18 |
| 87.54 | shadowsocks | 432.9 | 3.8 | 17.76 | 14.86 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 15.204.247.206 |
| 85.83 | shadowsocks | 442.6 | 7.0 | 17.53 | 14.74 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 156.146.38.170 |
| 85.55 | vless | 260.7 | 2.2 | 21.74 | 14.92 | 9.49 | 8.84 | 15.86 | Au1rxx-base64 | 159.89.87.21 |
| 85.19 | hysteria2 | 244.9 | 3.6 | 22.11 | 14.87 | 0.0 | 12.27 | 16.94 | mheidari-all | 206.189.229.48 |
| 85.14 | shadowsocks | 266.2 | 6.6 | 21.61 | 14.75 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 193.151.163.18 |
| 85.04 | shadowsocks | 515.3 | 19.6 | 15.85 | 14.27 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 185.230.230.18 |
| 84.87 | vless | 371.3 | 5.9 | 19.18 | 14.78 | 10.0 | 8.84 | 15.86 | Au1rxx-base64 | 169.40.42.74 |
| 84.48 | shadowsocks | 368.8 | 2.9 | 19.24 | 14.89 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 173.244.56.6 |
| 84.2 | shadowsocks | 374.0 | 0.1 | 19.12 | 14.99 | 10.0 | 13.56 | 15.86 | Au1rxx-base64 | 173.244.56.9 |
| 83.82 | trojan | 343.9 | 2.8 | 19.82 | 14.89 | 10.0 | 6.25 | 15.86 | Au1rxx-base64 | 69.164.240.85 |
| 83.79 | http | 425.1 | 3.7 | 17.94 | 14.86 | 0.0 | 14.41 | 19.08 | ermaozi | 172.64.68.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.995 | 0.934 | 91 | 1751 | prefer |
| ermaozi | 0.979 | 1.0 | 25 | 403 | prefer |
| Surfboard-tg-mixed | 0.897 | 0.822 | 129 | 8209 | prefer |
| mheidari-all | 0.878 | 0.801 | 176 | 15044 | prefer |
| tg-LonUp_M | 0.446 | 1.0 | 5 | 173 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ermaozi-get_subscribe | 0.307 | 0.6 | 5 | 356 | observe |
| SoliSpirit-all | 0.287 | 0.5 | 2 | 11598 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4958 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5378 | observe |
| barry-far-vless | 0.255 | None | 0 | 5559 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 38 |
| 204 | TimeoutError | - | 7 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 4 |
| cn-block | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | TimeoutError | - | 1 |
| geo | ClientOSError | - | 1 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 80 | 81 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
