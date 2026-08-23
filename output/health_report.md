# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-23 06:54:48 |
| 运行耗时 | 300.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 98 |
| 原始节点 | 77609 |
| 去重后节点 | 21148 |
| TCP 可达 | 3000 |
| 真实可用 | 797 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 21148 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| geo | 1.4 |
| tcp | 33.8 |
| probe | 61.9 |
| real_test | 160.4 |
| generate | 35.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 47389 |
| shadowsocks | 10138 |
| vmess | 10012 |
| trojan | 8579 |
| hysteria2 | 1091 |
| http | 166 |
| shadowsocksr | 125 |
| socks | 100 |
| hysteria | 7 |
| tuic | 2 |

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
| 82.69 | shadowsocks | 245.5 | 678.8 | 22.09 | 0.0 | 10.0 | 14.6 | 20.0 | Au1rxx-base64 | 37.19.198.236 |
| 81.75 | vless | 255.1 | 690.1 | 21.87 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 79.127.243.217 |
| 81.28 | shadowsocks | 246.9 | 674.5 | 22.06 | 0.0 | 10.0 | 14.6 | 18.62 | Surfboard-tg-mixed | 37.19.198.160 |
| 80.65 | shadowsocks | 312.4 | 814.7 | 20.55 | 0.0 | 10.0 | 14.6 | 20.0 | Au1rxx-base64 | 38.180.135.156 |
| 80.52 | vless | 260.7 | 729.0 | 21.74 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 45.138.100.226 |
| 80.52 | vless | 308.4 | 713.1 | 20.64 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 169.40.42.225 |
| 80.49 | vless | 309.6 | 855.1 | 20.61 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 80.38 | shadowsocks | 323.8 | 821.3 | 20.28 | 0.0 | 10.0 | 14.6 | 20.0 | Au1rxx-base64 | 51.79.64.198 |
| 80.37 | vless | 314.8 | 798.3 | 20.49 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 169.40.42.16 |
| 80.02 | vless | 329.9 | 829.8 | 20.14 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 169.40.42.232 |
| 79.69 | vless | 257.6 | 639.2 | 21.81 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 169.40.42.89 |
| 79.5 | vless | 301.2 | 684.1 | 20.81 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 198.251.78.29 |
| 79.39 | vless | 357.1 | 969.8 | 19.51 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 169.40.42.182 |
| 79.3 | vless | 274.7 | 677.5 | 21.42 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 169.40.42.184 |
| 79.3 | shadowsocks | 277.1 | 622.5 | 21.36 | 0.0 | 10.0 | 14.6 | 20.0 | Au1rxx-base64 | 156.146.38.169 |
| 79.17 | shadowsocks | 287.8 | 668.3 | 21.12 | 0.0 | 10.0 | 14.6 | 20.0 | Au1rxx-base64 | 156.146.38.170 |
| 79.13 | shadowsocks | 286.6 | 658.0 | 21.14 | 0.0 | 10.0 | 14.6 | 20.0 | Au1rxx-base64 | 156.146.38.167 |
| 78.97 | shadowsocks | 384.6 | 918.6 | 18.87 | 0.0 | 10.0 | 14.6 | 20.0 | Au1rxx-base64 | 15.204.246.132 |
| 78.9 | shadowsocks | 244.0 | 616.4 | 22.13 | 0.0 | 9.17 | 14.6 | 20.0 | Au1rxx-base64 | 155.138.136.240 |
| 78.86 | vless | 298.3 | 688.5 | 20.87 | 0.0 | 10.0 | 9.88 | 20.0 | Au1rxx-base64 | 140.99.223.187 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | 1.0 | 111 | 144 | prefer |
| Au1rxx-base64 | 0.996 | 0.925 | 494 | 1821 | prefer |
| Surfboard-tg-mixed | 0.896 | 0.82 | 150 | 6303 | prefer |
| mheidari-all | 0.618 | 0.538 | 104 | 14434 | observe |
| DeltaKronecker-all | 0.574 | 0.494 | 81 | 5288 | observe |
| nscl5-all | 0.428 | 0.714 | 7 | 1082 | observe |
| tg-oneclickvpnkeys | 0.316 | 1.0 | 2 | 131 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.287 | 0.5 | 2 | 4989 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Epodonios-all | 0.255 | None | 0 | 6859 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3985 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7111 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5154 | observe |
| barry-far-vless | 0.255 | None | 0 | 5430 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 47 |
| speed | TimeoutError | - | 32 |
| speed | ClientOSError | - | 18 |
| cn-block | TimeoutError | - | 15 |
| geo | ClientOSError | - | 14 |
| 204 | TimeoutError | - | 12 |
| 204 | ProxyError | - | 11 |
| cn-block | ClientOSError | - | 7 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
