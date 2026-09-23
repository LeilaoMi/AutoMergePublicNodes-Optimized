# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-23 11:21:46 |
| 运行耗时 | 594.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 96 |
| 原始节点 | 96837 |
| 去重后节点 | 26486 |
| TCP 可达 | 3000 |
| 真实可用 | 406 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26486 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| geo | 1.5 |
| tcp | 42.3 |
| probe | 272.5 |
| real_test | 195.0 |
| generate | 76.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 59305 |
| vmess | 14980 |
| shadowsocks | 11153 |
| trojan | 8826 |
| hysteria2 | 1622 |
| http | 650 |
| shadowsocksr | 174 |
| socks | 77 |
| anytls | 24 |
| hysteria | 18 |
| tuic | 8 |

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
| 81.65 | hysteria2 | 258.4 | 698.3 | 21.8 | 0.0 | 8.43 | 14.44 | 18.08 | Au1rxx-base64 | 159.223.157.129 |
| 76.42 | shadowsocks | 276.4 | 633.6 | 21.38 | 0.0 | 8.49 | 14.34 | 18.08 | Au1rxx-base64 | 156.146.38.168 |
| 76.35 | shadowsocks | 329.2 | 869.6 | 20.16 | 0.0 | 8.56 | 14.34 | 18.08 | Au1rxx-base64 | 15.204.233.41 |
| 74.91 | shadowsocks | 412.5 | 928.6 | 18.23 | 0.0 | 8.76 | 14.34 | 18.08 | Au1rxx-base64 | 15.204.246.132 |
| 74.37 | shadowsocks | 439.0 | 1204.8 | 17.62 | 0.0 | 8.33 | 14.34 | 18.08 | Au1rxx-base64 | 142.4.216.225 |
| 73.25 | shadowsocks | 325.3 | 888.1 | 20.25 | 0.0 | 10.0 | 14.34 | 12.66 | Surfboard-tg-mixed | 37.19.198.243 |
| 72.95 | shadowsocks | 412.8 | 1095.5 | 18.22 | 0.0 | 6.81 | 14.34 | 18.08 | Au1rxx-base64 | yyz-ca-01.blncvpn4u.cc |
| 72.85 | hysteria2 | 396.8 | 745.7 | 18.59 | 0.0 | 8.54 | 14.44 | 18.08 | Au1rxx-base64 | 45.192.12.93 |
| 72.61 | hysteria2 | 405.4 | 835.6 | 18.39 | 0.0 | 8.36 | 14.44 | 18.08 | Au1rxx-base64 | 66.94.121.46 |
| 72.18 | shadowsocks | 389.6 | 999.4 | 18.76 | 0.0 | 8.5 | 14.34 | 18.08 | Au1rxx-base64 | 185.156.47.97 |
| 71.98 | shadowsocks | 283.3 | 646.7 | 21.22 | 0.0 | 10.0 | 14.34 | 12.66 | Surfboard-tg-mixed | 156.146.38.169 |
| 71.92 | vless | 273.6 | 657.8 | 21.45 | 0.0 | 8.54 | 5.23 | 18.08 | Au1rxx-base64 | 195.211.98.43 |
| 71.88 | vless | 331.5 | 891.5 | 20.1 | 0.0 | 8.47 | 5.23 | 18.08 | Au1rxx-base64 | 137.184.218.169 |
| 71.59 | hysteria2 | 401.7 | 765.8 | 18.48 | 0.0 | 7.38 | 14.44 | 18.08 | Au1rxx-base64 | admin.wwwinternetvideo.click |
| 71.36 | vless | 365.7 | 967.3 | 19.31 | 0.0 | 8.74 | 5.23 | 18.08 | Au1rxx-base64 | 185.95.231.233 |
| 71.17 | vless | 368.5 | 945.6 | 19.25 | 0.0 | 8.61 | 5.23 | 18.08 | Au1rxx-base64 | 66.70.179.198 |
| 71.15 | vless | 363.7 | 996.1 | 19.36 | 0.0 | 8.48 | 5.23 | 18.08 | Au1rxx-base64 | 185.95.231.156 |
| 70.94 | vless | 369.1 | 996.7 | 19.23 | 0.0 | 8.4 | 5.23 | 18.08 | Au1rxx-base64 | 169.40.42.52 |
| 70.85 | vless | 374.5 | 876.6 | 19.11 | 0.0 | 8.43 | 5.23 | 18.08 | Au1rxx-base64 | 169.40.42.163 |
| 70.8 | vless | 366.9 | 978.5 | 19.28 | 0.0 | 8.47 | 5.23 | 18.08 | Au1rxx-base64 | 169.40.42.15 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.993 | 0.933 | 223 | 1602 | prefer |
| mheidari-all | 0.778 | 0.702 | 94 | 22242 | prefer |
| Surfboard-tg-mixed | 0.739 | 0.662 | 133 | 7036 | prefer |
| ermaozi | 0.645 | 0.636 | 55 | 346 | observe |
| DeltaKronecker-all | 0.503 | 0.583 | 12 | 6471 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5131 | observe |
| Epodonios-all | 0.255 | None | 0 | 7633 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9066 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5755 | observe |
| barry-far-vless | 0.255 | None | 0 | 5975 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4187 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1602 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 32 |
| 204 | TimeoutError | - | 22 |
| geo | ClientOSError | - | 16 |
| cn-block | TimeoutError | - | 12 |
| 204 | ProxyConnectionError | - | 10 |
| cn-block | ClientOSError | - | 9 |
| geo | TimeoutError | - | 8 |
| speed | TimeoutError | - | 6 |
| speed | ClientOSError | - | 4 |
| 204 | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
