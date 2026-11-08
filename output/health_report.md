# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-08 22:20:45 |
| 运行耗时 | 289.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81580 |
| 去重后节点 | 26785 |
| TCP 可达 | 3000 |
| 真实可用 | 494 |
| Verified 输出 | 84 |
| Global 输出 | 300 |
| All 输出 | 26785 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.5 |
| tcp | 81.0 |
| probe | 80.3 |
| real_test | 75.6 |
| china_check | 34.3 |
| write_verified | 0.0 |
| generate | 11.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48699 |
| vmess | 14284 |
| shadowsocks | 9059 |
| trojan | 7437 |
| hysteria2 | 1617 |
| http | 214 |
| shadowsocksr | 152 |
| socks | 54 |
| hysteria | 23 |
| tuic | 21 |
| anytls | 20 |

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
| 94.53 | shadowsocks | 272.1 | 0.4 | 21.48 | 14.98 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 156.146.38.167 |
| 93.46 | shadowsocks | 297.1 | 0.3 | 20.9 | 14.99 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 45.86.51.18 |
| 92.87 | trojan | 264.0 | 0.1 | 21.67 | 15.0 | 10.0 | 11.18 | 18.06 | Au1rxx-base64 | 66.163.114.45 |
| 92.49 | shadowsocks | 296.8 | 5.1 | 20.91 | 14.81 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 37.19.198.243 |
| 92.14 | shadowsocks | 295.1 | 4.5 | 20.95 | 14.83 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 37.19.198.236 |
| 91.44 | shadowsocks | 395.2 | 5.0 | 18.63 | 14.81 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 37.19.198.160 |
| 91.05 | trojan | 256.6 | 1.6 | 21.84 | 14.94 | 7.53 | 11.18 | 18.06 | Au1rxx-base64 | 66.163.114.245 |
| 91.02 | trojan | 262.0 | 0.9 | 21.71 | 14.97 | 8.48 | 11.18 | 18.06 | Au1rxx-base64 | 66.163.114.132 |
| 90.84 | trojan | 262.2 | 0.3 | 21.71 | 14.99 | 7.4 | 11.18 | 18.06 | Au1rxx-base64 | 66.163.114.114 |
| 90.77 | trojan | 246.0 | 2.4 | 22.08 | 14.91 | 7.38 | 11.18 | 18.06 | Au1rxx-base64 | 66.163.114.126 |
| 90.69 | trojan | 270.5 | 0.2 | 21.52 | 14.99 | 7.44 | 11.18 | 18.06 | Au1rxx-base64 | 66.163.114.106 |
| 90.66 | trojan | 270.9 | 0.7 | 21.51 | 14.97 | 7.44 | 11.18 | 18.06 | Au1rxx-base64 | 66.163.114.166 |
| 90.54 | shadowsocks | 296.5 | 2.9 | 20.91 | 14.89 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 185.230.230.18 |
| 90.37 | shadowsocks | 278.8 | 1.3 | 21.32 | 14.95 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 95.215.201.18 |
| 90.13 | vless | 235.6 | 1.4 | 22.32 | 14.95 | 7.36 | 10.5 | 18.06 | Au1rxx-base64 | 108.61.119.63 |
| 89.58 | shadowsocks | 286.6 | 2.1 | 21.14 | 14.92 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 173.244.56.9 |
| 89.23 | shadowsocks | 309.4 | 1.6 | 20.62 | 14.94 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 193.151.163.18 |
| 89.05 | shadowsocks | 276.0 | 0.7 | 21.39 | 14.97 | 10.0 | 14.01 | 18.06 | Au1rxx-base64 | 156.146.38.170 |
| 88.77 | vless | 314.3 | 2.4 | 20.5 | 14.91 | 9.1 | 10.5 | 18.06 | Au1rxx-base64 | 167.17.69.171 |
| 88.2 | http | 293.8 | 0.6 | 20.98 | 14.98 | 0.0 | 14.74 | 20.0 | ermaozi | 193.239.236.134 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.99 | 0.982 | 57 | 586 | prefer |
| mheidari-all | 0.964 | 0.892 | 93 | 13955 | prefer |
| Surfboard-tg-mixed | 0.917 | 0.84 | 194 | 8189 | prefer |
| Au1rxx-base64 | 0.875 | 0.808 | 234 | 1751 | prefer |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5035 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3024 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10983 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5913 | observe |
| barry-far-vless | 0.255 | None | 0 | 6123 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4597 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 50 |
| 204 | ProxyError | - | 13 |
| speed | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| 204 | TimeoutError | - | 2 |
| geo | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 68 | 84 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
