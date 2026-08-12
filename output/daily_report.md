# AutoNodes 每日报告

生成时间：2026-08-12 07:45:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 88266 |
| 去重后节点数 | 23639 |
| TCP 可达数 | 3000 |
| 真测通过数 | 609 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23639 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 41.7 |
| geo | 1.3 |
| probe | 59.0 |
| real_test | 150.0 |
| tcp | 35.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 152 | 136 | 16 | 89.5% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 119 | 109 | 10 | 91.6% |
| vless | 495 | 212 | 283 | 42.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 93 |
| geo:TimeoutError | 93 |
| speed:TimeoutError | 47 |
| speed:ClientOSError | 32 |
| 204:TimeoutError | 14 |
| 204:ProxyError | 14 |
| cn-block:TimeoutError | 13 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5053 |
| ConnectionRefusedError | 801 |
| OSError | 226 |
| gaierror | 163 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Au1rxx-base64 | 0.908 | prefer | 412 | 0.845 | 1632 |
| Surfboard-tg-mixed | 0.682 | observe | 101 | 0.604 | 5943 |
| DeltaKronecker-all | 0.535 | observe | 20 | 0.45 | 4975 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4568 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 5328 |
| nscl5-all | 0.314 | observe | 1 | 1.0 | 1481 |
| mheidari-all | 0.308 | observe | 252 | 0.226 | 20330 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-shadowproxy66 | 0.255 | observe | 1 | 1.0 | 12 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |
| tg-AzadNet | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.226 | 57 | 195 | 252 |
| DeltaKronecker-all | 0.45 | 9 | 11 | 20 |
| Surfboard-tg-mixed | 0.604 | 61 | 40 | 101 |
| Au1rxx-base64 | 0.845 | 348 | 64 | 412 |
| tg-shadowproxy66 | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20330 | yes | 4.83 | 0 |
| SoliSpirit-all | 7652 | yes | 2.79 | 0 |
| Epodonios-all | 6602 | yes | 4.3 | 0 |
| Surfboard-tg-mixed | 5943 | yes | 3.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 5328 | yes | 2.55 | 0 |
| barry-far-vless | 5267 | yes | 2.31 | 0 |
| mahdibland-V2RayAggregator | 5196 | yes | 2.55 | 0 |
| DeltaKronecker-all | 4975 | yes | 6.0 | 0 |
| Surfboard-tg-vless | 4919 | yes | 5.07 | 0 |
| xiaoji235-airport-v2ray-all | 4568 | yes | 2.61 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 186 |
| speed | 80 |
| 204 | 32 |
| cn-block | 14 |
