# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-31 13:19:36 |
| 运行耗时 | 260.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 79273 |
| 去重后节点 | 22282 |
| TCP 可达 | 3000 |
| 真实可用 | 503 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22282 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.5 |
| tcp | 35.0 |
| probe | 81.9 |
| real_test | 95.4 |
| generate | 40.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50131 |
| vmess | 10956 |
| shadowsocks | 10129 |
| trojan | 6151 |
| hysteria2 | 1548 |
| http | 140 |
| shadowsocksr | 131 |
| socks | 76 |
| hysteria | 7 |
| tuic | 4 |

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
| 83.81 | hysteria2 | 297.4 | 770.2 | 20.89 | 0.0 | 10.0 | 14.06 | 19.96 | Au1rxx-base64 | 159.223.157.129 |
| 82.8 | shadowsocks | 239.3 | 585.3 | 22.24 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 156.146.38.168 |
| 82.54 | shadowsocks | 250.7 | 609.9 | 21.98 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 156.146.38.169 |
| 82.43 | shadowsocks | 255.4 | 632.7 | 21.87 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 37.19.198.244 |
| 82.3 | shadowsocks | 260.9 | 648.8 | 21.74 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 37.19.198.243 |
| 82.28 | shadowsocks | 261.7 | 663.0 | 21.72 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 37.19.198.236 |
| 82.11 | shadowsocks | 269.2 | 670.9 | 21.55 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 37.19.198.160 |
| 81.7 | vless | 247.8 | 639.8 | 22.04 | 0.0 | 10.0 | 9.7 | 19.96 | Au1rxx-base64 | 216.152.147.28 |
| 81.53 | shadowsocks | 294.1 | 747.9 | 20.97 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 156.146.38.167 |
| 80.93 | vless | 281.2 | 775.4 | 21.27 | 0.0 | 10.0 | 9.7 | 19.96 | Au1rxx-base64 | 195.211.99.45 |
| 80.81 | vless | 286.4 | 792.8 | 21.15 | 0.0 | 10.0 | 9.7 | 19.96 | Au1rxx-base64 | 195.211.99.49 |
| 80.33 | vless | 276.6 | 674.9 | 21.38 | 0.0 | 9.64 | 9.7 | 19.96 | Au1rxx-base64 | ql6k-m23nix.logicara.top |
| 80.32 | shadowsocks | 207.0 | 576.7 | 22.99 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 84.32.131.61 |
| 79.74 | shadowsocks | 349.8 | 871.3 | 19.68 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 38.180.135.156 |
| 79.58 | vless | 339.4 | 780.3 | 19.92 | 0.0 | 10.0 | 9.7 | 19.96 | Au1rxx-base64 | 169.40.42.225 |
| 79.43 | shadowsocks | 249.7 | 612.4 | 22.0 | 0.0 | 10.0 | 14.6 | 19.96 | Au1rxx-base64 | 156.146.38.170 |
| 78.84 | vless | 371.3 | 994.9 | 19.18 | 0.0 | 10.0 | 9.7 | 19.96 | Au1rxx-base64 | 172.105.104.54 |
| 78.64 | vless | 318.8 | 796.4 | 20.4 | 0.0 | 10.0 | 9.7 | 19.96 | Au1rxx-base64 | 169.40.42.133 |
| 78.63 | vless | 290.5 | 689.9 | 21.05 | 0.0 | 10.0 | 9.7 | 19.96 | Au1rxx-base64 | 204.48.20.223 |
| 78.48 | hysteria2 | 254.9 | 529.4 | 21.88 | 0.0 | 10.0 | 14.06 | 19.96 | Au1rxx-base64 | 66.94.121.46 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.938 | 306 | 1804 | prefer |
| mheidari-all | 0.937 | 0.879 | 33 | 14620 | prefer |
| DeltaKronecker-all | 0.845 | 0.776 | 49 | 5904 | prefer |
| Surfboard-tg-mixed | 0.845 | 0.768 | 168 | 6828 | prefer |
| zhangkai | 0.806 | 0.826 | 23 | 144 | prefer |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7174 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7956 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5768 | observe |
| barry-far-vless | 0.255 | None | 0 | 5864 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 3987 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1804 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 19 |
| 204 | TimeoutError | - | 18 |
| geo | ClientOSError | - | 11 |
| geo | TimeoutError | - | 10 |
| 204 | ProxyConnectionError | - | 4 |
| 204 | ClientOSError | - | 4 |
| 204 | ProxyError | - | 4 |
| speed | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| speed | TimeoutError | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
