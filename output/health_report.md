# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-05 10:24:32 |
| 运行耗时 | 276.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 83253 |
| 去重后节点 | 22135 |
| TCP 可达 | 3000 |
| 真实可用 | 504 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22135 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| geo | 1.4 |
| tcp | 37.3 |
| probe | 87.3 |
| real_test | 113.9 |
| generate | 30.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52816 |
| vmess | 11203 |
| shadowsocks | 9747 |
| trojan | 7845 |
| hysteria2 | 1292 |
| http | 146 |
| shadowsocksr | 131 |
| socks | 53 |
| hysteria | 10 |
| tuic | 10 |

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
| 83.05 | shadowsocks | 201.4 | 479.8 | 23.12 | 0.0 | 10.0 | 14.57 | 19.86 | Au1rxx-base64 | 108.181.118.10 |
| 82.23 | shadowsocks | 258.2 | 627.0 | 21.8 | 0.0 | 10.0 | 14.57 | 19.86 | Au1rxx-base64 | 156.146.38.170 |
| 82.11 | shadowsocks | 263.3 | 638.1 | 21.68 | 0.0 | 10.0 | 14.57 | 19.86 | Au1rxx-base64 | 156.146.38.167 |
| 81.75 | vless | 198.1 | 509.5 | 23.19 | 0.0 | 10.0 | 8.7 | 19.86 | Au1rxx-base64 | 172.235.38.85 |
| 81.63 | vless | 203.6 | 539.5 | 23.07 | 0.0 | 10.0 | 8.7 | 19.86 | Au1rxx-base64 | 172.233.139.46 |
| 81.55 | vless | 206.7 | 529.0 | 22.99 | 0.0 | 10.0 | 8.7 | 19.86 | Au1rxx-base64 | 172.235.43.210 |
| 80.17 | hysteria2 | 256.5 | 589.9 | 21.84 | 0.0 | 10.0 | 13.57 | 19.86 | Au1rxx-base64 | 66.94.121.46 |
| 79.78 | shadowsocks | 239.5 | 598.2 | 22.23 | 0.0 | 10.0 | 14.57 | 17.48 | Surfboard-tg-mixed | 108.181.0.177 |
| 79.64 | vless | 202.7 | 521.7 | 23.08 | 0.0 | 10.0 | 8.7 | 19.86 | Au1rxx-base64 | 38.209.125.45 |
| 79.6 | shadowsocks | 262.1 | 630.5 | 21.71 | 0.0 | 10.0 | 14.57 | 17.48 | Surfboard-tg-mixed | 156.146.38.168 |
| 79.43 | shadowsocks | 251.8 | 605.9 | 21.95 | 0.0 | 10.0 | 14.57 | 17.48 | Surfboard-tg-mixed | 156.146.38.169 |
| 79.42 | shadowsocks | 278.5 | 619.8 | 21.33 | 0.0 | 10.0 | 14.57 | 19.86 | Au1rxx-base64 | 23.150.248.20 |
| 78.86 | shadowsocks | 273.9 | 573.4 | 21.44 | 0.0 | 10.0 | 14.57 | 19.86 | Au1rxx-base64 | 149.22.95.183 |
| 77.35 | vless | 193.8 | 503.6 | 23.29 | 0.0 | 10.0 | 8.7 | 19.86 | Au1rxx-base64 | 204.44.127.222 |
| 77.29 | shadowsocks | 255.5 | 624.3 | 21.86 | 0.0 | 10.0 | 14.57 | 19.86 | Au1rxx-base64 | 173.244.56.9 |
| 76.93 | shadowsocks | 308.5 | 296.4 | 20.64 | 3.88 | 9.88 | 14.57 | 19.86 | Au1rxx-base64 | 176.97.73.215 |
| 76.81 | vless | 210.3 | 541.1 | 22.91 | 0.0 | 10.0 | 8.7 | 19.86 | Au1rxx-base64 | 23.94.227.94 |
| 76.69 | shadowsocks | 281.5 | 640.3 | 21.26 | 0.0 | 10.0 | 14.57 | 19.86 | Au1rxx-base64 | 173.244.56.6 |
| 76.24 | http | 419.2 | 1180.2 | 18.07 | 0.0 | 10.0 | 13.55 | 17.62 | zhangkai | 138.199.35.198 |
| 76.12 | http | 424.7 | 1194.5 | 17.95 | 0.0 | 10.0 | 13.55 | 17.62 | zhangkai | 138.199.35.216 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| Au1rxx-base64 | 0.955 | 0.886 | 271 | 1813 | prefer |
| Surfboard-tg-mixed | 0.878 | 0.801 | 171 | 7332 | prefer |
| mheidari-all | 0.862 | 0.787 | 108 | 15508 | prefer |
| DeltaKronecker-all | 0.688 | 0.667 | 18 | 6212 | observe |
| tg-oneclickvpnkeys | 0.518 | 1.0 | 7 | 118 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4887 | observe |
| Epodonios-all | 0.255 | None | 0 | 7793 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8561 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6108 | observe |
| barry-far-vless | 0.255 | None | 0 | 6302 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4095 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1813 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 22 |
| geo | ClientOSError | - | 15 |
| cn-block | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 11 |
| 204 | ProxyError | - | 9 |
| geo | TimeoutError | - | 6 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 6 |
| speed | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
