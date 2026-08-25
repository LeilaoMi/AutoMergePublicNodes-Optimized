# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-25 01:41:18 |
| 运行耗时 | 310.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 83410 |
| 去重后节点 | 23892 |
| TCP 可达 | 3000 |
| 真实可用 | 787 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23892 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| geo | 1.5 |
| tcp | 38.1 |
| probe | 59.2 |
| real_test | 180.4 |
| generate | 26.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52265 |
| shadowsocks | 11137 |
| vmess | 10512 |
| trojan | 7603 |
| hysteria2 | 1509 |
| http | 164 |
| shadowsocksr | 132 |
| socks | 68 |
| hysteria | 13 |
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
| 81.49 | vless | 257.4 | 646.1 | 21.82 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.179 |
| 81.33 | vless | 264.1 | 686.8 | 21.66 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 79.127.243.217 |
| 81.31 | vless | 265.1 | 663.2 | 21.64 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 167.17.69.171 |
| 81.14 | vless | 272.3 | 740.2 | 21.47 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 47.89.186.170 |
| 80.76 | vless | 252.7 | 648.4 | 21.93 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.184 |
| 80.16 | shadowsocks | 259.3 | 701.4 | 21.78 | 0.0 | 10.0 | 13.32 | 19.06 | Au1rxx-base64 | 37.19.198.160 |
| 80.07 | shadowsocks | 262.9 | 709.6 | 21.69 | 0.0 | 10.0 | 13.32 | 19.06 | Au1rxx-base64 | 37.19.198.244 |
| 79.94 | vless | 324.4 | 879.0 | 20.27 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 137.184.218.169 |
| 79.94 | vless | 324.5 | 862.5 | 20.27 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.173 |
| 79.81 | shadowsocks | 263.4 | 664.4 | 21.68 | 0.0 | 10.0 | 13.32 | 19.06 | Au1rxx-base64 | 155.138.136.240 |
| 79.8 | shadowsocks | 253.1 | 697.1 | 21.92 | 0.0 | 10.0 | 13.32 | 19.06 | Au1rxx-base64 | 15.204.247.175 |
| 79.54 | vless | 270.9 | 649.3 | 21.51 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.35 |
| 79.53 | vless | 325.0 | 846.4 | 20.26 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.75 |
| 79.39 | vless | 348.1 | 859.9 | 19.72 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.223 |
| 79.15 | vless | 358.4 | 938.3 | 19.48 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 185.95.231.156 |
| 79.13 | vless | 359.4 | 764.6 | 19.46 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.16 |
| 78.98 | vless | 295.4 | 711.4 | 20.94 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 216.152.147.28 |
| 78.97 | vless | 366.4 | 939.7 | 19.3 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.225 |
| 78.94 | vless | 367.7 | 930.3 | 19.27 | 0.0 | 10.0 | 10.61 | 19.06 | Au1rxx-base64 | 169.40.42.232 |
| 78.9 | shadowsocks | 226.9 | 597.0 | 22.52 | 0.0 | 10.0 | 13.32 | 19.06 | Au1rxx-base64 | 198.98.53.130 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.979 | 0.908 | 87 | 6540 | prefer |
| Au1rxx-base64 | 0.975 | 0.909 | 471 | 1713 | prefer |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| mheidari-all | 0.436 | 0.356 | 669 | 19487 | observe |
| DeltaKronecker-all | 0.397 | 0.31 | 58 | 5914 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4899 | observe |
| Epodonios-all | 0.255 | None | 0 | 7074 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3989 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7047 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5352 | observe |
| barry-far-vless | 0.255 | None | 0 | 5640 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4132 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1714 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 223 |
| speed | TimeoutError | - | 99 |
| geo | ClientOSError | - | 97 |
| speed | ClientOSError | - | 59 |
| cn-block | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 12 |
| cn-block | TimeoutError | - | 9 |
| 204 | ProxyError | - | 5 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:33184: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
