# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-26 04:16:11 |
| 运行耗时 | 252.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 82567 |
| 去重后节点 | 22943 |
| TCP 可达 | 3000 |
| 真实可用 | 527 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22943 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.3 |
| tcp | 30.4 |
| probe | 57.6 |
| real_test | 123.8 |
| generate | 35.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46148 |
| trojan | 14530 |
| vmess | 11206 |
| shadowsocks | 10060 |
| hysteria2 | 254 |
| shadowsocksr | 160 |
| http | 129 |
| socks | 72 |
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
| 76.49 | shadowsocks | 227.3 | 627.3 | 22.52 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 37.19.198.160 |
| 76.38 | shadowsocks | 231.7 | 640.1 | 22.41 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 37.19.198.244 |
| 76.32 | shadowsocks | 234.6 | 651.4 | 22.35 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 37.19.198.243 |
| 74.19 | shadowsocks | 283.3 | 794.3 | 21.22 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 37.19.198.236 |
| 73.71 | vless | 299.7 | 832.2 | 20.84 | 0.0 | 10.0 | 9.47 | 16.4 | Au1rxx-base64 | 159.89.87.21 |
| 72.99 | vless | 259.8 | 735.4 | 21.76 | 0.0 | 10.0 | 9.47 | 11.76 | mheidari-all | 47.253.226.114 |
| 72.56 | vless | 316.7 | 741.2 | 20.45 | 0.0 | 10.0 | 9.47 | 15.7 | Surfboard-tg-mixed | 15.223.121.250 |
| 71.96 | shadowsocks | 286.1 | 654.1 | 21.16 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 156.146.38.167 |
| 71.93 | shadowsocks | 223.8 | 608.0 | 22.6 | 0.0 | 10.0 | 11.57 | 11.76 | mheidari-all | 198.98.53.130 |
| 71.79 | shadowsocks | 330.1 | 801.4 | 20.14 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 156.146.38.168 |
| 71.45 | shadowsocks | 239.7 | 644.0 | 22.23 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 70.81 | vless | 308.2 | 834.3 | 20.64 | 0.0 | 10.0 | 9.47 | 15.7 | Surfboard-tg-mixed | 137.184.218.169 |
| 70.46 | shadowsocks | 265.5 | 709.5 | 21.63 | 0.0 | 10.0 | 11.57 | 11.76 | mheidari-all | 108.181.57.93 |
| 70.06 | vless | 299.2 | 815.5 | 20.85 | 0.0 | 10.0 | 9.47 | 9.74 | DeltaKronecker-all | 152.53.171.40 |
| 69.66 | shadowsocks | 293.6 | 593.2 | 20.98 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 173.244.56.9 |
| 69.08 | shadowsocks | 330.8 | 708.1 | 20.12 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 173.244.56.6 |
| 68.79 | shadowsocks | 313.2 | 544.2 | 20.53 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 108.181.118.10 |
| 68.37 | shadowsocks | 330.3 | 627.2 | 20.13 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 149.22.95.183 |
| 68.27 | shadowsocks | 344.8 | 940.1 | 19.8 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 172.234.202.34 |
| 68.08 | shadowsocks | 312.3 | 549.7 | 20.55 | 0.0 | 10.0 | 11.57 | 16.4 | Au1rxx-base64 | 108.181.0.177 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | 1.0 | 36 | 82 | prefer |
| Surfboard-tg-mixed | 0.856 | 0.778 | 284 | 5079 | prefer |
| Au1rxx-base64 | 0.759 | 0.764 | 55 | 110 | prefer |
| mheidari-all | 0.69 | 0.611 | 234 | 16097 | observe |
| nscl5-all | 0.358 | 1.0 | 2 | 1175 | observe |
| DeltaKronecker-all | 0.286 | 0.204 | 401 | 12590 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7810 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3981 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7388 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3792 | observe |
| barry-far-vless | 0.255 | None | 0 | 4580 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5117 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| xiaoji235-airport-v2ray-all | 0.22 | None | 0 | 1125 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 213 |
| geo | TimeoutError | - | 180 |
| geo | ClientOSError | - | 26 |
| speed | TimeoutError | - | 25 |
| cn-block | TimeoutError | - | 15 |
| 204 | ClientOSError | - | 10 |
| 204 | ProxyError | - | 8 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 5 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 287 | 300 | - |
| global | False | 293 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
