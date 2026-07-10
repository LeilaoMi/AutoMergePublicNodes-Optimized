# AutoNodes 每日报告

生成时间：2026-07-10 03:55:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76163 |
| 去重后节点数 | 23386 |
| TCP 可达数 | 3000 |
| 真测通过数 | 474 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23386 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 25.7 |
| geo | 1.5 |
| probe | 57.0 |
| real_test | 111.4 |
| tcp | 31.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 128 | 120 | 8 | 93.8% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 137 | 134 | 3 | 97.8% |
| vless | 445 | 177 | 268 | 39.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 134 |
| geo:TimeoutError | 70 |
| geo:ClientOSError | 22 |
| 204:ProxyError | 21 |
| speed:TimeoutError | 13 |
| cn-block:TimeoutError | 8 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4269 |
| ConnectionRefusedError | 668 |
| gaierror | 275 |
| OSError | 176 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.808 | prefer | 39 | 0.821 | 84 |
| Surfboard-tg-mixed | 0.744 | prefer | 349 | 0.665 | 5645 |
| mheidari-all | 0.634 | observe | 211 | 0.555 | 16112 |
| DeltaKronecker-all | 0.54 | observe | 111 | 0.459 | 7533 |
| nscl5-all | 0.404 | observe | 3 | 1.0 | 1148 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| abc-configs-readme-latest30 | 0.256 | observe | 1 | 1.0 | 19 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4306 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-Farah_VPN | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-Farah_VPN | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.459 | 51 | 60 | 111 |
| mheidari-all | 0.555 | 117 | 94 | 211 |
| Surfboard-tg-mixed | 0.665 | 232 | 117 | 349 |
| Au1rxx-base64 | 0.821 | 32 | 7 | 39 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| abc-configs-readme-latest30 | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16112 | yes | 3.76 | 0 |
| DeltaKronecker-all | 7533 | yes | 3.44 | 0 |
| SoliSpirit-all | 6617 | yes | 2.1 | 0 |
| Epodonios-all | 6482 | yes | 1.73 | 0 |
| Surfboard-tg-mixed | 5645 | yes | 2.76 | 0 |
| mahdibland-V2RayAggregator | 5403 | yes | 1.22 | 0 |
| barry-far-vless | 4661 | yes | 1.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 4306 | yes | 1.35 | 0 |
| Surfboard-tg-vless | 4155 | yes | 2.92 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.45 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 147 |
| geo | 93 |
| 204 | 27 |
| cn-block | 14 |
