# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-19 13:41:42 |
| 运行耗时 | 310.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 95109 |
| 去重后节点 | 26270 |
| TCP 可达 | 3000 |
| 真实可用 | 394 |
| Verified 输出 | 71 |
| Global 输出 | 300 |
| All 输出 | 26270 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.3 |
| geo | 1.5 |
| tcp | 80.8 |
| probe | 99.6 |
| real_test | 86.4 |
| china_check | 20.5 |
| write_verified | 0.0 |
| generate | 14.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 55647 |
| vmess | 16651 |
| shadowsocks | 11604 |
| trojan | 8900 |
| hysteria2 | 1506 |
| http | 497 |
| shadowsocksr | 172 |
| socks | 63 |
| anytls | 46 |
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
| 92.77 | vless | 300.0 | 2.0 | 20.83 | 14.93 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 66.70.179.198 |
| 92.34 | shadowsocks | 269.0 | 1.6 | 21.55 | 14.94 | 10.0 | 13.49 | 18.36 | Au1rxx-base64 | 37.19.198.243 |
| 91.88 | shadowsocks | 282.9 | 3.5 | 21.23 | 14.87 | 10.0 | 13.49 | 18.36 | Au1rxx-base64 | 156.146.38.169 |
| 91.67 | shadowsocks | 282.1 | 4.7 | 21.25 | 14.82 | 10.0 | 13.49 | 18.36 | Au1rxx-base64 | 156.146.38.170 |
| 91.18 | vless | 379.7 | 1.6 | 18.99 | 14.94 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.104 |
| 91.13 | vless | 373.7 | 6.7 | 19.13 | 14.75 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.202 |
| 90.71 | vless | 320.9 | 1.3 | 20.35 | 14.95 | 8.16 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.163 |
| 90.54 | vless | 385.7 | 15.0 | 18.85 | 14.44 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.168 |
| 90.51 | vless | 386.9 | 5.9 | 18.82 | 14.78 | 9.66 | 8.89 | 18.36 | Au1rxx-base64 | 185.95.231.156 |
| 90.36 | vless | 361.7 | 1.8 | 19.4 | 14.93 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.235 |
| 90.21 | vless | 360.0 | 2.6 | 19.45 | 14.9 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.90 |
| 90.18 | vless | 393.8 | 5.9 | 18.66 | 14.78 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.225 |
| 90.12 | vless | 359.6 | 0.8 | 19.45 | 14.97 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.229 |
| 89.75 | shadowsocks | 265.0 | 1.0 | 21.64 | 14.96 | 5.3 | 13.49 | 18.36 | Au1rxx-base64 | 37.19.198.160 |
| 89.61 | shadowsocks | 266.7 | 1.4 | 21.6 | 14.95 | 5.21 | 13.49 | 18.36 | Au1rxx-base64 | 37.19.198.236 |
| 89.49 | shadowsocks | 271.2 | 4.4 | 21.5 | 14.84 | 5.3 | 13.49 | 18.36 | Au1rxx-base64 | 37.19.198.244 |
| 88.75 | vless | 381.8 | 4.7 | 18.94 | 14.82 | 10.0 | 8.89 | 18.36 | Au1rxx-base64 | 169.40.42.35 |
| 87.54 | hysteria2 | 396.1 | 87.7 | 18.61 | 11.71 | 10.0 | 13.57 | 18.36 | Au1rxx-base64 | 129.213.91.185 |
| 87.17 | shadowsocks | 282.1 | 0.3 | 21.25 | 14.99 | 5.07 | 13.49 | 18.36 | Au1rxx-base64 | 156.146.38.167 |
| 86.85 | shadowsocks | 331.8 | 1.3 | 20.1 | 14.95 | 10.0 | 13.49 | 18.36 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | 1.0 | 19 | 144 | prefer |
| Au1rxx-base64 | 0.868 | 0.801 | 362 | 1717 | prefer |
| ermaozi-get_subscribe | 0.815 | 0.889 | 18 | 508 | prefer |
| Surfboard-tg-mixed | 0.641 | 0.564 | 55 | 6948 | observe |
| ermaozi | 0.441 | 1.0 | 5 | 42 | observe |
| mheidari-all | 0.373 | 0.6 | 5 | 23446 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 4940 | observe |
| tg-LonUp_M | 0.318 | 1.0 | 2 | 167 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| DeltaKronecker-all | 0.31 | 0.225 | 120 | 3294 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 77 | observe |
| Epodonios-all | 0.255 | None | 0 | 7331 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10136 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5438 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 85 |
| speed | ClientOSError | - | 42 |
| geo | ClientOSError | - | 31 |
| 204 | ProxyError | - | 9 |
| 204 | TimeoutError | - | 8 |
| cn-block | TimeoutError | - | 8 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 3 |
| speed | TimeoutError | - | 2 |
| geo | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 118 | 71 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
