# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-10-03 20:57:56 |
| 运行耗时 | 394.8s |
| 订阅源总数 | 107 |
| 健康订阅源 | 93 |
| 原始节点 | 99458 |
| 去重后节点 | 27317 |
| TCP 可达 | 3000 |
| 真实可用 | 324 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 27317 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| geo | 0.8 |
| tcp | 47.3 |
| probe | 129.3 |
| real_test | 135.6 |
| generate | 74.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 60561 |
| vmess | 15732 |
| shadowsocks | 11337 |
| trojan | 9467 |
| hysteria2 | 1552 |
| http | 521 |
| shadowsocksr | 173 |
| socks | 68 |
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
| 85.22 | hysteria2 | 211.0 | 223.7 | 22.89 | 6.61 | 9.44 | 13.85 | 18.9 | Au1rxx-base64 | open.w2m.ink |
| 81.56 | vless | 262.6 | 576.8 | 21.7 | 0.0 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 172.235.43.210 |
| 81.41 | vless | 256.8 | 557.3 | 21.83 | 0.0 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 172.235.38.85 |
| 81.25 | hysteria2 | 357.8 | 795.3 | 19.5 | 0.0 | 10.0 | 13.85 | 18.9 | Au1rxx-base64 | 66.94.121.46 |
| 78.39 | vless | 220.3 | 405.1 | 22.68 | 0.0 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 162.159.45.19 |
| 77.67 | vless | 316.2 | 324.5 | 20.46 | 2.83 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 43.133.11.187 |
| 77.64 | vless | 329.5 | 322.5 | 20.15 | 2.91 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 46.250.250.149 |
| 77.49 | shadowsocks | 248.6 | 581.7 | 22.02 | 0.0 | 10.0 | 12.39 | 18.9 | Au1rxx-base64 | 74.201.177.54 |
| 77.41 | vless | 289.8 | 727.5 | 21.07 | 0.0 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 34.3.101.206 |
| 77.3 | shadowsocks | 232.3 | 527.3 | 22.4 | 0.0 | 10.0 | 12.39 | 18.9 | Au1rxx-base64 | 103.214.109.197 |
| 77.1 | http | 276.4 | 569.1 | 21.38 | 0.0 | 10.0 | 13.27 | 18.22 | ermaozi | 138.199.35.216 |
| 76.96 | shadowsocks | 258.8 | 271.9 | 21.79 | 4.8 | 10.0 | 12.39 | 18.9 | Au1rxx-base64 | 149.22.87.240 |
| 76.93 | vless | 230.2 | 513.8 | 22.45 | 0.0 | 10.0 | 12.79 | 17.24 | mheidari-all | 47.251.108.158 |
| 75.09 | trojan | 274.8 | 700.0 | 21.42 | 0.0 | 10.0 | 12.27 | 18.9 | Au1rxx-base64 | happy-gibbon.rooster465.autos |
| 74.91 | shadowsocks | 283.3 | 599.6 | 21.22 | 0.0 | 10.0 | 12.39 | 18.9 | Au1rxx-base64 | 173.244.56.6 |
| 74.39 | shadowsocks | 277.1 | 328.0 | 21.36 | 2.7 | 10.0 | 12.39 | 18.9 | Au1rxx-base64 | 149.22.87.241 |
| 74.37 | trojan | 307.9 | 317.1 | 20.65 | 3.11 | 9.26 | 12.27 | 18.9 | Au1rxx-base64 | jp.tronsg.com |
| 74.13 | shadowsocks | 345.6 | 285.8 | 19.78 | 4.28 | 10.0 | 12.39 | 18.9 | Au1rxx-base64 | 84.247.155.196 |
| 74.05 | vless | 392.0 | 731.3 | 18.7 | 0.0 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 195.123.235.177 |
| 73.5 | vless | 422.2 | 820.5 | 18.01 | 0.0 | 10.0 | 12.79 | 18.9 | Au1rxx-base64 | 66.70.179.198 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.984 | 0.915 | 293 | 1802 | prefer |
| ermaozi | 0.872 | 0.875 | 24 | 656 | prefer |
| mheidari-all | 0.83 | 0.762 | 42 | 23599 | prefer |
| Surfboard-tg-mixed | 0.438 | 1.0 | 3 | 7340 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5192 | observe |
| Epodonios-all | 0.255 | None | 0 | 7819 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3995 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 9376 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5938 | observe |
| barry-far-vless | 0.255 | None | 0 | 6176 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4285 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 6752 | observe |
| Au1rxx-clash | 0.247 | None | 0 | 1802 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |
| moneyfly1-collectSub | 0.222 | None | 0 | 1164 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| cn-block | TimeoutError | - | 13 |
| speed | TimeoutError | - | 6 |
| geo | TimeoutError | - | 5 |
| 204 | ProxyConnectionError | - | 4 |
| 204 | TimeoutError | - | 3 |
| geo | ClientOSError | - | 3 |
| 204 | ProxyError | - | 2 |
| speed | ClientOSError | - | 2 |
| cn-block | ClientOSError | - | 2 |
| 204 | ClientOSError | - | 1 |
| cn-block | ProxyError | - | 1 |
| speed | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
