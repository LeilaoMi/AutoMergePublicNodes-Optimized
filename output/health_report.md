# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-12 19:12:36 |
| 运行耗时 | 264.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 79820 |
| 去重后节点 | 22379 |
| TCP 可达 | 3000 |
| 真实可用 | 604 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22379 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 14.5 |
| geo | 1.3 |
| tcp | 32.9 |
| probe | 56.4 |
| real_test | 119.8 |
| generate | 39.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 45463 |
| vmess | 13284 |
| shadowsocks | 9740 |
| trojan | 9667 |
| hysteria2 | 1344 |
| http | 159 |
| shadowsocksr | 73 |
| socks | 72 |
| tuic | 11 |
| hysteria | 7 |

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
| 84.34 | hysteria2 | 245.6 | 675.3 | 22.09 | 0.0 | 10.0 | 14.21 | 19.04 | Au1rxx-base64 | 138.124.68.188 |
| 83.97 | http | 244.8 | 647.7 | 22.11 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.33 |
| 83.92 | http | 247.0 | 657.2 | 22.06 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.31 |
| 83.86 | http | 249.8 | 671.7 | 22.0 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.10 |
| 83.76 | http | 254.0 | 673.8 | 21.9 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.28 |
| 83.74 | http | 254.8 | 673.2 | 21.88 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.39 |
| 83.73 | http | 255.3 | 687.7 | 21.87 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.41 |
| 83.7 | http | 256.6 | 682.3 | 21.84 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.34 |
| 83.63 | http | 259.6 | 704.7 | 21.77 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.5 |
| 83.59 | http | 261.1 | 713.7 | 21.73 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.21 |
| 83.31 | http | 273.5 | 726.2 | 21.45 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.27 |
| 83.18 | hysteria2 | 291.7 | 676.8 | 21.03 | 0.0 | 10.0 | 14.21 | 19.04 | Au1rxx-base64 | 159.223.157.129 |
| 82.97 | hysteria2 | 239.5 | 657.6 | 22.23 | 0.0 | 8.49 | 14.21 | 19.04 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 82.64 | http | 302.4 | 811.2 | 20.78 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.15 |
| 82.54 | http | 306.4 | 835.2 | 20.68 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.9 |
| 82.51 | http | 308.1 | 846.2 | 20.65 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.23 |
| 82.38 | http | 313.6 | 865.5 | 20.52 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.8 |
| 82.35 | http | 314.8 | 862.5 | 20.49 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.19 |
| 82.25 | http | 319.1 | 867.9 | 20.39 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.11 |
| 82.17 | http | 322.7 | 865.5 | 20.31 | 0.0 | 10.0 | 14.88 | 19.98 | zhangkai | 156.146.59.25 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | 1.0 | 128 | 159 | prefer |
| Au1rxx-base64 | 0.928 | 0.861 | 468 | 1703 | prefer |
| Surfboard-tg-mixed | 0.855 | 0.783 | 69 | 5991 | prefer |
| DeltaKronecker-all | 0.622 | 0.545 | 22 | 4975 | observe |
| mheidari-all | 0.529 | 0.857 | 7 | 16743 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 5328 | observe |
| Epodonios-all | 0.255 | None | 0 | 6597 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7349 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4839 | observe |
| barry-far-vless | 0.255 | None | 0 | 5121 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5209 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.243 | None | 0 | 1703 | observe |
| nscl5-all | 0.234 | None | 0 | 1481 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 22 |
| speed | TimeoutError | - | 16 |
| geo | ClientOSError | - | 15 |
| speed | ClientOSError | - | 11 |
| cn-block | TimeoutError | - | 7 |
| 204 | ProxyError | - | 7 |
| geo | TimeoutError | - | 6 |
| cn-block | ClientOSError | - | 3 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
