# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-04 05:31:52 |
| 运行耗时 | 872.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99314 |
| 去重后节点 | 27386 |
| TCP 可达 | 3000 |
| 真实可用 | 429 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27386 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| geo | 1.2 |
| tcp | 47.3 |
| probe | 327.6 |
| real_test | 452.0 |
| generate | 37.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60054 |
| vmess | 15641 |
| shadowsocks | 11539 |
| trojan | 9620 |
| hysteria2 | 1656 |
| http | 520 |
| shadowsocksr | 166 |
| socks | 68 |
| anytls | 27 |
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
| 85.87 | vless | 197.2 | 516.7 | 23.21 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 172.235.38.85 |
| 85.53 | vless | 211.8 | 498.4 | 22.87 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 137.175.82.40 |
| 85.27 | vless | 218.1 | 536.4 | 22.73 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 195.123.240.65 |
| 82.35 | vless | 212.4 | 500.9 | 22.86 | 0.0 | 10.0 | 12.98 | 16.6 | mheidari-all | 47.251.108.158 |
| 81.72 | shadowsocks | 213.6 | 535.1 | 22.83 | 0.0 | 10.0 | 13.21 | 19.68 | Au1rxx-base64 | 173.244.56.9 |
| 81.68 | shadowsocks | 215.5 | 535.9 | 22.79 | 0.0 | 10.0 | 13.21 | 19.68 | Au1rxx-base64 | 173.244.56.6 |
| 81.54 | vless | 270.2 | 600.7 | 21.52 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 15.204.97.216 |
| 81.01 | shadowsocks | 222.7 | 570.3 | 22.62 | 0.0 | 10.0 | 13.21 | 19.68 | Au1rxx-base64 | 108.181.0.177 |
| 80.71 | shadowsocks | 257.6 | 625.9 | 21.82 | 0.0 | 10.0 | 13.21 | 19.68 | Au1rxx-base64 | 156.146.38.167 |
| 80.22 | vless | 257.7 | 434.0 | 21.81 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 162.159.0.53 |
| 80.0 | vless | 191.5 | 501.5 | 23.34 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 172.233.139.46 |
| 79.82 | shadowsocks | 292.8 | 741.3 | 21.0 | 0.0 | 10.0 | 13.21 | 19.68 | Au1rxx-base64 | 156.146.38.169 |
| 78.71 | vless | 274.5 | 424.9 | 21.42 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 104.18.47.113 |
| 78.35 | vless | 327.7 | 408.8 | 20.19 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 172.64.154.8 |
| 78.29 | vless | 287.1 | 435.5 | 21.13 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 162.159.24.131 |
| 78.04 | vless | 211.7 | 481.7 | 22.88 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 162.159.48.32 |
| 78.03 | vless | 288.7 | 644.8 | 21.1 | 0.0 | 10.0 | 12.98 | 16.6 | mheidari-all | 216.227.161.95 |
| 77.73 | vless | 234.9 | 550.4 | 22.34 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 172.64.42.85 |
| 77.14 | shadowsocks | 181.5 | 482.6 | 23.58 | 0.0 | 10.0 | 13.21 | 19.68 | Au1rxx-base64 | 103.214.109.197 |
| 77.0 | vless | 256.5 | 667.9 | 21.84 | 0.0 | 10.0 | 12.98 | 19.68 | Au1rxx-base64 | 172.64.229.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.977 | 0.908 | 284 | 1782 | prefer |
| ermaozi | 0.73 | 0.72 | 25 | 646 | prefer |
| Surfboard-tg-mixed | 0.715 | 0.639 | 72 | 7318 | prefer |
| mheidari-all | 0.355 | 0.273 | 384 | 23371 | observe |
| DeltaKronecker-all | 0.263 | 0.25 | 8 | 5207 | observe |
| Epodonios-all | 0.255 | None | 0 | 7797 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9571 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5909 | observe |
| barry-far-vless | 0.255 | None | 0 | 6122 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4285 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1782 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 152 |
| speed | TimeoutError | - | 81 |
| geo | ClientOSError | - | 33 |
| 204 | TimeoutError | - | 18 |
| cn-block | TimeoutError | - | 15 |
| 204 | ProxyConnectionError | - | 14 |
| 204 | ProxyError | - | 14 |
| speed | ClientOSError | - | 13 |
| cn-block | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
