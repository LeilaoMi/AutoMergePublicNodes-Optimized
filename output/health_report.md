# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-30 14:19:53 |
| 运行耗时 | 264.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78844 |
| 去重后节点 | 22974 |
| TCP 可达 | 3000 |
| 真实可用 | 473 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22974 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| geo | 1.4 |
| tcp | 32.9 |
| probe | 56.3 |
| real_test | 120.1 |
| generate | 46.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46036 |
| vmess | 11321 |
| shadowsocks | 10321 |
| trojan | 10267 |
| hysteria2 | 587 |
| http | 116 |
| shadowsocksr | 77 |
| socks | 59 |
| anytls | 26 |
| tuic | 20 |
| hysteria | 14 |

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
| 78.8 | shadowsocks | 209.4 | 554.4 | 22.93 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 149.22.95.183 |
| 76.22 | vless | 277.0 | 671.6 | 21.37 | 0.0 | 10.0 | 7.25 | 17.6 | Au1rxx-base64 | 52.43.158.158 |
| 74.13 | shadowsocks | 275.3 | 585.1 | 21.4 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 108.181.0.177 |
| 73.77 | shadowsocks | 285.4 | 614.2 | 21.17 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 108.181.118.10 |
| 72.99 | shadowsocks | 277.0 | 326.3 | 21.37 | 2.76 | 9.95 | 12.27 | 17.6 | Au1rxx-base64 | 149.22.87.240 |
| 72.36 | trojan | 331.3 | 667.2 | 20.11 | 0.0 | 10.0 | 12.77 | 17.6 | Au1rxx-base64 | 163.245.196.68 |
| 72.26 | hysteria2 | 345.4 | 709.6 | 19.78 | 0.0 | 10.0 | 10.83 | 17.6 | Au1rxx-base64 | 159.223.157.129 |
| 72.12 | shadowsocks | 282.6 | 344.7 | 21.24 | 2.07 | 9.95 | 12.27 | 17.6 | Au1rxx-base64 | 149.22.87.241 |
| 71.85 | shadowsocks | 314.5 | 651.9 | 20.5 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 156.146.38.168 |
| 71.29 | shadowsocks | 324.2 | 654.8 | 20.27 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 156.146.38.167 |
| 71.2 | vless | 242.0 | 511.4 | 22.18 | 0.0 | 10.0 | 7.25 | 17.6 | Au1rxx-base64 | 64.23.143.23 |
| 70.56 | shadowsocks | 320.4 | 599.3 | 20.36 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 173.244.56.9 |
| 69.9 | http | 542.8 | 1395.6 | 15.21 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.196 |
| 69.57 | shadowsocks | 361.3 | 732.9 | 19.41 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 37.19.198.243 |
| 69.33 | trojan | 409.8 | 811.5 | 18.29 | 0.0 | 10.0 | 12.77 | 17.6 | Au1rxx-base64 | 153.75.250.171 |
| 69.3 | shadowsocks | 372.0 | 762.3 | 19.17 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 37.19.198.236 |
| 69.01 | http | 539.3 | 1382.6 | 15.29 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.214 |
| 68.94 | http | 538.5 | 1385.2 | 15.31 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.220 |
| 68.89 | http | 538.8 | 1367.2 | 15.3 | 0.0 | 10.0 | 14.88 | 19.96 | zhangkai | 138.199.35.204 |
| 68.79 | shadowsocks | 335.2 | 598.5 | 20.02 | 0.0 | 10.0 | 12.27 | 17.6 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | 1.0 | 113 | 129 | prefer |
| Au1rxx-base64 | 0.869 | 0.813 | 262 | 1460 | prefer |
| DeltaKronecker-all | 0.62 | 0.541 | 159 | 5759 | observe |
| Surfboard-tg-mixed | 0.618 | 0.538 | 104 | 5443 | observe |
| mheidari-all | 0.446 | 0.8 | 5 | 16526 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5342 | observe |
| Epodonios-all | 0.255 | None | 0 | 6193 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3973 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6515 | observe |
| barry-far-vless | 0.255 | None | 0 | 4667 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5029 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.233 | None | 0 | 1460 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 55 |
| geo | ClientOSError | - | 30 |
| speed | TimeoutError | - | 25 |
| 204 | TimeoutError | - | 21 |
| 204 | ProxyError | - | 15 |
| speed | ClientOSError | - | 13 |
| cn-block | TimeoutError | - | 7 |
| cn-block | ClientOSError | - | 4 |
| geo | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| 204 | ClientOSError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
