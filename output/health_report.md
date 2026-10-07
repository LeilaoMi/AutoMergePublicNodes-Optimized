# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-07 05:33:56 |
| 运行耗时 | 829.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 94 |
| 原始节点 | 97105 |
| 去重后节点 | 27064 |
| TCP 可达 | 3000 |
| 真实可用 | 454 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27064 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.8 |
| geo | 1.6 |
| tcp | 46.7 |
| probe | 300.4 |
| real_test | 395.2 |
| generate | 77.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56747 |
| vmess | 15985 |
| shadowsocks | 11619 |
| trojan | 10241 |
| hysteria2 | 1486 |
| http | 698 |
| shadowsocksr | 166 |
| socks | 105 |
| anytls | 30 |
| hysteria | 17 |
| tuic | 11 |

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
| 84.35 | vless | 274.3 | 688.3 | 21.43 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 66.70.179.198 |
| 84.13 | vless | 283.5 | 712.1 | 21.21 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.74 |
| 84.02 | hysteria2 | 257.3 | 665.0 | 21.82 | 0.0 | 10.0 | 13.7 | 20.0 | Au1rxx-base64 | 129.213.91.185 |
| 83.73 | vless | 301.0 | 694.3 | 20.81 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.235 |
| 83.55 | vless | 265.6 | 710.2 | 21.63 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.225 |
| 83.48 | hysteria2 | 248.0 | 668.0 | 22.04 | 0.0 | 10.0 | 13.7 | 18.84 | mheidari-all | 159.223.157.129 |
| 83.37 | vless | 316.6 | 887.0 | 20.45 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 137.184.218.169 |
| 83.26 | vless | 321.5 | 836.3 | 20.34 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 2.24.124.64 |
| 83.23 | vless | 322.5 | 905.2 | 20.31 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 159.89.87.21 |
| 83.12 | vless | 327.2 | 894.8 | 20.2 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.173 |
| 82.97 | vless | 334.0 | 796.0 | 20.05 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.95 |
| 82.9 | vless | 293.5 | 748.6 | 20.98 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.182 |
| 82.72 | vless | 344.7 | 826.5 | 19.8 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.224 |
| 82.72 | vless | 344.7 | 962.9 | 19.8 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 185.95.231.156 |
| 82.62 | vless | 348.9 | 898.5 | 19.7 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 209.200.246.148 |
| 82.6 | vless | 286.5 | 702.1 | 21.15 | 0.0 | 10.0 | 12.92 | 18.84 | mheidari-all | 167.17.69.171 |
| 82.55 | vless | 351.8 | 920.3 | 19.63 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.163 |
| 82.43 | vless | 282.4 | 634.9 | 21.24 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.104 |
| 81.96 | vless | 313.1 | 853.1 | 20.53 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.133 |
| 81.73 | vless | 387.4 | 959.6 | 18.81 | 0.0 | 10.0 | 12.92 | 20.0 | Au1rxx-base64 | 169.40.42.168 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.968 | 0.898 | 305 | 1797 | prefer |
| Surfboard-tg-mixed | 0.742 | 0.667 | 69 | 7006 | prefer |
| mheidari-all | 0.435 | 0.354 | 325 | 22990 | observe |
| ermaozi | 0.414 | 0.38 | 50 | 726 | observe |
| Epodonios-all | 0.255 | None | 0 | 7476 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9204 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5583 | observe |
| barry-far-vless | 0.255 | None | 0 | 5829 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4373 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1797 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |
| 10ium-ScrapeCategorize-Vless | 0.207 | 0.0 | 1 | 4990 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 122 |
| speed | TimeoutError | - | 57 |
| geo | ClientOSError | - | 31 |
| cn-block | TimeoutError | - | 20 |
| 204 | ProxyError | - | 19 |
| 204 | ProxyConnectionError | - | 15 |
| 204 | TimeoutError | - | 15 |
| speed | ClientOSError | - | 13 |
| cn-block | ProxyError | - | 3 |
| cn-block | ClientOSError | - | 3 |
| geo | ProxyError | - | 3 |
| 204 | ClientOSError | - | 2 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
