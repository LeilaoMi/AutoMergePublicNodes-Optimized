# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 04:05:44 |
| 运行耗时 | 326.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99761 |
| 去重后节点 | 27999 |
| TCP 可达 | 3000 |
| 真实可用 | 99 |
| Verified 输出 | 99 |
| Global 输出 | 106 |
| All 输出 | 27999 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.5 |
| tcp | 86.3 |
| probe | 95.5 |
| real_test | 99.4 |
| china_check | 28.4 |
| write_verified | 0.2 |
| generate | 9.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58945 |
| vmess | 16453 |
| shadowsocks | 11836 |
| trojan | 10316 |
| hysteria2 | 1225 |
| http | 713 |
| shadowsocksr | 166 |
| socks | 59 |
| anytls | 25 |
| hysteria | 17 |
| tuic | 6 |

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
| 77.02 | shadowsocks | 238.5 | 597.8 | 22.26 | 0.0 | 9.93 | 13.37 | 15.46 | Au1rxx-base64 | 156.146.38.168 |
| 76.85 | shadowsocks | 245.9 | 608.5 | 22.09 | 0.0 | 9.93 | 13.37 | 15.46 | Au1rxx-base64 | 156.146.38.167 |
| 74.2 | shadowsocks | 303.5 | 742.1 | 20.75 | 0.0 | 9.93 | 13.37 | 15.46 | Au1rxx-base64 | 37.19.198.244 |
| 73.27 | hysteria2 | 277.8 | 722.4 | 21.35 | 0.0 | 4.96 | 13.0 | 15.46 | Au1rxx-base64 | 129.213.91.185 |
| 73.09 | http | 267.0 | 675.8 | 21.6 | 0.0 | 0.0 | 14.35 | 19.64 | ermaozi | 172.64.68.89 |
| 72.7 | shadowsocks | 336.2 | 825.0 | 20.0 | 0.0 | 9.61 | 13.37 | 15.46 | Au1rxx-base64 | 37.19.198.243 |
| 72.43 | shadowsocks | 305.1 | 748.6 | 20.71 | 0.0 | 9.93 | 13.37 | 15.46 | Au1rxx-base64 | 37.19.198.236 |
| 72.38 | hysteria2 | 245.7 | 534.0 | 22.09 | 0.0 | 9.47 | 13.0 | 15.46 | Au1rxx-base64 | 179.255.104.98 |
| 72.21 | shadowsocks | 307.0 | 758.3 | 20.67 | 0.0 | 9.93 | 13.37 | 15.46 | Au1rxx-base64 | 37.19.198.160 |
| 71.87 | vless | 266.6 | 665.7 | 21.61 | 0.0 | 6.09 | 8.71 | 15.46 | Au1rxx-base64 | 195.211.98.43 |
| 70.11 | http | 285.8 | 603.7 | 21.16 | 0.0 | 0.0 | 14.35 | 19.64 | ermaozi | 64.98.50.100 |
| 68.3 | vless | 334.6 | 757.5 | 20.03 | 0.0 | 8.27 | 8.71 | 15.46 | Au1rxx-base64 | 167.17.69.171 |
| 68.12 | shadowsocks | 250.7 | 622.0 | 21.97 | 0.0 | 1.32 | 13.37 | 15.46 | Au1rxx-base64 | 156.146.38.169 |
| 67.1 | http | 327.0 | 759.5 | 20.21 | 0.0 | 0.0 | 14.35 | 19.64 | ermaozi | 38.247.141.135 |
| 66.98 | http | 315.1 | 644.3 | 20.48 | 0.0 | 0.0 | 14.35 | 19.64 | ermaozi | 138.199.35.202 |
| 66.87 | http | 406.2 | 1031.6 | 18.38 | 0.0 | 0.0 | 14.35 | 19.64 | ermaozi | 121.127.34.82 |
| 66.83 | http | 372.0 | 902.0 | 19.17 | 0.0 | 0.0 | 14.35 | 19.64 | ermaozi | 206.223.161.47 |
| 66.42 | vless | 341.6 | 802.6 | 19.87 | 0.0 | 6.01 | 8.71 | 15.46 | Au1rxx-base64 | 66.70.179.198 |
| 65.28 | vless | 294.4 | 646.3 | 20.96 | 0.0 | 6.32 | 8.71 | 15.46 | Au1rxx-base64 | 195.123.235.183 |
| 65.25 | vless | 300.6 | 662.5 | 20.82 | 0.0 | 8.4 | 8.71 | 15.46 | Au1rxx-base64 | 195.123.235.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.983 | 0.966 | 87 | 693 | prefer |
| Au1rxx-base64 | 0.804 | 0.725 | 459 | 1991 | prefer |
| mheidari-all | 0.436 | 0.354 | 144 | 23985 | observe |
| Surfboard-tg-mixed | 0.391 | 1.0 | 2 | 7135 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5089 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1991 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5147 | observe |
| Epodonios-all | 0.255 | None | 0 | 7647 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9903 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5628 | observe |
| barry-far-vless | 0.255 | None | 0 | 5878 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4235 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 148 |
| speed | ClientOSError | - | 36 |
| geo | ClientOSError | - | 19 |
| cn-block | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 4 |
| 204 | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound: start inbound/socks[socks-in]: listen tcp 127.0.0.1:43955: bind: address already in use | - | 1 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 85 | 99 | - |
| global | False | 93 | 106 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
