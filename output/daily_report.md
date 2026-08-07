# AutoNodes 每日报告

生成时间：2026-08-07 00:12:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 88824 |
| 去重后节点数 | 24625 |
| TCP 可达数 | 3000 |
| 真测通过数 | 499 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24625 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 52.8 |
| geo | 1.3 |
| probe | 60.7 |
| real_test | 142.5 |
| tcp | 37.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 21 | 21 | 0 | 100.0% |
| hysteria2 | 21 | 21 | 0 | 100.0% |
| shadowsocks | 163 | 149 | 14 | 91.4% |
| socks | 7 | 5 | 2 | 71.4% |
| trojan | 160 | 149 | 11 | 93.1% |
| vless | 611 | 151 | 460 | 24.7% |
| vmess | 5 | 3 | 2 | 60.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 225 |
| geo:ClientOSError | 82 |
| speed:TimeoutError | 70 |
| speed:ClientOSError | 59 |
| cn-block:TimeoutError | 16 |
| 204:TimeoutError | 13 |
| cn-block:ProxyError | 9 |
| geo:ProxyError | 4 |
| 204:ProxyError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| speed:ProxyError | 2 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5048 |
| ConnectionRefusedError | 818 |
| gaierror | 320 |
| OSError | 229 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.986 | prefer | 328 | 0.936 | 1327 |
| zhangkai | 0.958 | prefer | 21 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.541 | observe | 202 | 0.46 | 5904 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 5184 |
| nscl5-all | 0.32 | observe | 1 | 1.0 | 1621 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| DeltaKronecker-all | 0.259 | observe | 37 | 0.162 | 5897 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5219 |
| Epodonios-all | 0.255 | observe | 0 | None | 6481 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.162 | 6 | 31 | 37 |
| mheidari-all | 0.173 | 68 | 326 | 394 |
| Surfboard-tg-mixed | 0.46 | 93 | 109 | 202 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.936 | 307 | 21 | 328 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 21 | 0 | 21 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20787 | yes | 4.72 | 0 |
| SoliSpirit-all | 7217 | yes | 3.06 | 0 |
| Epodonios-all | 6481 | yes | 4.14 | 0 |
| Surfboard-tg-mixed | 5904 | yes | 2.84 | 0 |
| DeltaKronecker-all | 5897 | yes | 5.19 | 0 |
| mahdibland-V2RayAggregator | 5225 | yes | 2.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 5219 | yes | 1.25 | 0 |
| xiaoji235-airport-v2ray-all | 5184 | yes | 1.87 | 0 |
| barry-far-vless | 5041 | yes | 1.02 | 0 |
| Surfboard-tg-vless | 4729 | yes | 2.28 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 311 |
| speed | 132 |
| cn-block | 27 |
| 204 | 19 |
