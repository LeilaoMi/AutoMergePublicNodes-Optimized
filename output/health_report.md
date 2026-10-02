# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-02 05:15:55 |
| 运行耗时 | 862.6s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 98630 |
| 去重后节点 | 27538 |
| TCP 可达 | 3000 |
| 真实可用 | 460 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27538 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| geo | 1.5 |
| tcp | 46.6 |
| probe | 321.7 |
| real_test | 400.1 |
| generate | 85.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60090 |
| vmess | 15752 |
| shadowsocks | 11578 |
| trojan | 8982 |
| hysteria2 | 1429 |
| http | 509 |
| shadowsocksr | 168 |
| socks | 61 |
| anytls | 35 |
| hysteria | 17 |
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
| 84.65 | vless | 248.2 | 650.9 | 22.03 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.235 |
| 84.49 | vless | 255.4 | 700.7 | 21.87 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 159.89.87.21 |
| 84.08 | vless | 273.1 | 725.3 | 21.46 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.15 |
| 83.98 | vless | 277.1 | 735.0 | 21.36 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.89 |
| 83.87 | vless | 282.0 | 626.4 | 21.25 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.16 |
| 83.62 | vless | 292.8 | 619.2 | 21.0 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 79.141.172.154 |
| 83.5 | vless | 298.0 | 679.5 | 20.88 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.184 |
| 83.41 | vless | 301.7 | 838.0 | 20.79 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 137.184.218.169 |
| 83.3 | vless | 306.6 | 708.2 | 20.68 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.212 |
| 82.43 | vless | 344.4 | 870.4 | 19.81 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 167.17.69.171 |
| 82.26 | vless | 351.6 | 915.2 | 19.64 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.163 |
| 82.14 | vless | 356.7 | 920.7 | 19.52 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.229 |
| 82.13 | vless | 270.6 | 724.3 | 21.51 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 50.114.179.2 |
| 82.13 | vless | 357.2 | 930.7 | 19.51 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.168 |
| 82.09 | vless | 277.3 | 685.9 | 21.36 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.90 |
| 81.94 | vless | 365.4 | 891.5 | 19.32 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.52 |
| 81.91 | vless | 314.6 | 722.8 | 20.5 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.133 |
| 81.85 | vless | 369.4 | 904.9 | 19.23 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.179 |
| 81.77 | vless | 372.5 | 950.2 | 19.15 | 0.0 | 10.0 | 12.74 | 19.88 | Au1rxx-base64 | 169.40.42.104 |
| 81.76 | vless | 291.2 | 809.0 | 21.04 | 0.0 | 9.1 | 12.74 | 19.88 | Au1rxx-base64 | usa-2.letsconnectpoint.com |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.987 | 0.921 | 267 | 1731 | prefer |
| Surfboard-tg-mixed | 0.919 | 0.85 | 60 | 7165 | prefer |
| ermaozi | 0.914 | 0.92 | 25 | 618 | prefer |
| mheidari-all | 0.41 | 0.329 | 416 | 23308 | observe |
| 10ium-ScrapeCategorize-Vless | 0.335 | 1.0 | 1 | 5324 | observe |
| DeltaKronecker-all | 0.263 | 0.25 | 8 | 5603 | observe |
| Epodonios-all | 0.255 | None | 0 | 7654 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9200 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5778 | observe |
| barry-far-vless | 0.255 | None | 0 | 6015 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4310 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| Au1rxx-clash | 0.244 | None | 0 | 1731 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 151 |
| speed | TimeoutError | - | 66 |
| geo | ClientOSError | - | 29 |
| 204 | ProxyError | - | 22 |
| speed | ClientOSError | - | 17 |
| cn-block | TimeoutError | - | 11 |
| 204 | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 6 |
| 204 | ProxyConnectionError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
