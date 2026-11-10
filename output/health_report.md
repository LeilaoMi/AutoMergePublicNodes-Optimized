# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-10 01:45:35 |
| 运行耗时 | 308.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81932 |
| 去重后节点 | 26820 |
| TCP 可达 | 3000 |
| 真实可用 | 600 |
| Verified 输出 | 145 |
| Global 输出 | 300 |
| All 输出 | 26820 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.5 |
| tcp | 78.2 |
| probe | 90.8 |
| real_test | 87.1 |
| china_check | 29.6 |
| write_verified | 0.1 |
| generate | 14.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49470 |
| vmess | 14209 |
| shadowsocks | 9159 |
| trojan | 7011 |
| hysteria2 | 1570 |
| http | 246 |
| shadowsocksr | 149 |
| socks | 52 |
| hysteria | 30 |
| tuic | 21 |
| anytls | 15 |

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
| 94.78 | shadowsocks | 240.6 | 5.9 | 22.21 | 14.78 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 37.19.198.160 |
| 94.72 | shadowsocks | 250.7 | 1.0 | 21.97 | 14.96 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 37.19.198.236 |
| 94.45 | shadowsocks | 260.7 | 2.1 | 21.74 | 14.92 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 37.19.198.244 |
| 94.08 | shadowsocks | 245.9 | 8.0 | 22.09 | 14.7 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 185.230.230.18 |
| 94.05 | shadowsocks | 278.7 | 1.8 | 21.33 | 14.93 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 37.19.198.243 |
| 93.84 | vless | 258.0 | 6.8 | 21.81 | 14.75 | 9.91 | 9.77 | 17.6 | Au1rxx-base64 | 159.89.87.21 |
| 93.75 | trojan | 262.5 | 1.5 | 21.7 | 14.94 | 8.51 | 13.5 | 17.6 | Au1rxx-base64 | 216.152.155.59 |
| 93.55 | trojan | 269.0 | 2.2 | 21.55 | 14.92 | 8.48 | 13.5 | 17.6 | Au1rxx-base64 | 170.101.101.19 |
| 93.1 | vless | 287.8 | 6.2 | 21.12 | 14.77 | 9.84 | 9.77 | 17.6 | Au1rxx-base64 | 66.70.179.198 |
| 92.66 | trojan | 286.5 | 10.9 | 21.15 | 14.59 | 9.39 | 13.5 | 17.6 | Au1rxx-base64 | 216.152.147.48 |
| 92.61 | trojan | 352.6 | 2.8 | 19.62 | 14.89 | 10.0 | 13.5 | 17.6 | Au1rxx-base64 | 69.164.240.85 |
| 92.21 | trojan | 261.6 | 1.5 | 21.72 | 14.94 | 6.95 | 13.5 | 17.6 | Au1rxx-base64 | 216.152.155.23 |
| 92.0 | vless | 336.8 | 6.9 | 19.98 | 14.74 | 9.91 | 9.77 | 17.6 | Au1rxx-base64 | 169.40.42.202 |
| 91.87 | shadowsocks | 295.1 | 12.7 | 20.95 | 14.52 | 9.36 | 14.19 | 17.6 | Au1rxx-base64 | 193.151.160.18 |
| 91.24 | shadowsocks | 281.1 | 2.2 | 21.27 | 14.92 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 156.146.38.168 |
| 91.09 | shadowsocks | 284.8 | 3.4 | 21.18 | 14.87 | 7.25 | 14.19 | 17.6 | Au1rxx-base64 | 198.98.53.130 |
| 90.74 | shadowsocks | 399.4 | 2.0 | 18.53 | 14.92 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 45.86.51.18 |
| 90.62 | shadowsocks | 246.8 | 1.1 | 22.06 | 14.96 | 10.0 | 14.19 | 17.6 | Au1rxx-base64 | 193.151.163.18 |
| 90.59 | trojan | 290.3 | 2.0 | 21.06 | 14.92 | 10.0 | 13.5 | 17.6 | Au1rxx-base64 | 66.163.114.45 |
| 90.57 | vless | 260.8 | 3.2 | 21.74 | 14.88 | 9.92 | 9.77 | 17.6 | Au1rxx-base64 | 167.17.69.171 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 1.0 | 87 | 602 | prefer |
| Surfboard-tg-mixed | 0.936 | 0.86 | 214 | 8250 | prefer |
| Au1rxx-base64 | 0.897 | 0.829 | 258 | 1751 | prefer |
| mheidari-all | 0.743 | 0.665 | 170 | 14061 | prefer |
| DeltaKronecker-all | 0.349 | 0.667 | 3 | 2754 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11226 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6133 | observe |
| barry-far-vless | 0.255 | None | 0 | 6103 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4583 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.207 | 0.0 | 1 | 4976 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 90 |
| speed | ClientOSError | - | 14 |
| geo | ClientOSError | - | 9 |
| 204 | ProxyError | - | 7 |
| cn-block | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | status | 530 | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 49 | 145 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
