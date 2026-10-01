# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-01 05:24:19 |
| 运行耗时 | 661.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97857 |
| 去重后节点 | 27300 |
| TCP 可达 | 3000 |
| 真实可用 | 437 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27300 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| geo | 1.6 |
| tcp | 44.9 |
| probe | 240.8 |
| real_test | 283.3 |
| generate | 83.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59761 |
| vmess | 15334 |
| shadowsocks | 11441 |
| trojan | 9069 |
| hysteria2 | 1407 |
| http | 551 |
| shadowsocksr | 164 |
| socks | 66 |
| anytls | 40 |
| hysteria | 16 |
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
| 82.68 | vless | 236.2 | 627.5 | 22.31 | 0.0 | 10.0 | 11.57 | 18.8 | Surfboard-tg-mixed | 195.123.235.177 |
| 82.31 | hysteria2 | 249.2 | 694.3 | 22.01 | 0.0 | 10.0 | 13.12 | 18.28 | Au1rxx-base64 | 159.223.157.129 |
| 81.87 | vless | 248.8 | 660.6 | 22.02 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 137.184.218.169 |
| 81.19 | vless | 277.9 | 672.2 | 21.34 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.224 |
| 81.13 | vless | 280.8 | 680.5 | 21.28 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.202 |
| 81.12 | vless | 281.2 | 708.7 | 21.27 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 66.70.179.198 |
| 80.99 | vless | 286.8 | 766.3 | 21.14 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.15 |
| 80.71 | vless | 298.7 | 737.9 | 20.86 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 158.69.112.254 |
| 80.31 | vless | 316.2 | 875.9 | 20.46 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 159.89.87.21 |
| 80.25 | shadowsocks | 253.7 | 706.0 | 21.91 | 0.0 | 10.0 | 14.06 | 18.28 | Au1rxx-base64 | 37.19.198.160 |
| 80.12 | vless | 256.1 | 663.0 | 21.85 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.235 |
| 79.88 | vless | 334.9 | 975.2 | 20.03 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 79.141.172.154 |
| 79.83 | vless | 336.8 | 911.9 | 19.98 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.223 |
| 79.71 | vless | 342.1 | 877.2 | 19.86 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.179 |
| 79.7 | shadowsocks | 277.4 | 781.9 | 21.36 | 0.0 | 10.0 | 14.06 | 18.28 | Au1rxx-base64 | 37.19.198.243 |
| 79.56 | vless | 348.5 | 880.6 | 19.71 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.184 |
| 79.51 | vless | 299.0 | 684.8 | 20.86 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 198.251.78.29 |
| 79.41 | vless | 266.3 | 700.5 | 21.61 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.173 |
| 79.34 | vless | 288.6 | 647.4 | 21.1 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.163 |
| 79.3 | vless | 281.7 | 743.3 | 21.26 | 0.0 | 10.0 | 11.57 | 18.28 | Au1rxx-base64 | 169.40.42.35 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.872 | 0.806 | 314 | 1694 | prefer |
| ermaozi | 0.807 | 0.842 | 19 | 588 | prefer |
| Surfboard-tg-mixed | 0.691 | 0.613 | 160 | 7136 | observe |
| DeltaKronecker-all | 0.612 | 0.625 | 16 | 5434 | observe |
| mheidari-all | 0.381 | 0.298 | 191 | 22835 | observe |
| tg-oneclickvpnkeys | 0.314 | 1.0 | 2 | 80 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5327 | observe |
| Epodonios-all | 0.255 | None | 0 | 7637 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9403 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5815 | observe |
| barry-far-vless | 0.255 | None | 0 | 6001 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4183 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 82 |
| speed | ClientOSError | - | 58 |
| speed | TimeoutError | - | 44 |
| geo | ClientOSError | - | 30 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 13 |
| cn-block | ClientOSError | - | 8 |
| 204 | ProxyError | - | 7 |
| 204 | ClientOSError | - | 5 |
| 204 | ProxyConnectionError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | parse | TimeoutError | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
