# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-27 16:53:44 |
| 运行耗时 | 549.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 96135 |
| 去重后节点 | 26661 |
| TCP 可达 | 3000 |
| 真实可用 | 397 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 26661 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| geo | 1.5 |
| tcp | 43.7 |
| probe | 225.0 |
| real_test | 189.5 |
| generate | 82.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 58742 |
| vmess | 14608 |
| shadowsocks | 11295 |
| trojan | 9175 |
| hysteria2 | 1454 |
| http | 574 |
| shadowsocksr | 170 |
| socks | 69 |
| anytls | 25 |
| hysteria | 15 |
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
| 81.59 | vless | 277.1 | 706.1 | 21.36 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.173 |
| 80.89 | vless | 307.3 | 680.2 | 20.66 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.179 |
| 80.2 | vless | 337.1 | 902.5 | 19.97 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 185.95.231.233 |
| 80.08 | vless | 342.5 | 916.0 | 19.85 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.89 |
| 80.07 | vless | 343.1 | 910.9 | 19.84 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.163 |
| 80.06 | vless | 256.9 | 704.0 | 21.83 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 47.253.144.114 |
| 80.05 | vless | 314.7 | 704.2 | 20.49 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.184 |
| 79.93 | vless | 348.8 | 929.2 | 19.7 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.95 |
| 79.85 | vless | 329.0 | 869.2 | 20.16 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.52 |
| 79.7 | vless | 358.9 | 914.7 | 19.47 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.202 |
| 79.67 | vless | 360.1 | 900.0 | 19.44 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.229 |
| 79.66 | vless | 360.8 | 852.6 | 19.43 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.75 |
| 79.58 | vless | 364.2 | 931.8 | 19.35 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.232 |
| 79.16 | vless | 369.2 | 865.3 | 19.23 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.168 |
| 79.14 | vless | 253.6 | 696.7 | 21.91 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 47.90.153.88 |
| 78.68 | vless | 403.0 | 1087.8 | 18.45 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.182 |
| 78.33 | vless | 309.3 | 748.0 | 20.62 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.35 |
| 77.76 | vless | 442.8 | 1020.1 | 17.53 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 185.95.231.156 |
| 77.58 | vless | 279.1 | 657.4 | 21.32 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.74 |
| 77.21 | vless | 337.4 | 740.7 | 19.97 | 0.0 | 10.0 | 11.51 | 18.72 | Au1rxx-base64 | 169.40.42.235 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.9 | 0.838 | 303 | 1601 | prefer |
| Surfboard-tg-mixed | 0.835 | 0.759 | 108 | 7109 | prefer |
| mheidari-all | 0.765 | 0.692 | 52 | 22413 | prefer |
| ermaozi | 0.633 | 0.629 | 35 | 289 | observe |
| xiaoji235-airport-v2ray-all | 0.335 | 1.0 | 1 | 6752 | observe |
| Epodonios-all | 0.255 | None | 0 | 7600 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9194 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5703 | observe |
| barry-far-vless | 0.255 | None | 0 | 5938 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4277 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.239 | None | 0 | 1601 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | TimeoutError | - | 27 |
| cn-block | TimeoutError | - | 21 |
| 204 | ProxyError | - | 20 |
| speed | TimeoutError | - | 19 |
| geo | TimeoutError | - | 13 |
| speed | ClientOSError | - | 6 |
| 204 | ProxyConnectionError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:48242: bind: address already in use | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
