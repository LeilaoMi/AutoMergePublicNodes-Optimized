# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-22 16:48:53 |
| 运行耗时 | 515.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 84229 |
| 去重后节点 | 23642 |
| TCP 可达 | 3000 |
| 真实可用 | 405 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23642 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.5 |
| geo | 1.4 |
| tcp | 38.9 |
| probe | 258.1 |
| real_test | 179.4 |
| generate | 28.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50246 |
| vmess | 14082 |
| shadowsocks | 9646 |
| trojan | 8453 |
| hysteria2 | 1006 |
| http | 576 |
| shadowsocksr | 134 |
| socks | 68 |
| hysteria | 11 |
| tuic | 4 |
| anytls | 3 |

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
| 79.62 | shadowsocks | 263.0 | 636.7 | 21.69 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 156.146.38.170 |
| 78.76 | shadowsocks | 260.8 | 635.7 | 21.74 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 156.146.38.168 |
| 78.52 | vless | 202.6 | 511.5 | 23.09 | 0.0 | 10.0 | 7.35 | 18.08 | Au1rxx-base64 | 172.235.43.210 |
| 76.71 | shadowsocks | 286.5 | 637.0 | 21.15 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 23.150.248.20 |
| 75.54 | shadowsocks | 201.6 | 540.3 | 23.11 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 129.146.124.141 |
| 75.07 | hysteria2 | 487.8 | 1238.9 | 16.49 | 0.0 | 10.0 | 13.42 | 18.08 | Au1rxx-base64 | 66.94.121.46 |
| 74.91 | hysteria2 | 361.9 | 823.6 | 19.4 | 0.0 | 10.0 | 13.42 | 18.08 | Au1rxx-base64 | 159.223.157.129 |
| 73.82 | shadowsocks | 275.9 | 767.0 | 21.39 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 129.146.24.204 |
| 73.61 | shadowsocks | 301.1 | 341.8 | 20.81 | 2.18 | 9.91 | 13.85 | 18.08 | Au1rxx-base64 | 149.22.87.240 |
| 73.29 | shadowsocks | 246.2 | 616.5 | 22.08 | 0.0 | 10.0 | 13.85 | 11.86 | Surfboard-tg-mixed | 108.181.0.177 |
| 72.73 | vless | 235.0 | 514.5 | 22.34 | 0.0 | 10.0 | 7.35 | 18.08 | Au1rxx-base64 | 31.58.50.200 |
| 72.48 | vless | 304.3 | 651.3 | 20.73 | 0.0 | 10.0 | 7.35 | 18.08 | Au1rxx-base64 | 51.81.203.63 |
| 72.23 | shadowsocks | 360.9 | 782.9 | 19.42 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 37.19.198.244 |
| 72.11 | shadowsocks | 373.3 | 815.4 | 19.14 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 37.19.198.236 |
| 72.03 | vless | 288.5 | 456.0 | 21.1 | 0.0 | 10.0 | 7.35 | 18.08 | Au1rxx-base64 | 162.159.0.169 |
| 71.88 | shadowsocks | 393.1 | 882.8 | 18.68 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 37.19.198.160 |
| 71.28 | vless | 203.4 | 525.7 | 23.07 | 0.0 | 10.0 | 7.35 | 11.86 | Surfboard-tg-mixed | 172.235.38.85 |
| 71.27 | shadowsocks | 397.9 | 884.1 | 18.57 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 198.98.53.130 |
| 71.22 | shadowsocks | 371.1 | 761.0 | 19.19 | 0.0 | 10.0 | 13.85 | 18.08 | Au1rxx-base64 | 108.181.57.93 |
| 71.15 | hysteria2 | 322.4 | 755.3 | 20.32 | 0.0 | 10.0 | 13.42 | 18.08 | Au1rxx-base64 | 108.59.244.158 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.924 | 0.858 | 296 | 1703 | prefer |
| DeltaKronecker-all | 0.83 | 0.767 | 30 | 6324 | prefer |
| ermaozi | 0.763 | 0.769 | 26 | 325 | prefer |
| mheidari-all | 0.642 | 0.563 | 71 | 16289 | observe |
| Surfboard-tg-mixed | 0.511 | 0.43 | 151 | 7076 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 132 | observe |
| Epodonios-all | 0.255 | None | 0 | 7611 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9154 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5712 | observe |
| barry-far-vless | 0.255 | None | 0 | 6010 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4344 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1703 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 54 |
| geo | ClientOSError | - | 34 |
| 204 | TimeoutError | - | 22 |
| 204 | ProxyError | - | 15 |
| cn-block | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 12 |
| geo | TimeoutError | - | 8 |
| speed | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | ClientOSError | - | 4 |
| geo | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41535: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
