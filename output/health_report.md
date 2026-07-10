# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-10 03:54:47 |
| 运行耗时 | 232.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 76163 |
| 去重后节点 | 23386 |
| TCP 可达 | 3000 |
| 真实可用 | 474 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23386 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| geo | 1.5 |
| tcp | 31.5 |
| probe | 57.0 |
| real_test | 111.4 |
| generate | 25.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43097 |
| trojan | 12456 |
| vmess | 10677 |
| shadowsocks | 9266 |
| hysteria2 | 286 |
| shadowsocksr | 142 |
| http | 135 |
| socks | 90 |
| hysteria | 8 |
| anytls | 5 |
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
| 78.31 | shadowsocks | 221.1 | 480.0 | 22.66 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 173.244.56.9 |
| 78.22 | shadowsocks | 225.0 | 486.4 | 22.57 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 173.244.56.6 |
| 77.45 | shadowsocks | 258.1 | 630.2 | 21.8 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 156.146.38.169 |
| 77.35 | shadowsocks | 240.9 | 614.5 | 22.2 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 108.181.118.10 |
| 77.32 | shadowsocks | 242.3 | 608.2 | 22.17 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 108.181.0.177 |
| 77.26 | shadowsocks | 266.5 | 637.7 | 21.61 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 156.146.38.167 |
| 76.56 | shadowsocks | 257.3 | 624.8 | 21.82 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 156.146.38.168 |
| 74.14 | shadowsocks | 314.0 | 257.1 | 20.51 | 5.36 | 9.85 | 12.57 | 17.08 | Au1rxx-base64 | 149.22.87.204 |
| 73.22 | shadowsocks | 256.0 | 624.7 | 21.85 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 156.146.38.170 |
| 71.48 | shadowsocks | 341.4 | 310.6 | 19.88 | 3.35 | 9.86 | 12.57 | 17.08 | Au1rxx-base64 | 149.22.87.241 |
| 70.14 | shadowsocks | 344.7 | 698.3 | 19.8 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 198.98.53.130 |
| 69.77 | shadowsocks | 368.7 | 762.9 | 19.24 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 37.19.198.244 |
| 69.66 | trojan | 339.5 | 834.2 | 19.92 | 0.0 | 10.0 | 5.87 | 17.08 | Au1rxx-base64 | 149.28.241.235 |
| 69.48 | shadowsocks | 370.7 | 767.9 | 19.2 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 37.19.198.236 |
| 69.26 | shadowsocks | 370.2 | 782.1 | 19.21 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 37.19.198.160 |
| 69.16 | shadowsocks | 359.9 | 761.5 | 19.45 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 108.181.57.93 |
| 68.52 | vless | 212.0 | 490.1 | 22.87 | 0.0 | 10.0 | 4.83 | 11.82 | Surfboard-tg-mixed | 104.16.9.20 |
| 68.25 | vless | 223.8 | 559.7 | 22.6 | 0.0 | 10.0 | 4.83 | 11.82 | Surfboard-tg-mixed | 198.41.209.87 |
| 68.16 | shadowsocks | 282.1 | 592.0 | 21.25 | 0.0 | 10.0 | 12.57 | 17.08 | Au1rxx-base64 | 149.22.95.183 |
| 67.38 | shadowsocks | 372.3 | 551.4 | 19.16 | 0.0 | 9.85 | 12.57 | 17.08 | Au1rxx-base64 | 149.22.87.240 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.808 | 0.821 | 39 | 84 | prefer |
| Surfboard-tg-mixed | 0.744 | 0.665 | 349 | 5645 | prefer |
| mheidari-all | 0.634 | 0.555 | 211 | 16112 | observe |
| DeltaKronecker-all | 0.54 | 0.459 | 111 | 7533 | observe |
| nscl5-all | 0.404 | 1.0 | 3 | 1148 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| abc-configs-readme-latest30 | 0.256 | 1.0 | 1 | 19 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4306 | observe |
| Epodonios-all | 0.255 | None | 0 | 6482 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3975 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6617 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4155 | observe |
| barry-far-vless | 0.255 | None | 0 | 4661 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 134 |
| geo | TimeoutError | - | 70 |
| geo | ClientOSError | - | 22 |
| 204 | ProxyError | - | 21 |
| speed | TimeoutError | - | 13 |
| cn-block | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 279 | 300 | - |
| global | False | 293 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
