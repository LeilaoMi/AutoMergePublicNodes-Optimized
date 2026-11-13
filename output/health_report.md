# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-13 19:56:42 |
| 运行耗时 | 259.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 83309 |
| 去重后节点 | 26903 |
| TCP 可达 | 3000 |
| 真实可用 | 393 |
| Verified 输出 | 89 |
| Global 输出 | 300 |
| All 输出 | 26903 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| geo | 1.4 |
| tcp | 82.3 |
| probe | 71.2 |
| real_test | 71.6 |
| china_check | 19.2 |
| write_verified | 0.0 |
| generate | 9.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50006 |
| vmess | 14681 |
| shadowsocks | 9723 |
| trojan | 6859 |
| hysteria2 | 1508 |
| http | 253 |
| shadowsocksr | 149 |
| socks | 60 |
| hysteria | 34 |
| tuic | 20 |
| anytls | 16 |

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
| 90.61 | shadowsocks | 288.6 | 0.2 | 21.1 | 14.99 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 156.146.38.168 |
| 87.92 | shadowsocks | 297.2 | 1.9 | 20.9 | 14.93 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 185.230.230.18 |
| 87.49 | http | 274.1 | 1.8 | 21.43 | 14.93 | 0.0 | 14.21 | 19.42 | ermaozi | 172.64.68.89 |
| 86.74 | shadowsocks | 261.1 | 5.1 | 21.73 | 14.81 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 156.146.38.167 |
| 86.59 | shadowsocks | 317.5 | 1.2 | 20.43 | 14.96 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 193.151.163.18 |
| 86.15 | shadowsocks | 288.1 | 0.8 | 21.11 | 14.97 | 6.59 | 13.06 | 16.14 | Au1rxx-base64 | 156.146.38.169 |
| 85.98 | shadowsocks | 287.7 | 1.3 | 21.12 | 14.95 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 45.86.51.18 |
| 85.75 | shadowsocks | 266.9 | 28.1 | 21.6 | 13.95 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 156.146.38.170 |
| 85.26 | vless | 332.5 | 2.6 | 20.08 | 14.9 | 9.29 | 9.05 | 16.14 | Au1rxx-base64 | 167.17.69.171 |
| 85.05 | shadowsocks | 397.3 | 0.7 | 18.58 | 14.97 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 15.204.247.206 |
| 84.98 | http | 384.7 | 0.5 | 18.87 | 14.98 | 0.0 | 14.21 | 19.42 | ermaozi | 172.64.69.89 |
| 84.7 | hysteria2 | 302.0 | 30.2 | 20.79 | 13.87 | 3.66 | 13.0 | 16.14 | Au1rxx-base64 | 66.94.121.46 |
| 84.67 | shadowsocks | 314.8 | 2.6 | 20.49 | 14.9 | 8.23 | 13.06 | 16.14 | Au1rxx-base64 | 193.151.160.18 |
| 84.5 | vless | 411.5 | 0.6 | 18.25 | 14.98 | 10.0 | 9.05 | 16.14 | Au1rxx-base64 | 169.40.42.35 |
| 84.32 | shadowsocks | 284.6 | 2.0 | 21.19 | 14.93 | 10.0 | 13.06 | 16.14 | Au1rxx-base64 | 95.215.201.18 |
| 84.09 | http | 355.1 | 4.2 | 19.56 | 14.84 | 0.0 | 14.21 | 19.42 | ermaozi | 206.223.183.16 |
| 83.83 | vless | 294.4 | 0.4 | 20.96 | 14.98 | 7.24 | 9.05 | 16.14 | Au1rxx-base64 | 45.63.53.81 |
| 83.56 | http | 373.2 | 0.9 | 19.14 | 14.97 | 0.0 | 14.21 | 19.42 | ermaozi | 206.223.183.13 |
| 83.08 | vless | 352.0 | 0.5 | 19.63 | 14.98 | 9.4 | 9.05 | 16.14 | Au1rxx-base64 | 66.70.179.198 |
| 83.01 | http | 340.6 | 0.9 | 19.89 | 14.97 | 0.0 | 14.21 | 19.42 | ermaozi | 206.223.183.21 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.989 | 0.982 | 56 | 590 | prefer |
| Au1rxx-base64 | 0.818 | 0.752 | 153 | 1751 | prefer |
| Surfboard-tg-mixed | 0.799 | 0.721 | 226 | 8804 | prefer |
| mheidari-all | 0.767 | 0.691 | 81 | 14267 | prefer |
| xiaoji235-airport-v2ray-all | 0.349 | 0.667 | 3 | 6752 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| ermaozi-get_subscribe | 0.273 | 1.0 | 1 | 442 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4900 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2734 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11528 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6228 | observe |
| barry-far-vless | 0.255 | None | 0 | 6409 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4624 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 49 |
| 204 | ProxyError | - | 28 |
| speed | ClientOSError | - | 27 |
| 204 | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| speed | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | ClientOSError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 68 | 89 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
