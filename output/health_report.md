# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-17 01:45:27 |
| 运行耗时 | 392.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 80829 |
| 去重后节点 | 22248 |
| TCP 可达 | 3000 |
| 真实可用 | 1311 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22248 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.0 |
| tcp | 33.5 |
| probe | 76.1 |
| real_test | 244.4 |
| generate | 30.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 44376 |
| trojan | 14790 |
| vmess | 10738 |
| shadowsocks | 9515 |
| hysteria2 | 1073 |
| http | 159 |
| socks | 84 |
| shadowsocksr | 75 |
| tuic | 8 |
| hysteria | 7 |
| anytls | 4 |

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
| 83.95 | http | 245.7 | 635.7 | 22.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.76 | http | 254.1 | 659.7 | 21.9 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.74 | http | 254.8 | 657.6 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.63 | http | 259.6 | 676.9 | 21.77 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.57 | http | 262.3 | 677.8 | 21.71 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.52 | http | 264.3 | 688.0 | 21.66 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.47 | http | 266.5 | 694.4 | 21.61 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 83.46 | http | 266.9 | 691.3 | 21.6 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.45 | http | 267.3 | 698.5 | 21.59 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.45 | http | 267.5 | 696.1 | 21.59 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 83.38 | http | 270.3 | 705.2 | 21.52 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.27 | http | 275.1 | 707.9 | 21.41 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.26 | http | 275.6 | 721.7 | 21.4 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 83.24 | http | 276.2 | 725.9 | 21.38 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.11 | http | 281.8 | 741.1 | 21.25 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 82.96 | vless | 259.2 | 676.7 | 21.78 | 0.0 | 10.0 | 11.18 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 82.75 | vless | 268.4 | 658.1 | 21.57 | 0.0 | 10.0 | 11.18 | 20.0 | Au1rxx-base64 | 167.17.69.171 |
| 82.65 | vless | 272.6 | 700.4 | 21.47 | 0.0 | 10.0 | 11.18 | 20.0 | Au1rxx-base64 | 169.40.42.212 |
| 82.24 | vless | 273.4 | 642.1 | 21.45 | 0.0 | 10.0 | 11.18 | 20.0 | Au1rxx-base64 | 195.211.98.214 |
| 81.64 | http | 345.6 | 933.4 | 19.78 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.966 | 913 | 1994 | prefer |
| zhangkai | 0.991 | 0.992 | 127 | 159 | prefer |
| Surfboard-tg-mixed | 0.908 | 0.833 | 132 | 5916 | prefer |
| mheidari-all | 0.651 | 0.571 | 324 | 17074 | observe |
| nscl5-all | 0.335 | 1.0 | 1 | 3043 | observe |
| tg-oneclickvpnkeys | 0.26 | 1.0 | 1 | 129 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4990 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1994 | observe |
| Epodonios-all | 0.255 | None | 0 | 6595 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3988 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7537 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4572 | observe |
| barry-far-vless | 0.255 | None | 0 | 4905 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4025 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 105 |
| speed | TimeoutError | - | 44 |
| cn-block | TimeoutError | - | 40 |
| geo | ClientOSError | - | 22 |
| speed | ClientOSError | - | 16 |
| 204 | TimeoutError | - | 7 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:45089: bind: address already in use | - | 1 |
| geo | ProxyError | - | 1 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
