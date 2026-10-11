# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-11 05:26:03 |
| 运行耗时 | 1086.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97520 |
| 去重后节点 | 27407 |
| TCP 可达 | 3000 |
| 真实可用 | 526 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27407 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.4 |
| tcp | 46.5 |
| probe | 349.6 |
| real_test | 604.6 |
| generate | 78.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56885 |
| vmess | 15828 |
| shadowsocks | 11863 |
| trojan | 10557 |
| hysteria2 | 1539 |
| http | 550 |
| shadowsocksr | 163 |
| socks | 75 |
| anytls | 37 |
| hysteria | 16 |
| tuic | 7 |

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
| 84.85 | hysteria2 | 221.4 | 229.3 | 22.65 | 6.4 | 9.58 | 13.7 | 19.66 | Au1rxx-base64 | vp3.yysyy.online |
| 84.04 | hysteria2 | 225.9 | 236.8 | 22.55 | 6.12 | 9.94 | 13.7 | 19.66 | Au1rxx-base64 | 45.32.10.7 |
| 83.8 | vless | 229.3 | 556.0 | 22.47 | 0.0 | 10.0 | 11.67 | 19.66 | Au1rxx-base64 | 15.204.97.197 |
| 83.07 | vless | 260.7 | 652.4 | 21.74 | 0.0 | 10.0 | 11.67 | 19.66 | Au1rxx-base64 | 15.204.97.216 |
| 82.49 | vless | 175.3 | 481.3 | 23.72 | 0.0 | 10.0 | 11.67 | 19.66 | Au1rxx-base64 | 47.251.108.158 |
| 81.1 | shadowsocks | 250.2 | 605.4 | 21.99 | 0.0 | 10.0 | 13.45 | 19.66 | Au1rxx-base64 | 149.22.95.183 |
| 80.66 | hysteria2 | 237.7 | 268.7 | 22.28 | 4.93 | 7.09 | 13.7 | 19.66 | Au1rxx-base64 | open.2ml.bid |
| 80.5 | vless | 328.5 | 845.2 | 20.17 | 0.0 | 10.0 | 11.67 | 19.66 | Au1rxx-base64 | 104.17.98.5 |
| 80.42 | shadowsocks | 279.5 | 596.7 | 21.31 | 0.0 | 10.0 | 13.45 | 19.66 | Au1rxx-base64 | 173.244.56.6 |
| 80.13 | shadowsocks | 270.5 | 714.0 | 21.52 | 0.0 | 10.0 | 13.45 | 19.66 | Au1rxx-base64 | 5.78.51.123 |
| 79.99 | http | 200.8 | 518.3 | 23.13 | 0.0 | 10.0 | 10.54 | 19.32 | zhangkai | 138.199.35.198 |
| 79.71 | shadowsocks | 291.4 | 574.8 | 21.03 | 0.0 | 10.0 | 13.45 | 19.66 | Au1rxx-base64 | 173.244.56.9 |
| 79.24 | vless | 209.6 | 530.4 | 22.93 | 0.0 | 10.0 | 11.67 | 19.66 | Au1rxx-base64 | 154.29.145.196 |
| 78.97 | trojan | 251.7 | 592.3 | 21.95 | 0.0 | 10.0 | 14.86 | 19.66 | Au1rxx-base64 | 16.144.66.136 |
| 78.59 | trojan | 251.1 | 589.1 | 21.97 | 0.0 | 4.6 | 14.86 | 19.66 | Au1rxx-base64 | pro-mako.rooster465.autos |
| 78.24 | hysteria2 | 342.1 | 750.5 | 19.86 | 0.0 | 10.0 | 13.7 | 19.66 | Au1rxx-base64 | 129.213.91.185 |
| 77.43 | vless | 288.3 | 730.7 | 21.1 | 0.0 | 10.0 | 11.67 | 19.66 | Au1rxx-base64 | 15.204.97.195 |
| 77.42 | shadowsocks | 294.8 | 663.8 | 20.95 | 0.0 | 10.0 | 13.45 | 19.66 | Au1rxx-base64 | 156.146.38.170 |
| 77.25 | shadowsocks | 291.3 | 658.5 | 21.03 | 0.0 | 10.0 | 13.45 | 19.66 | Au1rxx-base64 | 156.146.38.167 |
| 77.2 | shadowsocks | 288.7 | 641.3 | 21.1 | 0.0 | 10.0 | 13.45 | 19.66 | Au1rxx-base64 | 156.146.38.168 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.991 | 0.922 | 370 | 1799 | prefer |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Surfboard-tg-mixed | 0.624 | 0.818 | 11 | 7087 | observe |
| ermaozi-get_subscribe | 0.596 | 0.577 | 26 | 610 | observe |
| DeltaKronecker-all | 0.418 | 0.375 | 16 | 5009 | observe |
| mheidari-all | 0.408 | 0.327 | 398 | 23694 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4347 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4999 | observe |
| Epodonios-all | 0.255 | None | 0 | 7576 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9365 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5545 | observe |
| barry-far-vless | 0.255 | None | 0 | 5790 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 153 |
| speed | TimeoutError | - | 52 |
| geo | ClientOSError | - | 35 |
| speed | ClientOSError | - | 28 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyError | - | 13 |
| 204 | ClientOSError | - | 12 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 4 |
| speed | ClientPayloadError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
