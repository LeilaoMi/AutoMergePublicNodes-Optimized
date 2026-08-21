# AutoNodes 每日报告

生成时间：2026-08-21 18:49:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 93362 |
| 去重后节点数 | 23312 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1135 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23312 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 44.9 |
| geo | 0.9 |
| probe | 69.4 |
| real_test | 196.9 |
| tcp | 39.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 113 | 113 | 0 | 100.0% |
| hysteria2 | 20 | 18 | 2 | 90.0% |
| shadowsocks | 150 | 139 | 11 | 92.7% |
| socks | 7 | 4 | 3 | 57.1% |
| trojan | 623 | 621 | 2 | 99.7% |
| vless | 287 | 238 | 49 | 82.9% |
| vmess | 3 | 2 | 1 | 66.7% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 13 |
| geo:TimeoutError | 13 |
| 204:TimeoutError | 11 |
| speed:TimeoutError | 10 |
| geo:ClientOSError | 9 |
| 204:ProxyError | 4 |
| cn-block:ClientOSError | 3 |
| speed:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5236 |
| ConnectionRefusedError | 926 |
| gaierror | 462 |
| OSError | 222 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 678 | 0.982 | 1933 |
| zhangkai | 0.997 | prefer | 113 | 1.0 | 144 |
| mheidari-all | 0.99 | prefer | 220 | 0.914 | 21956 |
| Surfboard-tg-mixed | 0.905 | prefer | 181 | 0.829 | 6488 |
| nscl5-all | 0.391 | observe | 2 | 1.0 | 3031 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 177 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5148 |
| Epodonios-all | 0.255 | observe | 0 | None | 7155 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.216 | 6 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.167 | 1 | 5 | 6 |
| Surfboard-tg-mixed | 0.829 | 150 | 31 | 181 |
| mheidari-all | 0.914 | 201 | 19 | 220 |
| Au1rxx-base64 | 0.982 | 666 | 12 | 678 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 113 | 0 | 113 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21956 | yes | 4.95 | 0 |
| SoliSpirit-all | 7163 | yes | 4.54 | 0 |
| Epodonios-all | 7155 | yes | 4.39 | 0 |
| Surfboard-tg-mixed | 6488 | yes | 3.79 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 1.46 | 0 |
| barry-far-vless | 5535 | yes | 2.63 | 0 |
| Surfboard-tg-vless | 5287 | yes | 3.11 | 0 |
| 10ium-ScrapeCategorize-Vless | 5148 | yes | 2.82 | 0 |
| DeltaKronecker-all | 4433 | yes | 5.34 | 0 |
| mahdibland-V2RayAggregator | 4091 | yes | 2.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 23 |
| cn-block | 17 |
| 204 | 16 |
| speed | 12 |
