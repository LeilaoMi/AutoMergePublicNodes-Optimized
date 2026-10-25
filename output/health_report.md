# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-25 11:51:08 |
| 运行耗时 | 320.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 88 |
| 原始节点 | 97033 |
| 去重后节点 | 27210 |
| TCP 可达 | 3000 |
| 真实可用 | 474 |
| Verified 输出 | 172 |
| Global 输出 | 300 |
| All 输出 | 27210 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.5 |
| tcp | 84.9 |
| probe | 92.7 |
| real_test | 88.4 |
| china_check | 31.9 |
| write_verified | 0.1 |
| generate | 13.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57300 |
| vmess | 17287 |
| shadowsocks | 12701 |
| trojan | 7762 |
| hysteria2 | 1392 |
| http | 312 |
| shadowsocksr | 164 |
| socks | 67 |
| anytls | 25 |
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
| 95.64 | shadowsocks | 242.0 | 2.8 | 22.18 | 14.9 | 9.51 | 14.53 | 18.52 | Au1rxx-base64 | 156.146.38.169 |
| 95.62 | shadowsocks | 246.2 | 1.2 | 22.08 | 14.96 | 9.53 | 14.53 | 18.52 | Au1rxx-base64 | 156.146.38.170 |
| 94.02 | trojan | 322.5 | 0.5 | 20.31 | 14.98 | 8.89 | 14.32 | 18.52 | Au1rxx-base64 | 66.23.203.21 |
| 92.62 | hysteria2 | 333.4 | 2.1 | 20.06 | 14.92 | 6.5 | 14.12 | 18.52 | Au1rxx-base64 | 129.213.91.185 |
| 92.25 | vless | 242.2 | 1.1 | 22.17 | 14.96 | 8.75 | 8.78 | 18.52 | Au1rxx-base64 | 45.76.172.197 |
| 91.75 | vless | 244.8 | 4.0 | 22.11 | 14.85 | 8.75 | 8.78 | 18.52 | Au1rxx-base64 | 144.202.126.147 |
| 91.49 | vless | 238.5 | 2.2 | 22.26 | 14.92 | 8.42 | 8.78 | 18.52 | Au1rxx-base64 | 45.63.53.81 |
| 91.31 | hysteria2 | 323.4 | 4.6 | 20.29 | 14.83 | 7.92 | 14.12 | 18.52 | Au1rxx-base64 | 66.94.121.46 |
| 90.86 | shadowsocks | 237.1 | 0.9 | 22.29 | 14.97 | 9.55 | 14.53 | 18.52 | Au1rxx-base64 | 156.146.38.168 |
| 90.18 | shadowsocks | 320.1 | 1.1 | 20.37 | 14.96 | 9.28 | 14.53 | 18.52 | Au1rxx-base64 | 37.19.198.236 |
| 90.11 | shadowsocks | 322.3 | 2.9 | 20.32 | 14.89 | 9.24 | 14.53 | 18.52 | Au1rxx-base64 | 37.19.198.244 |
| 89.62 | shadowsocks | 328.7 | 3.7 | 20.17 | 14.86 | 8.85 | 14.53 | 18.52 | Au1rxx-base64 | 37.19.198.243 |
| 89.38 | vless | 240.2 | 2.6 | 22.22 | 14.9 | 6.96 | 8.78 | 18.52 | Au1rxx-base64 | 47.251.108.158 |
| 89.32 | shadowsocks | 285.4 | 1.0 | 21.17 | 14.96 | 9.28 | 14.53 | 18.52 | Au1rxx-base64 | 173.244.56.9 |
| 89.27 | vless | 276.7 | 1.3 | 21.37 | 14.95 | 9.26 | 8.78 | 18.52 | Au1rxx-base64 | 51.81.203.63 |
| 89.26 | shadowsocks | 320.1 | 0.1 | 20.37 | 15.0 | 9.17 | 14.53 | 18.52 | Au1rxx-base64 | 149.22.95.183 |
| 89.15 | shadowsocks | 332.7 | 0.7 | 20.08 | 14.98 | 9.28 | 14.53 | 18.52 | Au1rxx-base64 | 173.244.56.6 |
| 88.97 | shadowsocks | 326.3 | 7.5 | 20.22 | 14.72 | 9.26 | 14.53 | 18.52 | Au1rxx-base64 | 193.151.163.18 |
| 88.85 | shadowsocks | 326.0 | 1.4 | 20.23 | 14.95 | 7.97 | 14.53 | 18.52 | Au1rxx-base64 | 37.19.198.160 |
| 88.84 | shadowsocks | 341.1 | 0.3 | 19.88 | 14.99 | 9.3 | 14.53 | 18.52 | Au1rxx-base64 | 95.215.201.18 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.988 | 83 | 604 | prefer |
| zhangkai | 0.964 | 1.0 | 24 | 59 | prefer |
| Au1rxx-base64 | 0.893 | 0.831 | 307 | 1618 | prefer |
| Surfboard-tg-mixed | 0.805 | 0.73 | 89 | 7259 | prefer |
| mheidari-all | 0.802 | 0.735 | 34 | 24013 | prefer |
| DeltaKronecker-all | 0.638 | 0.561 | 41 | 3849 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| tg-oneclickvpnkeys | 0.316 | 1.0 | 2 | 112 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 7583 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10577 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5481 | observe |
| barry-far-vless | 0.255 | None | 0 | 5633 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 72 |
| 204 | TimeoutError | - | 12 |
| geo | ClientOSError | - | 7 |
| 204 | ClientOSError | - | 5 |
| 204 | ProxyError | - | 3 |
| cn-block | TimeoutError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| speed | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 104 | 172 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
