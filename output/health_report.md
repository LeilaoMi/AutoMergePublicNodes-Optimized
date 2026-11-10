# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-10 07:34:54 |
| 运行耗时 | 326.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81817 |
| 去重后节点 | 26754 |
| TCP 可达 | 3000 |
| 真实可用 | 488 |
| Verified 输出 | 108 |
| Global 输出 | 300 |
| All 输出 | 26754 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 79.1 |
| probe | 98.0 |
| real_test | 86.7 |
| china_check | 39.9 |
| write_verified | 0.0 |
| generate | 14.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49474 |
| vmess | 14144 |
| shadowsocks | 9203 |
| trojan | 6913 |
| hysteria2 | 1567 |
| http | 247 |
| shadowsocksr | 152 |
| socks | 52 |
| hysteria | 30 |
| tuic | 20 |
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
| 98.48 | trojan | 171.1 | 1.0 | 23.82 | 14.96 | 10.0 | 14.08 | 18.12 | Au1rxx-base64 | 167.88.61.175 |
| 96.89 | trojan | 175.8 | 1.4 | 23.71 | 14.95 | 8.53 | 14.08 | 18.12 | Au1rxx-base64 | 167.88.61.20 |
| 96.88 | trojan | 176.1 | 1.1 | 23.7 | 14.96 | 8.52 | 14.08 | 18.12 | Au1rxx-base64 | 167.88.61.193 |
| 96.81 | trojan | 180.6 | 0.6 | 23.6 | 14.98 | 8.53 | 14.08 | 18.12 | Au1rxx-base64 | 167.88.61.198 |
| 96.59 | trojan | 244.4 | 6.1 | 22.12 | 14.77 | 10.0 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.112.121 |
| 95.88 | trojan | 266.3 | 0.3 | 21.61 | 14.99 | 10.0 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.114.45 |
| 95.7 | shadowsocks | 230.0 | 2.0 | 22.45 | 14.93 | 10.0 | 14.2 | 18.12 | Au1rxx-base64 | 173.244.56.6 |
| 95.19 | trojan | 242.7 | 0.6 | 22.16 | 14.98 | 8.35 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.112.242 |
| 94.95 | shadowsocks | 231.6 | 7.6 | 22.42 | 14.71 | 10.0 | 14.2 | 18.12 | Au1rxx-base64 | 95.215.201.18 |
| 94.81 | trojan | 239.2 | 0.5 | 22.24 | 14.98 | 7.89 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.112.13 |
| 94.66 | trojan | 240.6 | 0.1 | 22.21 | 15.0 | 7.88 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.112.76 |
| 94.49 | trojan | 260.8 | 0.6 | 21.74 | 14.98 | 8.24 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.114.132 |
| 94.39 | trojan | 173.2 | 1.4 | 23.77 | 14.95 | 5.97 | 14.08 | 18.12 | Au1rxx-base64 | 167.88.61.85 |
| 94.21 | trojan | 265.6 | 0.5 | 21.63 | 14.98 | 7.94 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.114.245 |
| 93.22 | shadowsocks | 240.5 | 1.6 | 22.21 | 14.94 | 10.0 | 14.2 | 18.12 | Au1rxx-base64 | 149.22.95.183 |
| 93.01 | trojan | 298.8 | 1.2 | 20.86 | 14.96 | 7.71 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.114.126 |
| 92.93 | trojan | 239.3 | 2.0 | 22.24 | 14.93 | 6.06 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.112.31 |
| 92.88 | trojan | 241.5 | 1.9 | 22.19 | 14.93 | 6.06 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.112.142 |
| 92.82 | trojan | 305.8 | 1.3 | 20.7 | 14.95 | 7.8 | 14.08 | 18.12 | Au1rxx-base64 | 66.163.114.166 |
| 92.62 | trojan | 222.9 | 1.1 | 22.62 | 14.96 | 5.34 | 14.08 | 18.12 | Au1rxx-base64 | 216.106.186.32 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.99 | 0.977 | 86 | 602 | prefer |
| Au1rxx-base64 | 0.897 | 0.83 | 223 | 1751 | prefer |
| Surfboard-tg-mixed | 0.895 | 0.818 | 176 | 8228 | prefer |
| mheidari-all | 0.869 | 0.795 | 88 | 13900 | prefer |
| DeltaKronecker-all | 0.391 | 1.0 | 2 | 2754 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4976 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11021 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6133 | observe |
| barry-far-vless | 0.255 | None | 0 | 6344 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4583 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 47 |
| 204 | ProxyError | - | 10 |
| 204 | TimeoutError | - | 7 |
| speed | ClientOSError | - | 7 |
| speed | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| geo | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 134 | 108 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
