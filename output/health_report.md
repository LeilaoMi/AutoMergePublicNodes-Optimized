# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-26 19:57:11 |
| 运行耗时 | 239.4s |
| 订阅源总数 | 107 |
| 健康订阅源 | 97 |
| 原始节点 | 89577 |
| 去重后节点 | 24385 |
| TCP 可达 | 3000 |
| 真实可用 | 455 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24385 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| geo | 1.4 |
| tcp | 39.3 |
| probe | 51.6 |
| real_test | 106.4 |
| generate | 35.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 56365 |
| shadowsocks | 11837 |
| vmess | 11451 |
| trojan | 7341 |
| hysteria2 | 2156 |
| http | 172 |
| shadowsocksr | 138 |
| socks | 79 |
| anytls | 20 |
| hysteria | 13 |
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
| 81.79 | vless | 299.4 | 809.2 | 20.85 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 166.88.186.151 |
| 80.76 | vless | 218.4 | 568.1 | 22.72 | 0.0 | 10.0 | 11.38 | 18.66 | DeltaKronecker-all | 108.186.202.51 |
| 80.71 | vless | 273.8 | 616.3 | 21.44 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 15.204.97.195 |
| 80.56 | vless | 269.6 | 597.5 | 21.54 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 15.204.97.216 |
| 80.17 | trojan | 205.4 | 522.9 | 23.02 | 0.0 | 10.0 | 10.59 | 19.56 | Au1rxx-base64 | 107.150.105.84 |
| 79.13 | vless | 345.9 | 833.5 | 19.77 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 15.204.97.209 |
| 78.91 | vless | 350.6 | 854.5 | 19.66 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 15.204.97.197 |
| 78.21 | shadowsocks | 228.3 | 527.7 | 22.49 | 0.0 | 10.0 | 13.72 | 16.0 | Surfboard-tg-mixed | 173.244.56.9 |
| 77.98 | shadowsocks | 273.7 | 641.4 | 21.44 | 0.0 | 10.0 | 13.72 | 19.56 | Au1rxx-base64 | 156.146.38.170 |
| 77.45 | shadowsocks | 239.7 | 595.6 | 22.23 | 0.0 | 10.0 | 13.72 | 16.0 | Surfboard-tg-mixed | 108.181.0.177 |
| 77.38 | shadowsocks | 264.4 | 656.8 | 21.66 | 0.0 | 10.0 | 13.72 | 16.0 | Surfboard-tg-mixed | 156.146.38.167 |
| 77.38 | vless | 404.3 | 1011.0 | 18.42 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 15.204.97.214 |
| 77.31 | trojan | 199.4 | 501.0 | 23.16 | 0.0 | 10.0 | 10.59 | 19.56 | Au1rxx-base64 | us01.duotg.top |
| 76.93 | vless | 243.3 | 549.5 | 22.15 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 31.58.50.200 |
| 76.92 | http | 443.6 | 1249.5 | 17.51 | 0.0 | 10.0 | 13.89 | 18.52 | zhangkai | 138.199.35.198 |
| 76.9 | http | 444.3 | 1245.7 | 17.49 | 0.0 | 10.0 | 13.89 | 18.52 | zhangkai | 138.199.35.216 |
| 76.79 | shadowsocks | 288.8 | 630.2 | 21.09 | 0.0 | 10.0 | 13.72 | 19.56 | Au1rxx-base64 | 149.22.95.183 |
| 76.71 | shadowsocks | 276.2 | 672.1 | 21.38 | 0.0 | 10.0 | 13.72 | 16.0 | Surfboard-tg-mixed | 156.146.38.168 |
| 76.6 | shadowsocks | 264.2 | 613.3 | 21.66 | 0.0 | 10.0 | 13.72 | 16.0 | Surfboard-tg-mixed | 173.244.56.6 |
| 76.15 | vless | 347.2 | 786.6 | 19.74 | 0.0 | 10.0 | 11.38 | 19.56 | Au1rxx-base64 | 45.138.100.226 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.966 | 0.889 | 350 | 1979 | prefer |
| zhangkai | 0.926 | 0.957 | 23 | 144 | prefer |
| Surfboard-tg-mixed | 0.757 | 0.68 | 122 | 6645 | prefer |
| DeltaKronecker-all | 0.509 | 0.426 | 68 | 6107 | observe |
| mheidari-all | 0.46 | 0.412 | 17 | 19290 | observe |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 205 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4825 | observe |
| Epodonios-all | 0.255 | None | 0 | 7011 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 7313 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5444 | observe |
| barry-far-vless | 0.255 | None | 0 | 5698 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 4011 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5418 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 35 |
| cn-block | TimeoutError | - | 22 |
| 204 | TimeoutError | - | 19 |
| geo | ClientOSError | - | 17 |
| 204 | ProxyError | - | 13 |
| speed | ClientOSError | - | 11 |
| geo | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
