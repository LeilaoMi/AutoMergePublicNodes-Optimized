# AutoNodes 每日报告

生成时间：2026-07-20 14:26:06

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 85546 |
| 去重后节点数 | 24077 |
| TCP 可达数 | 3000 |
| 真测通过数 | 379 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24077 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 27.6 |
| geo | 0.6 |
| probe | 84.4 |
| real_test | 223.1 |
| tcp | 33.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 124 | 108 | 16 | 87.1% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 237 | 196 | 41 | 82.7% |
| vless | 998 | 34 | 964 | 3.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 799 |
| speed:ClientOSError | 122 |
| geo:ClientOSError | 31 |
| cn-block:TimeoutError | 29 |
| speed:TimeoutError | 10 |
| 204:ProxyError | 8 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 5 |
| speed:ProxyError | 3 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4417 |
| ConnectionRefusedError | 700 |
| gaierror | 552 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.927 | prefer | 240 | 0.892 | 969 |
| Surfboard-tg-mixed | 0.658 | observe | 43 | 0.581 | 5287 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5035 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4714 |
| Epodonios-all | 0.255 | observe | 0 | None | 6550 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6894 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4082 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| DeltaKronecker-all | 0.174 | downweight | 1046 | 0.093 | 0 | 5962 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.174 | 1046 | 0.093 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.093 | 97 | 949 | 1046 |
| mheidari-all | 0.152 | 5 | 28 | 33 |
| Surfboard-tg-mixed | 0.581 | 25 | 18 | 43 |
| Au1rxx-base64 | 0.892 | 214 | 26 | 240 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19893 | yes | 4.02 | 0 |
| SoliSpirit-all | 6894 | yes | 4.16 | 0 |
| Epodonios-all | 6550 | yes | 4.24 | 0 |
| DeltaKronecker-all | 5962 | yes | 3.79 | 0 |
| Surfboard-tg-mixed | 5287 | yes | 2.16 | 0 |
| mahdibland-V2RayAggregator | 5193 | yes | 2.24 | 0 |
| xiaoji235-airport-v2ray-all | 5035 | yes | 1.59 | 0 |
| barry-far-vless | 4908 | yes | 1.34 | 0 |
| 10ium-ScrapeCategorize-Vless | 4714 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 4082 | yes | 2.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vless | 0.034 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 830 |
| speed | 135 |
| cn-block | 40 |
| 204 | 17 |
