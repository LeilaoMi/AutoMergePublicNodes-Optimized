# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-25 18:50:01 |
| 运行耗时 | 240.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 78004 |
| 去重后节点 | 22569 |
| TCP 可达 | 3000 |
| 真实可用 | 564 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22569 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| geo | 1.3 |
| tcp | 37.2 |
| probe | 55.0 |
| real_test | 118.5 |
| generate | 24.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48801 |
| shadowsocks | 10605 |
| vmess | 10458 |
| trojan | 6418 |
| hysteria2 | 1341 |
| http | 164 |
| shadowsocksr | 132 |
| socks | 75 |
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
| 80.12 | shadowsocks | 236.1 | 596.1 | 22.31 | 0.0 | 10.0 | 13.51 | 18.3 | Au1rxx-base64 | 156.146.38.169 |
| 80.08 | shadowsocks | 237.9 | 597.6 | 22.27 | 0.0 | 10.0 | 13.51 | 18.3 | Au1rxx-base64 | 156.146.38.168 |
| 79.65 | vless | 268.6 | 606.9 | 21.56 | 0.0 | 10.0 | 11.49 | 18.3 | Au1rxx-base64 | 15.204.97.197 |
| 79.61 | shadowsocks | 273.9 | 716.7 | 21.44 | 0.0 | 10.0 | 13.51 | 18.66 | mheidari-all | 156.146.38.170 |
| 79.54 | hysteria2 | 310.2 | 690.7 | 20.6 | 0.0 | 10.0 | 14.0 | 18.66 | mheidari-all | 159.223.157.129 |
| 79.52 | shadowsocks | 256.2 | 618.3 | 21.85 | 0.0 | 10.0 | 13.51 | 18.66 | mheidari-all | 23.150.248.20 |
| 79.4 | vless | 264.9 | 600.1 | 21.65 | 0.0 | 10.0 | 11.49 | 18.3 | Au1rxx-base64 | 15.204.97.195 |
| 78.86 | shadowsocks | 244.9 | 575.6 | 22.11 | 0.0 | 10.0 | 13.51 | 18.3 | Au1rxx-base64 | 94.72.127.55 |
| 78.83 | trojan | 272.0 | 679.6 | 21.48 | 0.0 | 10.0 | 12.05 | 18.3 | Au1rxx-base64 | 64.94.95.114 |
| 78.19 | shadowsocks | 241.6 | 618.9 | 22.18 | 0.0 | 10.0 | 13.51 | 16.5 | Surfboard-tg-mixed | 156.146.38.167 |
| 77.77 | vless | 355.1 | 869.9 | 19.56 | 0.0 | 10.0 | 11.49 | 18.3 | Au1rxx-base64 | 15.204.97.209 |
| 77.76 | shadowsocks | 259.1 | 536.0 | 21.78 | 0.0 | 10.0 | 13.51 | 18.3 | Au1rxx-base64 | 94.72.127.58 |
| 76.85 | vless | 320.3 | 673.3 | 20.36 | 0.0 | 10.0 | 11.49 | 18.3 | Au1rxx-base64 | 198.251.78.29 |
| 76.47 | trojan | 342.6 | 868.0 | 19.85 | 0.0 | 10.0 | 12.05 | 16.44 | DeltaKronecker-all | 69.164.205.61 |
| 75.92 | shadowsocks | 294.0 | 647.8 | 20.97 | 0.0 | 10.0 | 13.51 | 18.3 | Au1rxx-base64 | 155.138.136.240 |
| 75.9 | shadowsocks | 291.4 | 555.6 | 21.03 | 0.0 | 10.0 | 13.51 | 18.66 | mheidari-all | 173.244.56.9 |
| 75.89 | http | 475.8 | 1234.2 | 16.76 | 0.0 | 10.0 | 14.4 | 19.34 | zhangkai | 138.199.35.198 |
| 75.86 | vless | 362.7 | 857.9 | 19.38 | 0.0 | 10.0 | 11.49 | 18.3 | Au1rxx-base64 | 45.138.100.226 |
| 75.35 | trojan | 271.7 | 528.1 | 21.49 | 0.0 | 10.0 | 12.05 | 18.3 | Au1rxx-base64 | 35.91.251.124 |
| 75.33 | shadowsocks | 277.4 | 640.1 | 21.36 | 0.0 | 10.0 | 13.51 | 18.3 | Au1rxx-base64 | 154.53.60.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| DeltaKronecker-all | 0.943 | 0.878 | 49 | 6340 | prefer |
| Surfboard-tg-mixed | 0.908 | 0.835 | 97 | 6487 | prefer |
| Au1rxx-base64 | 0.902 | 0.843 | 427 | 1502 | prefer |
| mheidari-all | 0.843 | 0.77 | 74 | 14446 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 6936 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7007 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5327 | observe |
| barry-far-vless | 0.255 | None | 0 | 5601 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4119 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.235 | None | 0 | 1505 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 34 |
| geo | TimeoutError | - | 20 |
| 204 | TimeoutError | - | 19 |
| cn-block | TimeoutError | - | 15 |
| speed | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| 204 | ProxyError | - | 4 |
| 204 | ClientOSError | - | 3 |
| geo | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
