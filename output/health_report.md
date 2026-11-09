# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-09 22:42:07 |
| 运行耗时 | 281.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 81601 |
| 去重后节点 | 26712 |
| TCP 可达 | 3000 |
| 真实可用 | 476 |
| Verified 输出 | 55 |
| Global 输出 | 300 |
| All 输出 | 26712 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| geo | 1.4 |
| tcp | 81.3 |
| probe | 81.0 |
| real_test | 79.2 |
| china_check | 22.8 |
| write_verified | 0.0 |
| generate | 10.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49306 |
| vmess | 14234 |
| shadowsocks | 9151 |
| trojan | 6984 |
| hysteria2 | 1577 |
| shadowsocksr | 148 |
| http | 91 |
| socks | 50 |
| hysteria | 23 |
| tuic | 21 |
| anytls | 16 |

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
| 94.62 | hysteria2 | 197.2 | 1.3 | 23.21 | 14.95 | 5.95 | 13.75 | 17.76 | Au1rxx-base64 | 66.94.121.46 |
| 93.7 | trojan | 238.9 | 0.8 | 22.25 | 14.97 | 10.0 | 12.1 | 17.76 | Au1rxx-base64 | 167.88.61.20 |
| 93.47 | trojan | 233.9 | 2.0 | 22.36 | 14.92 | 10.0 | 12.1 | 17.76 | Au1rxx-base64 | 167.88.61.175 |
| 93.38 | trojan | 235.7 | 1.5 | 22.32 | 14.94 | 10.0 | 12.1 | 17.76 | Au1rxx-base64 | 167.88.61.193 |
| 93.37 | shadowsocks | 189.0 | 2.5 | 23.4 | 14.91 | 10.0 | 13.99 | 17.76 | Au1rxx-base64 | 149.22.95.183 |
| 93.36 | trojan | 232.5 | 1.6 | 22.4 | 14.94 | 10.0 | 12.1 | 17.76 | Au1rxx-base64 | 167.88.61.198 |
| 92.6 | trojan | 272.2 | 0.1 | 21.48 | 14.99 | 10.0 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.114.132 |
| 92.58 | trojan | 252.4 | 0.7 | 21.94 | 14.97 | 10.0 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.114.45 |
| 92.05 | trojan | 201.2 | 0.8 | 23.12 | 14.97 | 6.6 | 12.1 | 17.76 | Au1rxx-base64 | 216.106.186.32 |
| 91.33 | trojan | 275.0 | 0.3 | 21.41 | 14.99 | 8.43 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.114.114 |
| 91.29 | trojan | 258.1 | 0.4 | 21.8 | 14.99 | 8.4 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.114.126 |
| 91.15 | trojan | 272.1 | 1.3 | 21.48 | 14.95 | 8.42 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.114.106 |
| 90.98 | shadowsocks | 274.2 | 4.1 | 21.43 | 14.85 | 10.0 | 13.99 | 17.76 | Au1rxx-base64 | 95.215.201.18 |
| 90.81 | trojan | 240.2 | 7.1 | 22.22 | 14.73 | 7.13 | 12.1 | 17.76 | Au1rxx-base64 | 167.88.61.85 |
| 90.64 | trojan | 206.1 | 1.4 | 23.01 | 14.95 | 5.32 | 12.1 | 17.76 | Au1rxx-base64 | 216.106.186.33 |
| 89.47 | trojan | 287.7 | 1.5 | 21.12 | 14.94 | 10.0 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.112.121 |
| 89.21 | trojan | 288.0 | 2.3 | 21.11 | 14.91 | 9.9 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.112.242 |
| 88.97 | shadowsocks | 313.9 | 2.8 | 20.51 | 14.9 | 10.0 | 13.99 | 17.76 | Au1rxx-base64 | 156.146.38.170 |
| 88.07 | trojan | 291.3 | 3.4 | 21.03 | 14.87 | 8.33 | 12.1 | 17.76 | Au1rxx-base64 | 66.163.112.76 |
| 88.03 | vless | 241.2 | 2.8 | 22.19 | 14.89 | 8.34 | 9.09 | 17.76 | Au1rxx-base64 | 47.251.108.158 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.942 | 1.0 | 19 | 518 | prefer |
| Surfboard-tg-mixed | 0.941 | 0.865 | 192 | 8250 | prefer |
| mheidari-all | 0.941 | 0.868 | 106 | 14061 | prefer |
| Au1rxx-base64 | 0.898 | 0.831 | 237 | 1751 | prefer |
| ninja-vless | 0.383 | 1.0 | 2 | 1791 | observe |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4976 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2754 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11213 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6133 | observe |
| barry-far-vless | 0.255 | None | 0 | 6103 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4583 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 36 |
| cn-block | TimeoutError | - | 9 |
| cn-block | ProxyError | - | 7 |
| 204 | ProxyError | - | 6 |
| 204 | TimeoutError | - | 6 |
| speed | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 5 |
| speed | TimeoutError | - | 2 |
| geo | TimeoutError | - | 1 |
| cn-block | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |
| cn-block | status | 530 | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 44 | 55 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
