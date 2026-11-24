# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-24 00:07:27 |
| 运行耗时 | 305.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 80217 |
| 去重后节点 | 27776 |
| TCP 可达 | 3000 |
| 真实可用 | 457 |
| Verified 输出 | 82 |
| Global 输出 | 300 |
| All 输出 | 27776 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 83.3 |
| probe | 96.6 |
| real_test | 72.3 |
| china_check | 30.7 |
| generate | 14.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48085 |
| vmess | 14920 |
| shadowsocks | 9479 |
| trojan | 5742 |
| hysteria2 | 1543 |
| shadowsocksr | 148 |
| http | 121 |
| socks | 105 |
| hysteria | 32 |
| anytls | 30 |
| tuic | 12 |

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
| 94.44 | shadowsocks | 239.9 | 0.1 | 22.22 | 15.0 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 173.244.56.9 |
| 94.11 | shadowsocks | 250.9 | 2.2 | 21.97 | 14.92 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 149.22.95.183 |
| 94.02 | shadowsocks | 231.6 | 3.1 | 22.42 | 14.88 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 95.215.201.18 |
| 94.0 | vless | 203.5 | 0.3 | 23.07 | 14.99 | 8.29 | 9.85 | 17.8 | Au1rxx-base64 | 45.63.53.81 |
| 93.26 | trojan | 173.3 | 3.3 | 23.77 | 14.88 | 10.0 | 9.31 | 17.8 | Au1rxx-base64 | 167.88.61.175 |
| 93.26 | shadowsocks | 244.1 | 2.5 | 22.13 | 14.91 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 173.244.56.6 |
| 92.57 | hysteria2 | 214.1 | 1.8 | 22.82 | 14.93 | 5.75 | 12.27 | 17.8 | Au1rxx-base64 | 66.94.121.46 |
| 90.25 | http | 198.7 | 0.3 | 23.18 | 14.99 | 0.0 | 14.58 | 20.0 | ermaozi | 172.64.68.89 |
| 90.18 | http | 196.1 | 3.6 | 23.24 | 14.86 | 0.0 | 14.58 | 20.0 | ermaozi | 172.64.69.89 |
| 89.4 | trojan | 173.9 | 2.6 | 23.75 | 14.9 | 9.14 | 9.31 | 17.8 | Au1rxx-base64 | 167.88.61.193 |
| 89.3 | shadowsocks | 304.8 | 3.2 | 20.72 | 14.88 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 156.146.38.170 |
| 87.57 | trojan | 170.4 | 0.3 | 23.83 | 14.99 | 9.14 | 9.31 | 17.8 | Au1rxx-base64 | 167.88.61.198 |
| 87.46 | hysteria2 | 238.0 | 5.0 | 22.27 | 14.81 | 7.47 | 12.27 | 17.8 | Au1rxx-base64 | 8.209.247.109 |
| 87.43 | trojan | 175.6 | 0.7 | 23.71 | 14.97 | 9.14 | 9.31 | 17.8 | Au1rxx-base64 | 167.88.61.20 |
| 85.83 | vless | 184.0 | 1.6 | 23.52 | 14.94 | 0.0 | 9.85 | 17.52 | Surfboard-tg-mixed | 198.247.127.131 |
| 85.81 | shadowsocks | 289.3 | 0.9 | 21.08 | 14.96 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 156.146.38.168 |
| 85.33 | shadowsocks | 304.0 | 0.2 | 20.74 | 14.99 | 9.78 | 13.42 | 17.8 | Au1rxx-base64 | 149.22.87.240 |
| 85.2 | shadowsocks | 362.7 | 0.5 | 19.38 | 14.98 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 37.19.198.244 |
| 85.16 | shadowsocks | 365.4 | 0.0 | 19.32 | 15.0 | 10.0 | 13.42 | 17.8 | Au1rxx-base64 | 37.19.198.243 |
| 85.01 | trojan | 174.4 | 0.1 | 23.74 | 14.99 | 7.28 | 9.31 | 17.8 | Au1rxx-base64 | 167.88.61.85 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.982 | 1.0 | 27 | 420 | prefer |
| Au1rxx-base64 | 0.896 | 0.83 | 165 | 1751 | prefer |
| Surfboard-tg-mixed | 0.86 | 0.782 | 275 | 8626 | prefer |
| mheidari-all | 0.606 | 0.526 | 152 | 15543 | observe |
| ermaozi-get_subscribe | 0.324 | 1.0 | 2 | 330 | observe |
| SoliSpirit-all | 0.287 | 0.5 | 2 | 11809 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5064 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5667 | observe |
| barry-far-vless | 0.255 | None | 0 | 5847 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | 0.222 | 9 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 94 |
| speed | ClientOSError | - | 24 |
| geo | ClientOSError | - | 14 |
| 204 | ProxyError | - | 11 |
| 204 | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 82 | 31 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
