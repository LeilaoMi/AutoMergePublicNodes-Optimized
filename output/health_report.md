# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-16 18:42:21 |
| 运行耗时 | 404.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 79897 |
| 去重后节点 | 21949 |
| TCP 可达 | 3000 |
| 真实可用 | 1043 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21949 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 0.6 |
| tcp | 33.3 |
| probe | 77.0 |
| real_test | 244.7 |
| generate | 43.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 43751 |
| trojan | 14313 |
| vmess | 10867 |
| shadowsocks | 9554 |
| hysteria2 | 1085 |
| http | 159 |
| socks | 77 |
| shadowsocksr | 72 |
| tuic | 10 |
| hysteria | 7 |
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
| 83.96 | hysteria2 | 247.1 | 675.6 | 22.06 | 0.0 | 10.0 | 13.0 | 20.0 | Au1rxx-base64 | 159.223.157.129 |
| 83.51 | http | 264.6 | 674.2 | 21.65 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.5 | http | 265.1 | 690.2 | 21.64 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.43 | http | 268.1 | 689.9 | 21.57 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 83.27 | http | 275.2 | 723.3 | 21.41 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.25 | http | 275.9 | 716.5 | 21.39 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.06 | hysteria2 | 265.0 | 706.7 | 21.64 | 0.0 | 10.0 | 13.0 | 19.42 | mheidari-all | 138.124.68.188 |
| 82.51 | http | 307.8 | 814.0 | 20.65 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 82.25 | http | 319.2 | 850.4 | 20.39 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 82.24 | http | 319.5 | 849.1 | 20.38 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 82.14 | http | 324.0 | 849.4 | 20.28 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 82.01 | http | 329.7 | 860.8 | 20.15 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 82.0 | http | 330.0 | 886.2 | 20.14 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 82.0 | http | 330.1 | 873.0 | 20.14 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 81.94 | http | 332.5 | 878.1 | 20.08 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 81.92 | http | 333.3 | 896.0 | 20.06 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 81.9 | vless | 253.1 | 665.3 | 21.92 | 0.0 | 9.33 | 10.65 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 81.85 | http | 336.5 | 884.6 | 19.99 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 81.77 | http | 339.7 | 908.0 | 19.91 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 81.75 | http | 340.9 | 906.1 | 19.89 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.967 | 748 | 1994 | prefer |
| zhangkai | 0.999 | 1.0 | 127 | 159 | prefer |
| mheidari-all | 0.859 | 0.783 | 152 | 17005 | prefer |
| Surfboard-tg-mixed | 0.835 | 0.761 | 92 | 5798 | prefer |
| nscl5-all | 0.391 | 1.0 | 2 | 2601 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 174 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4990 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1994 | observe |
| Epodonios-all | 0.255 | None | 0 | 6468 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3982 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7449 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4549 | observe |
| barry-far-vless | 0.255 | None | 0 | 4856 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4025 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 18 |
| cn-block | TimeoutError | - | 13 |
| speed | TimeoutError | - | 12 |
| geo | TimeoutError | - | 9 |
| geo | ClientOSError | - | 7 |
| cn-block | ClientOSError | - | 7 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 3 |
| speed | ClientOSError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
