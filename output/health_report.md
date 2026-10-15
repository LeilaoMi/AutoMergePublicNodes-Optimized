# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-15 11:15:54 |
| 运行耗时 | 314.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99769 |
| 去重后节点 | 27864 |
| TCP 可达 | 3000 |
| 真实可用 | 100 |
| Verified 输出 | 100 |
| Global 输出 | 104 |
| All 输出 | 27864 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.5 |
| tcp | 88.3 |
| probe | 101.4 |
| real_test | 71.5 |
| china_check | 33.7 |
| write_verified | 0.0 |
| generate | 11.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58912 |
| vmess | 16425 |
| shadowsocks | 12085 |
| trojan | 10184 |
| hysteria2 | 1166 |
| http | 706 |
| shadowsocksr | 170 |
| socks | 66 |
| anytls | 32 |
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
| 73.64 | shadowsocks | 242.2 | 615.0 | 22.17 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 156.146.38.170 |
| 73.52 | shadowsocks | 304.5 | 651.0 | 20.73 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 173.244.56.9 |
| 73.29 | shadowsocks | 300.9 | 645.0 | 20.81 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 173.244.56.6 |
| 73.27 | shadowsocks | 246.4 | 629.5 | 22.07 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 156.146.38.168 |
| 73.03 | http | 255.7 | 565.7 | 21.86 | 0.0 | 0.0 | 14.75 | 19.92 | ermaozi | 64.98.50.100 |
| 71.89 | http | 252.8 | 568.0 | 21.93 | 0.0 | 0.0 | 14.75 | 19.92 | ermaozi | 138.199.35.198 |
| 71.8 | shadowsocks | 327.1 | 678.5 | 20.21 | 0.0 | 9.79 | 13.61 | 16.64 | Au1rxx-base64 | 149.22.95.183 |
| 71.56 | shadowsocks | 358.0 | 841.4 | 19.49 | 0.0 | 9.98 | 13.61 | 16.64 | Au1rxx-base64 | 37.19.198.244 |
| 70.71 | shadowsocks | 242.1 | 619.6 | 22.17 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 156.146.38.169 |
| 70.5 | shadowsocks | 243.7 | 616.4 | 22.14 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 156.146.38.167 |
| 69.26 | vless | 286.2 | 642.2 | 21.15 | 0.0 | 5.06 | 8.77 | 16.64 | Au1rxx-base64 | 216.227.161.95 |
| 68.79 | http | 254.4 | 558.8 | 21.89 | 0.0 | 0.0 | 14.75 | 19.92 | ermaozi | 138.199.35.216 |
| 68.62 | shadowsocks | 349.1 | 842.5 | 19.7 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 103.214.109.45 |
| 68.05 | shadowsocks | 360.9 | 835.5 | 19.42 | 0.0 | 6.21 | 13.61 | 16.64 | Au1rxx-base64 | 37.19.198.243 |
| 67.75 | http | 313.7 | 615.1 | 20.52 | 0.0 | 0.0 | 14.75 | 19.92 | ermaozi | 129.153.93.183 |
| 66.69 | shadowsocks | 353.9 | 796.5 | 19.59 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 37.19.198.236 |
| 66.59 | vless | 372.9 | 763.1 | 19.15 | 0.0 | 6.86 | 8.77 | 16.64 | Au1rxx-base64 | 193.233.202.250 |
| 66.33 | shadowsocks | 441.3 | 528.8 | 17.56 | 0.0 | 10.0 | 13.61 | 16.64 | Au1rxx-base64 | 103.11.76.248 |
| 65.9 | hysteria2 | 346.5 | 858.4 | 19.76 | 0.0 | 0.0 | 11.79 | 16.64 | Au1rxx-base64 | 129.213.91.185 |
| 64.89 | shadowsocks | 347.1 | 844.4 | 19.74 | 0.0 | 6.32 | 13.61 | 16.64 | Au1rxx-base64 | 64.110.25.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.956 | 0.938 | 81 | 703 | prefer |
| Au1rxx-base64 | 0.821 | 0.752 | 274 | 1769 | prefer |
| mheidari-all | 0.671 | 0.6 | 20 | 24005 | observe |
| Surfboard-tg-mixed | 0.337 | 0.429 | 7 | 7139 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5089 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5147 | observe |
| Epodonios-all | 0.255 | None | 0 | 7652 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10113 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5693 | observe |
| barry-far-vless | 0.255 | None | 0 | 5924 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4338 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1769 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 53 |
| speed | ClientOSError | - | 7 |
| 204 | ProxyError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 6 |
| geo | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 62 | 100 | - |
| global | False | 72 | 104 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
