# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-10 12:26:41 |
| 运行耗时 | 794.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97803 |
| 去重后节点 | 27173 |
| TCP 可达 | 3000 |
| 真实可用 | 481 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27173 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| geo | 1.1 |
| tcp | 46.4 |
| probe | 305.2 |
| real_test | 351.5 |
| generate | 84.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57316 |
| vmess | 15803 |
| shadowsocks | 11808 |
| trojan | 10476 |
| hysteria2 | 1561 |
| http | 548 |
| shadowsocksr | 167 |
| socks | 71 |
| anytls | 28 |
| hysteria | 17 |
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
| 84.95 | hysteria2 | 223.9 | 224.6 | 22.59 | 6.58 | 9.56 | 14.17 | 19.94 | Au1rxx-base64 | vp3.yysyy.online |
| 84.53 | hysteria2 | 235.1 | 235.9 | 22.33 | 6.15 | 9.04 | 14.17 | 19.94 | Au1rxx-base64 | open.2ml.bid |
| 84.47 | hysteria2 | 247.0 | 240.1 | 22.06 | 5.99 | 9.76 | 14.17 | 19.94 | Au1rxx-base64 | 158.101.148.79 |
| 84.19 | hysteria2 | 224.0 | 226.0 | 22.59 | 6.52 | 9.91 | 14.17 | 19.94 | Au1rxx-base64 | 45.32.10.7 |
| 82.24 | shadowsocks | 236.4 | 506.4 | 22.3 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 173.244.56.9 |
| 81.91 | shadowsocks | 251.0 | 617.5 | 21.97 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 156.146.38.167 |
| 81.78 | shadowsocks | 256.4 | 626.4 | 21.84 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 156.146.38.169 |
| 81.71 | shadowsocks | 259.4 | 633.8 | 21.77 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 156.146.38.170 |
| 81.58 | shadowsocks | 252.6 | 621.5 | 21.93 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 156.146.38.168 |
| 80.45 | shadowsocks | 258.2 | 611.1 | 21.8 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 5.78.51.123 |
| 79.24 | hysteria2 | 320.2 | 748.4 | 20.37 | 0.0 | 10.0 | 14.17 | 19.94 | Au1rxx-base64 | 129.213.91.185 |
| 79.23 | vless | 206.7 | 501.9 | 22.99 | 0.0 | 10.0 | 6.3 | 19.94 | Au1rxx-base64 | 137.175.82.40 |
| 79.06 | vless | 214.1 | 513.5 | 22.82 | 0.0 | 10.0 | 6.3 | 19.94 | Au1rxx-base64 | 47.251.108.158 |
| 78.52 | vless | 237.5 | 546.2 | 22.28 | 0.0 | 10.0 | 6.3 | 19.94 | Au1rxx-base64 | 154.12.38.202 |
| 78.36 | http | 335.7 | 926.9 | 20.01 | 0.0 | 10.0 | 12.07 | 19.28 | zhangkai | 138.199.35.198 |
| 78.32 | shadowsocks | 272.5 | 556.7 | 21.47 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 173.244.56.6 |
| 78.12 | shadowsocks | 294.2 | 644.3 | 20.97 | 0.0 | 10.0 | 14.0 | 19.94 | Au1rxx-base64 | 149.22.95.183 |
| 77.46 | http | 331.3 | 911.5 | 20.11 | 0.0 | 10.0 | 12.07 | 19.28 | zhangkai | 138.199.35.216 |
| 76.83 | hysteria2 | 499.7 | 1090.9 | 16.21 | 0.0 | 10.0 | 14.17 | 19.94 | Au1rxx-base64 | 66.94.121.46 |
| 76.41 | vless | 285.4 | 690.1 | 21.17 | 0.0 | 10.0 | 6.3 | 19.94 | Au1rxx-base64 | 104.17.98.5 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.96 | 1.0 | 20 | 144 | prefer |
| Au1rxx-base64 | 0.951 | 0.88 | 367 | 1820 | prefer |
| mheidari-all | 0.898 | 0.833 | 42 | 23754 | prefer |
| Surfboard-tg-mixed | 0.712 | 0.634 | 131 | 7103 | prefer |
| DeltaKronecker-all | 0.68 | 0.607 | 28 | 5009 | observe |
| ermaozi-get_subscribe | 0.384 | 1.0 | 3 | 653 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4999 | observe |
| Epodonios-all | 0.255 | None | 0 | 7579 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9335 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5620 | observe |
| barry-far-vless | 0.255 | None | 0 | 5861 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4347 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1820 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 31 |
| 204 | TimeoutError | - | 25 |
| geo | ClientOSError | - | 12 |
| speed | ClientOSError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| speed | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 6 |
| 204 | ProxyError | - | 5 |
| geo | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
