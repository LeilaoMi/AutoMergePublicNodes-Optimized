# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-18 20:52:54 |
| 运行耗时 | 654.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 87619 |
| 去重后节点 | 25094 |
| TCP 可达 | 3000 |
| 真实可用 | 460 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25094 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| geo | 1.4 |
| tcp | 40.6 |
| probe | 290.5 |
| real_test | 236.3 |
| generate | 79.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52439 |
| vmess | 13862 |
| shadowsocks | 10579 |
| trojan | 8620 |
| hysteria2 | 1317 |
| http | 586 |
| shadowsocksr | 120 |
| socks | 72 |
| anytls | 11 |
| hysteria | 10 |
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
| 82.93 | hysteria2 | 247.4 | 685.9 | 22.05 | 0.0 | 10.0 | 14.17 | 19.2 | Au1rxx-base64 | 159.223.157.129 |
| 82.16 | vless | 229.5 | 594.6 | 22.47 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 195.123.235.177 |
| 81.89 | vless | 240.9 | 687.3 | 22.2 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 79.141.172.154 |
| 81.73 | vless | 247.9 | 641.3 | 22.04 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.35 |
| 81.05 | vless | 277.3 | 675.4 | 21.36 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.182 |
| 80.67 | shadowsocks | 241.8 | 666.3 | 22.18 | 0.0 | 10.0 | 13.29 | 19.2 | Au1rxx-base64 | 37.19.198.160 |
| 80.57 | vless | 297.9 | 671.8 | 20.88 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.235 |
| 80.17 | vless | 315.1 | 874.8 | 20.48 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 137.184.218.169 |
| 80.04 | vless | 320.7 | 811.4 | 20.35 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 66.70.179.198 |
| 80.04 | vless | 321.0 | 855.9 | 20.35 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.89 |
| 79.98 | vless | 323.6 | 851.8 | 20.29 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.212 |
| 79.8 | vless | 331.1 | 838.7 | 20.11 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.104 |
| 79.71 | vless | 334.9 | 908.1 | 20.02 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.16 |
| 79.61 | vless | 339.4 | 784.4 | 19.92 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.95 |
| 79.51 | vless | 343.6 | 874.5 | 19.82 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.163 |
| 79.38 | vless | 281.8 | 758.4 | 21.25 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.225 |
| 78.96 | vless | 367.5 | 1015.0 | 19.27 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 185.95.231.156 |
| 78.9 | vless | 284.0 | 632.7 | 21.2 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.74 |
| 78.76 | vless | 376.4 | 917.5 | 19.07 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.90 |
| 78.75 | vless | 376.7 | 899.3 | 19.06 | 0.0 | 10.0 | 10.49 | 19.2 | Au1rxx-base64 | 169.40.42.229 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.919 | 0.857 | 273 | 1615 | prefer |
| ermaozi | 0.828 | 0.84 | 25 | 325 | prefer |
| Surfboard-tg-mixed | 0.726 | 0.648 | 159 | 7333 | prefer |
| mheidari-all | 0.642 | 0.562 | 176 | 19747 | observe |
| mahdibland-V2RayAggregator | 0.335 | 1.0 | 1 | 4241 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5076 | observe |
| Epodonios-all | 0.255 | None | 0 | 7771 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8922 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5838 | observe |
| barry-far-vless | 0.255 | None | 0 | 6051 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.24 | None | 0 | 1615 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | ClientOSError | - | 42 |
| geo | ClientOSError | - | 39 |
| 204 | TimeoutError | - | 28 |
| 204 | ProxyError | - | 20 |
| cn-block | TimeoutError | - | 20 |
| geo | TimeoutError | - | 14 |
| speed | ClientOSError | - | 12 |
| 204 | ClientOSError | - | 5 |
| speed | TimeoutError | - | 5 |
| geo | ProxyError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
