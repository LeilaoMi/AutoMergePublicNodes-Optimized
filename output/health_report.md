# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-02 16:25:04 |
| 运行耗时 | 283.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82564 |
| 去重后节点 | 23518 |
| TCP 可达 | 3000 |
| 真实可用 | 572 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23518 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.2 |
| geo | 1.5 |
| tcp | 37.1 |
| probe | 83.8 |
| real_test | 112.6 |
| generate | 40.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51773 |
| vmess | 11154 |
| shadowsocks | 9978 |
| trojan | 7701 |
| hysteria2 | 1587 |
| http | 143 |
| shadowsocksr | 130 |
| socks | 80 |
| tuic | 11 |
| hysteria | 7 |

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
| 84.88 | vless | 174.7 | 474.5 | 23.73 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 45.33.107.237 |
| 84.85 | vless | 176.1 | 496.7 | 23.7 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 173.230.155.55 |
| 84.8 | vless | 178.2 | 487.6 | 23.65 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 45.33.107.60 |
| 84.8 | vless | 178.2 | 490.7 | 23.65 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 192.155.87.188 |
| 84.79 | vless | 178.9 | 501.1 | 23.64 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 50.116.9.184 |
| 84.75 | vless | 180.7 | 502.3 | 23.6 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 45.79.103.108 |
| 84.73 | vless | 181.5 | 490.4 | 23.58 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 45.33.62.166 |
| 84.18 | vless | 205.2 | 533.1 | 23.03 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 172.233.156.123 |
| 84.15 | vless | 206.4 | 539.5 | 23.0 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 172.233.156.118 |
| 83.92 | vless | 216.2 | 567.2 | 22.77 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 108.186.202.51 |
| 83.76 | vless | 223.2 | 593.6 | 22.61 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 172.233.139.46 |
| 83.7 | vless | 225.6 | 595.7 | 22.55 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 172.236.252.35 |
| 83.57 | vless | 231.6 | 597.8 | 22.42 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 172.239.67.156 |
| 83.34 | vless | 241.5 | 479.4 | 22.19 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 172.235.38.85 |
| 81.85 | vless | 305.6 | 800.7 | 20.7 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 15.204.97.197 |
| 81.82 | vless | 177.7 | 488.0 | 23.67 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 31.58.50.200 |
| 81.81 | vless | 307.3 | 803.8 | 20.66 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 15.204.97.206 |
| 81.57 | vless | 170.8 | 470.9 | 23.82 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 74.207.245.124 |
| 81.5 | vless | 320.9 | 844.0 | 20.35 | 0.0 | 10.0 | 11.79 | 19.36 | Au1rxx-base64 | 15.204.97.216 |
| 81.22 | hysteria2 | 347.0 | 923.0 | 19.74 | 0.0 | 10.0 | 13.12 | 19.36 | Au1rxx-base64 | 66.94.121.46 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.961 | 0.894 | 349 | 1741 | prefer |
| mheidari-all | 0.947 | 0.874 | 111 | 15532 | prefer |
| zhangkai | 0.926 | 0.957 | 23 | 144 | prefer |
| DeltaKronecker-all | 0.92 | 0.87 | 23 | 7295 | prefer |
| Surfboard-tg-mixed | 0.819 | 0.742 | 159 | 7112 | prefer |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 178 | observe |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 103 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 50 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4765 | observe |
| Epodonios-all | 0.255 | None | 0 | 7553 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7794 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5992 | observe |
| barry-far-vless | 0.255 | None | 0 | 6200 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4066 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 18 |
| cn-block | TimeoutError | - | 17 |
| cn-block | ClientOSError | - | 15 |
| geo | ClientOSError | - | 12 |
| 204 | ProxyConnectionError | - | 7 |
| 204 | ProxyError | - | 7 |
| speed | ClientOSError | - | 6 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 5 |
| geo | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
