# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-28 04:24:45 |
| 运行耗时 | 260.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 105 |
| 原始节点 | 76091 |
| 去重后节点 | 23164 |
| TCP 可达 | 3000 |
| 真实可用 | 547 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23164 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.5 |
| geo | 1.4 |
| tcp | 31.1 |
| probe | 57.0 |
| real_test | 133.9 |
| generate | 33.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42282 |
| trojan | 12751 |
| vmess | 11173 |
| shadowsocks | 9318 |
| hysteria2 | 226 |
| shadowsocksr | 155 |
| http | 135 |
| socks | 43 |
| hysteria | 6 |
| tuic | 2 |

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
| 75.28 | shadowsocks | 246.9 | 609.4 | 22.06 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 156.146.38.167 |
| 74.98 | shadowsocks | 258.6 | 636.6 | 21.79 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 156.146.38.170 |
| 74.92 | shadowsocks | 262.5 | 653.7 | 21.7 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 37.19.198.160 |
| 74.91 | shadowsocks | 263.0 | 662.4 | 21.69 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 37.19.198.236 |
| 74.88 | shadowsocks | 264.5 | 665.4 | 21.66 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 37.19.198.243 |
| 74.22 | shadowsocks | 292.9 | 743.8 | 21.0 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 156.146.38.168 |
| 73.6 | shadowsocks | 276.2 | 685.5 | 21.38 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 37.19.198.244 |
| 73.4 | vmess | 349.9 | 902.0 | 19.68 | 0.0 | 10.0 | 12.86 | 15.36 | Surfboard-tg-mixed | 67.220.85.46 |
| 73.0 | vless | 315.4 | 743.4 | 20.48 | 0.0 | 10.0 | 9.27 | 15.36 | Surfboard-tg-mixed | 15.223.121.250 |
| 72.71 | shadowsocks | 336.6 | 982.3 | 19.99 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 172.234.202.34 |
| 72.19 | vless | 296.9 | 751.8 | 20.9 | 0.0 | 10.0 | 9.27 | 12.02 | mheidari-all | 47.253.226.114 |
| 71.42 | shadowsocks | 246.1 | 613.9 | 22.08 | 0.0 | 10.0 | 11.32 | 12.02 | mheidari-all | 198.98.53.130 |
| 71.07 | vless | 349.3 | 869.2 | 19.69 | 0.0 | 10.0 | 9.27 | 15.9 | Au1rxx-base64 | 159.89.87.21 |
| 70.18 | shadowsocks | 278.3 | 679.3 | 21.34 | 0.0 | 10.0 | 11.32 | 12.02 | mheidari-all | 108.181.57.93 |
| 69.71 | shadowsocks | 293.4 | 543.5 | 20.99 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 173.244.56.9 |
| 69.61 | vless | 342.0 | 860.7 | 19.86 | 0.0 | 10.0 | 9.27 | 10.48 | DeltaKronecker-all | 152.53.171.40 |
| 68.89 | vless | 406.0 | 884.1 | 18.38 | 0.0 | 10.0 | 9.27 | 15.9 | Au1rxx-base64 | 15.204.97.219 |
| 68.72 | vless | 355.5 | 888.6 | 19.55 | 0.0 | 10.0 | 9.27 | 15.36 | Surfboard-tg-mixed | 137.184.218.169 |
| 68.54 | vless | 407.9 | 896.0 | 18.34 | 0.0 | 10.0 | 9.27 | 15.9 | Au1rxx-base64 | 15.204.97.214 |
| 68.28 | shadowsocks | 331.0 | 711.1 | 20.12 | 0.0 | 10.0 | 11.32 | 15.9 | Au1rxx-base64 | 173.244.56.6 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| Surfboard-tg-mixed | 0.866 | 0.789 | 279 | 5004 | prefer |
| Au1rxx-base64 | 0.744 | 0.746 | 67 | 117 | prefer |
| mheidari-all | 0.686 | 0.607 | 178 | 16017 | observe |
| DeltaKronecker-all | 0.37 | 0.289 | 450 | 6822 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4579 | observe |
| Epodonios-all | 0.255 | None | 0 | 7564 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3980 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7009 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3679 | observe |
| barry-far-vless | 0.255 | None | 0 | 4479 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5287 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 189 |
| speed | ClientOSError | - | 150 |
| geo | ClientOSError | - | 48 |
| cn-block | TimeoutError | - | 31 |
| cn-block | ClientOSError | - | 10 |
| speed | TimeoutError | - | 9 |
| 204 | ClientOSError | - | 9 |
| 204 | TimeoutError | - | 9 |
| 204 | ProxyError | - | 7 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
