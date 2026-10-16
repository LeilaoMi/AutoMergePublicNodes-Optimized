# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 14:42:19 |
| 运行耗时 | 289.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99222 |
| 去重后节点 | 27685 |
| TCP 可达 | 3000 |
| 真实可用 | 343 |
| Verified 输出 | 50 |
| Global 输出 | 300 |
| All 输出 | 27685 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.5 |
| tcp | 91.9 |
| probe | 65.6 |
| real_test | 82.9 |
| china_check | 34.0 |
| write_verified | 0.0 |
| generate | 8.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58510 |
| vmess | 16398 |
| shadowsocks | 11895 |
| trojan | 10173 |
| hysteria2 | 1309 |
| http | 662 |
| shadowsocksr | 164 |
| socks | 59 |
| anytls | 29 |
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
| 93.11 | shadowsocks | 224.4 | 0.2 | 22.58 | 14.99 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 156.146.38.170 |
| 93.06 | shadowsocks | 225.4 | 1.1 | 22.56 | 14.96 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 156.146.38.168 |
| 92.94 | shadowsocks | 229.6 | 1.5 | 22.46 | 14.94 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 156.146.38.167 |
| 92.19 | shadowsocks | 264.1 | 0.3 | 21.66 | 14.99 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 156.146.38.169 |
| 91.39 | hysteria2 | 294.4 | 3.7 | 20.96 | 14.86 | 9.06 | 11.05 | 16.96 | Au1rxx-base64 | 129.213.91.185 |
| 89.97 | vless | 254.2 | 9.5 | 21.89 | 14.64 | 8.11 | 10.35 | 16.96 | Au1rxx-base64 | 131.143.180.110 |
| 89.47 | shadowsocks | 319.7 | 2.4 | 20.38 | 14.91 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 173.244.56.6 |
| 87.59 | shadowsocks | 331.9 | 4.4 | 20.1 | 14.84 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 37.19.198.160 |
| 85.01 | http | 284.4 | 1.6 | 21.2 | 14.94 | 0.0 | 14.5 | 20.0 | ermaozi | 138.199.35.198 |
| 84.4 | vless | 264.9 | 5.9 | 21.64 | 14.78 | 10.0 | 10.35 | 16.96 | Au1rxx-base64 | 147.45.60.160 |
| 83.6 | shadowsocks | 333.5 | 0.0 | 20.06 | 15.0 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 149.22.95.183 |
| 83.56 | vless | 362.1 | 6.3 | 19.4 | 14.76 | 7.84 | 10.35 | 16.96 | Au1rxx-base64 | 51.81.203.63 |
| 83.51 | shadowsocks | 337.9 | 5.0 | 19.96 | 14.81 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 37.19.198.244 |
| 82.75 | shadowsocks | 320.9 | 0.7 | 20.35 | 14.97 | 9.63 | 12.58 | 16.96 | Au1rxx-base64 | 149.22.87.240 |
| 82.68 | shadowsocks | 325.2 | 1.6 | 20.25 | 14.94 | 9.64 | 12.58 | 16.96 | Au1rxx-base64 | 149.22.87.241 |
| 82.64 | trojan | 388.9 | 2.3 | 18.78 | 14.91 | 9.54 | 12.86 | 16.96 | Au1rxx-base64 | 108.61.186.37 |
| 82.61 | shadowsocks | 332.0 | 3.8 | 20.09 | 14.86 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 37.19.198.236 |
| 82.61 | shadowsocks | 438.9 | 14.5 | 17.62 | 14.46 | 10.0 | 12.58 | 16.96 | Au1rxx-base64 | 51.222.136.236 |
| 82.16 | vless | 500.3 | 9.1 | 16.2 | 14.66 | 7.69 | 10.35 | 16.96 | Au1rxx-base64 | 185.95.231.156 |
| 82.1 | shadowsocks | 343.6 | 2.4 | 19.83 | 14.91 | 9.64 | 12.58 | 16.96 | Au1rxx-base64 | 149.22.87.204 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.959 | 0.949 | 59 | 618 | prefer |
| Au1rxx-base64 | 0.789 | 0.711 | 384 | 1991 | prefer |
| mheidari-all | 0.461 | 0.545 | 11 | 23974 | observe |
| DeltaKronecker-all | 0.4 | 0.75 | 4 | 4946 | observe |
| Surfboard-tg-mixed | 0.391 | 1.0 | 2 | 7090 | observe |
| ninja-vless | 0.291 | 0.4 | 5 | 1791 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1991 | observe |
| Epodonios-all | 0.255 | None | 0 | 7568 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10094 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5572 | observe |
| barry-far-vless | 0.255 | None | 0 | 5827 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 73 |
| speed | ClientOSError | - | 12 |
| 204 | ProxyError | - | 9 |
| geo | ClientOSError | - | 7 |
| cn-block | TimeoutError | - | 7 |
| 204 | TimeoutError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |
| speed | TimeoutError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 21 | 50 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
