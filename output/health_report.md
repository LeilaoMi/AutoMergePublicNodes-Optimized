# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-20 05:06:01 |
| 运行耗时 | 311.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 94570 |
| 去重后节点 | 26219 |
| TCP 可达 | 3000 |
| 真实可用 | 437 |
| Verified 输出 | 91 |
| Global 输出 | 300 |
| All 输出 | 26219 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.3 |
| geo | 1.5 |
| tcp | 82.0 |
| probe | 93.2 |
| real_test | 80.6 |
| china_check | 32.2 |
| write_verified | 0.1 |
| generate | 13.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56615 |
| vmess | 16985 |
| shadowsocks | 11208 |
| trojan | 7998 |
| hysteria2 | 1194 |
| http | 277 |
| shadowsocksr | 168 |
| socks | 68 |
| anytls | 34 |
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
| 94.16 | shadowsocks | 239.9 | 1.0 | 22.22 | 14.96 | 9.46 | 13.48 | 18.04 | Au1rxx-base64 | 156.146.38.168 |
| 93.87 | shadowsocks | 244.5 | 6.6 | 22.12 | 14.75 | 9.48 | 13.48 | 18.04 | Au1rxx-base64 | 156.146.38.167 |
| 92.17 | hysteria2 | 247.0 | 2.0 | 22.06 | 14.92 | 9.29 | 13.33 | 18.04 | Au1rxx-base64 | 179.255.104.98 |
| 91.54 | shadowsocks | 244.7 | 1.5 | 22.11 | 14.94 | 6.97 | 13.48 | 18.04 | Au1rxx-base64 | 156.146.38.169 |
| 91.37 | trojan | 398.2 | 9.4 | 18.56 | 14.65 | 9.24 | 13.88 | 18.04 | Au1rxx-base64 | 66.23.203.21 |
| 90.76 | vless | 251.9 | 1.6 | 21.95 | 14.94 | 7.08 | 11.01 | 18.04 | Au1rxx-base64 | 45.63.53.81 |
| 89.64 | vless | 246.2 | 3.1 | 22.08 | 14.88 | 6.06 | 11.01 | 18.04 | Au1rxx-base64 | 144.202.126.147 |
| 88.33 | shadowsocks | 291.6 | 2.0 | 21.03 | 14.93 | 9.21 | 13.48 | 18.04 | Au1rxx-base64 | 173.244.56.9 |
| 88.15 | shadowsocks | 336.3 | 1.1 | 19.99 | 14.96 | 9.01 | 13.48 | 18.04 | Au1rxx-base64 | 37.19.198.243 |
| 88.04 | vless | 328.7 | 5.9 | 20.17 | 14.78 | 6.94 | 11.01 | 18.04 | Au1rxx-base64 | 208.84.100.209 |
| 88.01 | shadowsocks | 333.7 | 3.2 | 20.05 | 14.88 | 9.27 | 13.48 | 18.04 | Au1rxx-base64 | 37.19.198.236 |
| 87.74 | vless | 462.8 | 2.8 | 17.07 | 14.9 | 8.92 | 11.01 | 18.04 | Au1rxx-base64 | 51.81.203.63 |
| 87.26 | shadowsocks | 314.7 | 0.5 | 20.49 | 14.98 | 9.04 | 13.48 | 18.04 | Au1rxx-base64 | 149.22.95.183 |
| 87.23 | vless | 258.0 | 0.1 | 21.81 | 15.0 | 9.04 | 11.01 | 18.04 | Au1rxx-base64 | 181.214.152.137 |
| 86.97 | shadowsocks | 344.5 | 1.1 | 19.8 | 14.96 | 9.26 | 13.48 | 18.04 | Au1rxx-base64 | 15.204.233.41 |
| 86.92 | vless | 370.9 | 1.4 | 19.19 | 14.95 | 8.54 | 11.01 | 18.04 | Au1rxx-base64 | 167.17.69.171 |
| 86.83 | vless | 304.3 | 12.6 | 20.73 | 14.53 | 6.95 | 11.01 | 18.04 | Au1rxx-base64 | 154.9.241.170 |
| 86.71 | vless | 377.2 | 3.8 | 19.05 | 14.86 | 8.56 | 11.01 | 18.04 | Au1rxx-base64 | 66.70.179.198 |
| 85.95 | vless | 270.2 | 2.8 | 21.52 | 14.9 | 8.84 | 11.01 | 18.04 | Au1rxx-base64 | 104.225.239.122 |
| 85.72 | vless | 278.7 | 8.4 | 21.33 | 14.69 | 8.31 | 11.01 | 18.04 | Au1rxx-base64 | 131.143.180.87 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.948 | 0.943 | 53 | 510 | prefer |
| Au1rxx-base64 | 0.926 | 0.872 | 288 | 1418 | prefer |
| zhangkai | 0.923 | 1.0 | 19 | 27 | prefer |
| DeltaKronecker-all | 0.913 | 0.844 | 64 | 3294 | prefer |
| Surfboard-tg-mixed | 0.624 | 0.818 | 11 | 6911 | observe |
| mheidari-all | 0.482 | 0.4 | 125 | 23317 | observe |
| SoliSpirit-all | 0.391 | 1.0 | 2 | 10162 | observe |
| 10ium-HighSpeed | 0.345 | 1.0 | 2 | 839 | observe |
| roosterkid-openproxylist-v2ray | 0.317 | 1.0 | 2 | 150 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 172 | observe |
| tg-oneclickvpnkeys | 0.258 | 1.0 | 1 | 81 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4940 | observe |
| Epodonios-all | 0.255 | None | 0 | 7379 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5515 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 82 |
| geo | ClientOSError | - | 18 |
| speed | ClientOSError | - | 11 |
| cn-block | ClientOSError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| 204 | ProxyError | - | 4 |
| 204 | TimeoutError | - | 3 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 38 | 91 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
