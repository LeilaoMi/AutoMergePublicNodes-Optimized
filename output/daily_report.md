# AutoNodes 每日报告

生成时间：2026-09-16 04:30:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 85338 |
| 去重后节点数 | 23260 |
| TCP 可达数 | 3000 |
| 真测通过数 | 515 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23260 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| generate | 80.7 |
| geo | 1.4 |
| probe | 273.2 |
| real_test | 420.1 |
| tcp | 37.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 61 | 46 | 15 | 75.4% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 160 | 151 | 9 | 94.4% |
| socks | 8 | 4 | 4 | 50.0% |
| trojan | 17 | 9 | 8 | 52.9% |
| vless | 566 | 283 | 283 | 50.0% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 119 |
| geo:ClientOSError | 51 |
| speed:TimeoutError | 49 |
| speed:ClientOSError | 27 |
| 204:ProxyError | 19 |
| cn-block:ClientOSError | 17 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 14 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 2 |
| 204:ProxyConnectionError | 1 |
| cn-block:ProxyError | 1 |
| 204:ServerDisconnectedError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5053 |
| ConnectionRefusedError | 854 |
| gaierror | 476 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.93 | prefer | 275 | 0.865 | 1685 |
| ermaozi | 0.736 | prefer | 55 | 0.727 | 407 |
| Surfboard-tg-mixed | 0.71 | prefer | 190 | 0.632 | 7549 |
| mheidari-all | 0.653 | observe | 115 | 0.574 | 16114 |
| ermaozi-get_subscribe | 0.467 | observe | 7 | 0.857 | 438 |
| DeltaKronecker-all | 0.308 | observe | 187 | 0.225 | 5932 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 163 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5015 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.225 | 42 | 145 | 187 |
| mheidari-all | 0.574 | 66 | 49 | 115 |
| Surfboard-tg-mixed | 0.632 | 120 | 70 | 190 |
| ermaozi | 0.727 | 40 | 15 | 55 |
| ermaozi-get_subscribe | 0.857 | 6 | 1 | 7 |
| Au1rxx-base64 | 0.865 | 238 | 37 | 275 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16114 | yes | 5.01 | 0 |
| SoliSpirit-all | 8939 | yes | 4.73 | 0 |
| Epodonios-all | 8042 | yes | 5.24 | 0 |
| Surfboard-tg-mixed | 7549 | yes | 3.75 | 0 |
| barry-far-vless | 6344 | yes | 1.29 | 0 |
| Surfboard-tg-vless | 6134 | yes | 4.02 | 0 |
| DeltaKronecker-all | 5932 | yes | 5.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 3.44 | 0 |
| mahdibland-V2RayAggregator | 4258 | yes | 0.69 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.2 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 170 |
| speed | 78 |
| 204 | 37 |
| cn-block | 35 |
