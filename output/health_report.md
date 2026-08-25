# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-25 13:00:23 |
| 运行耗时 | 254.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 78389 |
| 去重后节点 | 22412 |
| TCP 可达 | 3000 |
| 真实可用 | 580 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22412 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| geo | 1.4 |
| tcp | 36.3 |
| probe | 54.5 |
| real_test | 112.9 |
| generate | 43.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48617 |
| shadowsocks | 10762 |
| vmess | 10462 |
| trojan | 6680 |
| hysteria2 | 1494 |
| http | 164 |
| shadowsocksr | 133 |
| socks | 67 |
| hysteria | 7 |
| tuic | 3 |

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
| 81.22 | vless | 249.3 | 689.6 | 22.01 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 47.89.186.170 |
| 81.2 | vless | 250.2 | 657.1 | 21.99 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 167.17.69.171 |
| 80.58 | vless | 276.9 | 734.6 | 21.37 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.232 |
| 79.88 | hysteria2 | 280.8 | 785.0 | 21.28 | 0.0 | 10.0 | 13.64 | 16.06 | mheidari-all | 159.223.157.129 |
| 79.84 | vless | 308.9 | 696.5 | 20.63 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.35 |
| 79.83 | vless | 294.6 | 728.9 | 20.96 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.212 |
| 79.77 | vless | 311.8 | 869.3 | 20.56 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 79.127.243.217 |
| 79.68 | vless | 300.8 | 744.7 | 20.81 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.225 |
| 79.56 | shadowsocks | 281.1 | 783.0 | 21.27 | 0.0 | 10.0 | 13.79 | 18.5 | Au1rxx-base64 | 37.19.198.236 |
| 79.36 | vless | 329.5 | 847.5 | 20.15 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.75 |
| 79.2 | vless | 336.4 | 879.9 | 19.99 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.104 |
| 79.2 | vless | 336.6 | 915.7 | 19.99 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.16 |
| 79.1 | vless | 340.9 | 918.9 | 19.89 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.133 |
| 78.96 | vless | 346.7 | 974.2 | 19.75 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 137.184.218.169 |
| 78.82 | vless | 352.9 | 979.0 | 19.61 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 185.95.231.156 |
| 78.3 | shadowsocks | 314.0 | 865.5 | 20.51 | 0.0 | 10.0 | 13.79 | 18.5 | Au1rxx-base64 | 38.180.135.156 |
| 78.27 | vless | 291.9 | 649.4 | 21.02 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.231 |
| 78.01 | vless | 305.2 | 755.1 | 20.71 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 169.40.42.229 |
| 77.94 | vless | 391.1 | 941.7 | 18.73 | 0.0 | 10.0 | 10.71 | 18.5 | Au1rxx-base64 | 66.70.179.198 |
| 77.68 | shadowsocks | 246.1 | 630.3 | 22.08 | 0.0 | 10.0 | 13.79 | 16.06 | mheidari-all | 155.138.136.240 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | 1.0 | 24 | 144 | prefer |
| mheidari-all | 0.933 | 0.863 | 73 | 14402 | prefer |
| Au1rxx-base64 | 0.915 | 0.853 | 389 | 1581 | prefer |
| Surfboard-tg-mixed | 0.825 | 0.748 | 155 | 6520 | prefer |
| DeltaKronecker-all | 0.822 | 0.75 | 60 | 6340 | prefer |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4912 | observe |
| Epodonios-all | 0.255 | None | 0 | 7010 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3987 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7084 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5377 | observe |
| barry-far-vless | 0.255 | None | 0 | 5577 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4119 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1589 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 24 |
| 204 | TimeoutError | - | 23 |
| cn-block | TimeoutError | - | 22 |
| speed | TimeoutError | - | 14 |
| speed | ClientOSError | - | 10 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 7 |
| 204 | ProxyError | - | 5 |
| geo | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
