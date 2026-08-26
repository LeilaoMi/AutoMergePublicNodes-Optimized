# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-26 07:02:00 |
| 运行耗时 | 286.3s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 77824 |
| 去重后节点 | 22072 |
| TCP 可达 | 3000 |
| 真实可用 | 591 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22072 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| geo | 1.5 |
| tcp | 34.3 |
| probe | 59.8 |
| real_test | 140.5 |
| generate | 43.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 48969 |
| vmess | 10276 |
| shadowsocks | 10258 |
| trojan | 6581 |
| hysteria2 | 1362 |
| http | 172 |
| shadowsocksr | 128 |
| socks | 68 |
| hysteria | 7 |
| tuic | 3 |

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
| 83.99 | http | 196.4 | 497.4 | 23.23 | 0.0 | 10.0 | 14.44 | 19.32 | zhangkai | 138.199.35.198 |
| 83.95 | http | 198.2 | 507.3 | 23.19 | 0.0 | 10.0 | 14.44 | 19.32 | zhangkai | 138.199.35.216 |
| 81.29 | trojan | 211.7 | 549.1 | 22.88 | 0.0 | 10.0 | 11.41 | 20.0 | Au1rxx-base64 | us01.duotg.top |
| 81.22 | trojan | 214.8 | 554.9 | 22.81 | 0.0 | 10.0 | 11.41 | 20.0 | Au1rxx-base64 | 107.150.105.84 |
| 80.61 | trojan | 240.9 | 650.0 | 22.2 | 0.0 | 10.0 | 11.41 | 20.0 | Au1rxx-base64 | 14.1.28.76 |
| 80.09 | shadowsocks | 230.9 | 561.6 | 22.43 | 0.0 | 10.0 | 14.2 | 17.46 | Surfboard-tg-mixed | 94.72.127.58 |
| 79.94 | shadowsocks | 237.6 | 566.8 | 22.28 | 0.0 | 10.0 | 14.2 | 17.46 | Surfboard-tg-mixed | 154.12.240.141 |
| 79.89 | shadowsocks | 239.6 | 585.7 | 22.23 | 0.0 | 10.0 | 14.2 | 17.46 | Surfboard-tg-mixed | 94.72.127.55 |
| 79.88 | shadowsocks | 218.5 | 540.8 | 22.72 | 0.0 | 10.0 | 14.2 | 17.46 | Surfboard-tg-mixed | 108.181.0.177 |
| 79.81 | shadowsocks | 232.3 | 568.5 | 22.4 | 0.0 | 10.0 | 14.2 | 17.46 | Surfboard-tg-mixed | 154.53.60.212 |
| 79.16 | shadowsocks | 256.7 | 572.9 | 21.84 | 0.0 | 10.0 | 14.2 | 17.12 | mheidari-all | 149.22.95.183 |
| 79.14 | trojan | 231.0 | 529.7 | 22.43 | 0.0 | 7.97 | 11.41 | 20.0 | Au1rxx-base64 | sincere-gelding.rooster465.autos |
| 78.88 | shadowsocks | 246.9 | 629.9 | 22.06 | 0.0 | 10.0 | 14.2 | 17.12 | mheidari-all | 108.181.118.10 |
| 77.95 | shadowsocks | 308.9 | 735.0 | 20.63 | 0.0 | 10.0 | 14.2 | 17.12 | mheidari-all | 173.244.56.9 |
| 76.77 | shadowsocks | 316.4 | 720.6 | 20.45 | 0.0 | 10.0 | 14.2 | 17.12 | mheidari-all | 173.244.56.6 |
| 76.69 | vless | 226.6 | 564.5 | 22.53 | 0.0 | 10.0 | 4.16 | 20.0 | Au1rxx-base64 | 15.204.97.197 |
| 76.69 | vless | 226.6 | 561.3 | 22.53 | 0.0 | 10.0 | 4.16 | 20.0 | Au1rxx-base64 | 15.204.97.209 |
| 76.67 | vless | 227.5 | 567.9 | 22.51 | 0.0 | 10.0 | 4.16 | 20.0 | Au1rxx-base64 | 15.204.97.216 |
| 76.57 | vless | 231.7 | 582.9 | 22.41 | 0.0 | 10.0 | 4.16 | 20.0 | Au1rxx-base64 | 15.204.97.195 |
| 76.34 | vless | 198.8 | 519.9 | 23.18 | 0.0 | 10.0 | 4.16 | 20.0 | Au1rxx-base64 | 166.88.186.151 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.929 | 0.958 | 24 | 144 | prefer |
| Au1rxx-base64 | 0.912 | 0.835 | 375 | 1986 | prefer |
| Surfboard-tg-mixed | 0.787 | 0.709 | 165 | 6380 | prefer |
| mheidari-all | 0.705 | 0.627 | 126 | 14091 | prefer |
| DeltaKronecker-all | 0.58 | 0.5 | 98 | 6107 | observe |
| nscl5-all | 0.402 | 0.8 | 5 | 887 | observe |
| 10ium-ScrapeCategorize-Vless | 0.391 | 1.0 | 2 | 4825 | observe |
| tg-oneclickvpnkeys | 0.319 | 1.0 | 2 | 206 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| Barabama-yudou | 0.262 | 1.0 | 1 | 166 | observe |
| Au1rxx-clash | 0.255 | None | 0 | 1990 | observe |
| Epodonios-all | 0.255 | None | 0 | 6845 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3990 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6976 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5270 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | TimeoutError | - | 56 |
| geo | TimeoutError | - | 55 |
| geo | ClientOSError | - | 24 |
| cn-block | TimeoutError | - | 24 |
| 204 | TimeoutError | - | 22 |
| speed | ClientOSError | - | 14 |
| 204 | ProxyError | - | 6 |
| cn-block | ClientOSError | - | 6 |
| cn-block | ProxyError | - | 2 |
| 204 | ClientOSError | - | 1 |
| speed | ClientPayloadError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
