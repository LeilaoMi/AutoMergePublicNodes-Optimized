# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-08 07:05:29 |
| 运行耗时 | 243.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 82085 |
| 去重后节点 | 23445 |
| TCP 可达 | 3000 |
| 真实可用 | 465 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23445 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| geo | 1.5 |
| tcp | 36.0 |
| probe | 54.6 |
| real_test | 108.5 |
| generate | 36.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47749 |
| vmess | 12907 |
| trojan | 10234 |
| shadowsocks | 9722 |
| hysteria2 | 1280 |
| shadowsocksr | 69 |
| socks | 65 |
| http | 36 |
| hysteria | 13 |
| tuic | 9 |
| anytls | 1 |

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
| 84.33 | trojan | 197.1 | 466.8 | 23.22 | 0.0 | 10.0 | 13.61 | 20.0 | Au1rxx-base64 | 35.86.90.51 |
| 83.98 | trojan | 212.0 | 513.5 | 22.87 | 0.0 | 10.0 | 13.61 | 20.0 | Au1rxx-base64 | 44.242.235.129 |
| 83.9 | trojan | 215.7 | 520.2 | 22.79 | 0.0 | 10.0 | 13.61 | 20.0 | Au1rxx-base64 | 44.244.3.114 |
| 83.76 | trojan | 221.4 | 474.7 | 22.65 | 0.0 | 10.0 | 13.61 | 20.0 | Au1rxx-base64 | 44.246.163.102 |
| 80.46 | hysteria2 | 337.6 | 746.4 | 19.96 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 138.124.68.188 |
| 79.31 | http | 262.2 | 552.8 | 21.71 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.199 |
| 79.08 | http | 260.0 | 552.6 | 21.76 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.207 |
| 78.9 | http | 260.7 | 555.9 | 21.74 | 0.0 | 10.0 | 14.32 | 19.12 | zhangkai | 138.199.35.214 |
| 78.06 | shadowsocks | 210.8 | 565.3 | 22.9 | 0.0 | 10.0 | 14.16 | 20.0 | Au1rxx-base64 | 149.22.95.183 |
| 77.77 | hysteria2 | 412.4 | 939.9 | 18.23 | 0.0 | 10.0 | 14.42 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 77.4 | trojan | 313.3 | 315.3 | 20.53 | 3.18 | 9.99 | 13.61 | 20.0 | Au1rxx-base64 | 43.207.139.153 |
| 77.36 | trojan | 311.1 | 318.0 | 20.58 | 3.08 | 9.99 | 13.61 | 20.0 | Au1rxx-base64 | 13.231.232.184 |
| 77.31 | trojan | 311.1 | 318.6 | 20.58 | 3.05 | 9.99 | 13.61 | 20.0 | Au1rxx-base64 | 54.249.34.120 |
| 77.26 | trojan | 313.7 | 317.6 | 20.52 | 3.09 | 9.97 | 13.61 | 20.0 | Au1rxx-base64 | 18.181.194.227 |
| 77.21 | trojan | 313.3 | 319.1 | 20.53 | 3.03 | 9.97 | 13.61 | 20.0 | Au1rxx-base64 | 3.113.24.17 |
| 77.17 | trojan | 311.3 | 321.6 | 20.57 | 2.94 | 9.99 | 13.61 | 20.0 | Au1rxx-base64 | 18.181.164.216 |
| 77.15 | shadowsocks | 281.3 | 330.0 | 21.27 | 2.62 | 10.0 | 14.16 | 20.0 | Au1rxx-base64 | 149.22.87.204 |
| 77.15 | trojan | 312.0 | 322.5 | 20.55 | 2.9 | 10.0 | 13.61 | 20.0 | Au1rxx-base64 | 43.207.89.29 |
| 77.15 | trojan | 312.6 | 321.5 | 20.54 | 2.94 | 9.98 | 13.61 | 20.0 | Au1rxx-base64 | 3.112.223.141 |
| 77.13 | trojan | 312.4 | 320.4 | 20.55 | 2.98 | 9.97 | 13.61 | 20.0 | Au1rxx-base64 | 57.180.13.78 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.994 | 0.941 | 358 | 1368 | prefer |
| zhangkai | 0.956 | 1.0 | 20 | 25 | prefer |
| Surfboard-tg-mixed | 0.609 | 0.53 | 117 | 6419 | observe |
| DeltaKronecker-all | 0.543 | 0.463 | 80 | 5347 | observe |
| mheidari-all | 0.356 | 0.259 | 27 | 17696 | observe |
| ninja-vless | 0.327 | 1.0 | 1 | 1791 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5450 | observe |
| Epodonios-all | 0.255 | None | 0 | 6914 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7402 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5218 | observe |
| barry-far-vless | 0.255 | None | 0 | 5409 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5162 | observe |
| nscl5-all | 0.241 | None | 0 | 1643 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 49 |
| geo | ClientOSError | - | 28 |
| 204 | TimeoutError | - | 26 |
| cn-block | TimeoutError | - | 12 |
| speed | ClientOSError | - | 9 |
| speed | TimeoutError | - | 6 |
| 204 | ClientOSError | - | 4 |
| 204 | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
