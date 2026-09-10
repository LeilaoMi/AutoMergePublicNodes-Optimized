# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-10 20:51:51 |
| 运行耗时 | 636.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 83486 |
| 去重后节点 | 22847 |
| TCP 可达 | 3000 |
| 真实可用 | 371 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22847 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.4 |
| tcp | 38.8 |
| probe | 275.6 |
| real_test | 215.4 |
| generate | 98.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50614 |
| vmess | 12528 |
| shadowsocks | 9805 |
| trojan | 8072 |
| hysteria2 | 1699 |
| http | 567 |
| shadowsocksr | 124 |
| socks | 55 |
| tuic | 10 |
| hysteria | 8 |
| anytls | 4 |

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
| 81.36 | vless | 234.1 | 604.1 | 22.36 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 195.123.235.177 |
| 81.04 | vless | 248.0 | 693.5 | 22.04 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 47.253.226.114 |
| 80.73 | vless | 261.4 | 681.8 | 21.73 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 167.17.69.171 |
| 80.4 | vless | 275.7 | 733.3 | 21.4 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.235 |
| 80.08 | vless | 289.3 | 713.8 | 21.08 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.89 |
| 80.06 | vless | 290.2 | 658.5 | 21.06 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.212 |
| 79.79 | vless | 301.8 | 773.9 | 20.79 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 66.70.179.198 |
| 79.71 | vless | 305.2 | 707.3 | 20.71 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.229 |
| 79.45 | vless | 316.8 | 730.9 | 20.45 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.179 |
| 79.29 | vless | 323.4 | 871.0 | 20.29 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.133 |
| 78.95 | shadowsocks | 302.5 | 641.1 | 20.78 | 0.0 | 10.0 | 13.71 | 18.96 | Au1rxx-base64 | 51.79.85.185 |
| 78.86 | shadowsocks | 242.2 | 666.4 | 22.17 | 0.0 | 10.0 | 13.71 | 16.98 | Surfboard-tg-mixed | 37.19.198.244 |
| 78.79 | vless | 329.6 | 819.4 | 20.15 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.95 |
| 78.75 | shadowsocks | 246.8 | 676.5 | 22.06 | 0.0 | 10.0 | 13.71 | 16.98 | Surfboard-tg-mixed | 37.19.198.160 |
| 78.73 | vless | 347.6 | 821.6 | 19.73 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.74 |
| 78.71 | vless | 348.7 | 896.5 | 19.71 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.184 |
| 78.64 | vless | 351.4 | 830.6 | 19.64 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.225 |
| 78.56 | vless | 310.2 | 852.6 | 20.6 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 137.184.218.169 |
| 78.24 | shadowsocks | 333.1 | 949.4 | 20.07 | 0.0 | 10.0 | 13.71 | 18.96 | Au1rxx-base64 | 15.204.247.206 |
| 78.16 | vless | 286.3 | 761.5 | 21.15 | 0.0 | 10.0 | 10.04 | 18.96 | Au1rxx-base64 | 169.40.42.224 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.94 | 0.878 | 237 | 1642 | prefer |
| DeltaKronecker-all | 0.819 | 0.762 | 21 | 5853 | prefer |
| Surfboard-tg-mixed | 0.78 | 0.703 | 128 | 7221 | prefer |
| ermaozi | 0.776 | 0.783 | 23 | 405 | prefer |
| mheidari-all | 0.705 | 0.63 | 54 | 15823 | prefer |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 194 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4995 | observe |
| Epodonios-all | 0.255 | None | 0 | 7677 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8881 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5840 | observe |
| barry-far-vless | 0.255 | None | 0 | 6058 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4255 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 24 |
| cn-block | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 11 |
| 204 | ProxyError | - | 9 |
| 204 | ClientOSError | - | 6 |
| speed | TimeoutError | - | 5 |
| speed | ClientOSError | - | 4 |
| geo | TimeoutError | - | 4 |
| 204 | ProxyConnectionError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
