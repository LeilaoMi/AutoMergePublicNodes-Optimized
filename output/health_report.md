# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-06 13:15:25 |
| 运行耗时 | 512.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97839 |
| 去重后节点 | 26950 |
| TCP 可达 | 3000 |
| 真实可用 | 423 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26950 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.5 |
| geo | 1.5 |
| tcp | 45.4 |
| probe | 201.7 |
| real_test | 162.0 |
| generate | 94.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57284 |
| vmess | 16153 |
| shadowsocks | 11738 |
| trojan | 10190 |
| hysteria2 | 1428 |
| http | 715 |
| shadowsocksr | 171 |
| socks | 97 |
| anytls | 36 |
| hysteria | 17 |
| tuic | 10 |

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
| 84.52 | hysteria2 | 278.6 | 733.4 | 21.33 | 0.0 | 10.0 | 14.29 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 81.66 | hysteria2 | 384.8 | 1101.9 | 18.87 | 0.0 | 10.0 | 14.29 | 20.0 | Au1rxx-base64 | 129.213.91.185 |
| 81.43 | shadowsocks | 253.8 | 704.0 | 21.9 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 81.39 | shadowsocks | 255.7 | 714.9 | 21.86 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 81.38 | shadowsocks | 256.2 | 715.9 | 21.85 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.34 | shadowsocks | 257.6 | 718.5 | 21.81 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 37.19.198.243 |
| 80.92 | shadowsocks | 254.4 | 661.9 | 21.89 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 140.82.63.79 |
| 79.7 | vless | 254.4 | 689.8 | 21.89 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 159.89.87.21 |
| 79.35 | shadowsocks | 322.0 | 924.9 | 20.32 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 15.204.233.41 |
| 79.27 | vless | 272.7 | 711.5 | 21.46 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 79.25 | vless | 273.6 | 708.0 | 21.44 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 169.40.42.133 |
| 79.02 | shadowsocks | 336.3 | 961.2 | 19.99 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 15.204.247.206 |
| 78.95 | vless | 286.6 | 712.3 | 21.14 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 66.70.179.198 |
| 78.89 | vless | 289.4 | 723.4 | 21.08 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 2.24.124.64 |
| 78.75 | shadowsocks | 282.2 | 651.8 | 21.25 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 78.62 | vless | 300.8 | 694.8 | 20.81 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 169.40.42.235 |
| 77.77 | vless | 330.8 | 842.0 | 20.12 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 169.40.42.168 |
| 77.59 | vless | 345.6 | 885.9 | 19.78 | 0.0 | 10.0 | 7.81 | 20.0 | Au1rxx-base64 | 169.40.42.15 |
| 77.36 | shadowsocks | 362.0 | 948.5 | 19.4 | 0.0 | 10.0 | 13.53 | 20.0 | Au1rxx-base64 | 185.156.47.97 |
| 77.27 | vless | 318.4 | 874.3 | 20.41 | 0.0 | 9.05 | 7.81 | 20.0 | Au1rxx-base64 | ww9.levikogjgfdd.ir |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.95 | 298 | 1805 | prefer |
| Surfboard-tg-mixed | 0.798 | 0.721 | 140 | 7050 | prefer |
| mheidari-all | 0.57 | 0.727 | 11 | 23204 | observe |
| ermaozi | 0.399 | 0.367 | 79 | 708 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4990 | observe |
| Epodonios-all | 0.255 | None | 0 | 7553 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9571 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5573 | observe |
| barry-far-vless | 0.255 | None | 0 | 5839 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4373 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1805 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| ermaozi-get_subscribe | 0.231 | 0.5 | 2 | 597 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 42 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 13 |
| geo | ClientOSError | - | 9 |
| speed | ClientOSError | - | 8 |
| 204 | ProxyConnectionError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| geo | TimeoutError | - | 5 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
