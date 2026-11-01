# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-01 22:16:19 |
| 运行耗时 | 306.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82958 |
| 去重后节点 | 26789 |
| TCP 可达 | 3000 |
| 真实可用 | 429 |
| Verified 输出 | 74 |
| Global 输出 | 300 |
| All 输出 | 26789 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.5 |
| geo | 1.5 |
| tcp | 77.7 |
| probe | 94.9 |
| real_test | 83.9 |
| china_check | 26.1 |
| write_verified | 0.0 |
| generate | 14.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49372 |
| vmess | 13911 |
| trojan | 9074 |
| shadowsocks | 8618 |
| hysteria2 | 1507 |
| http | 205 |
| shadowsocksr | 156 |
| socks | 76 |
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
| 95.34 | http | 227.3 | 3.4 | 22.52 | 14.87 | 10.0 | 14.61 | 19.7 | ermaozi-get_subscribe | 138.199.35.212 |
| 92.96 | shadowsocks | 198.5 | 6.6 | 23.18 | 14.75 | 10.0 | 13.45 | 16.08 | Au1rxx-base64 | 95.215.201.18 |
| 92.91 | shadowsocks | 222.1 | 6.9 | 22.64 | 14.74 | 10.0 | 13.45 | 16.08 | Au1rxx-base64 | 173.244.56.9 |
| 92.37 | shadowsocks | 252.5 | 2.3 | 21.93 | 14.91 | 10.0 | 13.45 | 16.08 | Au1rxx-base64 | 156.146.38.168 |
| 91.46 | shadowsocks | 289.7 | 0.6 | 21.07 | 14.98 | 10.0 | 13.45 | 16.08 | Au1rxx-base64 | 156.146.38.170 |
| 91.26 | http | 326.3 | 147.6 | 20.22 | 9.47 | 10.0 | 14.61 | 19.7 | ermaozi-get_subscribe | 167.88.60.242 |
| 91.04 | trojan | 225.2 | 7.0 | 22.57 | 14.74 | 10.0 | 10.15 | 16.08 | Au1rxx-base64 | 167.88.61.175 |
| 90.82 | vless | 196.0 | 5.4 | 23.24 | 14.8 | 10.0 | 6.7 | 16.08 | Au1rxx-base64 | 144.202.126.147 |
| 90.76 | trojan | 225.1 | 1.7 | 22.57 | 14.94 | 9.52 | 10.15 | 16.08 | Au1rxx-base64 | 167.88.61.193 |
| 90.69 | trojan | 226.2 | 2.6 | 22.54 | 14.9 | 9.52 | 10.15 | 16.08 | Au1rxx-base64 | 167.88.61.20 |
| 90.65 | shadowsocks | 296.8 | 0.5 | 20.91 | 14.98 | 10.0 | 13.45 | 16.08 | Au1rxx-base64 | 156.146.38.167 |
| 90.54 | trojan | 223.7 | 8.6 | 22.6 | 14.68 | 9.53 | 10.15 | 16.08 | Au1rxx-base64 | 167.88.61.198 |
| 90.44 | trojan | 246.4 | 9.7 | 22.07 | 14.64 | 10.0 | 10.15 | 16.08 | Au1rxx-base64 | 66.163.112.121 |
| 90.43 | trojan | 197.3 | 0.3 | 23.21 | 14.99 | 8.5 | 10.15 | 16.08 | Au1rxx-base64 | 66.163.112.76 |
| 90.4 | trojan | 198.1 | 0.8 | 23.19 | 14.97 | 8.51 | 10.15 | 16.08 | Au1rxx-base64 | 66.163.112.13 |
| 88.87 | vless | 187.5 | 7.6 | 23.44 | 14.72 | 7.93 | 6.7 | 16.08 | Au1rxx-base64 | 45.63.53.81 |
| 88.61 | hysteria2 | 320.4 | 1.7 | 20.36 | 14.94 | 10.0 | 11.25 | 16.08 | Au1rxx-base64 | 129.213.91.185 |
| 88.28 | trojan | 202.9 | 1.8 | 23.08 | 14.93 | 6.54 | 10.15 | 16.08 | Au1rxx-base64 | 66.163.112.142 |
| 88.18 | shadowsocks | 267.4 | 6.1 | 21.59 | 14.77 | 6.29 | 13.45 | 16.08 | Au1rxx-base64 | 156.146.38.169 |
| 88.15 | shadowsocks | 308.6 | 4.9 | 20.63 | 14.82 | 10.0 | 13.45 | 16.08 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.923 | 1.0 | 19 | 43 | prefer |
| ermaozi-get_subscribe | 0.92 | 0.929 | 28 | 499 | prefer |
| Au1rxx-base64 | 0.868 | 0.8 | 320 | 1751 | prefer |
| mheidari-all | 0.866 | 0.796 | 54 | 15206 | prefer |
| Surfboard-tg-mixed | 0.643 | 0.564 | 149 | 8273 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4800 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| DeltaKronecker-all | 0.287 | 0.5 | 2 | 3716 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4976 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10673 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5823 | observe |
| barry-far-vless | 0.255 | None | 0 | 5986 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 73 |
| geo | ClientOSError | - | 23 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 10 |
| cn-block | ClientOSError | - | 6 |
| geo | ProxyError | - | 4 |
| cn-block | ProxyError | - | 3 |
| 204 | TimeoutError | - | 3 |
| speed | ClientOSError | - | 2 |
| speed | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 1 |
| 204 | ProxyConnectionError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 82 | 74 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
