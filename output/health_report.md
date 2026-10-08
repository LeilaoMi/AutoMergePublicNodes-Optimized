# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-08 05:43:24 |
| 运行耗时 | 843.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 99165 |
| 去重后节点 | 27686 |
| TCP 可达 | 3000 |
| 真实可用 | 415 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27686 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| geo | 1.5 |
| tcp | 46.9 |
| probe | 299.9 |
| real_test | 411.4 |
| generate | 76.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 57994 |
| vmess | 15811 |
| shadowsocks | 11970 |
| trojan | 10834 |
| hysteria2 | 1571 |
| http | 676 |
| shadowsocksr | 167 |
| socks | 88 |
| anytls | 29 |
| hysteria | 16 |
| tuic | 9 |

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
| 83.28 | hysteria2 | 245.8 | 683.7 | 22.09 | 0.0 | 10.0 | 13.89 | 18.8 | Au1rxx-base64 | 129.213.91.185 |
| 82.46 | vless | 252.8 | 689.0 | 21.93 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 159.89.87.21 |
| 82.45 | vless | 253.1 | 662.5 | 21.92 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.89 |
| 82.21 | vless | 263.4 | 651.2 | 21.68 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.35 |
| 81.73 | vless | 284.3 | 633.2 | 21.2 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.133 |
| 81.71 | vless | 285.1 | 721.7 | 21.18 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 66.70.179.198 |
| 81.64 | vless | 288.1 | 732.1 | 21.11 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 2.24.124.64 |
| 81.62 | vless | 288.8 | 716.9 | 21.09 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.90 |
| 81.45 | vless | 265.4 | 695.4 | 21.63 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.184 |
| 81.03 | vless | 314.3 | 734.1 | 20.5 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.163 |
| 80.9 | vless | 319.9 | 861.8 | 20.37 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.225 |
| 80.81 | vless | 324.1 | 831.4 | 20.28 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.231 |
| 80.58 | shadowsocks | 253.8 | 711.0 | 21.9 | 0.0 | 10.0 | 13.88 | 18.8 | Au1rxx-base64 | 37.19.198.160 |
| 80.51 | vless | 336.9 | 867.8 | 19.98 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.229 |
| 80.29 | vless | 285.3 | 648.0 | 21.17 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.104 |
| 80.29 | hysteria2 | 392.1 | 758.6 | 18.7 | 0.0 | 10.0 | 13.89 | 18.8 | Au1rxx-base64 | 159.223.157.129 |
| 79.8 | vless | 361.7 | 916.5 | 19.4 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 209.200.246.148 |
| 79.8 | vless | 367.7 | 832.6 | 19.27 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.74 |
| 79.79 | vless | 320.1 | 706.1 | 20.37 | 0.0 | 10.0 | 11.73 | 18.8 | Au1rxx-base64 | 169.40.42.224 |
| 79.76 | shadowsocks | 267.7 | 766.1 | 21.58 | 0.0 | 10.0 | 13.88 | 18.8 | Au1rxx-base64 | 15.204.246.132 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | 0.908 | 303 | 1772 | prefer |
| ermaozi-get_subscribe | 0.539 | 0.516 | 31 | 592 | observe |
| Surfboard-tg-mixed | 0.446 | 0.625 | 8 | 7193 | observe |
| ermaozi | 0.433 | 0.4 | 40 | 715 | observe |
| mheidari-all | 0.342 | 0.261 | 387 | 23407 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 7663 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9552 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5725 | observe |
| barry-far-vless | 0.255 | None | 0 | 5963 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4431 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.246 | None | 0 | 1772 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 157 |
| speed | TimeoutError | - | 58 |
| 204 | ProxyError | - | 40 |
| geo | ClientOSError | - | 38 |
| speed | ClientOSError | - | 24 |
| 204 | ProxyConnectionError | - | 21 |
| cn-block | TimeoutError | - | 17 |
| 204 | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
