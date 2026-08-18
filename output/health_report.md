# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-18 01:41:07 |
| 运行耗时 | 394.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 80389 |
| 去重后节点 | 22947 |
| TCP 可达 | 3000 |
| 真实可用 | 1304 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22947 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.2 |
| tcp | 36.1 |
| probe | 70.9 |
| real_test | 261.6 |
| generate | 19.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45542 |
| trojan | 13652 |
| shadowsocks | 10075 |
| vmess | 8512 |
| hysteria2 | 2187 |
| http | 193 |
| socks | 123 |
| shadowsocksr | 81 |
| tuic | 15 |
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
| 84.65 | hysteria2 | 249.6 | 678.0 | 22.0 | 0.0 | 10.0 | 14.25 | 19.4 | Au1rxx-base64 | 138.124.68.188 |
| 83.88 | http | 248.9 | 636.7 | 22.02 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 83.78 | http | 252.9 | 647.6 | 21.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 83.78 | http | 253.0 | 649.7 | 21.92 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.4 |
| 83.74 | http | 254.7 | 651.1 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.72 | http | 255.5 | 653.2 | 21.86 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.72 | http | 255.8 | 665.9 | 21.86 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 83.67 | http | 258.0 | 672.2 | 21.81 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 83.65 | http | 258.5 | 669.4 | 21.79 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.58 | http | 261.6 | 682.5 | 21.72 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 83.56 | http | 262.4 | 672.8 | 21.7 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.52 | http | 264.3 | 691.5 | 21.66 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.4 | http | 269.7 | 684.6 | 21.54 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.27 | http | 275.2 | 719.5 | 21.41 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.08 | hysteria2 | 313.0 | 848.7 | 20.53 | 0.0 | 10.0 | 14.25 | 19.4 | Au1rxx-base64 | 159.223.157.129 |
| 82.95 | http | 288.9 | 760.9 | 21.09 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 82.64 | http | 302.2 | 794.5 | 20.78 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |
| 82.6 | http | 303.8 | 801.8 | 20.74 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 82.01 | vless | 259.0 | 681.7 | 21.78 | 0.0 | 10.0 | 10.83 | 19.4 | Au1rxx-base64 | 137.184.218.169 |
| 81.89 | vless | 264.4 | 676.8 | 21.66 | 0.0 | 10.0 | 10.83 | 19.4 | Au1rxx-base64 | 167.17.69.171 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.964 | 527 | 1475 | prefer |
| zhangkai | 0.998 | 1.0 | 125 | 159 | prefer |
| mheidari-all | 0.949 | 0.871 | 672 | 16056 | prefer |
| Surfboard-tg-mixed | 0.8 | 0.724 | 98 | 6128 | prefer |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 179 | observe |
| DeltaKronecker-all | 0.257 | 0.169 | 77 | 6368 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5085 | observe |
| Epodonios-all | 0.255 | None | 0 | 6777 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3986 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6971 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4797 | observe |
| barry-far-vless | 0.255 | None | 0 | 5128 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4027 | observe |
| nscl5-all | 0.255 | None | 0 | 2992 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 88 |
| speed | TimeoutError | - | 50 |
| geo | ClientOSError | - | 24 |
| speed | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 6 |
| 204 | ProxyError | - | 6 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
