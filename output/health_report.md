# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-04 06:45:39 |
| 运行耗时 | 286.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82812 |
| 去重后节点 | 26757 |
| TCP 可达 | 3000 |
| 真实可用 | 424 |
| Verified 输出 | 61 |
| Global 输出 | 300 |
| All 输出 | 26757 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.5 |
| tcp | 80.8 |
| probe | 79.1 |
| real_test | 84.2 |
| china_check | 25.4 |
| write_verified | 0.1 |
| generate | 10.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49481 |
| vmess | 13906 |
| shadowsocks | 9016 |
| trojan | 8420 |
| hysteria2 | 1621 |
| shadowsocksr | 147 |
| http | 94 |
| socks | 77 |
| hysteria | 18 |
| tuic | 16 |
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
| 92.31 | shadowsocks | 219.7 | 0.1 | 22.69 | 15.0 | 10.0 | 12.96 | 15.66 | Au1rxx-base64 | 173.244.56.6 |
| 92.14 | shadowsocks | 199.3 | 3.8 | 23.16 | 14.86 | 10.0 | 12.96 | 15.66 | Au1rxx-base64 | 95.215.201.18 |
| 91.64 | shadowsocks | 209.4 | 0.4 | 22.93 | 14.99 | 10.0 | 12.96 | 15.66 | Au1rxx-base64 | 173.244.56.9 |
| 91.22 | trojan | 205.4 | 0.8 | 23.02 | 14.97 | 10.0 | 10.07 | 15.66 | Au1rxx-base64 | 66.163.112.121 |
| 91.2 | trojan | 199.5 | 0.3 | 23.16 | 14.99 | 9.82 | 10.07 | 15.66 | Au1rxx-base64 | 66.163.112.242 |
| 91.11 | vless | 194.7 | 4.7 | 23.27 | 14.83 | 10.0 | 7.35 | 15.66 | Au1rxx-base64 | 144.202.126.147 |
| 91.02 | trojan | 213.5 | 1.1 | 22.83 | 14.96 | 10.0 | 10.07 | 15.66 | Au1rxx-base64 | 167.88.61.175 |
| 90.87 | shadowsocks | 276.7 | 3.2 | 21.37 | 14.88 | 10.0 | 12.96 | 15.66 | Au1rxx-base64 | 156.146.38.168 |
| 90.73 | shadowsocks | 286.4 | 1.0 | 21.15 | 14.96 | 10.0 | 12.96 | 15.66 | Au1rxx-base64 | 156.146.38.170 |
| 90.52 | shadowsocks | 294.0 | 2.0 | 20.97 | 14.93 | 10.0 | 12.96 | 15.66 | Au1rxx-base64 | 156.146.38.167 |
| 90.4 | trojan | 225.3 | 0.9 | 22.56 | 14.96 | 9.65 | 10.07 | 15.66 | Au1rxx-base64 | 167.88.61.20 |
| 90.34 | trojan | 224.1 | 3.7 | 22.59 | 14.86 | 9.66 | 10.07 | 15.66 | Au1rxx-base64 | 167.88.61.198 |
| 90.23 | trojan | 197.7 | 0.1 | 23.2 | 15.0 | 8.8 | 10.07 | 15.66 | Au1rxx-base64 | 66.163.112.76 |
| 90.12 | trojan | 200.2 | 1.3 | 23.14 | 14.95 | 8.8 | 10.07 | 15.66 | Au1rxx-base64 | 66.163.112.13 |
| 89.66 | vless | 194.3 | 2.5 | 23.28 | 14.9 | 8.47 | 7.35 | 15.66 | Au1rxx-base64 | 45.63.53.81 |
| 89.12 | trojan | 214.3 | 4.0 | 22.82 | 14.85 | 9.66 | 10.07 | 15.66 | Au1rxx-base64 | 167.88.61.193 |
| 89.0 | trojan | 199.4 | 2.5 | 23.16 | 14.9 | 7.71 | 10.07 | 15.66 | Au1rxx-base64 | 66.163.112.142 |
| 88.66 | hysteria2 | 310.0 | 0.6 | 20.6 | 14.98 | 10.0 | 10.59 | 15.66 | Au1rxx-base64 | 129.213.91.185 |
| 88.16 | trojan | 217.2 | 2.8 | 22.75 | 14.9 | 7.41 | 10.07 | 15.66 | Au1rxx-base64 | 167.88.61.85 |
| 88.07 | trojan | 272.2 | 1.6 | 21.48 | 14.94 | 10.0 | 10.07 | 15.66 | Au1rxx-base64 | 66.163.114.45 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.945 | 1.0 | 19 | 578 | prefer |
| Au1rxx-base64 | 0.853 | 0.785 | 288 | 1751 | prefer |
| Surfboard-tg-mixed | 0.714 | 0.917 | 12 | 8544 | prefer |
| mheidari-all | 0.662 | 0.582 | 285 | 15179 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 130 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5017 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2526 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10853 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6022 | observe |
| barry-far-vless | 0.255 | None | 0 | 6238 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4608 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 70 |
| geo | ClientOSError | - | 45 |
| 204 | ProxyError | - | 31 |
| cn-block | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| speed | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |
| speed | TimeoutError | - | 1 |
| 204 | ServerDisconnectedError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 37 | 61 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
