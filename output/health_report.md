# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-07 21:27:04 |
| 运行耗时 | 297.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 84365 |
| 去重后节点 | 22975 |
| TCP 可达 | 3000 |
| 真实可用 | 554 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22975 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| geo | 1.5 |
| tcp | 37.4 |
| probe | 86.0 |
| real_test | 124.8 |
| generate | 41.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52409 |
| vmess | 12126 |
| shadowsocks | 9866 |
| trojan | 8396 |
| hysteria2 | 1228 |
| http | 138 |
| shadowsocksr | 128 |
| socks | 45 |
| hysteria | 11 |
| anytls | 10 |
| tuic | 8 |

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
| 85.79 | hysteria2 | 184.0 | 506.7 | 23.52 | 0.0 | 10.0 | 13.75 | 19.52 | Au1rxx-base64 | 66.94.121.46 |
| 80.48 | vless | 259.2 | 533.3 | 21.78 | 0.0 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 172.233.139.46 |
| 79.8 | vless | 231.5 | 253.3 | 22.42 | 5.5 | 10.0 | 10.71 | 16.78 | Surfboard-tg-mixed | 31.76.91.72 |
| 79.69 | vless | 273.8 | 547.6 | 21.44 | 0.0 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 172.235.38.85 |
| 78.09 | vless | 284.2 | 577.9 | 21.2 | 0.0 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 23.94.227.94 |
| 77.28 | shadowsocks | 273.0 | 480.3 | 21.46 | 0.0 | 10.0 | 13.74 | 19.52 | Au1rxx-base64 | 108.181.0.177 |
| 76.98 | http | 264.7 | 565.1 | 21.65 | 0.0 | 10.0 | 13.12 | 18.38 | zhangkai | 138.199.35.216 |
| 76.53 | vless | 261.5 | 558.5 | 21.72 | 0.0 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 38.244.20.160 |
| 76.48 | vless | 309.5 | 325.6 | 20.61 | 2.79 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 154.31.114.248 |
| 76.42 | vless | 313.6 | 321.3 | 20.52 | 2.95 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 13.230.222.139 |
| 76.37 | vless | 317.9 | 319.9 | 20.42 | 3.0 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 18.177.61.231 |
| 76.27 | vless | 315.4 | 324.0 | 20.48 | 2.85 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 13.231.156.101 |
| 76.24 | vless | 313.7 | 324.2 | 20.52 | 2.84 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 13.231.220.17 |
| 76.2 | vless | 318.3 | 322.8 | 20.41 | 2.89 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 13.230.66.70 |
| 76.08 | vless | 314.6 | 327.2 | 20.49 | 2.73 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 13.114.124.85 |
| 76.07 | vless | 314.8 | 328.9 | 20.49 | 2.67 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 43.207.162.145 |
| 76.07 | vless | 319.6 | 326.8 | 20.38 | 2.75 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 52.199.9.165 |
| 75.98 | vless | 316.6 | 329.6 | 20.45 | 2.64 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 52.194.245.53 |
| 75.98 | vless | 321.3 | 328.6 | 20.34 | 2.68 | 9.99 | 10.71 | 19.52 | Au1rxx-base64 | 3.112.131.211 |
| 75.97 | vless | 317.9 | 328.4 | 20.42 | 2.68 | 10.0 | 10.71 | 19.52 | Au1rxx-base64 | 13.193.9.59 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.936 | 374 | 1688 | prefer |
| zhangkai | 0.929 | 0.958 | 24 | 144 | prefer |
| mheidari-all | 0.905 | 0.833 | 78 | 16413 | prefer |
| DeltaKronecker-all | 0.84 | 0.783 | 23 | 6417 | prefer |
| Surfboard-tg-mixed | 0.771 | 0.693 | 137 | 7444 | prefer |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 196 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7899 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8444 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6179 | observe |
| barry-far-vless | 0.255 | None | 0 | 6394 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4218 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1688 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 24 |
| geo | ClientOSError | - | 19 |
| cn-block | TimeoutError | - | 16 |
| cn-block | ClientOSError | - | 8 |
| speed | ClientOSError | - | 5 |
| geo | TimeoutError | - | 4 |
| speed | TimeoutError | - | 3 |
| geo | ProxyError | - | 3 |
| 204 | ClientOSError | - | 3 |
| 204 | ProxyError | - | 2 |
| 204 | ProxyConnectionError | - | 1 |
| speed | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
