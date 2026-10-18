# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-18 20:58:50 |
| 运行耗时 | 294.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 97460 |
| 去重后节点 | 27664 |
| TCP 可达 | 3000 |
| 真实可用 | 347 |
| Verified 输出 | 143 |
| Global 输出 | 300 |
| All 输出 | 27664 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.5 |
| geo | 1.5 |
| tcp | 76.5 |
| probe | 99.9 |
| real_test | 74.1 |
| china_check | 21.3 |
| generate | 14.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57202 |
| vmess | 16828 |
| shadowsocks | 11698 |
| trojan | 9495 |
| hysteria2 | 1346 |
| http | 613 |
| shadowsocksr | 164 |
| socks | 68 |
| anytls | 22 |
| hysteria | 17 |
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
| 96.16 | hysteria2 | 248.1 | 0.6 | 22.03 | 14.98 | 10.0 | 12.27 | 18.38 | Au1rxx-base64 | 129.213.91.185 |
| 94.22 | shadowsocks | 267.0 | 0.8 | 21.6 | 14.97 | 10.0 | 13.27 | 18.38 | Au1rxx-base64 | 37.19.198.244 |
| 93.96 | shadowsocks | 265.6 | 8.5 | 21.63 | 14.68 | 10.0 | 13.27 | 18.38 | Au1rxx-base64 | 37.19.198.160 |
| 93.72 | vless | 287.1 | 0.9 | 21.13 | 14.97 | 8.9 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.163 |
| 93.37 | vless | 344.2 | 4.4 | 19.81 | 14.84 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.212 |
| 93.21 | vless | 328.3 | 18.3 | 20.18 | 14.31 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 137.184.218.169 |
| 93.2 | vless | 296.2 | 0.8 | 20.92 | 14.97 | 8.59 | 10.34 | 18.38 | Au1rxx-base64 | 66.70.179.198 |
| 92.99 | vless | 359.0 | 5.4 | 19.47 | 14.8 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.104 |
| 92.8 | vless | 239.5 | 3.2 | 22.23 | 14.88 | 6.97 | 10.34 | 18.38 | Au1rxx-base64 | 195.123.235.183 |
| 92.53 | vless | 318.4 | 6.2 | 20.41 | 14.77 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.15 |
| 92.53 | vless | 381.6 | 3.8 | 18.95 | 14.86 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.133 |
| 92.45 | vless | 342.6 | 0.3 | 19.85 | 14.99 | 8.89 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.16 |
| 92.44 | vless | 381.9 | 5.9 | 18.94 | 14.78 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 185.95.231.156 |
| 92.37 | shadowsocks | 260.2 | 0.8 | 21.75 | 14.97 | 10.0 | 13.27 | 18.38 | Au1rxx-base64 | 37.19.198.236 |
| 92.03 | shadowsocks | 283.0 | 0.6 | 21.23 | 14.98 | 10.0 | 13.27 | 18.38 | Au1rxx-base64 | 156.146.38.169 |
| 91.98 | vless | 318.1 | 0.4 | 20.41 | 14.99 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.173 |
| 91.9 | vless | 280.6 | 8.0 | 21.28 | 14.7 | 8.79 | 10.34 | 18.38 | Au1rxx-base64 | 195.211.98.43 |
| 91.86 | vless | 268.1 | 11.6 | 21.57 | 14.57 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 162.35.126.130 |
| 91.5 | shadowsocks | 280.9 | 1.3 | 21.28 | 14.95 | 9.98 | 13.27 | 18.38 | Au1rxx-base64 | 156.146.38.167 |
| 91.39 | vless | 416.1 | 0.7 | 18.15 | 14.98 | 10.0 | 10.34 | 18.38 | Au1rxx-base64 | 169.40.42.224 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.999 | 1.0 | 36 | 639 | prefer |
| Au1rxx-base64 | 0.892 | 0.825 | 280 | 1727 | prefer |
| mheidari-all | 0.822 | 0.747 | 91 | 23629 | prefer |
| DeltaKronecker-all | 0.53 | 0.7 | 10 | 4750 | observe |
| Surfboard-tg-mixed | 0.503 | 0.583 | 12 | 7036 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| SoliSpirit-all | 0.287 | 0.5 | 2 | 9755 | observe |
| roosterkid-openproxylist-v2ray | 0.275 | 0.667 | 3 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4983 | observe |
| Epodonios-all | 0.255 | None | 0 | 7503 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5553 | observe |
| barry-far-vless | 0.255 | None | 0 | 5766 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4246 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 40 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 10 |
| geo | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 3 |
| 204 | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | True | 143 | 56 | 0.5 |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
