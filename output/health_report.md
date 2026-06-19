# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.9.1 |
| 更新时间 | 2026-06-19 15:39:19 |
| 运行耗时 | 433.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 73391 |
| 去重后节点 | 22037 |
| TCP 可达 | 771 |
| 真实可用 | 647 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22037 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.3 |
| tcp | 67.5 |
| probe | 101.4 |
| real_test | 222.5 |
| generate | 35.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42212 |
| shadowsocks | 10579 |
| trojan | 10136 |
| vmess | 9869 |
| hysteria2 | 228 |
| shadowsocksr | 164 |
| http | 107 |
| socks | 69 |
| anytls | 19 |
| hysteria | 6 |
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
| 78.39 | shadowsocks | 216.0 | 522.7 | 22.78 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 173.244.56.9 |
| 78.11 | shadowsocks | 227.9 | 535.9 | 22.5 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 149.22.95.183 |
| 78.03 | vless | 308.9 | 812.2 | 20.63 | 0.0 | 10.0 | 11.08 | 18.32 | Au1rxx-base64 | 15.204.97.214 |
| 76.52 | shadowsocks | 188.5 | 474.9 | 23.41 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 216.105.168.18 |
| 74.78 | vless | 319.7 | 838.6 | 20.38 | 0.0 | 10.0 | 11.08 | 18.32 | Au1rxx-base64 | 15.204.97.219 |
| 73.67 | shadowsocks | 295.6 | 657.6 | 20.94 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 156.146.38.170 |
| 73.61 | shadowsocks | 269.3 | 680.4 | 21.54 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 173.244.56.6 |
| 72.78 | shadowsocks | 301.5 | 675.0 | 20.8 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 156.146.38.167 |
| 72.33 | shadowsocks | 287.8 | 643.5 | 21.12 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 156.146.38.169 |
| 71.83 | shadowsocks | 294.5 | 344.5 | 20.96 | 2.08 | 9.95 | 13.79 | 18.32 | Au1rxx-base64 | 149.22.87.240 |
| 71.6 | shadowsocks | 297.9 | 347.6 | 20.88 | 1.96 | 9.95 | 13.79 | 18.32 | Au1rxx-base64 | 149.22.87.241 |
| 71.33 | shadowsocks | 388.3 | 948.7 | 18.79 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 156.146.38.168 |
| 70.57 | shadowsocks | 304.5 | 370.2 | 20.73 | 1.12 | 9.93 | 13.79 | 18.32 | Au1rxx-base64 | 149.22.87.204 |
| 69.05 | shadowsocks | 370.0 | 748.2 | 19.21 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 37.19.198.236 |
| 68.75 | shadowsocks | 350.5 | 692.4 | 19.66 | 0.0 | 10.0 | 13.79 | 17.3 | mheidari-all | 198.98.53.130 |
| 68.39 | shadowsocks | 374.6 | 744.2 | 19.11 | 0.0 | 10.0 | 13.79 | 18.32 | Au1rxx-base64 | 37.19.198.160 |
| 68.3 | vless | 350.9 | 405.1 | 19.65 | 0.0 | 9.94 | 11.08 | 16.64 | Surfboard-tg-mixed | 31.76.91.18 |
| 68.19 | vless | 354.8 | 388.0 | 19.57 | 0.45 | 9.94 | 11.08 | 16.64 | Surfboard-tg-mixed | 31.76.91.24 |
| 67.88 | vless | 335.1 | 682.6 | 20.02 | 0.0 | 10.0 | 11.08 | 16.64 | Surfboard-tg-mixed | 84.32.131.99 |
| 67.82 | vless | 351.7 | 395.2 | 19.64 | 0.18 | 9.94 | 11.08 | 16.64 | Surfboard-tg-mixed | 31.76.91.28 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | 1.0 | 25 | 73 | prefer |
| mheidari-all | 0.919 | 0.842 | 284 | 14955 | prefer |
| Surfboard-tg-mixed | 0.918 | 0.84 | 388 | 4956 | prefer |
| Au1rxx-base64 | 0.837 | 0.857 | 28 | 85 | prefer |
| DeltaKronecker-all | 0.776 | 0.705 | 44 | 6989 | prefer |
| nscl5-all | 0.309 | 1.0 | 1 | 1360 | observe |
| xiaoji235-airport-v2ray-all | 0.289 | 1.0 | 1 | 844 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4458 | observe |
| Epodonios-all | 0.255 | None | 0 | 7116 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3981 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7256 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3736 | observe |
| barry-far-vless | 0.255 | None | 0 | 4206 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4527 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 34 |
| cn-block | TimeoutError | - | 23 |
| 204 | ProxyError | - | 16 |
| 204 | TimeoutError | - | 12 |
| speed | TimeoutError | - | 7 |
| geo | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| geo | ClientOSError | - | 5 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 4 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
