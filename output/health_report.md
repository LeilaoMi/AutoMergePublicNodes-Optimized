# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-13 18:20:11 |
| 运行耗时 | 284.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83174 |
| 去重后节点 | 26889 |
| TCP 可达 | 3000 |
| 真实可用 | 348 |
| Verified 输出 | 72 |
| Global 输出 | 300 |
| All 输出 | 26889 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.6 |
| tcp | 81.4 |
| probe | 81.3 |
| real_test | 66.8 |
| china_check | 34.5 |
| write_verified | 0.0 |
| generate | 11.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49863 |
| vmess | 14676 |
| shadowsocks | 9725 |
| trojan | 6863 |
| hysteria2 | 1508 |
| http | 253 |
| shadowsocksr | 156 |
| socks | 60 |
| hysteria | 34 |
| tuic | 20 |
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
| 93.33 | trojan | 230.0 | 4.5 | 22.45 | 14.83 | 9.38 | 12.94 | 17.36 | Au1rxx-base64 | 167.88.61.20 |
| 92.54 | trojan | 241.3 | 3.1 | 22.19 | 14.88 | 9.38 | 12.94 | 17.36 | Au1rxx-base64 | 167.88.61.193 |
| 90.06 | http | 203.0 | 1.2 | 23.08 | 14.95 | 0.0 | 14.59 | 19.94 | ermaozi | 172.64.68.89 |
| 89.35 | trojan | 234.2 | 1.3 | 22.36 | 14.95 | 6.36 | 12.94 | 17.36 | Au1rxx-base64 | 167.88.61.85 |
| 89.1 | http | 236.4 | 6.5 | 22.31 | 14.76 | 0.0 | 14.59 | 19.94 | ermaozi | 172.64.69.89 |
| 88.69 | http | 245.5 | 8.9 | 22.09 | 14.67 | 0.0 | 14.59 | 19.94 | ermaozi | 44.248.167.117 |
| 88.34 | trojan | 284.3 | 3.4 | 21.2 | 14.87 | 8.16 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.112.76 |
| 88.12 | trojan | 265.6 | 1.8 | 21.63 | 14.93 | 9.3 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.114.132 |
| 87.51 | vless | 268.7 | 0.9 | 21.56 | 14.97 | 7.82 | 8.35 | 17.36 | Au1rxx-base64 | 45.63.53.81 |
| 87.3 | trojan | 269.4 | 1.3 | 21.54 | 14.95 | 8.06 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.114.126 |
| 86.83 | trojan | 291.8 | 0.9 | 21.02 | 14.96 | 6.32 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.112.31 |
| 86.58 | trojan | 290.2 | 0.1 | 21.06 | 15.0 | 6.32 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.112.142 |
| 86.31 | trojan | 267.9 | 6.3 | 21.58 | 14.76 | 8.36 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.114.245 |
| 85.82 | shadowsocks | 386.4 | 3.5 | 18.83 | 14.87 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 156.146.38.168 |
| 85.46 | shadowsocks | 360.9 | 2.9 | 19.42 | 14.89 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 45.86.51.18 |
| 85.38 | trojan | 308.9 | 198.0 | 20.63 | 7.57 | 10.0 | 12.94 | 17.36 | Au1rxx-base64 | 167.88.61.175 |
| 85.17 | http | 319.4 | 2.0 | 20.38 | 14.93 | 0.0 | 14.59 | 19.94 | ermaozi | 167.88.60.242 |
| 85.02 | trojan | 281.1 | 192.0 | 21.27 | 7.8 | 9.38 | 12.94 | 17.36 | Au1rxx-base64 | 167.88.61.198 |
| 84.92 | http | 263.3 | 1.1 | 21.68 | 14.96 | 0.0 | 14.59 | 19.94 | ermaozi | 138.199.35.201 |
| 84.87 | http | 268.6 | 0.4 | 21.56 | 14.98 | 0.0 | 14.59 | 19.94 | ermaozi | 138.199.35.202 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.989 | 0.982 | 56 | 590 | prefer |
| Surfboard-tg-mixed | 0.88 | 0.805 | 128 | 8804 | prefer |
| Au1rxx-base64 | 0.814 | 0.747 | 170 | 1751 | prefer |
| mheidari-all | 0.71 | 0.633 | 98 | 14267 | prefer |
| xiaoji235-airport-v2ray-all | 0.287 | 0.5 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4900 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2734 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11395 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6228 | observe |
| barry-far-vless | 0.255 | None | 0 | 6409 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4624 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 44 |
| 204 | ProxyError | - | 21 |
| speed | ClientOSError | - | 11 |
| 204 | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| cn-block | ProxyError | - | 3 |
| geo | ClientOSError | - | 3 |
| speed | TimeoutError | - | 2 |
| speed | ProxyError | - | 2 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 92 | 72 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
