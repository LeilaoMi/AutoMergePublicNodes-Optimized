# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-10 02:15:07 |
| 运行耗时 | 277.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 86295 |
| 去重后节点 | 23966 |
| TCP 可达 | 3000 |
| 真实可用 | 583 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23966 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.4 |
| tcp | 34.3 |
| probe | 52.5 |
| real_test | 138.9 |
| generate | 44.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51902 |
| vmess | 13188 |
| trojan | 9850 |
| shadowsocks | 9679 |
| hysteria2 | 1444 |
| socks | 73 |
| shadowsocksr | 70 |
| http | 40 |
| anytls | 26 |
| hysteria | 15 |
| tuic | 8 |

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
| 84.87 | hysteria2 | 233.0 | 640.0 | 22.38 | 0.0 | 9.5 | 14.35 | 19.74 | Au1rxx-base64 | 159.223.157.129 |
| 84.73 | hysteria2 | 243.4 | 672.0 | 22.14 | 0.0 | 9.5 | 14.35 | 19.74 | Au1rxx-base64 | 138.124.68.188 |
| 83.45 | hysteria2 | 244.4 | 676.0 | 22.12 | 0.0 | 8.24 | 14.35 | 19.74 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 80.91 | vless | 301.2 | 808.0 | 20.81 | 0.0 | 10.0 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.16 |
| 80.83 | shadowsocks | 223.6 | 616.7 | 22.6 | 0.0 | 9.37 | 13.12 | 19.74 | Au1rxx-base64 | 37.19.198.244 |
| 80.8 | vless | 281.5 | 748.7 | 21.26 | 0.0 | 9.44 | 10.36 | 19.74 | Au1rxx-base64 | 167.17.69.171 |
| 80.79 | vless | 281.9 | 630.2 | 21.25 | 0.0 | 9.44 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.15 |
| 80.65 | vless | 286.4 | 718.9 | 21.15 | 0.0 | 9.4 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.232 |
| 80.52 | shadowsocks | 237.4 | 658.9 | 22.28 | 0.0 | 9.38 | 13.12 | 19.74 | Au1rxx-base64 | 37.19.198.236 |
| 80.41 | vless | 322.8 | 875.9 | 20.31 | 0.0 | 10.0 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.212 |
| 80.28 | vless | 303.7 | 815.8 | 20.75 | 0.0 | 9.43 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.95 |
| 80.21 | shadowsocks | 250.6 | 695.7 | 21.98 | 0.0 | 9.37 | 13.12 | 19.74 | Au1rxx-base64 | 37.19.198.243 |
| 79.68 | vless | 331.0 | 900.5 | 20.12 | 0.0 | 9.46 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.179 |
| 79.31 | vless | 302.0 | 832.3 | 20.79 | 0.0 | 9.42 | 10.36 | 19.74 | Au1rxx-base64 | 159.89.87.21 |
| 79.28 | vless | 346.0 | 816.7 | 19.77 | 0.0 | 9.41 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.192 |
| 78.86 | trojan | 301.0 | 653.9 | 20.81 | 0.0 | 10.0 | 14.51 | 19.74 | Au1rxx-base64 | 64.94.95.114 |
| 78.79 | trojan | 297.1 | 639.6 | 20.9 | 0.0 | 10.0 | 14.51 | 19.74 | Au1rxx-base64 | 64.94.95.115 |
| 78.79 | vless | 392.6 | 961.6 | 18.69 | 0.0 | 10.0 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.133 |
| 78.64 | trojan | 298.3 | 633.7 | 20.87 | 0.0 | 10.0 | 14.51 | 19.74 | Au1rxx-base64 | 64.94.95.117 |
| 78.52 | vless | 337.0 | 914.1 | 19.98 | 0.0 | 10.0 | 10.36 | 19.74 | Au1rxx-base64 | 169.40.42.184 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | 0.893 | 457 | 1716 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.662 | 0.583 | 156 | 6683 | observe |
| tg-oneclickvpnkeys | 0.402 | 1.0 | 4 | 44 | observe |
| nscl5-all | 0.313 | 1.0 | 1 | 1442 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| mheidari-all | 0.258 | 0.176 | 296 | 20202 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5505 | observe |
| Epodonios-all | 0.255 | None | 0 | 7220 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7672 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5494 | observe |
| barry-far-vless | 0.255 | None | 0 | 5808 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5189 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1716 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 152 |
| speed | TimeoutError | - | 80 |
| geo | ClientOSError | - | 73 |
| speed | ClientOSError | - | 31 |
| cn-block | TimeoutError | - | 28 |
| 204 | TimeoutError | - | 11 |
| 204 | ProxyError | - | 11 |
| 204 | ClientOSError | - | 3 |
| cn-block | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | status | 403 | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
