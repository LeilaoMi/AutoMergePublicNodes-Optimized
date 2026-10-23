# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-23 21:35:37 |
| 运行耗时 | 274.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 92424 |
| 去重后节点 | 24537 |
| TCP 可达 | 3000 |
| 真实可用 | 330 |
| Verified 输出 | 83 |
| Global 输出 | 300 |
| All 输出 | 24537 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.5 |
| tcp | 74.9 |
| probe | 87.5 |
| real_test | 70.7 |
| china_check | 21.4 |
| write_verified | 0.0 |
| generate | 11.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56305 |
| vmess | 16647 |
| shadowsocks | 11749 |
| trojan | 5927 |
| hysteria2 | 1334 |
| http | 201 |
| shadowsocksr | 169 |
| socks | 48 |
| anytls | 21 |
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
| 95.11 | hysteria2 | 257.6 | 8.8 | 21.82 | 14.67 | 8.69 | 13.93 | 17.5 | Au1rxx-base64 | 129.213.91.185 |
| 91.66 | shadowsocks | 261.5 | 5.4 | 21.72 | 14.8 | 8.96 | 12.68 | 17.5 | Au1rxx-base64 | 156.146.38.168 |
| 90.65 | shadowsocks | 305.9 | 11.3 | 20.7 | 14.58 | 9.19 | 12.68 | 17.5 | Au1rxx-base64 | 156.146.38.167 |
| 90.44 | shadowsocks | 275.0 | 17.4 | 21.41 | 14.35 | 9.0 | 12.68 | 17.5 | Au1rxx-base64 | 185.230.230.18 |
| 90.44 | shadowsocks | 290.5 | 11.6 | 21.05 | 14.56 | 8.65 | 12.68 | 17.5 | Au1rxx-base64 | 37.19.198.244 |
| 90.31 | shadowsocks | 259.2 | 2.2 | 21.78 | 14.92 | 7.43 | 12.68 | 17.5 | Au1rxx-base64 | 156.146.38.170 |
| 90.25 | shadowsocks | 275.5 | 0.7 | 21.4 | 14.97 | 7.7 | 12.68 | 17.5 | Au1rxx-base64 | 37.19.198.243 |
| 89.57 | shadowsocks | 290.8 | 2.9 | 21.05 | 14.89 | 7.45 | 12.68 | 17.5 | Au1rxx-base64 | 37.19.198.160 |
| 89.11 | shadowsocks | 346.2 | 8.9 | 19.76 | 14.67 | 9.0 | 12.68 | 17.5 | Au1rxx-base64 | 45.86.51.18 |
| 88.55 | vless | 292.9 | 0.9 | 21.0 | 14.97 | 7.81 | 9.8 | 17.5 | Au1rxx-base64 | 169.40.42.89 |
| 88.17 | shadowsocks | 288.3 | 2.6 | 21.1 | 14.9 | 5.99 | 12.68 | 17.5 | Au1rxx-base64 | 37.19.198.236 |
| 88.09 | vless | 400.4 | 6.6 | 18.51 | 14.75 | 7.82 | 9.8 | 17.5 | Au1rxx-base64 | 169.40.42.104 |
| 88.05 | shadowsocks | 345.3 | 3.6 | 19.79 | 14.86 | 7.72 | 12.68 | 17.5 | Au1rxx-base64 | 185.215.132.18 |
| 88.0 | vless | 321.4 | 1.1 | 20.34 | 14.96 | 7.58 | 9.8 | 17.5 | Au1rxx-base64 | 66.70.179.198 |
| 87.73 | vless | 409.7 | 2.4 | 18.29 | 14.91 | 7.57 | 9.8 | 17.5 | Au1rxx-base64 | 185.95.231.156 |
| 87.43 | vless | 332.2 | 13.7 | 20.09 | 14.49 | 7.69 | 9.8 | 17.5 | Au1rxx-base64 | 169.40.42.231 |
| 87.27 | shadowsocks | 265.8 | 2.9 | 21.63 | 14.89 | 4.57 | 12.68 | 17.5 | Au1rxx-base64 | 156.146.38.169 |
| 87.13 | shadowsocks | 392.0 | 9.0 | 18.7 | 14.66 | 9.17 | 12.68 | 17.5 | Au1rxx-base64 | 193.151.160.9 |
| 86.95 | vless | 352.8 | 13.4 | 19.61 | 14.5 | 7.04 | 9.8 | 17.5 | Au1rxx-base64 | 195.123.235.183 |
| 86.66 | shadowsocks | 304.1 | 3.4 | 20.74 | 14.87 | 8.96 | 12.68 | 17.5 | Au1rxx-base64 | 149.22.95.183 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.947 | 0.941 | 51 | 555 | prefer |
| Au1rxx-base64 | 0.86 | 0.799 | 268 | 1594 | prefer |
| mheidari-all | 0.826 | 0.754 | 57 | 23638 | prefer |
| Surfboard-tg-mixed | 0.749 | 0.923 | 13 | 7184 | prefer |
| roosterkid-openproxylist-v2ray | 0.433 | 0.75 | 8 | 150 | observe |
| Surfboard-tg-vless | 0.391 | 1.0 | 2 | 5437 | observe |
| 10ium-HighSpeed | 0.345 | 1.0 | 2 | 839 | observe |
| SoliSpirit-all | 0.335 | 1.0 | 1 | 10312 | observe |
| tg-oneclickvpnkeys | 0.324 | 0.75 | 4 | 92 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 175 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| Epodonios-all | 0.255 | None | 0 | 7680 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| barry-far-vless | 0.255 | None | 0 | 5798 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4117 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 50 |
| cn-block | TimeoutError | - | 8 |
| 204 | TimeoutError | - | 6 |
| geo | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| 204 | ProxyError | - | 2 |
| cn-block | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |
| cn-block | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 140 | 83 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
