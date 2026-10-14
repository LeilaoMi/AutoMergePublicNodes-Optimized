# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-14 04:29:39 |
| 运行耗时 | 901.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 98590 |
| 去重后节点 | 27454 |
| TCP 可达 | 3000 |
| 真实可用 | 57 |
| Verified 输出 | 57 |
| Global 输出 | 75 |
| All 输出 | 27454 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 117.5 |
| probe | 298.5 |
| real_test | 370.4 |
| generate | 106.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58026 |
| vmess | 16099 |
| shadowsocks | 11897 |
| trojan | 10489 |
| hysteria2 | 1309 |
| http | 486 |
| shadowsocksr | 165 |
| socks | 70 |
| anytls | 25 |
| hysteria | 18 |
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
| 81.34 | shadowsocks | 259.5 | 628.5 | 21.77 | 0.0 | 10.0 | 14.42 | 19.22 | Au1rxx-base64 | 156.146.38.170 |
| 80.76 | shadowsocks | 219.8 | 537.9 | 22.69 | 0.0 | 8.61 | 14.42 | 19.22 | Au1rxx-base64 | 173.244.56.6 |
| 77.39 | vless | 217.2 | 538.4 | 22.75 | 0.0 | 7.67 | 7.75 | 19.22 | Au1rxx-base64 | 154.12.38.159 |
| 77.36 | vless | 217.2 | 531.0 | 22.75 | 0.0 | 7.64 | 7.75 | 19.22 | Au1rxx-base64 | 195.123.240.65 |
| 77.25 | shadowsocks | 213.8 | 529.2 | 22.83 | 0.0 | 9.78 | 14.42 | 19.22 | Au1rxx-base64 | 173.244.56.9 |
| 77.16 | trojan | 270.5 | 581.1 | 21.52 | 0.0 | 7.81 | 13.81 | 19.22 | Au1rxx-base64 | 107.149.159.190 |
| 77.06 | vless | 218.1 | 534.3 | 22.73 | 0.0 | 8.22 | 7.75 | 19.22 | Au1rxx-base64 | 154.29.145.196 |
| 76.79 | vless | 195.2 | 498.3 | 23.26 | 0.0 | 6.56 | 7.75 | 19.22 | Au1rxx-base64 | 45.32.69.110 |
| 76.79 | shadowsocks | 284.2 | 293.6 | 21.2 | 3.99 | 9.28 | 14.42 | 19.22 | Au1rxx-base64 | 149.22.87.241 |
| 76.54 | vless | 212.1 | 502.2 | 22.87 | 0.0 | 6.7 | 7.75 | 19.22 | Au1rxx-base64 | 144.202.126.147 |
| 75.91 | vless | 305.6 | 736.2 | 20.7 | 0.0 | 8.79 | 7.75 | 19.22 | Au1rxx-base64 | 147.45.60.160 |
| 75.82 | vless | 343.6 | 924.2 | 19.82 | 0.0 | 9.03 | 7.75 | 19.22 | Au1rxx-base64 | 154.9.241.170 |
| 75.67 | shadowsocks | 297.1 | 329.9 | 20.9 | 2.63 | 9.76 | 14.42 | 19.22 | Au1rxx-base64 | 149.22.87.240 |
| 75.61 | shadowsocks | 260.5 | 626.4 | 21.75 | 0.0 | 10.0 | 14.42 | 19.22 | Au1rxx-base64 | 156.146.38.167 |
| 74.73 | hysteria2 | 226.4 | 229.5 | 22.54 | 6.39 | 0.0 | 13.64 | 19.22 | Au1rxx-base64 | vp3.yysyy.online |
| 74.63 | vless | 289.1 | 519.5 | 21.08 | 0.0 | 8.95 | 7.75 | 19.22 | Au1rxx-base64 | 95.111.212.241 |
| 74.46 | trojan | 340.0 | 338.4 | 19.91 | 2.31 | 9.76 | 13.81 | 19.22 | Au1rxx-base64 | 45.32.52.173 |
| 74.39 | shadowsocks | 303.2 | 354.3 | 20.76 | 1.71 | 9.76 | 14.42 | 19.22 | Au1rxx-base64 | 149.22.87.204 |
| 74.35 | vless | 218.8 | 537.9 | 22.71 | 0.0 | 7.96 | 7.75 | 19.22 | Au1rxx-base64 | 154.40.55.185 |
| 74.32 | shadowsocks | 262.1 | 635.6 | 21.71 | 0.0 | 8.45 | 14.42 | 19.22 | Au1rxx-base64 | 156.146.38.169 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.941 | 0.872 | 328 | 1771 | prefer |
| Surfboard-tg-mixed | 0.807 | 0.73 | 137 | 7113 | prefer |
| ermaozi-get_subscribe | 0.577 | 0.556 | 36 | 598 | observe |
| zhangkai | 0.555 | 1.0 | 8 | 144 | observe |
| mheidari-all | 0.529 | 0.449 | 205 | 24076 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5086 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 5076 | observe |
| Epodonios-all | 0.255 | None | 0 | 7613 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9825 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5621 | observe |
| barry-far-vless | 0.255 | None | 0 | 5866 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4216 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 90 |
| geo | ClientOSError | - | 30 |
| 204 | ProxyError | - | 28 |
| speed | ClientOSError | - | 17 |
| 204 | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 12 |
| cn-block | ClientOSError | - | 7 |
| speed | TimeoutError | - | 7 |
| 204 | ProxyConnectionError | - | 2 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 55 | 57 | - |
| global | False | 70 | 75 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
