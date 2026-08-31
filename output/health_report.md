# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-31 04:57:07 |
| 运行耗时 | 290.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 78971 |
| 去重后节点 | 21904 |
| TCP 可达 | 3000 |
| 真实可用 | 638 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21904 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| geo | 1.6 |
| tcp | 35.3 |
| probe | 82.5 |
| real_test | 141.4 |
| generate | 24.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49458 |
| vmess | 10820 |
| shadowsocks | 10176 |
| trojan | 6583 |
| hysteria2 | 1543 |
| http | 168 |
| shadowsocksr | 128 |
| socks | 85 |
| hysteria | 7 |
| tuic | 3 |

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
| 83.71 | hysteria2 | 271.3 | 685.6 | 21.5 | 0.0 | 10.0 | 14.21 | 20.0 | Au1rxx-base64 | 66.94.121.46 |
| 82.97 | vless | 252.5 | 551.0 | 21.93 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 64.23.229.123 |
| 81.57 | shadowsocks | 238.7 | 603.2 | 22.25 | 0.0 | 10.0 | 13.32 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 80.63 | vless | 333.3 | 795.9 | 20.06 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 15.204.97.197 |
| 80.6 | vless | 348.6 | 841.2 | 19.71 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 15.204.97.216 |
| 80.58 | http | 233.8 | 510.5 | 22.37 | 0.0 | 10.0 | 14.4 | 19.32 | zhangkai | 138.199.35.216 |
| 80.54 | shadowsocks | 255.8 | 606.7 | 21.86 | 0.0 | 10.0 | 13.32 | 20.0 | Au1rxx-base64 | 84.32.131.61 |
| 80.45 | vless | 274.8 | 585.6 | 21.42 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 172.233.156.42 |
| 80.34 | vless | 277.5 | 585.7 | 21.35 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 172.233.139.46 |
| 80.34 | shadowsocks | 292.0 | 765.8 | 21.02 | 0.0 | 10.0 | 13.32 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 80.32 | vless | 301.6 | 664.3 | 20.8 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 195.211.99.49 |
| 80.18 | vless | 295.9 | 552.3 | 20.93 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 172.239.67.156 |
| 80.1 | vless | 351.3 | 848.2 | 19.65 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 15.204.97.206 |
| 79.75 | vless | 363.6 | 882.1 | 19.36 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 15.204.97.209 |
| 79.74 | vless | 274.6 | 583.9 | 21.42 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 172.239.67.231 |
| 79.64 | vless | 281.8 | 569.3 | 21.25 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 45.33.107.237 |
| 79.47 | vless | 278.4 | 580.5 | 21.33 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 172.235.38.85 |
| 79.47 | vless | 291.7 | 592.6 | 21.02 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 173.230.155.55 |
| 79.07 | vless | 282.1 | 585.8 | 21.25 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 216.167.21.162 |
| 79.0 | vless | 295.8 | 596.7 | 20.93 | 0.0 | 10.0 | 12.31 | 20.0 | Au1rxx-base64 | 74.207.245.124 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.998 | 0.928 | 307 | 1804 | prefer |
| zhangkai | 0.929 | 0.958 | 24 | 144 | prefer |
| Surfboard-tg-mixed | 0.815 | 0.737 | 217 | 6765 | prefer |
| DeltaKronecker-all | 0.578 | 0.498 | 325 | 5576 | observe |
| mheidari-all | 0.568 | 0.875 | 8 | 14559 | observe |
| Epodonios-all | 0.335 | 1.0 | 1 | 7271 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4762 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7850 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5673 | observe |
| barry-far-vless | 0.255 | None | 0 | 5858 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4041 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1804 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 103 |
| geo | ClientOSError | - | 56 |
| speed | TimeoutError | - | 17 |
| 204 | ProxyError | - | 16 |
| cn-block | TimeoutError | - | 15 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 11 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| 204 | ProxyConnectionError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
