# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-01 18:03:50 |
| 运行耗时 | 279.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 89 |
| 原始节点 | 82878 |
| 去重后节点 | 26787 |
| TCP 可达 | 3000 |
| 真实可用 | 388 |
| Verified 输出 | 82 |
| Global 输出 | 300 |
| All 输出 | 26787 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.4 |
| tcp | 78.0 |
| probe | 71.0 |
| real_test | 81.6 |
| china_check | 33.1 |
| write_verified | 0.0 |
| generate | 9.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49388 |
| vmess | 13907 |
| trojan | 9121 |
| shadowsocks | 8534 |
| hysteria2 | 1501 |
| shadowsocksr | 147 |
| http | 143 |
| socks | 98 |
| anytls | 16 |
| tuic | 12 |
| hysteria | 11 |

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
| 97.97 | trojan | 199.3 | 0.6 | 23.16 | 14.98 | 10.0 | 13.55 | 18.78 | Au1rxx-base64 | 66.163.112.121 |
| 97.29 | http | 194.1 | 1.8 | 23.28 | 14.93 | 7.57 | 14.65 | 19.86 | ermaozi-get_subscribe | 138.199.35.212 |
| 97.22 | trojan | 229.8 | 1.9 | 22.46 | 14.93 | 10.0 | 13.55 | 18.78 | Au1rxx-base64 | 167.88.61.175 |
| 96.48 | trojan | 200.4 | 1.0 | 23.14 | 14.96 | 8.55 | 13.55 | 18.78 | Au1rxx-base64 | 66.163.112.242 |
| 96.27 | shadowsocks | 219.8 | 0.5 | 22.69 | 14.98 | 10.0 | 13.82 | 18.78 | Au1rxx-base64 | 173.244.56.6 |
| 96.2 | shadowsocks | 201.0 | 0.6 | 23.12 | 14.98 | 10.0 | 13.82 | 18.78 | Au1rxx-base64 | 95.215.201.18 |
| 95.7 | trojan | 203.6 | 0.7 | 23.06 | 14.97 | 7.84 | 13.55 | 18.78 | Au1rxx-base64 | 66.163.112.13 |
| 94.85 | trojan | 225.0 | 0.4 | 22.57 | 14.99 | 8.37 | 13.55 | 18.78 | Au1rxx-base64 | 167.88.61.198 |
| 94.82 | shadowsocks | 257.3 | 0.9 | 21.82 | 14.96 | 10.0 | 13.82 | 18.78 | Au1rxx-base64 | 156.146.38.170 |
| 92.9 | trojan | 293.1 | 2.3 | 20.99 | 14.91 | 10.0 | 13.55 | 18.78 | Au1rxx-base64 | 66.163.114.45 |
| 91.9 | trojan | 230.1 | 1.9 | 22.45 | 14.93 | 4.69 | 13.55 | 18.78 | Au1rxx-base64 | 167.88.61.85 |
| 91.69 | hysteria2 | 310.3 | 0.6 | 20.6 | 14.98 | 10.0 | 10.91 | 18.78 | Au1rxx-base64 | 129.213.91.185 |
| 91.49 | vless | 199.7 | 1.2 | 23.15 | 14.95 | 7.32 | 7.29 | 18.78 | Au1rxx-base64 | 45.63.53.81 |
| 91.47 | trojan | 327.5 | 0.9 | 20.2 | 14.97 | 10.0 | 13.55 | 18.78 | Au1rxx-base64 | 216.238.80.100 |
| 91.3 | trojan | 226.7 | 0.7 | 22.53 | 14.97 | 8.38 | 13.55 | 18.78 | Au1rxx-base64 | 167.88.61.20 |
| 90.91 | trojan | 274.5 | 5.0 | 21.42 | 14.81 | 4.85 | 13.55 | 18.78 | Au1rxx-base64 | 66.163.112.142 |
| 90.56 | trojan | 201.1 | 2.3 | 23.12 | 14.91 | 7.81 | 13.55 | 18.78 | Au1rxx-base64 | 66.163.112.76 |
| 90.44 | shadowsocks | 217.5 | 2.9 | 22.74 | 14.89 | 10.0 | 13.82 | 18.78 | Au1rxx-base64 | 173.244.56.9 |
| 90.28 | shadowsocks | 253.0 | 0.3 | 21.92 | 14.99 | 10.0 | 13.82 | 18.78 | Au1rxx-base64 | 156.146.38.168 |
| 89.41 | http | 290.8 | 1.6 | 21.05 | 14.94 | 7.68 | 14.65 | 19.86 | ermaozi-get_subscribe | 167.88.60.242 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.985 | 0.982 | 55 | 499 | prefer |
| zhangkai | 0.923 | 1.0 | 19 | 43 | prefer |
| Au1rxx-base64 | 0.804 | 0.736 | 284 | 1751 | prefer |
| Surfboard-tg-mixed | 0.66 | 0.581 | 117 | 8239 | observe |
| mheidari-all | 0.465 | 0.383 | 94 | 15458 | observe |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4976 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 3716 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10659 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5773 | observe |
| barry-far-vless | 0.255 | None | 0 | 5873 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4680 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 80 |
| geo | ClientOSError | - | 58 |
| 204 | ProxyError | - | 15 |
| 204 | TimeoutError | - | 7 |
| cn-block | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 4 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 98 | 82 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
