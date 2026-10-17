# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-17 11:00:37 |
| 运行耗时 | 301.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99307 |
| 去重后节点 | 27832 |
| TCP 可达 | 3000 |
| 真实可用 | 470 |
| Verified 输出 | 121 |
| Global 输出 | 300 |
| All 输出 | 27832 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.5 |
| tcp | 87.7 |
| probe | 82.2 |
| real_test | 91.7 |
| china_check | 21.6 |
| write_verified | 0.0 |
| generate | 10.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58118 |
| vmess | 16590 |
| shadowsocks | 12038 |
| trojan | 10223 |
| hysteria2 | 1343 |
| http | 717 |
| shadowsocksr | 168 |
| socks | 61 |
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
| 94.82 | shadowsocks | 219.7 | 1.8 | 22.69 | 14.93 | 8.89 | 13.99 | 18.32 | Au1rxx-base64 | 173.244.56.9 |
| 94.78 | shadowsocks | 219.7 | 6.1 | 22.69 | 14.77 | 9.01 | 13.99 | 18.32 | Au1rxx-base64 | 173.244.56.6 |
| 93.55 | shadowsocks | 265.5 | 6.3 | 21.63 | 14.76 | 8.85 | 13.99 | 18.32 | Au1rxx-base64 | 156.146.38.167 |
| 93.16 | shadowsocks | 264.8 | 6.5 | 21.65 | 14.75 | 8.83 | 13.99 | 18.32 | Au1rxx-base64 | 156.146.38.169 |
| 91.94 | shadowsocks | 258.6 | 0.6 | 21.79 | 14.98 | 8.85 | 13.99 | 18.32 | Au1rxx-base64 | 156.146.38.170 |
| 91.38 | vless | 205.6 | 7.4 | 23.02 | 14.72 | 6.88 | 8.44 | 18.32 | Au1rxx-base64 | 154.29.159.211 |
| 90.93 | vless | 282.5 | 0.9 | 21.24 | 14.97 | 8.35 | 8.44 | 18.32 | Au1rxx-base64 | 147.45.60.160 |
| 90.12 | vless | 204.8 | 0.6 | 23.04 | 14.98 | 5.34 | 8.44 | 18.32 | Au1rxx-base64 | 154.9.241.170 |
| 89.95 | http | 195.9 | 0.7 | 23.24 | 14.97 | 0.0 | 14.26 | 19.98 | ermaozi | 129.153.93.183 |
| 89.36 | http | 201.0 | 0.2 | 23.13 | 14.99 | 0.0 | 14.26 | 19.98 | ermaozi | 138.199.35.197 |
| 89.35 | shadowsocks | 328.8 | 5.3 | 20.17 | 14.8 | 6.57 | 13.99 | 18.32 | Au1rxx-base64 | 103.11.76.248 |
| 89.34 | http | 201.4 | 0.6 | 23.12 | 14.98 | 0.0 | 14.26 | 19.98 | ermaozi | 138.199.35.195 |
| 89.3 | http | 201.1 | 1.7 | 23.12 | 14.94 | 0.0 | 14.26 | 19.98 | ermaozi | 138.199.35.214 |
| 89.3 | http | 202.7 | 0.7 | 23.09 | 14.97 | 0.0 | 14.26 | 19.98 | ermaozi | 138.199.35.205 |
| 89.25 | shadowsocks | 291.8 | 2.5 | 21.02 | 14.91 | 8.61 | 13.99 | 18.32 | Au1rxx-base64 | 149.22.95.183 |
| 89.24 | http | 206.2 | 0.2 | 23.01 | 14.99 | 0.0 | 14.26 | 19.98 | ermaozi | 138.199.35.199 |
| 89.22 | http | 204.0 | 2.3 | 23.06 | 14.92 | 0.0 | 14.26 | 19.98 | ermaozi | 138.199.35.216 |
| 89.06 | http | 206.1 | 5.2 | 23.01 | 14.81 | 0.0 | 14.26 | 19.98 | ermaozi | 138.199.35.198 |
| 88.5 | http | 255.5 | 2.5 | 21.86 | 14.9 | 0.0 | 14.26 | 19.98 | ermaozi | fan.365747.xyz |
| 88.38 | vless | 278.0 | 3.6 | 21.34 | 14.87 | 8.02 | 8.44 | 18.32 | Au1rxx-base64 | 51.81.203.63 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.979 | 0.96 | 99 | 702 | prefer |
| Au1rxx-base64 | 0.898 | 0.819 | 426 | 1994 | prefer |
| Surfboard-tg-mixed | 0.48 | 0.395 | 43 | 7171 | observe |
| mheidari-all | 0.385 | 0.5 | 8 | 23828 | observe |
| Epodonios-all | 0.335 | 1.0 | 1 | 7611 | observe |
| DeltaKronecker-all | 0.292 | 0.194 | 31 | 4999 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4986 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1994 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9902 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5617 | observe |
| barry-far-vless | 0.255 | None | 0 | 5842 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4255 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 71 |
| geo | ClientOSError | - | 22 |
| speed | ClientOSError | - | 12 |
| 204 | TimeoutError | - | 11 |
| 204 | ProxyError | - | 9 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 145 | 121 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
