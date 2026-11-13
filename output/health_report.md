# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-13 18:26:23 |
| 运行耗时 | 260.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83175 |
| 去重后节点 | 26889 |
| TCP 可达 | 3000 |
| 真实可用 | 362 |
| Verified 输出 | 68 |
| Global 输出 | 300 |
| All 输出 | 26889 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.4 |
| tcp | 78.1 |
| probe | 78.8 |
| real_test | 68.4 |
| china_check | 17.9 |
| write_verified | 0.0 |
| generate | 10.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49864 |
| vmess | 14675 |
| shadowsocks | 9725 |
| trojan | 6863 |
| hysteria2 | 1509 |
| http | 253 |
| shadowsocksr | 156 |
| socks | 60 |
| hysteria | 34 |
| tuic | 20 |
| anytls | 16 |

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
| 93.34 | shadowsocks | 245.9 | 0.8 | 22.08 | 14.97 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 185.230.230.18 |
| 93.18 | shadowsocks | 253.6 | 0.6 | 21.91 | 14.98 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 193.151.163.18 |
| 92.37 | shadowsocks | 288.2 | 0.9 | 21.11 | 14.97 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 193.151.160.9 |
| 92.22 | shadowsocks | 288.7 | 4.2 | 21.09 | 14.84 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 45.86.51.18 |
| 90.88 | vless | 267.7 | 3.0 | 21.58 | 14.89 | 9.7 | 8.35 | 17.36 | Au1rxx-base64 | 167.17.69.171 |
| 90.84 | vless | 309.1 | 2.9 | 20.62 | 14.89 | 9.62 | 8.35 | 17.36 | Au1rxx-base64 | 66.70.179.198 |
| 90.45 | shadowsocks | 298.2 | 5.0 | 20.87 | 14.81 | 9.23 | 13.43 | 17.36 | Au1rxx-base64 | 193.151.160.18 |
| 89.83 | vless | 367.8 | 3.7 | 19.26 | 14.86 | 10.0 | 8.35 | 17.36 | Au1rxx-base64 | 169.40.42.35 |
| 89.2 | vless | 387.1 | 1.0 | 18.82 | 14.96 | 9.71 | 8.35 | 17.36 | Au1rxx-base64 | 169.40.42.168 |
| 88.57 | vless | 418.7 | 5.8 | 18.08 | 14.78 | 10.0 | 8.35 | 17.36 | Au1rxx-base64 | 169.40.42.74 |
| 88.53 | shadowsocks | 407.7 | 1.5 | 18.34 | 14.95 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 51.222.136.236 |
| 88.4 | http | 275.8 | 0.5 | 21.39 | 14.98 | 0.0 | 14.59 | 19.94 | ermaozi | 172.64.68.89 |
| 87.92 | vless | 381.3 | 0.1 | 18.95 | 15.0 | 9.71 | 8.35 | 17.36 | Au1rxx-base64 | 169.40.42.90 |
| 86.73 | trojan | 375.8 | 2.7 | 19.08 | 14.9 | 10.0 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.112.121 |
| 86.09 | trojan | 357.5 | 2.0 | 19.5 | 14.93 | 5.9 | 12.94 | 17.36 | Au1rxx-base64 | 169.197.140.169 |
| 85.22 | shadowsocks | 351.6 | 0.3 | 19.64 | 14.99 | 10.0 | 13.43 | 17.36 | Au1rxx-base64 | 15.204.247.206 |
| 85.18 | http | 339.9 | 0.1 | 19.91 | 15.0 | 0.0 | 14.59 | 19.94 | ermaozi | 206.223.183.16 |
| 84.88 | trojan | 365.9 | 2.2 | 19.31 | 14.92 | 8.82 | 12.94 | 17.36 | Au1rxx-base64 | 167.88.61.20 |
| 84.86 | http | 342.2 | 0.8 | 19.86 | 14.97 | 0.0 | 14.59 | 19.94 | ermaozi | 206.223.183.13 |
| 84.81 | trojan | 380.9 | 3.7 | 18.96 | 14.86 | 8.96 | 12.94 | 17.36 | Au1rxx-base64 | 66.163.112.242 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.971 | 0.964 | 55 | 590 | prefer |
| Surfboard-tg-mixed | 0.845 | 0.769 | 147 | 8804 | prefer |
| Au1rxx-base64 | 0.807 | 0.74 | 173 | 1751 | prefer |
| mheidari-all | 0.722 | 0.644 | 104 | 14267 | prefer |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4900 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2734 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11395 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6228 | observe |
| barry-far-vless | 0.255 | None | 0 | 6409 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4624 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.245 | None | 0 | 1751 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 44 |
| 204 | ProxyError | - | 33 |
| speed | ClientOSError | - | 13 |
| cn-block | ProxyError | - | 11 |
| 204 | TimeoutError | - | 9 |
| geo | ProxyError | - | 3 |
| speed | TimeoutError | - | 2 |
| cn-block | TimeoutError | - | 2 |
| 204 | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 1 |
| geo | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 92 | 68 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
