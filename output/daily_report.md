# AutoNodes 每日报告

生成时间：2026-08-19 18:48:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 93105 |
| 去重后节点数 | 24449 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1236 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24449 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.4 |
| generate | 43.8 |
| geo | 0.5 |
| probe | 80.1 |
| real_test | 232.9 |
| tcp | 38.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 20 | 17 | 3 | 85.0% |
| shadowsocks | 154 | 140 | 14 | 90.9% |
| socks | 9 | 5 | 4 | 55.6% |
| trojan | 775 | 770 | 5 | 99.4% |
| vless | 247 | 191 | 56 | 77.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 20 |
| cn-block:TimeoutError | 14 |
| geo:TimeoutError | 10 |
| speed:TimeoutError | 10 |
| geo:ClientOSError | 9 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 4 |
| speed:ClientOSError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4583 |
| ConnectionRefusedError | 978 |
| gaierror | 556 |
| OSError | 226 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 691 | 0.98 | 1890 |
| mheidari-all | 1.0 | prefer | 293 | 0.945 | 20423 |
| zhangkai | 0.988 | prefer | 113 | 0.991 | 144 |
| Surfboard-tg-mixed | 0.866 | prefer | 213 | 0.789 | 6336 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 3330 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5067 |
| Epodonios-all | 0.255 | observe | 0 | None | 7060 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7318 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5003 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.135 | observe | 1 | 0.0 | 0 | 179 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.25 | 1 | 3 | 4 |
| Surfboard-tg-mixed | 0.789 | 168 | 45 | 213 |
| mheidari-all | 0.945 | 277 | 16 | 293 |
| Au1rxx-base64 | 0.98 | 677 | 14 | 691 |
| zhangkai | 0.991 | 112 | 1 | 113 |
| nscl5-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20423 | yes | 5.02 | 0 |
| SoliSpirit-all | 7318 | yes | 5.36 | 0 |
| Epodonios-all | 7060 | yes | 5.23 | 0 |
| DeltaKronecker-all | 6390 | yes | 5.35 | 0 |
| Surfboard-tg-mixed | 6336 | yes | 3.31 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.7 | 0 |
| barry-far-vless | 5325 | yes | 3.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 5067 | yes | 3.54 | 0 |
| Surfboard-tg-vless | 5003 | yes | 3.48 | 0 |
| mahdibland-V2RayAggregator | 4086 | yes | 2.82 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| cn-block | 20 |
| geo | 19 |
| speed | 13 |
