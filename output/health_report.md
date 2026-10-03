# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-03 11:34:23 |
| 运行耗时 | 577.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98931 |
| 去重后节点 | 27239 |
| TCP 可达 | 3000 |
| 真实可用 | 357 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27239 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.5 |
| tcp | 47.9 |
| probe | 259.1 |
| real_test | 171.2 |
| generate | 90.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60581 |
| vmess | 15500 |
| shadowsocks | 11388 |
| trojan | 9034 |
| hysteria2 | 1611 |
| http | 521 |
| shadowsocksr | 171 |
| socks | 66 |
| anytls | 30 |
| hysteria | 17 |
| tuic | 12 |

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
| 82.78 | hysteria2 | 259.8 | 545.0 | 21.76 | 0.0 | 10.0 | 14.12 | 19.12 | Au1rxx-base64 | 192.255.128.123 |
| 81.02 | shadowsocks | 243.0 | 639.6 | 22.15 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 156.146.38.167 |
| 80.9 | shadowsocks | 248.4 | 618.5 | 22.03 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 156.146.38.169 |
| 79.07 | hysteria2 | 279.4 | 272.7 | 21.31 | 4.77 | 7.42 | 14.12 | 19.12 | Au1rxx-base64 | open.w2m.ink |
| 78.75 | shadowsocks | 308.4 | 749.2 | 20.64 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 37.19.198.236 |
| 78.69 | hysteria2 | 308.0 | 650.4 | 20.65 | 0.0 | 10.0 | 14.12 | 19.12 | Au1rxx-base64 | 66.94.121.46 |
| 78.2 | shadowsocks | 310.1 | 756.5 | 20.6 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 37.19.198.244 |
| 78.17 | shadowsocks | 310.4 | 766.3 | 20.59 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 37.19.198.160 |
| 77.18 | shadowsocks | 283.4 | 653.2 | 21.22 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 198.98.53.130 |
| 77.14 | shadowsocks | 303.1 | 694.2 | 20.76 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 140.82.63.79 |
| 76.7 | http | 290.4 | 589.2 | 21.06 | 0.0 | 10.0 | 13.85 | 18.98 | ermaozi | 138.199.35.216 |
| 76.65 | http | 287.9 | 583.7 | 21.11 | 0.0 | 10.0 | 13.85 | 18.98 | ermaozi | 138.199.35.198 |
| 76.62 | vless | 286.4 | 667.5 | 21.15 | 0.0 | 10.0 | 6.5 | 19.12 | Au1rxx-base64 | 198.251.78.29 |
| 75.84 | shadowsocks | 321.0 | 727.3 | 20.35 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 108.181.57.93 |
| 75.65 | shadowsocks | 344.3 | 814.1 | 19.81 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 103.214.109.197 |
| 75.48 | shadowsocks | 289.3 | 593.4 | 21.08 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 173.244.56.6 |
| 75.39 | shadowsocks | 310.0 | 664.9 | 20.6 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 149.22.95.183 |
| 75.19 | shadowsocks | 300.3 | 612.9 | 20.83 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 173.244.56.9 |
| 74.58 | shadowsocks | 362.0 | 872.6 | 19.4 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 51.222.200.165 |
| 74.45 | shadowsocks | 289.3 | 798.1 | 21.08 | 0.0 | 10.0 | 13.75 | 19.12 | Au1rxx-base64 | 66.23.205.182 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.958 | 0.891 | 239 | 1754 | prefer |
| mheidari-all | 0.854 | 0.783 | 60 | 23264 | prefer |
| Surfboard-tg-mixed | 0.705 | 0.627 | 126 | 7251 | prefer |
| ermaozi | 0.603 | 0.583 | 24 | 645 | observe |
| ermaozi-get_subscribe | 0.313 | 0.6 | 5 | 516 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5192 | observe |
| Epodonios-all | 0.255 | None | 0 | 7748 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9363 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5966 | observe |
| barry-far-vless | 0.255 | None | 0 | 6206 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4335 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1754 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 37 |
| cn-block | TimeoutError | - | 18 |
| 204 | ProxyConnectionError | - | 11 |
| 204 | ProxyError | - | 10 |
| geo | ClientOSError | - | 6 |
| speed | TimeoutError | - | 6 |
| speed | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| geo | TimeoutError | - | 4 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
