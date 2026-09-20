# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-20 15:56:52 |
| 运行耗时 | 516.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 84264 |
| 去重后节点 | 23485 |
| TCP 可达 | 3000 |
| 真实可用 | 504 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23485 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| geo | 1.5 |
| tcp | 37.6 |
| probe | 199.9 |
| real_test | 201.6 |
| generate | 71.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50856 |
| vmess | 13537 |
| shadowsocks | 9836 |
| trojan | 8203 |
| hysteria2 | 1049 |
| http | 576 |
| shadowsocksr | 122 |
| socks | 70 |
| hysteria | 11 |
| tuic | 3 |
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
| 84.6 | hysteria2 | 240.8 | 670.9 | 22.2 | 0.0 | 10.0 | 13.5 | 20.0 | mheidari-all | 159.223.157.129 |
| 80.81 | vless | 246.2 | 691.7 | 22.08 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 79.141.172.154 |
| 80.7 | vless | 250.7 | 651.2 | 21.97 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.74 |
| 80.5 | shadowsocks | 240.0 | 671.9 | 22.22 | 0.0 | 10.0 | 13.44 | 18.84 | Au1rxx-base64 | 37.19.198.160 |
| 80.47 | vless | 260.8 | 647.0 | 21.74 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 138.124.60.146 |
| 80.43 | shadowsocks | 243.1 | 672.9 | 22.15 | 0.0 | 10.0 | 13.44 | 18.84 | Au1rxx-base64 | 37.19.198.244 |
| 80.42 | vless | 262.8 | 646.2 | 21.69 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.16 |
| 80.16 | vless | 274.4 | 672.6 | 21.43 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.179 |
| 80.11 | vless | 276.3 | 645.4 | 21.38 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.52 |
| 79.2 | vless | 315.5 | 837.6 | 20.47 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.235 |
| 78.98 | vless | 324.8 | 870.9 | 20.26 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.224 |
| 78.93 | vless | 327.4 | 880.2 | 20.2 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.202 |
| 78.75 | vless | 335.0 | 791.7 | 20.02 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.231 |
| 78.21 | vless | 358.7 | 989.1 | 19.48 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.173 |
| 77.93 | vless | 283.4 | 631.7 | 21.22 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.90 |
| 77.76 | hysteria2 | 323.8 | 655.8 | 20.28 | 0.0 | 10.0 | 13.5 | 18.84 | Au1rxx-base64 | 66.94.121.46 |
| 77.66 | shadowsocks | 282.1 | 648.6 | 21.25 | 0.0 | 10.0 | 13.44 | 18.84 | Au1rxx-base64 | 156.146.38.167 |
| 77.56 | shadowsocks | 285.4 | 663.8 | 21.17 | 0.0 | 10.0 | 13.44 | 18.84 | Au1rxx-base64 | 156.146.38.168 |
| 77.49 | shadowsocks | 279.3 | 641.5 | 21.31 | 0.0 | 10.0 | 13.44 | 18.84 | Au1rxx-base64 | 156.146.38.170 |
| 77.46 | vless | 289.5 | 719.8 | 21.08 | 0.0 | 10.0 | 9.89 | 18.84 | Au1rxx-base64 | 169.40.42.229 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.979 | 0.917 | 301 | 1617 | prefer |
| ermaozi | 0.897 | 0.917 | 24 | 314 | prefer |
| Surfboard-tg-mixed | 0.772 | 0.693 | 212 | 7133 | prefer |
| mheidari-all | 0.65 | 0.571 | 91 | 16459 | observe |
| DeltaKronecker-all | 0.385 | 0.5 | 8 | 6092 | observe |
| tg-oneclickvpnkeys | 0.315 | 1.0 | 2 | 103 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7577 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9286 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5703 | observe |
| barry-far-vless | 0.255 | None | 0 | 5918 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4315 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1617 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 37 |
| cn-block | TimeoutError | - | 20 |
| 204 | ProxyError | - | 19 |
| 204 | TimeoutError | - | 19 |
| geo | TimeoutError | - | 16 |
| cn-block | ClientOSError | - | 14 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| speed | ClientOSError | - | 4 |
| speed | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
