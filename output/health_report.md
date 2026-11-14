# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-14 06:48:30 |
| 运行耗时 | 308.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83825 |
| 去重后节点 | 27035 |
| TCP 可达 | 3000 |
| 真实可用 | 468 |
| Verified 输出 | 89 |
| Global 输出 | 300 |
| All 输出 | 27035 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 67.7 |
| probe | 70.8 |
| real_test | 79.7 |
| china_check | 76.1 |
| generate | 8.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50537 |
| vmess | 14629 |
| shadowsocks | 9777 |
| trojan | 6790 |
| hysteria2 | 1507 |
| http | 291 |
| shadowsocksr | 147 |
| socks | 69 |
| hysteria | 37 |
| anytls | 21 |
| tuic | 20 |

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
| 89.67 | http | 208.8 | 0.9 | 22.94 | 14.97 | 0.0 | 14.48 | 19.78 | ermaozi | 172.64.68.89 |
| 89.64 | http | 204.7 | 1.5 | 23.04 | 14.94 | 0.0 | 14.48 | 19.78 | ermaozi | 44.248.167.117 |
| 87.12 | trojan | 247.5 | 0.2 | 22.05 | 14.99 | 7.1 | 9.12 | 16.36 | Au1rxx-base64 | 66.163.114.166 |
| 86.46 | trojan | 261.2 | 0.3 | 21.73 | 14.99 | 9.34 | 9.12 | 16.36 | Au1rxx-base64 | 167.88.61.193 |
| 86.06 | trojan | 291.4 | 0.2 | 21.03 | 14.99 | 10.0 | 9.12 | 16.36 | Au1rxx-base64 | 66.163.112.121 |
| 85.8 | trojan | 254.4 | 2.1 | 21.89 | 14.92 | 9.34 | 9.12 | 16.36 | Au1rxx-base64 | 167.88.61.198 |
| 85.58 | vless | 303.6 | 2.8 | 20.75 | 14.89 | 6.78 | 9.12 | 16.36 | Au1rxx-base64 | 45.63.53.81 |
| 85.46 | shadowsocks | 326.4 | 0.8 | 20.22 | 14.97 | 10.0 | 12.62 | 16.36 | Au1rxx-base64 | 156.146.38.168 |
| 85.37 | shadowsocks | 286.8 | 72.8 | 21.14 | 12.27 | 10.0 | 12.62 | 16.36 | Au1rxx-base64 | 95.215.201.18 |
| 85.15 | trojan | 304.7 | 1.3 | 20.72 | 14.95 | 9.33 | 9.12 | 16.36 | Au1rxx-base64 | 167.88.61.20 |
| 84.95 | trojan | 246.2 | 3.0 | 22.08 | 14.89 | 10.0 | 9.12 | 16.36 | Au1rxx-base64 | 66.163.114.45 |
| 84.69 | hysteria2 | 308.9 | 1.8 | 20.63 | 14.93 | 4.43 | 13.93 | 16.36 | Au1rxx-base64 | 66.94.121.46 |
| 84.63 | http | 293.6 | 1.2 | 20.98 | 14.96 | 0.0 | 14.48 | 19.78 | ermaozi | 138.199.35.202 |
| 84.46 | http | 304.7 | 0.1 | 20.72 | 15.0 | 0.0 | 14.48 | 19.78 | ermaozi | 138.199.35.203 |
| 84.44 | trojan | 257.0 | 9.0 | 21.83 | 14.66 | 10.0 | 9.12 | 16.36 | Au1rxx-base64 | 167.88.61.175 |
| 84.19 | trojan | 239.5 | 0.1 | 22.23 | 14.99 | 7.1 | 9.12 | 16.36 | Au1rxx-base64 | 66.163.114.245 |
| 83.88 | http | 226.6 | 0.4 | 22.53 | 14.99 | 0.0 | 14.48 | 19.78 | ermaozi | 172.64.69.89 |
| 83.55 | http | 260.0 | 1.6 | 21.76 | 14.94 | 0.0 | 14.48 | 19.78 | ermaozi | 138.199.35.205 |
| 82.7 | http | 290.4 | 0.8 | 21.05 | 14.97 | 0.0 | 14.48 | 19.78 | ermaozi | 138.199.35.198 |
| 82.62 | shadowsocks | 323.4 | 0.3 | 20.29 | 14.99 | 10.0 | 12.62 | 16.36 | Au1rxx-base64 | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.958 | 0.946 | 74 | 597 | prefer |
| Au1rxx-base64 | 0.888 | 0.821 | 196 | 1751 | prefer |
| mheidari-all | 0.834 | 0.761 | 67 | 14251 | prefer |
| Surfboard-tg-mixed | 0.816 | 0.738 | 248 | 8942 | prefer |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4551 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 162 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| ermaozi-get_subscribe | 0.274 | 1.0 | 1 | 471 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4900 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11507 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6457 | observe |
| barry-far-vless | 0.255 | None | 0 | 6640 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 49 |
| speed | ClientOSError | - | 28 |
| 204 | ProxyError | - | 18 |
| cn-block | TimeoutError | - | 7 |
| 204 | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 89 | 37 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
