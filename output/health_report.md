# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-08 23:19:43 |
| 运行耗时 | 623.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98866 |
| 去重后节点 | 27653 |
| TCP 可达 | 3000 |
| 真实可用 | 401 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27653 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 12.0 |
| geo | 1.5 |
| tcp | 47.0 |
| probe | 245.3 |
| real_test | 241.2 |
| generate | 76.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58825 |
| vmess | 15820 |
| shadowsocks | 12006 |
| trojan | 10086 |
| hysteria2 | 1413 |
| http | 410 |
| shadowsocksr | 162 |
| socks | 83 |
| anytls | 34 |
| hysteria | 16 |
| tuic | 11 |

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
| 84.43 | vless | 176.4 | 468.8 | 23.69 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 47.251.108.158 |
| 83.98 | vless | 195.8 | 516.8 | 23.24 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 23.95.222.127 |
| 83.17 | vless | 231.1 | 560.8 | 22.43 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 15.204.97.197 |
| 83.09 | vless | 234.4 | 556.0 | 22.35 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 15.204.97.216 |
| 82.93 | hysteria2 | 260.8 | 243.9 | 21.74 | 5.85 | 9.94 | 12.95 | 19.2 | Au1rxx-base64 | 158.101.148.79 |
| 81.94 | vless | 284.4 | 438.2 | 21.2 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 195.123.240.65 |
| 80.74 | shadowsocks | 207.5 | 518.2 | 22.97 | 0.0 | 10.0 | 13.07 | 19.2 | Au1rxx-base64 | 108.181.0.177 |
| 80.68 | shadowsocks | 210.4 | 505.8 | 22.91 | 0.0 | 10.0 | 13.07 | 19.2 | Au1rxx-base64 | 108.181.118.10 |
| 80.34 | shadowsocks | 246.4 | 590.8 | 22.07 | 0.0 | 10.0 | 13.07 | 19.2 | Au1rxx-base64 | 149.22.95.183 |
| 80.21 | hysteria2 | 250.1 | 233.5 | 21.99 | 6.24 | 7.31 | 12.95 | 19.2 | Au1rxx-base64 | open.2ml.bid |
| 79.58 | shadowsocks | 257.7 | 671.3 | 21.81 | 0.0 | 10.0 | 13.07 | 19.2 | Au1rxx-base64 | 5.78.51.123 |
| 78.68 | vless | 209.0 | 503.4 | 22.94 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 154.12.38.159 |
| 76.97 | shadowsocks | 274.3 | 278.7 | 21.43 | 4.55 | 9.94 | 13.07 | 19.2 | Au1rxx-base64 | 149.22.87.240 |
| 76.81 | shadowsocks | 274.6 | 285.3 | 21.42 | 4.3 | 9.94 | 13.07 | 19.2 | Au1rxx-base64 | 149.22.87.204 |
| 76.71 | vless | 373.8 | 283.8 | 19.12 | 4.36 | 9.9 | 11.54 | 19.2 | Au1rxx-base64 | 46.250.250.149 |
| 76.7 | hysteria2 | 350.4 | 772.2 | 19.67 | 0.0 | 10.0 | 12.95 | 19.2 | Au1rxx-base64 | 129.213.91.185 |
| 75.71 | vless | 413.5 | 1099.0 | 18.21 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 51.81.203.63 |
| 75.55 | shadowsocks | 302.6 | 669.9 | 20.77 | 0.0 | 10.0 | 13.07 | 19.2 | Au1rxx-base64 | 156.146.38.168 |
| 74.71 | shadowsocks | 185.7 | 492.1 | 23.48 | 0.0 | 10.0 | 13.07 | 17.16 | mheidari-all | 216.105.168.18 |
| 74.58 | vless | 471.1 | 1244.4 | 16.87 | 0.0 | 10.0 | 11.54 | 19.2 | Au1rxx-base64 | 104.17.98.5 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.966 | 0.895 | 344 | 1827 | prefer |
| mheidari-all | 0.901 | 0.829 | 76 | 23588 | prefer |
| zhangkai | 0.672 | 0.682 | 22 | 144 | observe |
| DeltaKronecker-all | 0.57 | 0.727 | 11 | 5197 | observe |
| Surfboard-tg-mixed | 0.48 | 1.0 | 4 | 7092 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5081 | observe |
| Epodonios-all | 0.255 | None | 0 | 7650 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10086 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5580 | observe |
| barry-far-vless | 0.255 | None | 0 | 5923 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4362 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 16 |
| speed | ClientOSError | - | 10 |
| geo | ClientOSError | - | 8 |
| 204 | ProxyConnectionError | - | 7 |
| 204 | TimeoutError | - | 7 |
| speed | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | TimeoutError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
