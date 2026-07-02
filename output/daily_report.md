# AutoNodes 每日报告

生成时间：2026-07-02 14:19:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76990 |
| 去重后节点数 | 23319 |
| TCP 可达数 | 3000 |
| 真测通过数 | 436 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23319 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 42.4 |
| geo | 1.5 |
| probe | 61.8 |
| real_test | 135.7 |
| tcp | 30.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 7 | 3 | 4 | 42.9% |
| shadowsocks | 125 | 101 | 24 | 80.8% |
| socks | 32 | 27 | 5 | 84.4% |
| trojan | 111 | 81 | 30 | 73.0% |
| vless | 364 | 184 | 180 | 50.5% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 88 |
| 204:ProxyError | 63 |
| cn-block:TimeoutError | 20 |
| 204:TimeoutError | 15 |
| 204:ClientOSError | 13 |
| geo:TimeoutError | 11 |
| cn-block:ClientOSError | 10 |
| geo:ClientOSError | 7 |
| speed:TimeoutError | 6 |
| cn-block:ProxyError | 5 |
| geo:ProxyError | 4 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4336 |
| ConnectionRefusedError | 693 |
| gaierror | 166 |
| OSError | 151 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.776 | prefer | 42 | 0.786 | 78 |
| Surfboard-tg-mixed | 0.76 | prefer | 292 | 0.682 | 5750 |
| mheidari-all | 0.634 | observe | 238 | 0.555 | 16231 |
| DeltaKronecker-all | 0.602 | observe | 65 | 0.523 | 7467 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1162 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4254 |
| Epodonios-all | 0.255 | observe | 0 | None | 6611 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.132 | observe | 4 | 0.0 | 0 | 1293 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 6 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 6 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.523 | 34 | 31 | 65 |
| mheidari-all | 0.555 | 132 | 106 | 238 |
| Surfboard-tg-mixed | 0.682 | 199 | 93 | 292 |
| Au1rxx-base64 | 0.786 | 33 | 9 | 42 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16231 | yes | 3.17 | 0 |
| DeltaKronecker-all | 7467 | yes | 3.47 | 0 |
| SoliSpirit-all | 6844 | yes | 2.63 | 0 |
| Epodonios-all | 6611 | yes | 4.24 | 0 |
| Surfboard-tg-mixed | 5750 | yes | 2.49 | 0 |
| mahdibland-V2RayAggregator | 5365 | yes | 1.66 | 0 |
| barry-far-vless | 4895 | yes | 1.89 | 0 |
| Surfboard-tg-vless | 4338 | yes | 2.0 | 0 |
| 10ium-ScrapeCategorize-Vless | 4254 | yes | 1.41 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.04 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 95 |
| 204 | 91 |
| cn-block | 35 |
| geo | 22 |
