# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-10 09:49:20 |
| 运行耗时 | 230.7s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 75289 |
| 去重后节点 | 23428 |
| TCP 可达 | 3000 |
| 真实可用 | 250 |
| Verified 输出 | 250 |
| Global 输出 | 279 |
| All 输出 | 23428 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| geo | 1.4 |
| tcp | 31.1 |
| probe | 53.6 |
| real_test | 94.4 |
| generate | 45.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42449 |
| trojan | 12410 |
| vmess | 10654 |
| shadowsocks | 9132 |
| hysteria2 | 262 |
| shadowsocksr | 142 |
| http | 135 |
| socks | 91 |
| hysteria | 8 |
| anytls | 5 |
| tuic | 1 |

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
| 78.76 | shadowsocks | 200.3 | 480.9 | 23.14 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 108.181.0.177 |
| 78.7 | shadowsocks | 224.6 | 502.3 | 22.58 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 173.244.56.9 |
| 78.47 | shadowsocks | 234.3 | 479.0 | 22.35 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 173.244.56.6 |
| 78.35 | shadowsocks | 217.9 | 553.0 | 22.73 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 108.181.118.10 |
| 74.85 | trojan | 345.5 | 781.9 | 19.78 | 0.0 | 10.0 | 14.57 | 16.16 | Au1rxx-base64 | 149.28.241.235 |
| 74.39 | shadowsocks | 290.0 | 641.9 | 21.07 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 156.146.38.168 |
| 74.12 | shadowsocks | 293.6 | 655.7 | 20.98 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 156.146.38.169 |
| 73.93 | shadowsocks | 297.3 | 673.4 | 20.9 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 156.146.38.170 |
| 73.78 | shadowsocks | 295.9 | 663.6 | 20.93 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 156.146.38.167 |
| 73.34 | shadowsocks | 239.9 | 565.1 | 22.22 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 149.22.95.183 |
| 73.04 | vless | 198.2 | 519.4 | 23.19 | 0.0 | 10.0 | 5.97 | 14.88 | Surfboard-tg-mixed | 104.16.9.20 |
| 71.01 | shadowsocks | 279.5 | 284.3 | 21.31 | 4.34 | 9.9 | 13.96 | 12.68 | mheidari-all | 149.22.87.240 |
| 69.89 | trojan | 303.2 | 646.7 | 20.76 | 0.0 | 10.0 | 14.57 | 10.8 | DeltaKronecker-all | 64.94.95.115 |
| 69.84 | shadowsocks | 362.1 | 720.1 | 19.4 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 198.98.53.130 |
| 69.8 | trojan | 379.7 | 868.5 | 18.99 | 0.0 | 10.0 | 14.57 | 12.68 | mheidari-all | 64.94.95.118 |
| 68.88 | shadowsocks | 388.6 | 777.5 | 18.78 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 37.19.198.244 |
| 68.85 | shadowsocks | 387.2 | 772.0 | 18.82 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 37.19.198.160 |
| 68.79 | trojan | 344.0 | 776.8 | 19.81 | 0.0 | 10.0 | 14.57 | 10.8 | DeltaKronecker-all | 45.32.195.168 |
| 68.67 | shadowsocks | 392.2 | 787.2 | 18.7 | 0.0 | 10.0 | 13.96 | 16.16 | Au1rxx-base64 | 37.19.198.236 |
| 68.6 | shadowsocks | 390.9 | 764.0 | 18.73 | 0.0 | 9.69 | 13.96 | 16.16 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Au1rxx-base64 | 0.87 | 0.893 | 28 | 75 | prefer |
| Surfboard-tg-mixed | 0.747 | 0.67 | 91 | 5466 | prefer |
| mheidari-all | 0.624 | 0.545 | 66 | 15738 | observe |
| DeltaKronecker-all | 0.622 | 0.542 | 166 | 7600 | observe |
| nscl5-all | 0.301 | 1.0 | 1 | 1148 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4165 | observe |
| Epodonios-all | 0.255 | None | 0 | 6278 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6680 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4082 | observe |
| barry-far-vless | 0.255 | None | 0 | 4587 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5391 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 32 |
| cn-block | ProxyError | - | 16 |
| speed | ClientOSError | - | 14 |
| geo | TimeoutError | - | 14 |
| cn-block | TimeoutError | - | 12 |
| cn-block | ClientOSError | - | 10 |
| geo | ProxyError | - | 10 |
| 204 | ClientOSError | - | 7 |
| 204 | TimeoutError | - | 7 |
| speed | ProxyError | - | 7 |
| geo | ClientOSError | - | 6 |
| speed | TimeoutError | - | 5 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 250 | - |
| global | False | 300 | 279 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
