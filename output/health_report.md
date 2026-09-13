# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-13 20:43:29 |
| 运行耗时 | 535.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 84974 |
| 去重后节点 | 23272 |
| TCP 可达 | 3000 |
| 真实可用 | 455 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23272 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.5 |
| tcp | 39.8 |
| probe | 229.4 |
| real_test | 180.3 |
| generate | 78.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51934 |
| vmess | 12906 |
| shadowsocks | 9850 |
| trojan | 7803 |
| hysteria2 | 1660 |
| http | 613 |
| shadowsocksr | 128 |
| socks | 55 |
| tuic | 12 |
| hysteria | 11 |
| anytls | 2 |

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
| 78.71 | vless | 247.3 | 680.4 | 22.05 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 79.141.172.154 |
| 78.55 | vless | 254.4 | 689.4 | 21.89 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 47.253.226.114 |
| 78.16 | vless | 271.1 | 690.1 | 21.5 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.173 |
| 78.08 | vless | 274.8 | 648.8 | 21.42 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.212 |
| 77.49 | vless | 300.2 | 743.1 | 20.83 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.104 |
| 77.4 | vless | 304.2 | 709.9 | 20.74 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.35 |
| 77.16 | vless | 314.4 | 831.1 | 20.5 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 137.184.218.169 |
| 77.06 | vless | 318.5 | 719.7 | 20.4 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.163 |
| 77.0 | vless | 321.2 | 724.4 | 20.34 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.179 |
| 76.88 | vless | 262.4 | 692.4 | 21.7 | 0.0 | 10.0 | 8.92 | 16.26 | Surfboard-tg-mixed | 47.89.186.170 |
| 76.57 | vless | 339.9 | 900.0 | 19.91 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.90 |
| 76.5 | vless | 343.1 | 909.5 | 19.84 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.16 |
| 76.49 | vless | 329.0 | 743.1 | 20.16 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.15 |
| 76.27 | vless | 352.8 | 826.6 | 19.61 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.232 |
| 76.23 | vless | 341.8 | 897.8 | 19.86 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.202 |
| 76.22 | vless | 326.3 | 739.8 | 20.22 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.229 |
| 76.21 | shadowsocks | 282.2 | 644.8 | 21.24 | 0.0 | 10.0 | 13.98 | 17.74 | Au1rxx-base64 | 156.146.38.170 |
| 76.21 | shadowsocks | 357.8 | 803.1 | 19.5 | 0.0 | 8.99 | 13.98 | 17.74 | Au1rxx-base64 | ca225.vpnbook.com |
| 76.19 | vless | 351.0 | 888.8 | 19.65 | 0.0 | 10.0 | 8.92 | 17.74 | Au1rxx-base64 | 169.40.42.235 |
| 76.13 | shadowsocks | 383.1 | 1009.0 | 18.91 | 0.0 | 10.0 | 13.98 | 17.74 | Au1rxx-base64 | 51.222.141.125 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | 0.891 | 304 | 1781 | prefer |
| mheidari-all | 0.869 | 0.806 | 36 | 16210 | prefer |
| Surfboard-tg-mixed | 0.822 | 0.745 | 153 | 7511 | prefer |
| DeltaKronecker-all | 0.8 | 0.739 | 23 | 5892 | prefer |
| ermaozi | 0.626 | 0.618 | 34 | 382 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4222 | observe |
| roosterkid-openproxylist-v2ray | 0.275 | 0.667 | 3 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4839 | observe |
| Epodonios-all | 0.255 | None | 0 | 8029 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8804 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6079 | observe |
| barry-far-vless | 0.255 | None | 0 | 6390 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1781 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 24 |
| cn-block | TimeoutError | - | 19 |
| geo | ClientOSError | - | 18 |
| speed | ClientOSError | - | 11 |
| cn-block | ClientOSError | - | 8 |
| speed | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| geo | exit-country | CN | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
