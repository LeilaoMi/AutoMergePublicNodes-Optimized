# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-24 07:13:07 |
| 运行耗时 | 307.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 78696 |
| 去重后节点 | 21962 |
| TCP 可达 | 3000 |
| 真实可用 | 715 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21962 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.4 |
| tcp | 34.2 |
| probe | 61.2 |
| real_test | 169.3 |
| generate | 35.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48967 |
| shadowsocks | 10352 |
| vmess | 10008 |
| trojan | 7779 |
| hysteria2 | 1199 |
| http | 164 |
| shadowsocksr | 129 |
| socks | 89 |
| hysteria | 7 |
| tuic | 2 |

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
| 82.59 | shadowsocks | 225.9 | 571.9 | 22.55 | 0.0 | 10.0 | 14.38 | 19.66 | Au1rxx-base64 | 154.12.240.141 |
| 82.21 | shadowsocks | 242.4 | 593.6 | 22.17 | 0.0 | 10.0 | 14.38 | 19.66 | Au1rxx-base64 | 149.22.95.183 |
| 82.19 | shadowsocks | 232.5 | 545.2 | 22.4 | 0.0 | 10.0 | 14.38 | 19.66 | Au1rxx-base64 | 154.53.60.212 |
| 82.0 | shadowsocks | 235.5 | 551.7 | 22.33 | 0.0 | 10.0 | 14.38 | 19.66 | Au1rxx-base64 | 94.72.127.55 |
| 81.52 | shadowsocks | 233.9 | 577.8 | 22.36 | 0.0 | 10.0 | 14.38 | 19.66 | Au1rxx-base64 | 94.72.127.58 |
| 80.64 | trojan | 239.9 | 556.2 | 22.23 | 0.0 | 10.0 | 11.25 | 19.66 | Au1rxx-base64 | sincere-gelding.rooster465.autos |
| 80.48 | vless | 290.1 | 602.1 | 21.06 | 0.0 | 10.0 | 10.06 | 19.66 | Au1rxx-base64 | 150.241.102.202 |
| 80.37 | trojan | 251.1 | 584.6 | 21.96 | 0.0 | 10.0 | 11.25 | 19.66 | Au1rxx-base64 | 44.251.158.80 |
| 80.32 | vless | 310.0 | 815.1 | 20.6 | 0.0 | 10.0 | 10.06 | 19.66 | Au1rxx-base64 | 15.204.97.195 |
| 80.29 | vless | 311.5 | 742.2 | 20.57 | 0.0 | 10.0 | 10.06 | 19.66 | Au1rxx-base64 | 150.241.82.19 |
| 80.26 | vless | 312.6 | 819.8 | 20.54 | 0.0 | 10.0 | 10.06 | 19.66 | Au1rxx-base64 | 15.204.97.214 |
| 80.11 | vless | 319.0 | 847.0 | 20.39 | 0.0 | 10.0 | 10.06 | 19.66 | Au1rxx-base64 | 15.204.97.197 |
| 79.94 | trojan | 265.5 | 636.5 | 21.63 | 0.0 | 10.0 | 11.25 | 19.66 | Au1rxx-base64 | 35.91.251.124 |
| 79.62 | vless | 281.9 | 646.6 | 21.25 | 0.0 | 10.0 | 10.06 | 19.66 | Au1rxx-base64 | 150.241.102.8 |
| 78.96 | shadowsocks | 260.7 | 635.6 | 21.74 | 0.0 | 10.0 | 14.38 | 17.34 | Surfboard-tg-mixed | 108.181.0.177 |
| 78.77 | trojan | 238.2 | 548.2 | 22.26 | 0.0 | 8.1 | 11.25 | 19.66 | Au1rxx-base64 | obliging-louse.rooster465.autos |
| 78.6 | http | 474.8 | 1339.0 | 16.79 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.216 |
| 78.55 | http | 477.0 | 1348.8 | 16.74 | 0.0 | 10.0 | 14.87 | 19.94 | zhangkai | 138.199.35.198 |
| 78.16 | vless | 272.4 | 615.3 | 21.47 | 0.0 | 10.0 | 10.06 | 19.66 | Au1rxx-base64 | us.windconnect.pro |
| 78.06 | trojan | 351.2 | 969.3 | 19.65 | 0.0 | 10.0 | 11.25 | 19.66 | Au1rxx-base64 | 34.94.125.227 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | 1.0 | 113 | 144 | prefer |
| Au1rxx-base64 | 0.97 | 0.903 | 382 | 1718 | prefer |
| mheidari-all | 0.922 | 0.861 | 36 | 14629 | prefer |
| Surfboard-tg-mixed | 0.844 | 0.768 | 155 | 6484 | prefer |
| DeltaKronecker-all | 0.4 | 0.319 | 329 | 5914 | observe |
| nscl5-all | 0.309 | 0.667 | 3 | 1008 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4899 | observe |
| Epodonios-all | 0.255 | None | 0 | 6867 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7231 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5385 | observe |
| barry-far-vless | 0.255 | None | 0 | 5530 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4097 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1728 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 126 |
| geo | ClientOSError | - | 53 |
| speed | ClientOSError | - | 33 |
| speed | TimeoutError | - | 32 |
| 204 | TimeoutError | - | 22 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyError | - | 12 |
| cn-block | ClientOSError | - | 11 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
