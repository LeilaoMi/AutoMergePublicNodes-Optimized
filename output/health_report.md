# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-05 08:47:54 |
| 运行耗时 | 246.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 85532 |
| 去重后节点 | 23905 |
| TCP 可达 | 3000 |
| 真实可用 | 504 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23905 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| geo | 1.1 |
| tcp | 35.5 |
| probe | 52.0 |
| real_test | 118.7 |
| generate | 32.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49981 |
| vmess | 13062 |
| trojan | 10665 |
| shadowsocks | 10250 |
| hysteria2 | 1291 |
| socks | 80 |
| http | 76 |
| shadowsocksr | 73 |
| anytls | 21 |
| hysteria | 19 |
| tuic | 14 |

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
| 85.57 | hysteria2 | 234.3 | 650.9 | 22.35 | 0.0 | 10.0 | 14.32 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 85.3 | hysteria2 | 250.5 | 688.2 | 21.98 | 0.0 | 10.0 | 14.32 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 84.94 | hysteria2 | 240.7 | 667.9 | 22.21 | 0.0 | 9.41 | 14.32 | 20.0 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 83.59 | http | 242.0 | 638.0 | 22.18 | 0.0 | 10.0 | 14.73 | 19.68 | zhangkai | 156.146.59.33 |
| 82.14 | shadowsocks | 229.3 | 637.6 | 22.47 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 82.03 | shadowsocks | 234.1 | 647.9 | 22.36 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 37.19.198.244 |
| 80.98 | shadowsocks | 279.4 | 777.8 | 21.31 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 37.19.198.160 |
| 80.97 | shadowsocks | 258.1 | 698.0 | 21.8 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 68.168.222.210 |
| 78.92 | shadowsocks | 346.8 | 867.5 | 19.75 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 185.196.61.82 |
| 78.8 | shadowsocks | 270.3 | 620.2 | 21.52 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 156.146.38.168 |
| 78.08 | trojan | 401.0 | 1136.6 | 18.5 | 0.0 | 10.0 | 12.58 | 20.0 | Au1rxx-base64 | 153.75.250.171 |
| 77.8 | shadowsocks | 290.2 | 809.5 | 21.06 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 198.98.53.130 |
| 77.56 | shadowsocks | 288.2 | 661.6 | 21.11 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 76.86 | hysteria2 | 361.4 | 711.3 | 19.41 | 0.0 | 10.0 | 14.32 | 20.0 | Au1rxx-base64 | 62.210.124.146 |
| 76.45 | shadowsocks | 277.7 | 639.4 | 21.35 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 76.39 | shadowsocks | 311.9 | 700.9 | 20.56 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 108.181.57.93 |
| 75.94 | hysteria2 | 418.8 | 863.1 | 18.08 | 0.0 | 10.0 | 14.32 | 20.0 | Au1rxx-base64 | 5.255.102.165 |
| 75.12 | hysteria2 | 350.4 | 404.4 | 19.67 | 0.0 | 9.36 | 14.32 | 20.0 | Au1rxx-base64 | 45.76.202.45 |
| 74.81 | http | 358.9 | 621.4 | 19.47 | 0.0 | 10.0 | 14.73 | 19.68 | zhangkai | 138.199.35.217 |
| 74.71 | shadowsocks | 314.4 | 601.3 | 20.5 | 0.0 | 10.0 | 13.67 | 20.0 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.965 | 0.911 | 405 | 1403 | prefer |
| zhangkai | 0.965 | 0.98 | 51 | 72 | prefer |
| Surfboard-tg-mixed | 0.628 | 0.548 | 124 | 5560 | observe |
| mheidari-all | 0.455 | 0.367 | 30 | 20226 | observe |
| DeltaKronecker-all | 0.361 | 0.278 | 18 | 5316 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5260 | observe |
| Epodonios-all | 0.255 | None | 0 | 6163 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6818 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4397 | observe |
| barry-far-vless | 0.255 | None | 0 | 4823 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5147 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 4655 | observe |
| nscl5-all | 0.239 | None | 0 | 1594 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 39 |
| 204 | ProxyError | - | 22 |
| 204 | TimeoutError | - | 19 |
| speed | TimeoutError | - | 11 |
| cn-block | TimeoutError | - | 10 |
| geo | ClientOSError | - | 9 |
| speed | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |
| geo | parse | TimeoutError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
