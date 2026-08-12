# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-12 13:25:38 |
| 运行耗时 | 259.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 80149 |
| 去重后节点 | 22315 |
| TCP 可达 | 3000 |
| 真实可用 | 587 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22315 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.6 |
| geo | 1.4 |
| tcp | 33.2 |
| probe | 54.3 |
| real_test | 125.9 |
| generate | 35.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46136 |
| vmess | 13300 |
| shadowsocks | 9638 |
| trojan | 9451 |
| hysteria2 | 1302 |
| http | 159 |
| socks | 73 |
| shadowsocksr | 71 |
| tuic | 11 |
| hysteria | 7 |
| anytls | 1 |

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
| 79.38 | shadowsocks | 254.8 | 618.3 | 21.88 | 0.0 | 10.0 | 13.34 | 18.16 | Au1rxx-base64 | 156.146.38.169 |
| 79.37 | shadowsocks | 255.2 | 624.5 | 21.87 | 0.0 | 10.0 | 13.34 | 18.16 | Au1rxx-base64 | 156.146.38.170 |
| 79.36 | shadowsocks | 255.7 | 618.0 | 21.86 | 0.0 | 10.0 | 13.34 | 18.16 | Au1rxx-base64 | 173.244.56.6 |
| 79.29 | shadowsocks | 258.5 | 635.3 | 21.79 | 0.0 | 10.0 | 13.34 | 18.16 | Au1rxx-base64 | 156.146.38.168 |
| 78.81 | shadowsocks | 257.8 | 656.3 | 21.81 | 0.0 | 10.0 | 13.34 | 18.16 | Au1rxx-base64 | 108.181.118.10 |
| 78.81 | shadowsocks | 258.0 | 656.8 | 21.81 | 0.0 | 10.0 | 13.34 | 18.16 | Au1rxx-base64 | 108.181.0.177 |
| 78.03 | vless | 187.3 | 479.7 | 23.44 | 0.0 | 10.0 | 6.43 | 18.16 | Au1rxx-base64 | 179.253.240.24 |
| 78.0 | vless | 188.8 | 488.1 | 23.41 | 0.0 | 10.0 | 6.43 | 18.16 | Au1rxx-base64 | 179.255.148.66 |
| 77.75 | vless | 199.5 | 514.4 | 23.16 | 0.0 | 10.0 | 6.43 | 18.16 | Au1rxx-base64 | 107.173.237.146 |
| 77.37 | trojan | 271.9 | 563.2 | 21.48 | 0.0 | 10.0 | 13.64 | 18.16 | Au1rxx-base64 | 44.246.163.102 |
| 77.36 | trojan | 277.9 | 583.8 | 21.35 | 0.0 | 10.0 | 13.64 | 18.16 | Au1rxx-base64 | 35.86.90.51 |
| 77.33 | hysteria2 | 352.0 | 713.4 | 19.63 | 0.0 | 10.0 | 13.57 | 18.16 | Au1rxx-base64 | 159.223.157.129 |
| 77.14 | http | 539.7 | 1536.6 | 15.28 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.206 |
| 77.09 | http | 541.9 | 1542.6 | 15.23 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.213 |
| 77.07 | trojan | 290.7 | 621.7 | 21.05 | 0.0 | 10.0 | 13.64 | 18.16 | Au1rxx-base64 | 44.244.3.114 |
| 77.07 | hysteria2 | 347.1 | 761.6 | 19.74 | 0.0 | 10.0 | 13.57 | 18.16 | Au1rxx-base64 | 138.124.68.188 |
| 77.06 | http | 543.2 | 1537.2 | 15.2 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.220 |
| 77.04 | http | 544.4 | 1538.2 | 15.18 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.214 |
| 77.03 | http | 544.8 | 1548.1 | 15.17 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.215 |
| 77.02 | http | 545.2 | 1548.9 | 15.16 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 138.199.35.210 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Au1rxx-base64 | 0.952 | 0.888 | 428 | 1660 | prefer |
| Surfboard-tg-mixed | 0.796 | 0.723 | 65 | 6099 | prefer |
| DeltaKronecker-all | 0.464 | 0.38 | 71 | 4975 | observe |
| mheidari-all | 0.4 | 0.75 | 4 | 16658 | observe |
| Au1rxx-clash | 0.322 | 1.0 | 1 | 1669 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5328 | observe |
| Epodonios-all | 0.255 | None | 0 | 6671 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7502 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4929 | observe |
| barry-far-vless | 0.255 | None | 0 | 5264 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5196 | observe |
| nscl5-all | 0.234 | None | 0 | 1481 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 28 |
| speed | TimeoutError | - | 27 |
| geo | TimeoutError | - | 16 |
| speed | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 5 |
| 204 | ProxyError | - | 5 |
| cn-block | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
