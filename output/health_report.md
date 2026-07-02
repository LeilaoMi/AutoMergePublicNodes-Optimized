# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-02 19:44:44 |
| 运行耗时 | 241.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 104 |
| 原始节点 | 77576 |
| 去重后节点 | 23214 |
| TCP 可达 | 3000 |
| 真实可用 | 347 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23214 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.4 |
| tcp | 30.5 |
| probe | 57.7 |
| real_test | 115.3 |
| generate | 31.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44782 |
| trojan | 12739 |
| vmess | 10338 |
| shadowsocks | 9035 |
| hysteria2 | 244 |
| socks | 154 |
| shadowsocksr | 142 |
| http | 135 |
| hysteria | 6 |
| tuic | 1 |

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
| 76.15 | shadowsocks | 224.6 | 497.0 | 22.58 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 173.244.56.9 |
| 75.31 | shadowsocks | 239.4 | 611.6 | 22.24 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 108.181.118.10 |
| 75.02 | shadowsocks | 219.5 | 520.4 | 22.7 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 173.244.56.6 |
| 74.22 | shadowsocks | 286.5 | 744.1 | 21.15 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 108.181.0.177 |
| 73.75 | shadowsocks | 241.9 | 577.8 | 22.18 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 149.22.95.183 |
| 73.66 | vless | 311.7 | 816.4 | 20.56 | 0.0 | 10.0 | 7.58 | 15.52 | Au1rxx-base64 | 15.204.97.214 |
| 71.15 | shadowsocks | 291.4 | 649.9 | 21.03 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 156.146.38.168 |
| 70.87 | shadowsocks | 294.1 | 669.5 | 20.97 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 156.146.38.167 |
| 70.63 | shadowsocks | 300.2 | 672.9 | 20.83 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 156.146.38.169 |
| 70.04 | shadowsocks | 295.8 | 669.8 | 20.93 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 156.146.38.170 |
| 67.22 | shadowsocks | 182.2 | 485.0 | 23.56 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 216.105.168.18 |
| 66.68 | shadowsocks | 294.9 | 342.5 | 20.95 | 2.16 | 9.95 | 12.05 | 12.68 | mheidari-all | 149.22.87.240 |
| 66.52 | shadowsocks | 375.9 | 727.3 | 19.08 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 37.19.198.236 |
| 66.43 | shadowsocks | 295.9 | 347.8 | 20.93 | 1.96 | 9.95 | 12.05 | 12.68 | mheidari-all | 149.22.87.204 |
| 66.43 | shadowsocks | 330.5 | 456.6 | 20.13 | 0.0 | 9.88 | 12.05 | 15.52 | Au1rxx-base64 | 149.22.87.241 |
| 65.56 | shadowsocks | 427.5 | 905.7 | 17.88 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 37.19.198.244 |
| 65.56 | shadowsocks | 432.0 | 900.7 | 17.78 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 37.19.198.243 |
| 65.49 | shadowsocks | 431.1 | 916.8 | 17.8 | 0.0 | 10.0 | 12.05 | 15.52 | Au1rxx-base64 | 37.19.198.160 |
| 64.77 | trojan | 393.7 | 895.2 | 18.67 | 0.0 | 10.0 | 10.88 | 12.68 | mheidari-all | 64.94.95.118 |
| 64.21 | shadowsocks | 349.0 | 346.8 | 19.7 | 1.99 | 9.61 | 12.05 | 15.2 | Surfboard-tg-mixed | 61.231.25.172 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.784 | 0.8 | 30 | 64 | prefer |
| mheidari-all | 0.747 | 0.672 | 67 | 16059 | prefer |
| Surfboard-tg-mixed | 0.658 | 0.578 | 346 | 6088 | observe |
| DeltaKronecker-all | 0.628 | 0.549 | 71 | 7467 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1162 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4254 | observe |
| Epodonios-all | 0.255 | None | 0 | 6895 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6658 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4550 | observe |
| barry-far-vless | 0.255 | None | 0 | 5048 | observe |
| ermaozi | 0.255 | 1.0 | 1 | 6 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5372 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 77 |
| 204 | TimeoutError | - | 21 |
| 204 | ProxyError | - | 16 |
| cn-block | ClientOSError | - | 16 |
| 204 | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 14 |
| geo | ClientOSError | - | 14 |
| geo | TimeoutError | - | 12 |
| cn-block | ProxyError | - | 11 |
| speed | TimeoutError | - | 5 |
| geo | ProxyError | - | 4 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
