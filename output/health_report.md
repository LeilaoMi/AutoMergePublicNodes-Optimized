# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-27 22:08:23 |
| 运行耗时 | 224.1s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 87058 |
| 去重后节点 | 23525 |
| TCP 可达 | 3000 |
| 真实可用 | 482 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23525 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| geo | 1.5 |
| tcp | 39.1 |
| probe | 47.3 |
| real_test | 90.3 |
| generate | 40.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 53670 |
| shadowsocks | 11824 |
| vmess | 11576 |
| trojan | 7616 |
| hysteria2 | 1951 |
| http | 164 |
| shadowsocksr | 141 |
| socks | 75 |
| anytls | 20 |
| hysteria | 16 |
| tuic | 5 |

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
| 82.56 | vless | 247.5 | 649.4 | 22.05 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.225 |
| 82.47 | vless | 251.5 | 696.5 | 21.96 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 47.89.186.170 |
| 82.31 | vless | 258.3 | 667.9 | 21.8 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.202 |
| 82.3 | vless | 258.8 | 666.8 | 21.79 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.179 |
| 82.26 | vless | 260.4 | 628.7 | 21.75 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 195.211.99.45 |
| 81.94 | vless | 274.3 | 662.2 | 21.43 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.35 |
| 81.91 | vless | 275.7 | 672.6 | 21.4 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.15 |
| 81.7 | shadowsocks | 229.1 | 629.9 | 22.48 | 0.0 | 10.0 | 13.78 | 19.44 | Au1rxx-base64 | 37.19.198.236 |
| 81.49 | vless | 293.9 | 656.3 | 20.98 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.74 |
| 81.26 | vless | 260.4 | 628.5 | 21.75 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 195.211.99.49 |
| 81.25 | vless | 303.9 | 748.5 | 20.74 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.231 |
| 80.83 | vless | 322.1 | 886.9 | 20.32 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 79.127.243.217 |
| 80.82 | vless | 322.7 | 876.5 | 20.31 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.133 |
| 80.42 | vless | 339.9 | 926.0 | 19.91 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 185.95.231.156 |
| 80.3 | vless | 345.0 | 938.4 | 19.79 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.212 |
| 80.27 | shadowsocks | 290.8 | 794.3 | 21.05 | 0.0 | 10.0 | 13.78 | 19.44 | Au1rxx-base64 | 198.98.53.130 |
| 80.03 | vless | 356.6 | 999.8 | 19.52 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 137.184.218.169 |
| 79.85 | vless | 295.5 | 659.5 | 20.94 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 198.251.78.29 |
| 79.75 | vless | 368.9 | 964.5 | 19.24 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 169.40.42.95 |
| 79.72 | vless | 300.4 | 715.6 | 20.82 | 0.0 | 10.0 | 11.07 | 19.44 | Au1rxx-base64 | 216.152.147.28 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | 0.944 | 303 | 1622 | prefer |
| zhangkai | 0.966 | 1.0 | 23 | 144 | prefer |
| Surfboard-tg-mixed | 0.868 | 0.792 | 149 | 6577 | prefer |
| mheidari-all | 0.622 | 0.543 | 94 | 19755 | observe |
| DeltaKronecker-all | 0.391 | 1.0 | 2 | 4318 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4783 | observe |
| Epodonios-all | 0.255 | None | 0 | 6955 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3991 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7129 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5393 | observe |
| barry-far-vless | 0.255 | None | 0 | 5568 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4019 | observe |
| ninja-vless | 0.247 | None | 0 | 1791 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | ClientOSError | - | 35 |
| 204 | TimeoutError | - | 16 |
| cn-block | TimeoutError | - | 11 |
| speed | ClientOSError | - | 9 |
| speed | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 5 |
| cn-block | ProxyError | - | 4 |
| cn-block | ClientOSError | - | 2 |
| 204 | ProxyError | - | 2 |
| geo | TimeoutError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
