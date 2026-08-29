# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-29 16:36:07 |
| 运行耗时 | 260.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 78465 |
| 去重后节点 | 21216 |
| TCP 可达 | 3000 |
| 真实可用 | 618 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21216 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.3 |
| tcp | 34.7 |
| probe | 52.2 |
| real_test | 120.1 |
| generate | 46.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48930 |
| vmess | 11164 |
| shadowsocks | 10533 |
| trojan | 6005 |
| hysteria2 | 1455 |
| http | 173 |
| shadowsocksr | 132 |
| socks | 59 |
| hysteria | 7 |
| tuic | 5 |
| anytls | 2 |

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
| 83.56 | http | 194.6 | 503.0 | 23.27 | 0.0 | 10.0 | 13.97 | 19.32 | zhangkai | 138.199.35.216 |
| 83.4 | vless | 212.0 | 530.1 | 22.87 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 166.88.186.151 |
| 83.38 | trojan | 187.0 | 479.3 | 23.45 | 0.0 | 10.0 | 13.75 | 19.18 | Au1rxx-base64 | 14.1.28.76 |
| 82.49 | vless | 208.1 | 499.3 | 22.96 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 64.23.229.123 |
| 82.13 | trojan | 240.9 | 627.1 | 22.2 | 0.0 | 10.0 | 13.75 | 19.18 | Au1rxx-base64 | us01.duotg.top |
| 82.04 | shadowsocks | 187.9 | 453.0 | 23.43 | 0.0 | 10.0 | 13.93 | 19.18 | Au1rxx-base64 | 108.181.118.10 |
| 81.97 | shadowsocks | 190.9 | 462.7 | 23.36 | 0.0 | 10.0 | 13.93 | 19.18 | Au1rxx-base64 | 108.181.0.177 |
| 81.4 | shadowsocks | 237.0 | 523.8 | 22.29 | 0.0 | 10.0 | 13.93 | 19.18 | Au1rxx-base64 | 173.244.56.6 |
| 81.39 | http | 193.7 | 495.7 | 23.29 | 0.0 | 10.0 | 13.97 | 19.32 | zhangkai | 138.199.35.198 |
| 81.25 | shadowsocks | 243.6 | 591.6 | 22.14 | 0.0 | 10.0 | 13.93 | 19.18 | Au1rxx-base64 | 156.146.38.169 |
| 81.04 | shadowsocks | 252.8 | 611.9 | 21.93 | 0.0 | 10.0 | 13.93 | 19.18 | Au1rxx-base64 | 156.146.38.170 |
| 80.85 | vless | 192.4 | 491.8 | 23.32 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 172.233.156.123 |
| 80.79 | vless | 195.0 | 505.5 | 23.26 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 172.233.139.46 |
| 80.74 | vless | 197.3 | 517.3 | 23.21 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 172.233.156.42 |
| 80.73 | vless | 197.8 | 497.4 | 23.2 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 192.204.45.220 |
| 80.7 | vless | 199.2 | 507.5 | 23.17 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 172.235.43.210 |
| 80.62 | vless | 202.4 | 467.4 | 23.09 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 216.167.21.162 |
| 80.42 | vless | 211.1 | 531.5 | 22.89 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 172.233.156.118 |
| 80.22 | vless | 219.8 | 520.1 | 22.69 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 173.255.242.56 |
| 80.19 | vless | 221.0 | 527.8 | 22.66 | 0.0 | 10.0 | 11.35 | 19.18 | Au1rxx-base64 | 45.33.107.237 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.995 | 0.925 | 372 | 1807 | prefer |
| Surfboard-tg-mixed | 0.955 | 0.885 | 78 | 6877 | prefer |
| zhangkai | 0.929 | 0.958 | 24 | 144 | prefer |
| mheidari-all | 0.895 | 0.823 | 79 | 14622 | prefer |
| DeltaKronecker-all | 0.865 | 0.789 | 142 | 4926 | prefer |
| tg-oneclickvpnkeys | 0.364 | 1.0 | 3 | 155 | observe |
| nscl5-all | 0.283 | 1.0 | 1 | 700 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4635 | observe |
| Epodonios-all | 0.255 | None | 0 | 7290 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7426 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5686 | observe |
| barry-far-vless | 0.255 | None | 0 | 5725 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4012 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 21 |
| cn-block | TimeoutError | - | 17 |
| speed | TimeoutError | - | 8 |
| geo | ClientOSError | - | 7 |
| speed | ClientOSError | - | 7 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 4 |
| geo | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| speed | ClientPayloadError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
