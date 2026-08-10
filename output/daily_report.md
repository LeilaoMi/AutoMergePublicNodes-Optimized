# AutoNodes 每日报告

生成时间：2026-08-10 19:07:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 84993 |
| 去重后节点数 | 24663 |
| TCP 可达数 | 3000 |
| 真测通过数 | 497 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24663 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 33.7 |
| geo | 1.4 |
| probe | 48.9 |
| real_test | 110.5 |
| tcp | 36.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 49 | 49 | 0 | 100.0% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 148 | 138 | 10 | 93.2% |
| socks | 5 | 5 | 0 | 100.0% |
| trojan | 121 | 117 | 4 | 96.7% |
| vless | 253 | 168 | 85 | 66.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 25 |
| 204:ProxyError | 17 |
| 204:TimeoutError | 14 |
| cn-block:TimeoutError | 13 |
| speed:TimeoutError | 12 |
| geo:TimeoutError | 7 |
| speed:ClientOSError | 6 |
| cn-block:ClientOSError | 2 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4456 |
| ConnectionRefusedError | 851 |
| gaierror | 329 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.983 | prefer | 49 | 1.0 | 67 |
| Au1rxx-base64 | 0.966 | prefer | 405 | 0.904 | 1614 |
| mheidari-all | 0.653 | observe | 73 | 0.575 | 20189 |
| Surfboard-tg-mixed | 0.637 | observe | 68 | 0.559 | 6152 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 178 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5881 |
| Epodonios-all | 0.255 | observe | 0 | None | 6803 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.559 | 38 | 30 | 68 |
| mheidari-all | 0.575 | 42 | 31 | 73 |
| Au1rxx-base64 | 0.904 | 366 | 39 | 405 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 49 | 0 | 49 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20189 | yes | 4.99 | 0 |
| SoliSpirit-all | 7537 | yes | 3.69 | 0 |
| Epodonios-all | 6803 | yes | 4.41 | 0 |
| Surfboard-tg-mixed | 6152 | yes | 3.76 | 0 |
| DeltaKronecker-all | 5881 | yes | 4.77 | 0 |
| barry-far-vless | 5417 | yes | 2.86 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 2.64 | 0 |
| mahdibland-V2RayAggregator | 5191 | yes | 2.75 | 0 |
| Surfboard-tg-vless | 5085 | yes | 3.56 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 3.32 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 33 |
| 204 | 32 |
| speed | 19 |
| cn-block | 16 |
