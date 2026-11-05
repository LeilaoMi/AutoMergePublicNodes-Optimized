# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-05 07:04:49 |
| 运行耗时 | 305.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 82241 |
| 去重后节点 | 26663 |
| TCP 可达 | 3000 |
| 真实可用 | 398 |
| Verified 输出 | 36 |
| Global 输出 | 300 |
| All 输出 | 26663 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.6 |
| tcp | 79.7 |
| probe | 98.7 |
| real_test | 78.5 |
| china_check | 24.8 |
| write_verified | 0.0 |
| generate | 14.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49451 |
| vmess | 13989 |
| shadowsocks | 9136 |
| trojan | 7647 |
| hysteria2 | 1632 |
| shadowsocksr | 154 |
| http | 98 |
| socks | 65 |
| hysteria | 37 |
| anytls | 17 |
| tuic | 15 |

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
| 90.77 | shadowsocks | 254.7 | 2.0 | 21.88 | 14.92 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 156.146.38.168 |
| 90.25 | shadowsocks | 279.6 | 0.7 | 21.31 | 14.97 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 156.146.38.170 |
| 89.67 | shadowsocks | 302.8 | 2.0 | 20.77 | 14.93 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 156.146.38.167 |
| 87.74 | shadowsocks | 333.7 | 7.1 | 20.05 | 14.73 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 37.19.198.243 |
| 87.71 | shadowsocks | 300.4 | 8.9 | 20.82 | 14.67 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 15.204.247.206 |
| 86.91 | shadowsocks | 291.1 | 1.2 | 21.04 | 14.95 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 45.86.51.18 |
| 85.63 | shadowsocks | 329.5 | 1.9 | 20.15 | 14.93 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 193.151.160.9 |
| 85.25 | vless | 350.9 | 0.2 | 19.66 | 14.99 | 9.94 | 10.05 | 15.18 | Au1rxx-base64 | 169.40.42.90 |
| 85.1 | shadowsocks | 318.7 | 2.5 | 20.4 | 14.9 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 193.151.163.18 |
| 85.1 | shadowsocks | 334.5 | 0.9 | 20.03 | 14.97 | 9.43 | 12.79 | 15.18 | Au1rxx-base64 | 193.151.160.18 |
| 84.71 | shadowsocks | 330.3 | 0.7 | 20.13 | 14.97 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 149.22.95.183 |
| 84.62 | shadowsocks | 302.5 | 1.9 | 20.78 | 14.93 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 173.244.56.9 |
| 84.6 | shadowsocks | 310.8 | 32.2 | 20.58 | 13.79 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 37.19.198.160 |
| 84.29 | vless | 421.4 | 3.0 | 18.02 | 14.89 | 9.96 | 10.05 | 15.18 | Au1rxx-base64 | 169.40.42.202 |
| 83.84 | shadowsocks | 295.2 | 9.2 | 20.94 | 14.65 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 37.19.198.236 |
| 83.68 | shadowsocks | 308.6 | 3.3 | 20.63 | 14.88 | 10.0 | 12.79 | 15.18 | Au1rxx-base64 | 173.244.56.6 |
| 83.07 | vless | 352.4 | 50.9 | 19.62 | 13.09 | 9.83 | 10.05 | 15.18 | Au1rxx-base64 | 167.17.69.171 |
| 82.98 | hysteria2 | 230.1 | 35.6 | 22.45 | 13.67 | 0.0 | 10.26 | 17.6 | mheidari-all | 88.216.195.188 |
| 82.33 | shadowsocks | 255.6 | 6.8 | 21.86 | 14.75 | 6.75 | 12.79 | 15.18 | Au1rxx-base64 | 156.146.38.169 |
| 82.18 | vless | 440.6 | 12.7 | 17.58 | 14.52 | 9.83 | 10.05 | 15.18 | Au1rxx-base64 | 169.40.42.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.963 | 0.897 | 58 | 8675 | prefer |
| ermaozi | 0.898 | 0.947 | 19 | 555 | prefer |
| mheidari-all | 0.866 | 0.789 | 185 | 14576 | prefer |
| Au1rxx-base64 | 0.843 | 0.775 | 236 | 1751 | prefer |
| xiaoji235-airport-v2ray-all | 0.391 | 1.0 | 2 | 6752 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5005 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2526 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10857 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6030 | observe |
| barry-far-vless | 0.255 | None | 0 | 6243 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4612 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 66 |
| 204 | ProxyError | - | 12 |
| 204 | TimeoutError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 3 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 40 | 36 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
