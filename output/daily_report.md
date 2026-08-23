# AutoNodes 每日报告

生成时间：2026-08-23 18:41:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77715 |
| 去重后节点数 | 21484 |
| TCP 可达数 | 3000 |
| 真测通过数 | 644 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21484 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 17.3 |
| generate | 46.3 |
| geo | 1.2 |
| probe | 58.1 |
| real_test | 142.6 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 177 | 158 | 19 | 89.3% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 23 | 21 | 2 | 91.3% |
| vless | 430 | 330 | 100 | 76.7% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 22 |
| 204:TimeoutError | 21 |
| geo:ClientOSError | 17 |
| cn-block:TimeoutError | 17 |
| speed:TimeoutError | 15 |
| 204:ProxyError | 10 |
| speed:ClientOSError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4525 |
| ConnectionRefusedError | 856 |
| gaierror | 456 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | prefer | 112 | 1.0 | 144 |
| Au1rxx-base64 | 0.979 | prefer | 398 | 0.912 | 1729 |
| Surfboard-tg-mixed | 0.817 | prefer | 131 | 0.74 | 6307 |
| mheidari-all | 0.77 | prefer | 69 | 0.696 | 14516 |
| DeltaKronecker-all | 0.498 | observe | 53 | 0.415 | 5415 |
| nscl5-all | 0.298 | observe | 1 | 1.0 | 1082 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 177 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4989 |
| Epodonios-all | 0.255 | observe | 0 | None | 6871 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.415 | 22 | 31 | 53 |
| mheidari-all | 0.696 | 48 | 21 | 69 |
| Surfboard-tg-mixed | 0.74 | 97 | 34 | 131 |
| Au1rxx-base64 | 0.912 | 363 | 35 | 398 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 112 | 0 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14516 | yes | 4.5 | 0 |
| SoliSpirit-all | 6995 | yes | 4.71 | 0 |
| Epodonios-all | 6871 | yes | 4.76 | 0 |
| Surfboard-tg-mixed | 6307 | yes | 4.16 | 0 |
| barry-far-vless | 5492 | yes | 3.17 | 0 |
| DeltaKronecker-all | 5415 | yes | 4.89 | 0 |
| Surfboard-tg-vless | 5215 | yes | 3.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 4989 | yes | 3.42 | 0 |
| mahdibland-V2RayAggregator | 4085 | yes | 0.14 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 2.98 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 39 |
| 204 | 34 |
| cn-block | 26 |
| speed | 23 |
