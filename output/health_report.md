# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-30 04:53:29 |
| 运行耗时 | 294.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 86359 |
| 去重后节点 | 21983 |
| TCP 可达 | 3000 |
| 真实可用 | 716 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21983 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.6 |
| tcp | 33.6 |
| probe | 55.5 |
| real_test | 150.3 |
| generate | 47.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52493 |
| vmess | 10882 |
| trojan | 10618 |
| shadowsocks | 10398 |
| hysteria2 | 1589 |
| http | 180 |
| shadowsocksr | 129 |
| socks | 54 |
| tuic | 8 |
| hysteria | 7 |
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
| 84.61 | vless | 239.7 | 651.5 | 22.23 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 84.52 | vless | 232.7 | 625.4 | 22.39 | 0.0 | 9.75 | 12.38 | 20.0 | Au1rxx-base64 | ql6k-m23nix.logicara.top |
| 84.48 | hysteria2 | 233.3 | 646.9 | 22.38 | 0.0 | 10.0 | 13.2 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 84.38 | vless | 249.5 | 658.1 | 22.0 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 167.17.69.171 |
| 84.36 | vless | 250.6 | 701.8 | 21.98 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 47.89.186.170 |
| 84.22 | vless | 256.5 | 622.0 | 21.84 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 195.211.99.49 |
| 84.11 | vless | 261.3 | 689.5 | 21.73 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.35 |
| 84.07 | vless | 263.0 | 622.1 | 21.69 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.212 |
| 83.86 | vless | 272.3 | 723.6 | 21.48 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.15 |
| 83.37 | vless | 293.1 | 789.4 | 20.99 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.89 |
| 83.29 | vless | 296.7 | 815.6 | 20.91 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 83.25 | vless | 255.4 | 679.6 | 21.87 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 38.77.133.141 |
| 83.23 | vless | 256.3 | 599.7 | 21.85 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 172.105.104.54 |
| 82.88 | vless | 314.3 | 714.1 | 20.5 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.133 |
| 82.87 | vless | 314.6 | 842.7 | 20.49 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.223 |
| 82.81 | vless | 317.5 | 825.0 | 20.43 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 79.127.243.217 |
| 82.66 | vless | 323.9 | 812.9 | 20.28 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.235 |
| 82.62 | vless | 319.2 | 816.3 | 20.39 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 66.70.179.198 |
| 82.55 | vless | 328.6 | 894.1 | 20.17 | 0.0 | 10.0 | 12.38 | 20.0 | Au1rxx-base64 | 169.40.42.95 |
| 82.37 | shadowsocks | 224.7 | 623.6 | 22.58 | 0.0 | 10.0 | 13.79 | 20.0 | Au1rxx-base64 | 37.19.198.243 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.999 | 0.929 | 378 | 1825 | prefer |
| zhangkai | 0.964 | 1.0 | 22 | 144 | prefer |
| DeltaKronecker-all | 0.955 | 0.9 | 30 | 4926 | prefer |
| Surfboard-tg-mixed | 0.824 | 0.746 | 209 | 6910 | prefer |
| mheidari-all | 0.624 | 0.544 | 285 | 18105 | observe |
| nscl5-all | 0.391 | 1.0 | 2 | 4310 | observe |
| tg-oneclickvpnkeys | 0.365 | 1.0 | 3 | 169 | observe |
| Epodonios-all | 0.255 | None | 0 | 7323 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3992 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7549 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5726 | observe |
| barry-far-vless | 0.255 | None | 0 | 5912 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4012 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1825 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 51 |
| geo | TimeoutError | - | 46 |
| speed | TimeoutError | - | 36 |
| cn-block | TimeoutError | - | 33 |
| 204 | TimeoutError | - | 17 |
| speed | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 9 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
