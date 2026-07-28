# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-07-28 14:27:39 |
| 运行耗时 | 292.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 100 |
| 原始节点 | 86876 |
| 去重后节点 | 23503 |
| TCP 可达 | 3000 |
| 真实可用 | 530 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 23503 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 23.6 |
| geo | 1.4 |
| tcp | 33.2 |
| probe | 59.1 |
| real_test | 133.8 |
| generate | 41.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 49209 |
| trojan | 16006 |
| shadowsocks | 10436 |
| vmess | 10378 |
| hysteria2 | 586 |
| shadowsocksr | 95 |
| http | 73 |
| socks | 66 |
| hysteria | 12 |
| anytls | 10 |
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
| 76.14 | hysteria2 | 349.6 | 724.7 | 19.68 | 0.0 | 10.0 | 12.86 | 19.22 | Au1rxx-base64 | 159.223.157.129 |
| 75.75 | shadowsocks | 207.4 | 551.3 | 22.98 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 149.22.95.183 |
| 75.61 | shadowsocks | 298.5 | 688.2 | 20.87 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 108.181.118.10 |
| 75.29 | shadowsocks | 296.7 | 689.0 | 20.91 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 173.244.56.9 |
| 74.94 | shadowsocks | 310.0 | 679.8 | 20.6 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 108.181.0.177 |
| 74.72 | shadowsocks | 278.8 | 329.5 | 21.32 | 2.65 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 149.22.87.240 |
| 74.45 | shadowsocks | 280.0 | 334.6 | 21.3 | 2.45 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 149.22.87.241 |
| 74.25 | shadowsocks | 314.4 | 732.8 | 20.5 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 173.244.56.6 |
| 73.48 | shadowsocks | 308.0 | 646.1 | 20.65 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 156.146.38.169 |
| 72.86 | trojan | 393.9 | 850.7 | 18.66 | 0.0 | 10.0 | 13.01 | 19.22 | Au1rxx-base64 | 163.245.196.68 |
| 72.75 | vless | 248.8 | 529.1 | 22.02 | 0.0 | 10.0 | 6.64 | 19.22 | Au1rxx-base64 | 172.67.187.219 |
| 72.69 | shadowsocks | 354.1 | 778.0 | 19.58 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 156.146.38.167 |
| 72.01 | vless | 243.0 | 511.5 | 22.15 | 0.0 | 10.0 | 6.64 | 19.22 | Au1rxx-base64 | 104.21.55.229 |
| 71.9 | vless | 248.0 | 525.3 | 22.04 | 0.0 | 10.0 | 6.64 | 19.22 | Au1rxx-base64 | 172.66.132.196 |
| 71.66 | shadowsocks | 357.7 | 717.7 | 19.5 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 37.19.198.160 |
| 71.53 | shadowsocks | 364.6 | 727.9 | 19.34 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 37.19.198.243 |
| 71.29 | vless | 210.3 | 484.5 | 22.91 | 0.0 | 10.0 | 6.64 | 12.74 | DeltaKronecker-all | 172.67.209.126 |
| 71.09 | vless | 214.5 | 484.2 | 22.81 | 0.0 | 10.0 | 6.64 | 12.74 | DeltaKronecker-all | 104.25.161.29 |
| 70.9 | vless | 208.7 | 480.9 | 22.95 | 0.0 | 10.0 | 6.64 | 12.74 | DeltaKronecker-all | 104.16.9.20 |
| 70.78 | shadowsocks | 318.2 | 654.4 | 20.41 | 0.0 | 10.0 | 12.55 | 19.22 | Au1rxx-base64 | 156.146.38.168 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 69 | 81 | prefer |
| Au1rxx-base64 | 0.965 | 0.914 | 197 | 1391 | prefer |
| mheidari-all | 0.926 | 0.86 | 50 | 18775 | prefer |
| Surfboard-tg-mixed | 0.816 | 0.745 | 51 | 5928 | prefer |
| DeltaKronecker-all | 0.689 | 0.61 | 323 | 5965 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.259 | 0.333 | 3 | 3959 | observe |
| Pawdroid | 0.256 | 1.0 | 1 | 17 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4972 | observe |
| Epodonios-all | 0.255 | None | 0 | 6785 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3976 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6846 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4700 | observe |
| barry-far-vless | 0.255 | None | 0 | 5220 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4991 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 62 |
| geo | ClientOSError | - | 23 |
| 204 | TimeoutError | - | 22 |
| speed | ClientOSError | - | 18 |
| cn-block | TimeoutError | - | 15 |
| speed | TimeoutError | - | 10 |
| 204 | ProxyError | - | 9 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
