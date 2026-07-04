# AutoNodes 每日报告

生成时间：2026-07-04 03:43:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78050 |
| 去重后节点数 | 23076 |
| TCP 可达数 | 3000 |
| 真测通过数 | 418 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23076 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| generate | 41.0 |
| geo | 1.3 |
| probe | 41.7 |
| real_test | 71.3 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 140 | 125 | 15 | 89.3% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 252 | 229 | 23 | 90.9% |
| vless | 87 | 15 | 72 | 17.2% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 44 |
| speed:ClientOSError | 27 |
| cn-block:ClientOSError | 10 |
| 204:ClientOSError | 9 |
| geo:ClientOSError | 7 |
| speed:TimeoutError | 7 |
| 204:ProxyError | 3 |
| 204:TimeoutError | 2 |
| cn-block:ProxyError | 1 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4489 |
| ConnectionRefusedError | 680 |
| OSError | 152 |
| gaierror | 92 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.877 | prefer | 141 | 0.801 | 6191 |
| mheidari-all | 0.864 | prefer | 100 | 0.79 | 16050 |
| Au1rxx-base64 | 0.849 | prefer | 24 | 0.875 | 82 |
| DeltaKronecker-all | 0.819 | prefer | 220 | 0.741 | 6997 |
| nscl5-all | 0.359 | observe | 2 | 1.0 | 1189 |
| tg-ConfigV2rayNG | 0.319 | observe | 2 | 1.0 | 200 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7108 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.741 | 163 | 57 | 220 |
| mheidari-all | 0.79 | 79 | 21 | 100 |
| Surfboard-tg-mixed | 0.801 | 113 | 28 | 141 |
| Au1rxx-base64 | 0.875 | 21 | 3 | 24 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| tg-ConfigV2rayNG | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16050 | yes | 2.77 | 0 |
| Epodonios-all | 7108 | yes | 2.95 | 0 |
| DeltaKronecker-all | 6997 | yes | 3.03 | 0 |
| SoliSpirit-all | 6859 | yes | 2.2 | 0 |
| Surfboard-tg-mixed | 6191 | yes | 2.13 | 0 |
| mahdibland-V2RayAggregator | 5333 | yes | 1.06 | 0 |
| barry-far-vless | 5259 | yes | 1.3 | 0 |
| Surfboard-tg-vless | 4665 | yes | 1.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 4368 | yes | 0.87 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 1.38 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 51 |
| speed | 34 |
| 204 | 14 |
| cn-block | 12 |
