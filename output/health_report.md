# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-02 13:44:50 |
| 运行耗时 | 303.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 78156 |
| 去重后节点 | 22890 |
| TCP 可达 | 3000 |
| 真实可用 | 673 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22890 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| geo | 1.4 |
| tcp | 34.7 |
| probe | 60.0 |
| real_test | 160.4 |
| generate | 40.8 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 46721 |
| vmess | 12700 |
| shadowsocks | 10107 |
| trojan | 7653 |
| hysteria2 | 627 |
| http | 165 |
| shadowsocksr | 77 |
| socks | 64 |
| anytls | 26 |
| hysteria | 12 |
| tuic | 4 |

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
| 83.93 | http | 244.8 | 663.1 | 22.11 | 0.0 | 10.0 | 14.9 | 19.92 | zhangkai | 156.146.59.8 |
| 83.91 | http | 245.5 | 650.3 | 22.09 | 0.0 | 10.0 | 14.9 | 19.92 | zhangkai | 156.146.59.23 |
| 83.91 | http | 245.6 | 648.7 | 22.09 | 0.0 | 10.0 | 14.9 | 19.92 | zhangkai | 156.146.59.21 |
| 83.68 | http | 255.6 | 675.8 | 21.86 | 0.0 | 10.0 | 14.9 | 19.92 | zhangkai | 156.146.59.7 |
| 83.6 | http | 258.9 | 694.0 | 21.78 | 0.0 | 10.0 | 14.9 | 19.92 | zhangkai | 156.146.59.20 |
| 83.59 | http | 259.3 | 691.3 | 21.77 | 0.0 | 10.0 | 14.9 | 19.92 | zhangkai | 156.146.59.5 |
| 83.49 | http | 264.0 | 714.5 | 21.67 | 0.0 | 10.0 | 14.9 | 19.92 | zhangkai | 156.146.59.25 |
| 80.44 | hysteria2 | 233.2 | 643.3 | 22.38 | 0.0 | 10.0 | 13.12 | 16.04 | Au1rxx-base64 | 159.223.157.129 |
| 80.34 | hysteria2 | 241.9 | 672.2 | 22.18 | 0.0 | 10.0 | 13.12 | 16.04 | Au1rxx-base64 | 138.124.68.188 |
| 80.31 | hysteria2 | 243.2 | 674.4 | 22.15 | 0.0 | 10.0 | 13.12 | 16.04 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 78.55 | vless | 243.7 | 657.9 | 22.14 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 167.99.48.117 |
| 77.48 | vless | 289.8 | 725.3 | 21.07 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 159.195.12.98 |
| 77.09 | vless | 306.6 | 840.0 | 20.68 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 137.184.218.169 |
| 76.91 | vless | 271.0 | 679.4 | 21.5 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 162.159.0.3 |
| 76.73 | vless | 322.2 | 747.8 | 20.32 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 78.111.89.171 |
| 76.57 | vless | 285.7 | 636.9 | 21.16 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 108.162.192.5 |
| 76.5 | vless | 332.3 | 773.6 | 20.09 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 169.40.42.179 |
| 76.28 | vless | 341.4 | 921.8 | 19.87 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 167.17.69.171 |
| 76.2 | vless | 345.2 | 938.5 | 19.79 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 169.40.42.75 |
| 76.14 | vless | 347.9 | 948.4 | 19.73 | 0.0 | 10.0 | 10.37 | 16.04 | Au1rxx-base64 | 169.40.42.212 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | 1.0 | 143 | 344 | prefer |
| Au1rxx-base64 | 0.797 | 0.732 | 555 | 1667 | prefer |
| Surfboard-tg-mixed | 0.66 | 0.581 | 117 | 5249 | observe |
| DeltaKronecker-all | 0.488 | 0.407 | 123 | 4549 | observe |
| mheidari-all | 0.373 | 0.6 | 5 | 16891 | observe |
| xiaoji235-airport-v2ray-all | 0.282 | 0.5 | 2 | 1861 | observe |
| nscl5-all | 0.262 | 0.5 | 2 | 1354 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 57 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5486 | observe |
| Epodonios-all | 0.255 | None | 0 | 5857 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3972 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6807 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4007 | observe |
| barry-far-vless | 0.255 | None | 0 | 4517 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5071 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 100 |
| speed | TimeoutError | - | 48 |
| 204 | TimeoutError | - | 37 |
| cn-block | TimeoutError | - | 24 |
| speed | ClientOSError | - | 23 |
| geo | ClientOSError | - | 17 |
| 204 | ProxyError | - | 13 |
| cn-block | ClientOSError | - | 8 |
| 204 | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |
| geo | parse | TimeoutError | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
