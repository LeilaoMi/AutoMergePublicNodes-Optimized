# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-11-17 08:11:25 |
| 运行耗时 | 264.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 87 |
| 原始节点 | 83224 |
| 去重后节点 | 27691 |
| TCP 可达 | 3000 |
| 真实可用 | 445 |
| Verified 输出 | 50 |
| Global 输出 | 300 |
| All 输出 | 27691 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| geo | 1.3 |
| tcp | 69.8 |
| probe | 67.7 |
| real_test | 78.7 |
| china_check | 34.3 |
| write_verified | 0.0 |
| generate | 8.5 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49683 |
| vmess | 14822 |
| shadowsocks | 9746 |
| trojan | 6952 |
| hysteria2 | 1504 |
| http | 250 |
| shadowsocksr | 151 |
| socks | 69 |
| hysteria | 19 |
| tuic | 16 |
| anytls | 12 |

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
| 95.7 | trojan | 241.8 | 0.3 | 22.18 | 14.99 | 8.09 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.114.245 |
| 95.69 | trojan | 322.2 | 2.0 | 20.32 | 14.93 | 10.0 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.114.132 |
| 95.58 | trojan | 242.9 | 0.1 | 22.15 | 15.0 | 7.99 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.114.166 |
| 95.39 | trojan | 251.1 | 0.3 | 21.96 | 14.99 | 8.0 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.114.106 |
| 94.59 | trojan | 241.9 | 0.7 | 22.18 | 14.97 | 8.0 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.114.114 |
| 94.0 | trojan | 243.8 | 0.0 | 22.13 | 15.0 | 7.91 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.114.126 |
| 93.87 | trojan | 244.1 | 1.4 | 22.13 | 14.95 | 10.0 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.114.45 |
| 93.59 | trojan | 290.8 | 0.1 | 21.05 | 15.0 | 10.0 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.112.121 |
| 93.33 | trojan | 208.2 | 2.2 | 22.96 | 14.92 | 6.01 | 14.38 | 18.56 | Au1rxx-base64 | 216.106.186.32 |
| 92.61 | trojan | 216.3 | 1.6 | 22.77 | 14.94 | 4.46 | 14.38 | 18.56 | Au1rxx-base64 | 216.106.186.33 |
| 91.92 | vless | 260.3 | 0.8 | 21.75 | 14.97 | 7.72 | 12.03 | 18.56 | Au1rxx-base64 | 45.63.53.81 |
| 90.78 | trojan | 290.5 | 1.4 | 21.05 | 14.95 | 9.85 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.112.242 |
| 90.55 | shadowsocks | 343.0 | 0.5 | 19.84 | 14.98 | 10.0 | 13.79 | 18.56 | Au1rxx-base64 | 95.215.201.18 |
| 89.81 | trojan | 209.0 | 3.5 | 22.94 | 14.87 | 1.56 | 14.38 | 18.56 | Au1rxx-base64 | resources.findlocaljobnetworkandbuildcommunityconnections.com |
| 89.69 | trojan | 289.7 | 1.1 | 21.07 | 14.96 | 6.48 | 14.38 | 18.56 | Au1rxx-base64 | 66.163.112.142 |
| 88.96 | shadowsocks | 322.1 | 1.9 | 20.32 | 14.93 | 10.0 | 13.79 | 18.56 | Au1rxx-base64 | 156.146.38.170 |
| 88.94 | shadowsocks | 321.2 | 0.3 | 20.34 | 14.99 | 10.0 | 13.79 | 18.56 | Au1rxx-base64 | 156.146.38.167 |
| 88.83 | shadowsocks | 326.2 | 0.9 | 20.23 | 14.97 | 10.0 | 13.79 | 18.56 | Au1rxx-base64 | 156.146.38.168 |
| 87.38 | trojan | 238.6 | 0.1 | 22.25 | 15.0 | 0.0 | 14.38 | 19.34 | mheidari-all | 96.44.133.37 |
| 87.05 | trojan | 197.4 | 4.0 | 23.21 | 14.85 | 1.55 | 14.38 | 18.56 | Au1rxx-base64 | www.findlocaljobnetworkandbuildcommunityconnections.com |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.898 | 0.82 | 245 | 8623 | prefer |
| mheidari-all | 0.892 | 0.821 | 78 | 14792 | prefer |
| ermaozi | 0.889 | 0.873 | 79 | 621 | prefer |
| Au1rxx-base64 | 0.832 | 0.766 | 141 | 1751 | prefer |
| Surfboard-tg-vless | 0.4 | 0.75 | 4 | 6028 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| tg-LonUp_M | 0.327 | 0.75 | 4 | 169 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4964 | observe |
| DeltaKronecker-all | 0.255 | None | 0 | 2915 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| Pawdroid | 0.255 | 1.0 | 1 | 12 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 11532 | observe |
| barry-far-vless | 0.255 | None | 0 | 6053 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4545 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 60 |
| 204 | ProxyError | - | 16 |
| 204 | TimeoutError | - | 8 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 3 |
| speed | ClientOSError | - | 2 |
| speed | ClientPayloadError | - | 1 |
| geo | ClientOSError | - | 1 |
| cn-block | TimeoutError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 27 | 50 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
