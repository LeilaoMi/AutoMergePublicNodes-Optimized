# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-31 22:45:42 |
| 运行耗时 | 271.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 78460 |
| 去重后节点 | 22374 |
| TCP 可达 | 3000 |
| 真实可用 | 639 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22374 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| geo | 1.4 |
| tcp | 35.1 |
| probe | 87.8 |
| real_test | 112.1 |
| generate | 29.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49181 |
| vmess | 11016 |
| shadowsocks | 10016 |
| trojan | 6180 |
| hysteria2 | 1715 |
| http | 142 |
| shadowsocksr | 121 |
| socks | 75 |
| hysteria | 7 |
| tuic | 7 |

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
| 84.74 | vless | 251.3 | 658.4 | 21.96 | 0.0 | 10.0 | 12.78 | 20.0 | Au1rxx-base64 | 79.127.243.217 |
| 83.86 | vless | 273.3 | 636.9 | 21.45 | 0.0 | 10.0 | 12.78 | 20.0 | Au1rxx-base64 | 195.211.99.45 |
| 83.44 | vless | 307.6 | 828.6 | 20.66 | 0.0 | 10.0 | 12.78 | 20.0 | Au1rxx-base64 | 204.48.20.223 |
| 83.25 | vless | 315.6 | 846.4 | 20.47 | 0.0 | 10.0 | 12.78 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 82.67 | vless | 340.9 | 850.5 | 19.89 | 0.0 | 10.0 | 12.78 | 20.0 | Au1rxx-base64 | 169.40.42.168 |
| 82.58 | vless | 290.0 | 624.6 | 21.06 | 0.0 | 10.0 | 12.78 | 18.74 | mheidari-all | 169.40.42.184 |
| 81.39 | vless | 261.9 | 671.5 | 21.71 | 0.0 | 10.0 | 12.78 | 16.9 | Surfboard-tg-mixed | 167.17.69.171 |
| 81.23 | vless | 308.3 | 745.0 | 20.64 | 0.0 | 10.0 | 12.78 | 18.74 | mheidari-all | 169.40.42.89 |
| 80.98 | vless | 280.0 | 715.9 | 21.3 | 0.0 | 10.0 | 12.78 | 16.9 | Surfboard-tg-mixed | 169.40.42.104 |
| 80.86 | vless | 331.1 | 796.4 | 20.11 | 0.0 | 10.0 | 12.78 | 18.74 | mheidari-all | 66.70.179.198 |
| 80.43 | shadowsocks | 243.9 | 654.6 | 22.13 | 0.0 | 10.0 | 13.56 | 18.74 | mheidari-all | 37.19.198.160 |
| 80.37 | shadowsocks | 246.6 | 650.8 | 22.07 | 0.0 | 10.0 | 13.56 | 18.74 | mheidari-all | 37.19.198.244 |
| 80.34 | vless | 266.0 | 653.4 | 21.62 | 0.0 | 10.0 | 12.78 | 16.9 | Surfboard-tg-mixed | 172.105.104.54 |
| 80.29 | shadowsocks | 304.3 | 783.8 | 20.73 | 0.0 | 10.0 | 13.56 | 20.0 | Au1rxx-base64 | ca225.vpnbook.com |
| 80.2 | vless | 265.3 | 675.3 | 21.64 | 0.0 | 10.0 | 12.78 | 18.74 | mheidari-all | 169.40.42.74 |
| 79.67 | vless | 401.2 | 958.5 | 18.49 | 0.0 | 10.0 | 12.78 | 18.74 | mheidari-all | 169.40.42.235 |
| 79.6 | vless | 371.5 | 1023.4 | 19.18 | 0.0 | 10.0 | 12.78 | 18.74 | mheidari-all | 45.138.100.226 |
| 79.28 | shadowsocks | 293.7 | 805.3 | 20.98 | 0.0 | 10.0 | 13.56 | 18.74 | mheidari-all | 37.19.198.236 |
| 79.16 | vless | 358.5 | 828.6 | 19.48 | 0.0 | 10.0 | 12.78 | 16.9 | Surfboard-tg-mixed | 169.40.42.15 |
| 79.13 | vless | 275.2 | 642.6 | 21.41 | 0.0 | 10.0 | 12.78 | 16.9 | DeltaKronecker-all | 195.211.99.49 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.975 | 0.901 | 151 | 7016 | prefer |
| Au1rxx-base64 | 0.972 | 0.927 | 289 | 1182 | prefer |
| mheidari-all | 0.928 | 0.852 | 189 | 14929 | prefer |
| DeltaKronecker-all | 0.898 | 0.828 | 64 | 5904 | prefer |
| zhangkai | 0.852 | 0.875 | 24 | 144 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4657 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7470 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5879 | observe |
| barry-far-vless | 0.255 | None | 0 | 6031 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4025 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.222 | None | 0 | 1182 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 18 |
| cn-block | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 10 |
| speed | ClientOSError | - | 8 |
| 204 | ProxyError | - | 6 |
| 204 | ProxyConnectionError | - | 5 |
| speed | TimeoutError | - | 5 |
| 204 | ClientOSError | - | 4 |
| 204 | TimeoutError | - | 4 |
| cn-block | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
