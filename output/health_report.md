# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-21 13:02:46 |
| 运行耗时 | 339.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 99 |
| 原始节点 | 95230 |
| 去重后节点 | 24848 |
| TCP 可达 | 3000 |
| 真实可用 | 1118 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24848 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.4 |
| geo | 0.9 |
| tcp | 38.9 |
| probe | 63.2 |
| real_test | 191.1 |
| generate | 36.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52462 |
| trojan | 18914 |
| vmess | 10873 |
| shadowsocks | 10791 |
| hysteria2 | 1641 |
| shadowsocksr | 196 |
| http | 166 |
| socks | 129 |
| anytls | 32 |
| hysteria | 15 |
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
| 85.09 | trojan | 213.0 | 476.4 | 22.85 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 35.88.210.26 |
| 85.04 | trojan | 214.9 | 482.7 | 22.8 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 34.220.224.252 |
| 84.75 | trojan | 215.3 | 479.4 | 22.79 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 34.223.2.163 |
| 84.71 | trojan | 229.1 | 528.9 | 22.47 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 44.247.89.62 |
| 84.66 | trojan | 229.7 | 518.7 | 22.46 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 35.88.120.18 |
| 84.41 | trojan | 242.3 | 557.0 | 22.17 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 54.213.46.211 |
| 84.35 | trojan | 244.8 | 568.8 | 22.11 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 44.255.190.116 |
| 84.32 | trojan | 229.4 | 525.9 | 22.47 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 35.91.138.234 |
| 84.02 | trojan | 259.3 | 615.2 | 21.78 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 35.90.27.143 |
| 83.93 | shadowsocks | 173.3 | 486.9 | 23.77 | 0.0 | 10.0 | 14.16 | 20.0 | Au1rxx-base64 | 167.99.103.190 |
| 83.81 | trojan | 263.6 | 631.1 | 21.68 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 35.91.98.35 |
| 83.7 | trojan | 229.7 | 531.4 | 22.46 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 35.160.249.189 |
| 83.62 | shadowsocks | 175.6 | 460.8 | 23.71 | 0.0 | 10.0 | 14.16 | 20.0 | Au1rxx-base64 | 209.38.142.23 |
| 83.55 | trojan | 279.5 | 676.9 | 21.31 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 54.244.169.225 |
| 83.51 | trojan | 238.1 | 544.0 | 22.27 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 34.210.213.17 |
| 83.23 | trojan | 293.1 | 713.4 | 20.99 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 44.243.85.47 |
| 83.14 | hysteria2 | 229.7 | 548.6 | 22.46 | 0.0 | 10.0 | 13.8 | 17.88 | mheidari-all | 150.241.102.127 |
| 83.08 | trojan | 299.8 | 733.3 | 20.84 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 44.246.163.102 |
| 83.03 | trojan | 293.3 | 716.3 | 20.99 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 54.245.126.186 |
| 82.94 | trojan | 305.9 | 749.1 | 20.7 | 0.0 | 10.0 | 14.74 | 20.0 | Au1rxx-base64 | 44.251.158.80 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.973 | 710 | 1897 | prefer |
| zhangkai | 0.997 | 1.0 | 111 | 144 | prefer |
| Surfboard-tg-mixed | 0.903 | 0.829 | 111 | 6419 | prefer |
| mheidari-all | 0.808 | 0.73 | 300 | 22031 | prefer |
| nscl5-all | 0.391 | 1.0 | 2 | 3031 | observe |
| DeltaKronecker-all | 0.284 | 0.333 | 6 | 6250 | observe |
| tg-oneclickvpnkeys | 0.263 | 1.0 | 1 | 192 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5148 | observe |
| Epodonios-all | 0.255 | None | 0 | 7104 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3985 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7205 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5125 | observe |
| barry-far-vless | 0.255 | None | 0 | 5444 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4647 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5974 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 46 |
| 204 | TimeoutError | - | 16 |
| geo | TimeoutError | - | 15 |
| speed | TimeoutError | - | 15 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyError | - | 8 |
| speed | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
