# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-15 21:13:29 |
| 运行耗时 | 494.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 84752 |
| 去重后节点 | 23104 |
| TCP 可达 | 3000 |
| 真实可用 | 417 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23104 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.4 |
| tcp | 38.0 |
| probe | 187.2 |
| real_test | 182.1 |
| generate | 79.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51851 |
| vmess | 12962 |
| shadowsocks | 9497 |
| trojan | 8299 |
| hysteria2 | 1320 |
| http | 625 |
| shadowsocksr | 125 |
| socks | 55 |
| hysteria | 11 |
| tuic | 5 |
| anytls | 2 |

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
| 83.46 | hysteria2 | 234.2 | 643.7 | 22.36 | 0.0 | 10.0 | 13.64 | 18.56 | Au1rxx-base64 | 159.223.157.129 |
| 80.28 | vless | 230.4 | 595.4 | 22.44 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 195.123.235.177 |
| 79.62 | vless | 259.1 | 639.3 | 21.78 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 169.40.42.15 |
| 79.44 | vless | 266.8 | 703.7 | 21.6 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 169.40.42.35 |
| 79.37 | shadowsocks | 238.5 | 642.7 | 22.26 | 0.0 | 10.0 | 13.55 | 18.56 | Au1rxx-base64 | 37.19.198.244 |
| 79.09 | vless | 282.1 | 693.7 | 21.25 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 2.24.124.64 |
| 78.62 | vless | 302.2 | 750.7 | 20.78 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 169.40.42.163 |
| 78.48 | vless | 308.6 | 844.5 | 20.64 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 137.184.218.169 |
| 78.26 | vless | 317.8 | 723.5 | 20.42 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 169.40.42.184 |
| 78.2 | vless | 320.6 | 810.8 | 20.36 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 66.70.179.198 |
| 78.02 | vless | 328.3 | 809.5 | 20.18 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 169.40.42.223 |
| 77.96 | shadowsocks | 320.7 | 843.3 | 20.35 | 0.0 | 10.0 | 13.55 | 18.56 | Au1rxx-base64 | 38.180.135.156 |
| 77.62 | vless | 345.4 | 949.9 | 19.78 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 185.95.231.156 |
| 77.44 | vless | 352.9 | 902.2 | 19.61 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 216.152.147.28 |
| 77.41 | vless | 302.8 | 679.3 | 20.77 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 198.251.78.29 |
| 77.35 | shadowsocks | 347.1 | 995.9 | 19.74 | 0.0 | 10.0 | 13.55 | 18.56 | Au1rxx-base64 | 15.204.247.206 |
| 77.11 | shadowsocks | 284.6 | 650.0 | 21.19 | 0.0 | 10.0 | 13.55 | 18.56 | Au1rxx-base64 | 156.146.38.170 |
| 77.11 | vless | 294.6 | 707.1 | 20.96 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 169.40.42.74 |
| 76.91 | vless | 342.0 | 810.1 | 19.86 | 0.0 | 10.0 | 9.28 | 18.56 | Au1rxx-base64 | 169.40.42.229 |
| 76.12 | shadowsocks | 292.3 | 807.2 | 21.01 | 0.0 | 10.0 | 13.55 | 18.56 | Au1rxx-base64 | 37.19.198.160 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.989 | 0.935 | 31 | 15952 | prefer |
| Au1rxx-base64 | 0.948 | 0.889 | 305 | 1553 | prefer |
| ermaozi | 0.779 | 0.778 | 36 | 406 | prefer |
| Surfboard-tg-mixed | 0.702 | 0.624 | 125 | 7516 | prefer |
| DeltaKronecker-all | 0.633 | 0.714 | 14 | 5932 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5015 | observe |
| Epodonios-all | 0.255 | None | 0 | 7982 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8946 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 6065 | observe |
| barry-far-vless | 0.255 | None | 0 | 6289 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4258 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.237 | None | 0 | 1553 | observe |
| ermaozi-get_subscribe | 0.224 | 0.5 | 2 | 422 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 19 |
| cn-block | TimeoutError | - | 16 |
| cn-block | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 13 |
| 204 | ProxyError | - | 11 |
| speed | ClientOSError | - | 11 |
| speed | TimeoutError | - | 6 |
| cn-block | ProxyError | - | 3 |
| geo | TimeoutError | - | 3 |
| 204 | ClientOSError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
