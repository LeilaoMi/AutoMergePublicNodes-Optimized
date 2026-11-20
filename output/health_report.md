# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-20 07:33:58 |
| 运行耗时 | 290.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 82463 |
| 去重后节点 | 27651 |
| TCP 可达 | 3000 |
| 真实可用 | 430 |
| Verified 输出 | 60 |
| Global 输出 | 300 |
| All 输出 | 27651 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 81.7 |
| probe | 97.6 |
| real_test | 63.2 |
| china_check | 23.8 |
| write_verified | 0.0 |
| generate | 15.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48529 |
| vmess | 14995 |
| shadowsocks | 10258 |
| trojan | 6782 |
| hysteria2 | 1501 |
| shadowsocksr | 146 |
| http | 130 |
| socks | 76 |
| hysteria | 20 |
| tuic | 14 |
| anytls | 12 |

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
| 91.47 | vless | 321.2 | 2.0 | 20.34 | 14.93 | 10.0 | 10.52 | 15.68 | Au1rxx-base64 | 169.40.42.35 |
| 90.78 | vless | 312.1 | 23.1 | 20.55 | 14.13 | 9.9 | 10.52 | 15.68 | Au1rxx-base64 | 169.40.42.202 |
| 90.52 | vless | 357.0 | 2.7 | 19.51 | 14.9 | 9.91 | 10.52 | 15.68 | Au1rxx-base64 | 167.17.69.171 |
| 90.25 | vless | 300.0 | 0.8 | 20.83 | 14.97 | 8.52 | 10.52 | 15.68 | Au1rxx-base64 | 169.40.42.229 |
| 89.51 | shadowsocks | 315.1 | 6.5 | 20.48 | 14.76 | 9.38 | 13.71 | 15.68 | Au1rxx-base64 | 193.151.160.18 |
| 89.2 | shadowsocks | 281.0 | 12.3 | 21.27 | 14.54 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 37.19.198.160 |
| 88.75 | shadowsocks | 373.4 | 7.1 | 19.13 | 14.73 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 193.151.163.18 |
| 88.68 | shadowsocks | 407.0 | 1.9 | 18.36 | 14.93 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 37.19.198.236 |
| 87.74 | shadowsocks | 397.2 | 19.6 | 18.58 | 14.27 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 45.86.51.18 |
| 87.54 | shadowsocks | 410.1 | 3.8 | 18.29 | 14.86 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 37.19.198.243 |
| 86.27 | shadowsocks | 343.0 | 9.1 | 19.84 | 14.66 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 185.230.230.18 |
| 85.18 | shadowsocks | 507.5 | 19.8 | 16.03 | 14.26 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 15.204.247.206 |
| 84.05 | shadowsocks | 286.5 | 9.8 | 21.15 | 14.63 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 37.19.198.244 |
| 83.71 | vless | 332.5 | 17.1 | 20.08 | 14.36 | 9.92 | 10.52 | 15.68 | Au1rxx-base64 | 169.40.42.89 |
| 83.56 | shadowsocks | 350.3 | 159.9 | 19.67 | 9.0 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 193.151.160.9 |
| 82.93 | http | 469.8 | 0.6 | 16.9 | 14.98 | 0.0 | 13.93 | 19.62 | ermaozi | 172.64.69.89 |
| 82.57 | shadowsocks | 342.1 | 1.7 | 19.86 | 14.94 | 0.0 | 13.71 | 18.56 | mheidari-all | 38.64.138.135 |
| 82.42 | shadowsocks | 288.2 | 0.4 | 21.11 | 14.99 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 156.146.38.168 |
| 82.26 | shadowsocks | 285.3 | 1.3 | 21.17 | 14.95 | 10.0 | 13.71 | 15.68 | Au1rxx-base64 | 156.146.38.170 |
| 81.9 | shadowsocks | 364.9 | 5.2 | 19.33 | 14.8 | 0.0 | 13.71 | 18.56 | mheidari-all | 38.91.107.57 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.98 | 1.0 | 24 | 469 | prefer |
| Surfboard-tg-mixed | 0.948 | 0.873 | 142 | 8500 | prefer |
| mheidari-all | 0.933 | 0.857 | 189 | 14360 | prefer |
| Au1rxx-base64 | 0.831 | 0.764 | 165 | 1751 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4935 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2728 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11813 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5726 | observe |
| barry-far-vless | 0.255 | None | 0 | 6117 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4501 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 44 |
| 204 | ProxyError | - | 14 |
| cn-block | ClientOSError | - | 9 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| 204 | TimeoutError | - | 3 |
| geo | ProxyError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| speed | ProxyError | - | 1 |
| speed | TimeoutError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 65 | 60 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
