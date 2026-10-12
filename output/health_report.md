# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-12 15:13:49 |
| 运行耗时 | 879.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 100392 |
| 去重后节点 | 27824 |
| TCP 可达 | 3000 |
| 真实可用 | 490 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27824 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| geo | 1.5 |
| tcp | 46.9 |
| probe | 372.9 |
| real_test | 368.3 |
| generate | 82.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58914 |
| vmess | 16072 |
| shadowsocks | 11789 |
| trojan | 11208 |
| hysteria2 | 1468 |
| http | 651 |
| shadowsocksr | 171 |
| socks | 70 |
| anytls | 26 |
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
| 85.58 | hysteria2 | 223.6 | 228.4 | 22.6 | 6.43 | 9.93 | 14.12 | 19.56 | Au1rxx-base64 | 45.32.10.7 |
| 84.99 | hysteria2 | 223.6 | 230.0 | 22.6 | 6.38 | 9.14 | 14.12 | 19.56 | Au1rxx-base64 | vp3.yysyy.online |
| 84.84 | hysteria2 | 242.8 | 603.3 | 22.16 | 0.0 | 10.0 | 14.12 | 19.56 | Au1rxx-base64 | 66.94.121.46 |
| 81.89 | trojan | 308.4 | 750.6 | 20.64 | 0.0 | 9.87 | 14.32 | 19.56 | Au1rxx-base64 | pro-mako.rooster465.autos |
| 79.5 | trojan | 417.1 | 878.4 | 18.12 | 0.0 | 10.0 | 14.32 | 19.56 | Au1rxx-base64 | 34.220.15.24 |
| 79.2 | vless | 180.6 | 454.4 | 23.6 | 0.0 | 10.0 | 6.04 | 19.56 | Au1rxx-base64 | 47.251.108.158 |
| 78.95 | shadowsocks | 250.2 | 528.7 | 21.99 | 0.0 | 10.0 | 13.75 | 19.56 | Au1rxx-base64 | 173.244.56.6 |
| 78.48 | hysteria2 | 255.4 | 299.1 | 21.87 | 3.78 | 9.18 | 14.12 | 19.56 | Au1rxx-base64 | open.2ml.cc.cd |
| 78.23 | vless | 222.4 | 556.9 | 22.63 | 0.0 | 10.0 | 6.04 | 19.56 | Au1rxx-base64 | 154.9.241.170 |
| 78.01 | hysteria2 | 354.3 | 765.3 | 19.58 | 0.0 | 10.0 | 14.12 | 19.56 | Au1rxx-base64 | 129.213.91.185 |
| 77.54 | vless | 252.1 | 637.7 | 21.94 | 0.0 | 10.0 | 6.04 | 19.56 | Au1rxx-base64 | 154.29.145.196 |
| 76.8 | shadowsocks | 319.6 | 740.3 | 20.38 | 0.0 | 10.0 | 13.75 | 19.56 | Au1rxx-base64 | 156.146.38.170 |
| 76.54 | shadowsocks | 292.2 | 656.0 | 21.02 | 0.0 | 10.0 | 13.75 | 19.56 | Au1rxx-base64 | 156.146.38.169 |
| 76.05 | trojan | 336.5 | 335.8 | 19.99 | 2.41 | 9.92 | 14.32 | 19.56 | Au1rxx-base64 | 13.193.213.184 |
| 75.99 | trojan | 334.6 | 338.7 | 20.03 | 2.3 | 9.93 | 14.32 | 19.56 | Au1rxx-base64 | 52.194.251.232 |
| 75.88 | trojan | 330.2 | 333.9 | 20.13 | 2.48 | 9.91 | 14.32 | 19.56 | Au1rxx-base64 | 45.32.52.173 |
| 75.73 | trojan | 334.6 | 343.0 | 20.03 | 2.14 | 9.88 | 14.32 | 19.56 | Au1rxx-base64 | 18.183.167.216 |
| 75.7 | trojan | 335.0 | 346.6 | 20.02 | 2.0 | 9.92 | 14.32 | 19.56 | Au1rxx-base64 | 43.206.225.188 |
| 75.59 | trojan | 330.3 | 333.9 | 20.13 | 2.48 | 9.21 | 14.32 | 19.56 | Au1rxx-base64 | live-stallion.rooster465.autos |
| 75.54 | trojan | 329.5 | 336.4 | 20.15 | 2.39 | 9.04 | 14.32 | 19.56 | Au1rxx-base64 | jp.tronsg.com |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.98 | 0.909 | 342 | 1816 | prefer |
| mheidari-all | 0.961 | 0.895 | 57 | 24027 | prefer |
| Surfboard-tg-mixed | 0.798 | 0.73 | 37 | 7166 | prefer |
| DeltaKronecker-all | 0.663 | 0.584 | 125 | 5701 | observe |
| ermaozi | 0.468 | 0.439 | 57 | 675 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| ermaozi-get_subscribe | 0.276 | 1.0 | 1 | 532 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5028 | observe |
| Epodonios-all | 0.255 | None | 0 | 7671 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9940 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5781 | observe |
| barry-far-vless | 0.255 | None | 0 | 6031 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 34 |
| cn-block | TimeoutError | - | 31 |
| 204 | TimeoutError | - | 26 |
| 204 | ProxyConnectionError | - | 8 |
| geo | ClientOSError | - | 8 |
| speed | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 6 |
| geo | TimeoutError | - | 3 |
| speed | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
