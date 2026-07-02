# AutoNodes 每日报告

生成时间：2026-07-02 19:45:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77576 |
| 去重后节点数 | 23214 |
| TCP 可达数 | 3000 |
| 真测通过数 | 347 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23214 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 31.4 |
| geo | 1.4 |
| probe | 57.7 |
| real_test | 115.3 |
| tcp | 30.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 8 | 4 | 4 | 50.0% |
| shadowsocks | 112 | 82 | 30 | 73.2% |
| socks | 26 | 19 | 7 | 73.1% |
| trojan | 113 | 59 | 54 | 52.2% |
| vless | 257 | 144 | 113 | 56.0% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 77 |
| 204:TimeoutError | 21 |
| 204:ProxyError | 16 |
| cn-block:ClientOSError | 16 |
| 204:ClientOSError | 16 |
| cn-block:TimeoutError | 14 |
| geo:ClientOSError | 14 |
| geo:TimeoutError | 12 |
| cn-block:ProxyError | 11 |
| speed:TimeoutError | 5 |
| geo:ProxyError | 4 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4219 |
| ConnectionRefusedError | 710 |
| gaierror | 198 |
| OSError | 153 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.784 | prefer | 30 | 0.8 | 64 |
| mheidari-all | 0.747 | prefer | 67 | 0.672 | 16059 |
| Surfboard-tg-mixed | 0.658 | observe | 346 | 0.578 | 6088 |
| DeltaKronecker-all | 0.628 | observe | 71 | 0.549 | 7467 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1162 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| ermaozi | 0.255 | observe | 1 | 1.0 | 6 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4254 |
| Epodonios-all | 0.255 | observe | 0 | None | 6895 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.155 | observe | 2 | 0.0 | 0 | 1293 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.549 | 39 | 32 | 71 |
| Surfboard-tg-mixed | 0.578 | 200 | 146 | 346 |
| mheidari-all | 0.672 | 45 | 22 | 67 |
| Au1rxx-base64 | 0.8 | 24 | 6 | 30 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16059 | yes | 3.53 | 0 |
| DeltaKronecker-all | 7467 | yes | 3.63 | 0 |
| Epodonios-all | 6895 | yes | 0.79 | 0 |
| SoliSpirit-all | 6658 | yes | 2.29 | 0 |
| Surfboard-tg-mixed | 6088 | yes | 2.05 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 1.66 | 0 |
| barry-far-vless | 5048 | yes | 1.52 | 0 |
| Surfboard-tg-vless | 4550 | yes | 2.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 4254 | yes | 0.98 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.79 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 84 |
| 204 | 53 |
| cn-block | 41 |
| geo | 30 |
