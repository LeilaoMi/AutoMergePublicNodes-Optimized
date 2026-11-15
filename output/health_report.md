# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-15 06:53:03 |
| 运行耗时 | 301.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83136 |
| 去重后节点 | 27053 |
| TCP 可达 | 3000 |
| 真实可用 | 449 |
| Verified 输出 | 67 |
| Global 输出 | 300 |
| All 输出 | 27053 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 78.5 |
| probe | 95.9 |
| real_test | 78.0 |
| china_check | 25.3 |
| write_verified | 0.0 |
| generate | 15.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49785 |
| vmess | 14789 |
| shadowsocks | 9679 |
| trojan | 6867 |
| hysteria2 | 1532 |
| http | 185 |
| shadowsocksr | 151 |
| socks | 77 |
| hysteria | 34 |
| anytls | 19 |
| tuic | 18 |

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
| 93.9 | shadowsocks | 239.1 | 2.8 | 22.24 | 14.9 | 10.0 | 13.7 | 17.56 | Au1rxx-base64 | 185.230.230.18 |
| 93.75 | shadowsocks | 248.5 | 1.0 | 22.03 | 14.96 | 10.0 | 13.7 | 17.56 | Au1rxx-base64 | 45.86.51.18 |
| 93.19 | vless | 328.1 | 1.4 | 20.18 | 14.95 | 9.92 | 10.58 | 17.56 | Au1rxx-base64 | 167.17.69.171 |
| 93.05 | vless | 325.0 | 4.9 | 20.26 | 14.82 | 9.83 | 10.58 | 17.56 | Au1rxx-base64 | 66.70.179.198 |
| 92.26 | shadowsocks | 294.9 | 4.1 | 20.95 | 14.85 | 10.0 | 13.7 | 17.56 | Au1rxx-base64 | 193.151.160.9 |
| 91.8 | shadowsocks | 294.6 | 2.4 | 20.96 | 14.91 | 9.17 | 13.7 | 17.56 | Au1rxx-base64 | 193.151.160.18 |
| 91.2 | vless | 401.6 | 3.2 | 18.48 | 14.88 | 9.91 | 10.58 | 17.56 | Au1rxx-base64 | 169.40.42.90 |
| 90.47 | shadowsocks | 284.4 | 3.8 | 21.19 | 14.86 | 10.0 | 13.7 | 17.56 | Au1rxx-base64 | 156.146.38.168 |
| 90.41 | trojan | 322.2 | 0.4 | 20.32 | 14.99 | 6.34 | 13.7 | 17.56 | Au1rxx-base64 | 216.152.155.23 |
| 90.2 | vless | 350.6 | 1.6 | 19.66 | 14.94 | 9.92 | 10.58 | 17.56 | Au1rxx-base64 | 169.40.42.168 |
| 90.07 | vless | 391.0 | 2.9 | 18.73 | 14.89 | 9.92 | 10.58 | 17.56 | Au1rxx-base64 | 169.40.42.89 |
| 89.99 | trojan | 273.9 | 7.7 | 21.44 | 14.71 | 8.08 | 13.7 | 17.56 | Au1rxx-base64 | 216.152.147.93 |
| 89.95 | trojan | 264.5 | 15.8 | 21.66 | 14.41 | 8.12 | 13.7 | 17.56 | Au1rxx-base64 | 216.152.155.59 |
| 89.49 | vless | 380.1 | 1.4 | 18.98 | 14.95 | 10.0 | 10.58 | 17.56 | Au1rxx-base64 | 169.40.42.35 |
| 89.07 | shadowsocks | 317.2 | 4.1 | 20.44 | 14.85 | 10.0 | 13.7 | 17.56 | Au1rxx-base64 | 156.146.38.167 |
| 88.77 | trojan | 376.6 | 4.0 | 19.06 | 14.85 | 10.0 | 13.7 | 17.56 | Au1rxx-base64 | 66.23.203.21 |
| 88.76 | trojan | 252.7 | 3.2 | 21.93 | 14.88 | 5.19 | 13.7 | 17.56 | Au1rxx-base64 | 216.152.155.176 |
| 88.51 | trojan | 312.0 | 0.2 | 20.55 | 14.99 | 5.15 | 13.7 | 17.56 | Au1rxx-base64 | 169.197.140.171 |
| 88.49 | trojan | 294.1 | 6.9 | 20.97 | 14.74 | 9.2 | 13.7 | 17.56 | Au1rxx-base64 | 216.152.147.48 |
| 88.41 | trojan | 258.9 | 5.4 | 21.79 | 14.8 | 6.06 | 13.7 | 17.56 | Au1rxx-base64 | 216.152.155.54 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.944 | 0.868 | 167 | 9013 | prefer |
| ermaozi | 0.93 | 0.927 | 41 | 576 | prefer |
| mheidari-all | 0.863 | 0.787 | 127 | 13787 | prefer |
| Au1rxx-base64 | 0.86 | 0.793 | 203 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.446 | 0.625 | 8 | 6752 | observe |
| DeltaKronecker-all | 0.335 | 1.0 | 1 | 2652 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4966 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11652 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6319 | observe |
| barry-far-vless | 0.255 | None | 0 | 6500 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4584 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 54 |
| 204 | ProxyError | - | 12 |
| 204 | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 5 |
| speed | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 5 |
| speed | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| speed | TimeoutError | - | 2 |
| geo | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 89 | 67 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
