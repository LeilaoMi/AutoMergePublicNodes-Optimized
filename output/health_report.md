# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-22 04:28:20 |
| 运行耗时 | 740.0s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 91704 |
| 去重后节点 | 25163 |
| TCP 可达 | 3000 |
| 真实可用 | 569 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 25163 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| geo | 1.5 |
| tcp | 42.2 |
| probe | 299.1 |
| real_test | 309.3 |
| generate | 80.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 54115 |
| vmess | 14758 |
| shadowsocks | 11177 |
| trojan | 9289 |
| hysteria2 | 1456 |
| http | 651 |
| shadowsocksr | 131 |
| socks | 81 |
| anytls | 21 |
| hysteria | 17 |
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
| 79.54 | vless | 233.1 | 608.0 | 22.38 | 0.0 | 9.02 | 9.4 | 18.74 | Au1rxx-base64 | 195.123.235.177 |
| 79.44 | vless | 237.4 | 682.1 | 22.28 | 0.0 | 9.02 | 9.4 | 18.74 | Au1rxx-base64 | 79.141.172.154 |
| 79.08 | vless | 257.7 | 635.0 | 21.81 | 0.0 | 9.13 | 9.4 | 18.74 | Au1rxx-base64 | 195.211.98.43 |
| 78.69 | vless | 254.5 | 701.8 | 21.89 | 0.0 | 8.66 | 9.4 | 18.74 | Au1rxx-base64 | ww9.levikogjgfdd.ir |
| 78.64 | vless | 268.0 | 715.7 | 21.57 | 0.0 | 8.93 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.212 |
| 78.22 | shadowsocks | 308.0 | 875.9 | 20.65 | 0.0 | 10.0 | 14.25 | 17.82 | Surfboard-tg-mixed | 15.204.246.132 |
| 77.3 | vless | 242.7 | 693.6 | 22.16 | 0.0 | 10.0 | 9.4 | 18.74 | Au1rxx-base64 | 47.253.226.114 |
| 77.26 | hysteria2 | 332.9 | 710.0 | 20.07 | 0.0 | 10.0 | 13.5 | 18.74 | Au1rxx-base64 | 66.94.121.46 |
| 77.07 | shadowsocks | 283.2 | 635.2 | 21.22 | 0.0 | 10.0 | 14.25 | 17.82 | Surfboard-tg-mixed | 156.146.38.167 |
| 77.07 | vless | 334.2 | 921.5 | 20.04 | 0.0 | 8.89 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.179 |
| 76.99 | vless | 345.8 | 827.7 | 19.77 | 0.0 | 9.08 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.15 |
| 76.98 | vless | 338.1 | 929.9 | 19.95 | 0.0 | 8.89 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.89 |
| 76.94 | vless | 342.7 | 934.8 | 19.84 | 0.0 | 8.96 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.52 |
| 76.82 | shadowsocks | 281.5 | 650.3 | 21.26 | 0.0 | 8.9 | 14.25 | 18.74 | Au1rxx-base64 | 156.146.38.168 |
| 76.8 | vless | 267.7 | 717.1 | 21.58 | 0.0 | 9.02 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.184 |
| 76.67 | vless | 399.7 | 1061.4 | 18.53 | 0.0 | 10.0 | 9.4 | 18.74 | Au1rxx-base64 | 138.124.60.146 |
| 76.44 | vless | 361.3 | 992.2 | 19.41 | 0.0 | 8.89 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.229 |
| 76.37 | vless | 370.4 | 966.3 | 19.2 | 0.0 | 9.03 | 9.4 | 18.74 | Au1rxx-base64 | 169.40.42.235 |
| 76.29 | hysteria2 | 287.4 | 803.7 | 21.13 | 0.0 | 10.0 | 13.5 | 12.76 | mheidari-all | 159.223.157.129 |
| 76.27 | vless | 371.9 | 1028.3 | 19.17 | 0.0 | 8.96 | 9.4 | 18.74 | Au1rxx-base64 | 185.95.231.156 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.907 | 0.843 | 305 | 1658 | prefer |
| Surfboard-tg-mixed | 0.673 | 0.594 | 229 | 7121 | observe |
| ermaozi | 0.623 | 0.612 | 49 | 369 | observe |
| mheidari-all | 0.582 | 0.502 | 275 | 19852 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 7572 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8704 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5672 | observe |
| barry-far-vless | 0.255 | None | 0 | 5888 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4344 | observe |
| Au1rxx-clash | 0.241 | None | 0 | 1660 | observe |
| ermaozi-get_subscribe | 0.235 | 0.4 | 5 | 393 | downweight |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 88 |
| geo | ClientOSError | - | 71 |
| speed | ClientOSError | - | 60 |
| cn-block | ClientOSError | - | 40 |
| 204 | ProxyError | - | 37 |
| speed | TimeoutError | - | 35 |
| cn-block | TimeoutError | - | 19 |
| 204 | TimeoutError | - | 18 |
| 204 | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 2 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
