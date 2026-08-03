# AutoNodes 每日报告

生成时间：2026-08-03 14:55:46

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 83610 |
| 去重后节点数 | 24688 |
| TCP 可达数 | 3000 |
| 真测通过数 | 486 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24688 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| generate | 32.2 |
| geo | 1.6 |
| probe | 58.0 |
| real_test | 116.8 |
| tcp | 37.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 67 | 66 | 1 | 98.5% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 151 | 134 | 17 | 88.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 23 | 21 | 2 | 91.3% |
| vless | 460 | 244 | 216 | 53.0% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 74 |
| 204:TimeoutError | 46 |
| geo:TimeoutError | 29 |
| 204:ProxyError | 24 |
| speed:TimeoutError | 21 |
| speed:ClientOSError | 20 |
| cn-block:ProxyError | 8 |
| cn-block:TimeoutError | 7 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41974: bind: address already in use | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5035 |
| ConnectionRefusedError | 794 |
| gaierror | 234 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 69 | 0.986 | 92 |
| Au1rxx-base64 | 0.8 | prefer | 518 | 0.734 | 1692 |
| DeltaKronecker-all | 0.402 | observe | 19 | 0.316 | 6205 |
| mheidari-all | 0.361 | observe | 10 | 0.4 | 18776 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 3833 |
| Surfboard-tg-mixed | 0.332 | observe | 105 | 0.248 | 5293 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 54 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5285 |
| Epodonios-all | 0.255 | observe | 0 | None | 5890 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.248 | 26 | 79 | 105 |
| DeltaKronecker-all | 0.316 | 6 | 13 | 19 |
| mheidari-all | 0.4 | 4 | 6 | 10 |
| Au1rxx-base64 | 0.734 | 380 | 138 | 518 |
| zhangkai | 0.986 | 68 | 1 | 69 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18776 | yes | 4.08 | 0 |
| SoliSpirit-all | 6783 | yes | 4.84 | 0 |
| DeltaKronecker-all | 6205 | yes | 5.22 | 0 |
| Epodonios-all | 5890 | yes | 5.37 | 0 |
| Surfboard-tg-mixed | 5293 | yes | 3.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 5285 | yes | 2.18 | 0 |
| mahdibland-V2RayAggregator | 5196 | yes | 2.95 | 0 |
| barry-far-vless | 4526 | yes | 1.94 | 0 |
| Surfboard-tg-vless | 4162 | yes | 3.34 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.33 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 105 |
| 204 | 73 |
| speed | 42 |
| cn-block | 19 |
| sing-box exited 1 | 1 |
