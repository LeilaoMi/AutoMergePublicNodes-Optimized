# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-24 14:48:06 |
| 运行耗时 | 263.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 77241 |
| 去重后节点 | 22530 |
| TCP 可达 | 3000 |
| 真实可用 | 457 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22530 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.5 |
| tcp | 29.8 |
| probe | 60.7 |
| real_test | 126.2 |
| generate | 38.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45576 |
| trojan | 10929 |
| vmess | 10225 |
| shadowsocks | 9871 |
| hysteria2 | 237 |
| shadowsocksr | 164 |
| http | 161 |
| socks | 70 |
| hysteria | 6 |
| tuic | 2 |

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
| 76.65 | shadowsocks | 213.6 | 513.0 | 22.83 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 173.244.56.9 |
| 76.6 | shadowsocks | 202.2 | 479.0 | 23.1 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 108.181.118.10 |
| 76.3 | shadowsocks | 214.9 | 532.9 | 22.8 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 108.181.0.177 |
| 75.99 | shadowsocks | 241.9 | 563.3 | 22.18 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 149.22.95.183 |
| 73.88 | vless | 304.0 | 795.3 | 20.74 | 0.0 | 10.0 | 7.82 | 15.32 | Au1rxx-base64 | 15.204.97.219 |
| 73.83 | vless | 306.2 | 806.2 | 20.69 | 0.0 | 10.0 | 7.82 | 15.32 | Au1rxx-base64 | 15.204.97.214 |
| 72.31 | vless | 166.2 | 473.3 | 23.93 | 0.0 | 10.0 | 7.82 | 15.56 | Surfboard-tg-mixed | 64.118.153.6 |
| 72.31 | shadowsocks | 287.7 | 647.4 | 21.12 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 156.146.38.167 |
| 72.12 | shadowsocks | 258.7 | 646.0 | 21.79 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 173.244.56.6 |
| 72.1 | shadowsocks | 302.7 | 683.6 | 20.77 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 156.146.38.170 |
| 71.92 | vless | 255.3 | 579.7 | 21.87 | 0.0 | 10.0 | 7.82 | 12.44 | mheidari-all | 34.213.172.16 |
| 71.41 | shadowsocks | 291.0 | 647.2 | 21.04 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 156.146.38.169 |
| 71.35 | shadowsocks | 290.6 | 652.5 | 21.05 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 156.146.38.168 |
| 69.35 | vless | 266.2 | 700.4 | 21.62 | 0.0 | 8.85 | 7.82 | 15.56 | Surfboard-tg-mixed | 141.193.154.182 |
| 69.16 | shadowsocks | 300.5 | 354.5 | 20.82 | 1.7 | 9.89 | 12.68 | 15.32 | Au1rxx-base64 | 149.22.87.240 |
| 68.74 | shadowsocks | 303.9 | 364.8 | 20.74 | 1.32 | 9.89 | 12.68 | 15.32 | Au1rxx-base64 | 149.22.87.241 |
| 68.32 | shadowsocks | 306.5 | 369.8 | 20.68 | 1.13 | 9.9 | 12.68 | 15.32 | Au1rxx-base64 | 149.22.87.204 |
| 68.11 | shadowsocks | 230.1 | 636.6 | 22.45 | 0.0 | 10.0 | 12.68 | 10.08 | DeltaKronecker-all | 107.172.219.230 |
| 68.04 | shadowsocks | 303.2 | 342.7 | 20.76 | 2.15 | 9.9 | 12.68 | 15.32 | Au1rxx-base64 | 47.79.144.115 |
| 66.96 | shadowsocks | 379.3 | 761.3 | 19.0 | 0.0 | 10.0 | 12.68 | 15.32 | Au1rxx-base64 | 37.19.198.236 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | 1.0 | 50 | 73 | prefer |
| Surfboard-tg-mixed | 0.821 | 0.742 | 264 | 5407 | prefer |
| Au1rxx-base64 | 0.805 | 0.81 | 63 | 114 | prefer |
| mheidari-all | 0.793 | 0.716 | 162 | 15574 | prefer |
| DeltaKronecker-all | 0.677 | 0.6 | 70 | 6644 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4745 | observe |
| Epodonios-all | 0.255 | None | 0 | 8169 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3983 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7672 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4121 | observe |
| barry-far-vless | 0.255 | None | 0 | 4921 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4710 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 60 |
| cn-block | TimeoutError | - | 23 |
| 204 | TimeoutError | - | 21 |
| 204 | ProxyError | - | 9 |
| cn-block | ClientOSError | - | 8 |
| geo | TimeoutError | - | 8 |
| geo | ClientOSError | - | 7 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 5 |
| geo | ProxyError | - | 3 |
| speed | ProxyError | - | 3 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
