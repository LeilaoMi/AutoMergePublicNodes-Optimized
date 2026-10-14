# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 12:17:16 |
| 运行耗时 | 320.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98058 |
| 去重后节点 | 27234 |
| TCP 可达 | 3000 |
| 真实可用 | 88 |
| Verified 输出 | 88 |
| Global 输出 | 98 |
| All 输出 | 27234 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.6 |
| tcp | 84.9 |
| probe | 111.1 |
| real_test | 57.2 |
| china_check | 28.1 |
| generate | 57.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57933 |
| vmess | 16089 |
| shadowsocks | 11784 |
| trojan | 10162 |
| hysteria2 | 1305 |
| http | 483 |
| shadowsocksr | 167 |
| socks | 86 |
| anytls | 25 |
| hysteria | 18 |
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
| 75.95 | shadowsocks | 262.8 | 662.8 | 21.7 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 156.146.38.167 |
| 75.39 | shadowsocks | 299.7 | 741.5 | 20.84 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.160 |
| 74.27 | hysteria2 | 289.2 | 722.8 | 21.08 | 0.0 | 10.0 | 11.25 | 16.44 | Au1rxx-base64 | 129.213.91.185 |
| 74.26 | shadowsocks | 249.3 | 624.5 | 22.01 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 156.146.38.168 |
| 74.2 | shadowsocks | 309.4 | 762.2 | 20.62 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.244 |
| 72.99 | shadowsocks | 308.3 | 670.7 | 20.64 | 0.0 | 10.0 | 12.81 | 16.44 | Au1rxx-base64 | 140.82.63.79 |
| 72.6 | vless | 298.8 | 729.2 | 20.86 | 0.0 | 9.28 | 9.02 | 16.44 | Au1rxx-base64 | 216.9.226.22 |
| 72.32 | shadowsocks | 373.8 | 967.5 | 19.13 | 0.0 | 9.92 | 12.81 | 16.44 | Au1rxx-base64 | 15.204.233.41 |
| 72.0 | shadowsocks | 246.4 | 618.7 | 22.08 | 0.0 | 6.22 | 12.81 | 16.44 | Au1rxx-base64 | 156.146.38.169 |
| 71.37 | shadowsocks | 302.9 | 740.7 | 20.77 | 0.0 | 7.31 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.243 |
| 71.27 | shadowsocks | 309.6 | 752.4 | 20.61 | 0.0 | 8.51 | 12.81 | 16.44 | Au1rxx-base64 | 37.19.198.236 |
| 71.11 | vless | 334.7 | 762.4 | 20.03 | 0.0 | 8.82 | 9.02 | 16.44 | Au1rxx-base64 | 66.70.179.198 |
| 70.81 | vless | 336.8 | 720.1 | 19.98 | 0.0 | 10.0 | 9.02 | 16.44 | Au1rxx-base64 | 45.32.69.110 |
| 69.93 | vless | 327.7 | 595.3 | 20.19 | 0.0 | 10.0 | 9.02 | 16.44 | Au1rxx-base64 | 154.29.145.196 |
| 69.7 | shadowsocks | 290.9 | 587.5 | 21.04 | 0.0 | 7.2 | 12.81 | 16.44 | Au1rxx-base64 | 173.244.56.6 |
| 68.5 | vless | 429.8 | 1006.4 | 17.83 | 0.0 | 8.12 | 9.02 | 16.44 | Au1rxx-base64 | 193.233.202.250 |
| 68.45 | vless | 369.8 | 925.6 | 19.22 | 0.0 | 8.27 | 9.02 | 16.44 | Au1rxx-base64 | 69.48.201.136 |
| 67.92 | vless | 432.5 | 765.7 | 17.77 | 0.0 | 9.91 | 9.02 | 16.44 | Au1rxx-base64 | 154.12.38.159 |
| 66.69 | vless | 408.7 | 756.2 | 18.32 | 0.0 | 9.51 | 9.02 | 16.44 | Au1rxx-base64 | 185.200.199.75 |
| 66.28 | vless | 501.0 | 1045.9 | 16.18 | 0.0 | 9.91 | 9.02 | 16.44 | Au1rxx-base64 | 209.200.246.148 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.968 | 0.957 | 70 | 598 | prefer |
| zhangkai | 0.927 | 1.0 | 19 | 144 | prefer |
| mheidari-all | 0.866 | 0.796 | 54 | 23983 | prefer |
| Au1rxx-base64 | 0.841 | 0.773 | 211 | 1782 | prefer |
| Surfboard-tg-mixed | 0.716 | 0.64 | 86 | 7056 | prefer |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5125 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 4803 | observe |
| Epodonios-all | 0.255 | None | 0 | 7542 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9836 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5579 | observe |
| barry-far-vless | 0.255 | None | 0 | 5831 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 44 |
| speed | ClientOSError | - | 12 |
| geo | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 7 |
| cn-block | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 3 |
| 204 | ProxyError | - | 2 |
| speed | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 84 | 88 | - |
| global | False | 91 | 98 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
