# AutoNodes 每日报告

生成时间：2026-08-20 07:01:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 93905 |
| 去重后节点数 | 25132 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1247 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25132 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.7 |
| generate | 42.0 |
| geo | 0.9 |
| probe | 83.2 |
| real_test | 220.8 |
| tcp | 39.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 111 | 111 | 0 | 100.0% |
| hysteria2 | 19 | 16 | 3 | 84.2% |
| shadowsocks | 182 | 172 | 10 | 94.5% |
| socks | 7 | 4 | 3 | 57.1% |
| trojan | 722 | 711 | 11 | 98.5% |
| vless | 343 | 231 | 112 | 67.3% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 47 |
| geo:ClientOSError | 23 |
| speed:TimeoutError | 20 |
| cn-block:TimeoutError | 13 |
| cn-block:ClientOSError | 10 |
| 204:TimeoutError | 7 |
| speed:ClientOSError | 6 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5055 |
| ConnectionRefusedError | 954 |
| gaierror | 395 |
| OSError | 224 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 712 | 0.975 | 1789 |
| zhangkai | 0.997 | prefer | 112 | 1.0 | 144 |
| mheidari-all | 0.962 | prefer | 278 | 0.885 | 21143 |
| Surfboard-tg-mixed | 0.829 | prefer | 257 | 0.751 | 6418 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5974 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4958 |
| Epodonios-all | 0.255 | observe | 0 | None | 7111 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7230 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5062 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| DeltaKronecker-all | 0.154 | downweight | 25 | 0.04 | 0 | 6781 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.154 | 25 | 0.04 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.04 | 1 | 24 | 25 |
| Surfboard-tg-mixed | 0.751 | 193 | 64 | 257 |
| mheidari-all | 0.885 | 246 | 32 | 278 |
| Au1rxx-base64 | 0.975 | 694 | 18 | 712 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 112 | 0 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21143 | yes | 5.18 | 0 |
| SoliSpirit-all | 7230 | yes | 3.11 | 0 |
| Epodonios-all | 7111 | yes | 5.4 | 0 |
| DeltaKronecker-all | 6781 | yes | 3.48 | 0 |
| Surfboard-tg-mixed | 6418 | yes | 4.38 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.58 | 0 |
| barry-far-vless | 5404 | yes | 0.81 | 0 |
| Surfboard-tg-vless | 5062 | yes | 4.56 | 0 |
| 10ium-ScrapeCategorize-Vless | 4958 | yes | 1.06 | 0 |
| mahdibland-V2RayAggregator | 4586 | yes | 2.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 70 |
| speed | 26 |
| cn-block | 25 |
| 204 | 19 |
