# AutoNodes 每日报告

生成时间：2026-10-05 14:20:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 98602 |
| 去重后节点数 | 27263 |
| TCP 可达数 | 3000 |
| 真测通过数 | 446 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27263 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 84.9 |
| geo | 1.4 |
| probe | 251.1 |
| real_test | 212.1 |
| tcp | 46.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 1 | 2 | 33.3% |
| http | 59 | 29 | 30 | 49.2% |
| hysteria2 | 22 | 19 | 3 | 86.4% |
| shadowsocks | 164 | 145 | 19 | 88.4% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 112 | 92 | 20 | 82.1% |
| vless | 213 | 158 | 55 | 74.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 42 |
| 204:ProxyError | 31 |
| cn-block:TimeoutError | 14 |
| speed:TimeoutError | 11 |
| speed:ClientOSError | 9 |
| geo:ClientOSError | 8 |
| geo:TimeoutError | 6 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6520 |
| ConnectionRefusedError | 1030 |
| gaierror | 383 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.978 | prefer | 57 | 0.912 | 23423 |
| Au1rxx-base64 | 0.934 | prefer | 301 | 0.864 | 1816 |
| Surfboard-tg-mixed | 0.784 | prefer | 133 | 0.707 | 7151 |
| DeltaKronecker-all | 0.507 | observe | 17 | 0.471 | 5300 |
| ermaozi | 0.505 | observe | 63 | 0.476 | 701 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 172 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5111 |
| Epodonios-all | 0.255 | observe | 0 | None | 7645 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9196 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.333 | 1 | 2 | 3 |
| DeltaKronecker-all | 0.471 | 8 | 9 | 17 |
| ermaozi | 0.476 | 30 | 33 | 63 |
| Surfboard-tg-mixed | 0.707 | 94 | 39 | 133 |
| Au1rxx-base64 | 0.864 | 260 | 41 | 301 |
| mheidari-all | 0.912 | 52 | 5 | 57 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23423 | yes | 3.16 | 0 |
| SoliSpirit-all | 9203 | yes | 1.78 | 0 |
| Epodonios-all | 7645 | yes | 2.49 | 0 |
| Surfboard-tg-mixed | 7151 | yes | 3.28 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.02 | 0 |
| barry-far-vless | 5930 | yes | 1.38 | 0 |
| Surfboard-tg-vless | 5695 | yes | 2.23 | 0 |
| DeltaKronecker-all | 5300 | yes | 3.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 5111 | yes | 1.09 | 0 |
| mahdibland-V2RayAggregator | 4375 | yes | 1.88 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 73 |
| cn-block | 21 |
| speed | 21 |
| geo | 16 |
