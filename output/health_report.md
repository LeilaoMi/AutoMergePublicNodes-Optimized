# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-16 06:34:50 |
| 运行耗时 | 324.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99735 |
| 去重后节点 | 27902 |
| TCP 可达 | 3000 |
| 真实可用 | 494 |
| Verified 输出 | 34 |
| Global 输出 | 300 |
| All 输出 | 27902 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.0 |
| geo | 1.5 |
| tcp | 86.2 |
| probe | 93.4 |
| real_test | 97.2 |
| china_check | 24.0 |
| write_verified | 0.0 |
| generate | 14.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58860 |
| vmess | 16449 |
| shadowsocks | 11805 |
| trojan | 10395 |
| hysteria2 | 1211 |
| http | 740 |
| shadowsocksr | 168 |
| socks | 59 |
| anytls | 25 |
| hysteria | 17 |
| tuic | 6 |

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
| 94.17 | shadowsocks | 250.7 | 0.2 | 21.97 | 14.99 | 10.0 | 13.65 | 17.56 | Au1rxx-base64 | 37.19.198.160 |
| 94.05 | shadowsocks | 255.5 | 0.4 | 21.86 | 14.98 | 10.0 | 13.65 | 17.56 | Au1rxx-base64 | 37.19.198.243 |
| 93.92 | shadowsocks | 238.4 | 1.2 | 22.26 | 14.95 | 10.0 | 13.65 | 17.56 | Au1rxx-base64 | 15.204.233.41 |
| 92.34 | shadowsocks | 306.1 | 1.6 | 20.69 | 14.94 | 10.0 | 13.65 | 17.56 | Au1rxx-base64 | 51.222.136.236 |
| 92.2 | vless | 335.6 | 0.4 | 20.01 | 14.98 | 9.76 | 9.89 | 17.56 | Au1rxx-base64 | 169.40.42.90 |
| 91.51 | shadowsocks | 277.6 | 0.2 | 21.35 | 14.99 | 10.0 | 13.65 | 17.56 | Au1rxx-base64 | 156.146.38.168 |
| 91.42 | vless | 262.6 | 3.8 | 21.7 | 14.86 | 7.41 | 9.89 | 17.56 | Au1rxx-base64 | 167.17.69.171 |
| 91.09 | vless | 263.0 | 1.4 | 21.69 | 14.95 | 10.0 | 9.89 | 17.56 | Au1rxx-base64 | 169.40.42.225 |
| 90.54 | shadowsocks | 317.2 | 0.1 | 20.44 | 15.0 | 10.0 | 13.65 | 17.56 | Au1rxx-base64 | 156.146.38.169 |
| 89.09 | vless | 368.3 | 0.2 | 19.25 | 14.99 | 7.4 | 9.89 | 17.56 | Au1rxx-base64 | 185.95.231.156 |
| 89.07 | vless | 277.4 | 1.2 | 21.36 | 14.96 | 5.3 | 9.89 | 17.56 | Au1rxx-base64 | 195.123.235.183 |
| 89.07 | vless | 338.2 | 2.6 | 19.95 | 14.9 | 9.77 | 9.89 | 17.56 | Au1rxx-base64 | 169.40.42.232 |
| 88.95 | shadowsocks | 255.9 | 2.9 | 21.85 | 14.89 | 10.0 | 13.65 | 17.56 | Au1rxx-base64 | 37.19.198.236 |
| 88.61 | vless | 281.3 | 4.4 | 21.27 | 14.83 | 5.06 | 9.89 | 17.56 | Au1rxx-base64 | 66.70.179.198 |
| 88.27 | hysteria2 | 259.4 | 2.5 | 21.77 | 14.91 | 10.0 | 9.71 | 17.56 | Au1rxx-base64 | 179.255.104.98 |
| 88.0 | vless | 299.9 | 2.5 | 20.84 | 14.91 | 9.77 | 9.89 | 17.56 | Au1rxx-base64 | 169.40.42.104 |
| 87.84 | vless | 295.0 | 6.1 | 20.95 | 14.77 | 7.67 | 9.89 | 17.56 | Au1rxx-base64 | 169.40.42.74 |
| 87.43 | vless | 280.2 | 5.1 | 21.29 | 14.81 | 7.67 | 9.89 | 17.56 | Au1rxx-base64 | 169.40.42.182 |
| 86.71 | vless | 305.0 | 11.2 | 20.72 | 14.58 | 7.65 | 9.89 | 17.56 | Au1rxx-base64 | 67.220.73.204 |
| 86.7 | http | 328.1 | 0.2 | 20.18 | 14.99 | 0.0 | 14.35 | 19.68 | ermaozi | 172.64.68.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.989 | 89 | 693 | prefer |
| Au1rxx-base64 | 0.887 | 0.809 | 470 | 1992 | prefer |
| Surfboard-tg-mixed | 0.4 | 0.75 | 4 | 7054 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| mheidari-all | 0.276 | 0.191 | 110 | 23985 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 79 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5024 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1992 | observe |
| Epodonios-all | 0.255 | None | 0 | 7651 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3999 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 10060 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5573 | observe |
| barry-far-vless | 0.255 | None | 0 | 5882 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4265 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 111 |
| geo | ClientOSError | - | 23 |
| speed | ClientOSError | - | 20 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| 204 | ClientOSError | - | 5 |
| 204 | ProxyError | - | 5 |
| cn-block | ProxyError | - | 4 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 18 | 34 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
