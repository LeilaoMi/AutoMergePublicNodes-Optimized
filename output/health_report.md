# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-24 04:52:51 |
| 运行耗时 | 309.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 86 |
| 原始节点 | 92457 |
| 去重后节点 | 24506 |
| TCP 可达 | 3000 |
| 真实可用 | 449 |
| Verified 输出 | 161 |
| Global 输出 | 300 |
| All 输出 | 24506 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.5 |
| tcp | 77.1 |
| probe | 91.4 |
| real_test | 88.7 |
| china_check | 32.7 |
| write_verified | 0.1 |
| generate | 11.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56140 |
| vmess | 16720 |
| shadowsocks | 11876 |
| trojan | 5854 |
| hysteria2 | 1348 |
| http | 254 |
| shadowsocksr | 166 |
| socks | 52 |
| anytls | 24 |
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
| 94.88 | vless | 209.4 | 0.4 | 22.93 | 14.98 | 9.44 | 10.33 | 17.2 | Au1rxx-base64 | 195.123.240.65 |
| 94.61 | vless | 214.7 | 0.7 | 22.81 | 14.97 | 9.41 | 10.33 | 17.2 | Au1rxx-base64 | 216.167.126.97 |
| 94.37 | vless | 197.5 | 1.7 | 23.21 | 14.94 | 8.69 | 10.33 | 17.2 | Au1rxx-base64 | 45.63.53.81 |
| 94.35 | vless | 196.0 | 3.0 | 23.24 | 14.89 | 8.69 | 10.33 | 17.2 | Au1rxx-base64 | 144.202.126.147 |
| 93.41 | shadowsocks | 257.0 | 0.1 | 21.83 | 15.0 | 9.29 | 14.09 | 17.2 | Au1rxx-base64 | 156.146.38.169 |
| 93.29 | shadowsocks | 259.3 | 1.8 | 21.78 | 14.93 | 9.29 | 14.09 | 17.2 | Au1rxx-base64 | 156.146.38.168 |
| 92.73 | shadowsocks | 285.2 | 0.1 | 21.18 | 15.0 | 9.26 | 14.09 | 17.2 | Au1rxx-base64 | 156.146.38.170 |
| 92.47 | shadowsocks | 262.3 | 2.6 | 21.71 | 14.9 | 9.27 | 14.09 | 17.2 | Au1rxx-base64 | 156.146.38.167 |
| 92.13 | shadowsocks | 256.8 | 4.5 | 21.83 | 14.83 | 9.48 | 14.09 | 17.2 | Au1rxx-base64 | 173.244.56.9 |
| 92.07 | vless | 207.6 | 3.5 | 22.97 | 14.87 | 8.59 | 10.33 | 17.2 | Au1rxx-base64 | 154.40.55.185 |
| 91.99 | vless | 205.8 | 12.4 | 23.01 | 14.53 | 6.92 | 10.33 | 17.2 | Au1rxx-base64 | 45.76.172.197 |
| 91.23 | vless | 232.4 | 14.9 | 22.4 | 14.44 | 6.86 | 10.33 | 17.2 | Au1rxx-base64 | 47.251.108.158 |
| 90.49 | vless | 207.3 | 0.0 | 22.98 | 15.0 | 4.98 | 10.33 | 17.2 | Au1rxx-base64 | 172.236.227.60 |
| 89.48 | vless | 241.6 | 21.5 | 22.19 | 14.19 | 5.57 | 10.33 | 17.2 | Au1rxx-base64 | 45.32.69.110 |
| 89.47 | shadowsocks | 231.6 | 1.2 | 22.42 | 14.96 | 9.0 | 14.09 | 17.2 | Au1rxx-base64 | 173.244.56.6 |
| 89.32 | shadowsocks | 298.3 | 2.6 | 20.87 | 14.9 | 9.12 | 14.09 | 17.2 | Au1rxx-base64 | 149.22.95.183 |
| 88.31 | vless | 334.1 | 7.5 | 20.04 | 14.72 | 9.17 | 10.33 | 17.2 | Au1rxx-base64 | 44.248.233.99 |
| 87.68 | http | 199.8 | 2.3 | 23.15 | 14.91 | 0.0 | 13.68 | 18.94 | ermaozi | 138.199.35.197 |
| 87.62 | http | 197.5 | 5.6 | 23.21 | 14.79 | 0.0 | 13.68 | 18.94 | ermaozi | 138.199.35.214 |
| 87.61 | http | 219.2 | 5.7 | 22.7 | 14.79 | 0.0 | 13.68 | 18.94 | ermaozi | 172.64.68.89 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | 0.987 | 79 | 608 | prefer |
| Au1rxx-base64 | 0.958 | 0.9 | 270 | 1532 | prefer |
| Surfboard-tg-mixed | 0.942 | 0.875 | 56 | 7159 | prefer |
| mheidari-all | 0.469 | 0.387 | 173 | 23800 | observe |
| roosterkid-openproxylist-v2ray | 0.406 | 1.0 | 4 | 150 | observe |
| SoliSpirit-all | 0.349 | 0.667 | 3 | 10227 | observe |
| 10ium-HighSpeed | 0.345 | 1.0 | 2 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.287 | 0.5 | 2 | 4911 | observe |
| ninja-vless | 0.279 | 0.5 | 2 | 1791 | observe |
| ermaozi-get_subscribe | 0.276 | 1.0 | 1 | 515 | observe |
| tg-LonUp_M | 0.262 | 1.0 | 1 | 172 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 53 | observe |
| Epodonios-all | 0.255 | None | 0 | 7650 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5520 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| test_one_timeout | 15.0s | - | 90 |
| geo | ClientOSError | - | 19 |
| speed | ClientOSError | - | 12 |
| cn-block | TimeoutError | - | 9 |
| 204 | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| 204 | TimeoutError | - | 3 |
| speed | ProxyError | - | 3 |
| cn-block | ProxyError | - | 1 |
| geo | TimeoutError | - | 1 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 83 | 161 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
