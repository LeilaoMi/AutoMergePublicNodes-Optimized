# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-02 11:03:37 |
| 运行耗时 | 266.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 82681 |
| 去重后节点 | 23587 |
| TCP 可达 | 3000 |
| 真实可用 | 602 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23587 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| geo | 1.3 |
| tcp | 38.0 |
| probe | 73.2 |
| real_test | 123.4 |
| generate | 26.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 51879 |
| vmess | 11142 |
| shadowsocks | 9912 |
| trojan | 7811 |
| hysteria2 | 1571 |
| http | 144 |
| shadowsocksr | 126 |
| socks | 78 |
| tuic | 11 |
| hysteria | 7 |

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
| 82.07 | shadowsocks | 239.9 | 613.1 | 22.22 | 0.0 | 10.0 | 14.35 | 19.5 | Au1rxx-base64 | 156.146.38.169 |
| 80.46 | hysteria2 | 258.1 | 565.3 | 21.8 | 0.0 | 10.0 | 13.33 | 19.5 | Au1rxx-base64 | 66.94.121.46 |
| 79.88 | vless | 266.8 | 660.2 | 21.6 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 195.211.99.49 |
| 79.32 | vless | 341.7 | 728.6 | 19.87 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 216.152.147.28 |
| 79.06 | vless | 260.7 | 596.6 | 21.74 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 195.211.99.45 |
| 79.01 | shadowsocks | 242.8 | 621.0 | 22.16 | 0.0 | 10.0 | 14.35 | 19.5 | Au1rxx-base64 | 156.146.38.167 |
| 78.83 | shadowsocks | 286.0 | 674.9 | 21.16 | 0.0 | 10.0 | 14.35 | 19.5 | Au1rxx-base64 | 37.19.198.243 |
| 77.03 | vless | 315.0 | 726.7 | 20.49 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 204.48.20.223 |
| 76.99 | shadowsocks | 287.1 | 704.8 | 21.13 | 0.0 | 10.0 | 14.35 | 19.5 | Au1rxx-base64 | 37.19.198.244 |
| 76.84 | vless | 401.1 | 1057.7 | 18.49 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 45.138.100.226 |
| 76.82 | vless | 298.5 | 723.0 | 20.87 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 172.105.104.54 |
| 76.82 | vless | 301.5 | 604.3 | 20.8 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 172.239.67.156 |
| 76.65 | vless | 456.8 | 779.3 | 17.2 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 38.180.242.205 |
| 76.53 | shadowsocks | 344.9 | 857.2 | 19.79 | 0.0 | 10.0 | 14.35 | 19.5 | Au1rxx-base64 | 142.4.216.225 |
| 76.31 | vless | 296.7 | 590.6 | 20.91 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 172.235.38.85 |
| 76.18 | vless | 281.6 | 568.2 | 21.26 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 172.239.67.231 |
| 75.99 | vless | 282.7 | 567.5 | 21.23 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 172.233.139.46 |
| 75.9 | vless | 359.4 | 844.0 | 19.46 | 0.0 | 10.0 | 9.95 | 19.5 | Au1rxx-base64 | 169.40.42.95 |
| 75.85 | shadowsocks | 302.8 | 575.6 | 20.77 | 0.0 | 10.0 | 14.35 | 19.5 | Au1rxx-base64 | 173.244.56.9 |
| 75.82 | shadowsocks | 294.8 | 565.0 | 20.95 | 0.0 | 10.0 | 14.35 | 19.5 | Au1rxx-base64 | 108.181.118.10 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.968 | 0.897 | 409 | 1826 | prefer |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| mheidari-all | 0.809 | 0.732 | 127 | 15813 | prefer |
| Surfboard-tg-mixed | 0.8 | 0.723 | 159 | 7112 | prefer |
| tg-oneclickvpnkeys | 0.259 | 1.0 | 1 | 102 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 47 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4765 | observe |
| Epodonios-all | 0.255 | None | 0 | 7428 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3996 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7727 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5992 | observe |
| barry-far-vless | 0.255 | None | 0 | 6070 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4066 | observe |
| Au1rxx-clash | 0.248 | None | 0 | 1826 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 24 |
| geo | ClientOSError | - | 23 |
| 204 | TimeoutError | - | 22 |
| speed | TimeoutError | - | 19 |
| geo | TimeoutError | - | 12 |
| 204 | ClientOSError | - | 8 |
| speed | ClientOSError | - | 8 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:44424: bind: address already in use | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
