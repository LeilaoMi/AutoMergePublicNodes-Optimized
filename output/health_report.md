# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-08 02:04:22 |
| 运行耗时 | 346.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 82250 |
| 去重后节点 | 23593 |
| TCP 可达 | 3000 |
| 真实可用 | 740 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23593 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.2 |
| tcp | 35.0 |
| probe | 64.7 |
| real_test | 197.3 |
| generate | 43.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47722 |
| vmess | 12918 |
| trojan | 10245 |
| shadowsocks | 9892 |
| hysteria2 | 1278 |
| shadowsocksr | 74 |
| socks | 64 |
| http | 35 |
| hysteria | 13 |
| tuic | 8 |
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
| 84.68 | hysteria2 | 247.4 | 673.1 | 22.05 | 0.0 | 10.0 | 13.85 | 19.78 | Au1rxx-base64 | 138.124.68.188 |
| 84.67 | hysteria2 | 243.3 | 654.1 | 22.14 | 0.0 | 10.0 | 13.85 | 19.78 | Au1rxx-base64 | 159.223.157.129 |
| 84.4 | hysteria2 | 259.5 | 700.5 | 21.77 | 0.0 | 10.0 | 13.85 | 19.78 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 81.39 | shadowsocks | 226.0 | 598.1 | 22.55 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 198.98.53.130 |
| 81.09 | shadowsocks | 238.6 | 637.3 | 22.25 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 37.19.198.236 |
| 81.07 | shadowsocks | 239.9 | 637.4 | 22.23 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 37.19.198.244 |
| 80.05 | shadowsocks | 283.9 | 774.4 | 21.21 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 37.19.198.160 |
| 78.6 | vless | 287.8 | 755.1 | 21.12 | 0.0 | 10.0 | 8.85 | 19.78 | Au1rxx-base64 | 104.17.21.111 |
| 77.44 | shadowsocks | 285.3 | 666.7 | 21.17 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 156.146.38.170 |
| 77.4 | shadowsocks | 285.8 | 658.5 | 21.16 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 156.146.38.169 |
| 76.54 | hysteria2 | 357.8 | 688.1 | 19.5 | 0.0 | 10.0 | 13.85 | 19.78 | Au1rxx-base64 | 62.210.124.146 |
| 76.24 | shadowsocks | 232.5 | 626.9 | 22.4 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 37.19.198.243 |
| 75.78 | shadowsocks | 446.7 | 1247.1 | 17.44 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 68.168.222.210 |
| 75.72 | hysteria2 | 356.1 | 666.2 | 19.54 | 0.0 | 10.0 | 13.85 | 19.78 | Au1rxx-base64 | 31.76.113.32 |
| 75.61 | shadowsocks | 355.0 | 872.9 | 19.56 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 185.196.61.82 |
| 75.26 | shadowsocks | 406.8 | 1026.1 | 18.36 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 156.146.38.168 |
| 73.98 | hysteria2 | 455.3 | 907.8 | 17.24 | 0.0 | 9.99 | 13.85 | 19.78 | Au1rxx-base64 | 91.196.32.163 |
| 73.91 | shadowsocks | 314.1 | 580.6 | 20.51 | 0.0 | 10.0 | 13.06 | 19.78 | Au1rxx-base64 | 173.244.56.9 |
| 73.83 | vless | 284.2 | 683.4 | 21.2 | 0.0 | 10.0 | 8.85 | 19.78 | Au1rxx-base64 | 74.49.215.8 |
| 73.79 | trojan | 414.3 | 790.5 | 18.19 | 0.0 | 10.0 | 14.79 | 19.78 | Au1rxx-base64 | 54.216.124.178 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.952 | 439 | 1365 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.747 | 0.68 | 25 | 6471 | prefer |
| mheidari-all | 0.544 | 0.462 | 26 | 17687 | observe |
| DeltaKronecker-all | 0.436 | 0.356 | 765 | 5326 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7081 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7469 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5179 | observe |
| barry-far-vless | 0.255 | None | 0 | 5509 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5175 | observe |
| nscl5-all | 0.241 | None | 0 | 1643 | observe |
| Au1rxx-clash | 0.23 | None | 0 | 1365 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 255 |
| cn-block | TimeoutError | - | 95 |
| geo | ClientOSError | - | 76 |
| speed | ClientOSError | - | 48 |
| speed | TimeoutError | - | 42 |
| 204 | ProxyError | - | 8 |
| 204 | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:30483: bind: address already in use | - | 1 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
