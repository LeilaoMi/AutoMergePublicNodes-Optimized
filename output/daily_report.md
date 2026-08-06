# AutoNodes 每日报告

生成时间：2026-08-06 08:49:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 88936 |
| 去重后节点数 | 24432 |
| TCP 可达数 | 3000 |
| 真测通过数 | 450 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24432 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 18.4 |
| generate | 49.5 |
| geo | 1.4 |
| probe | 45.4 |
| real_test | 86.9 |
| tcp | 36.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 21 | 18 | 3 | 85.7% |
| shadowsocks | 161 | 152 | 9 | 94.4% |
| socks | 11 | 6 | 5 | 54.5% |
| trojan | 166 | 156 | 10 | 94.0% |
| vless | 174 | 97 | 77 | 55.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 31 |
| geo:ClientOSError | 26 |
| cn-block:TimeoutError | 10 |
| 204:ClientOSError | 9 |
| 204:TimeoutError | 7 |
| 204:ProxyError | 6 |
| speed:TimeoutError | 5 |
| speed:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4763 |
| ConnectionRefusedError | 815 |
| gaierror | 317 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 351 | 0.949 | 1409 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.653 | observe | 122 | 0.574 | 5873 |
| DeltaKronecker-all | 0.555 | observe | 17 | 0.529 | 5897 |
| mheidari-all | 0.47 | observe | 39 | 0.385 | 20781 |
| nscl5-all | 0.32 | observe | 1 | 1.0 | 1621 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 5214 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5219 |
| Epodonios-all | 0.255 | observe | 0 | None | 6505 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.385 | 15 | 24 | 39 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.529 | 9 | 8 | 17 |
| Surfboard-tg-mixed | 0.574 | 70 | 52 | 122 |
| Au1rxx-base64 | 0.949 | 333 | 18 | 351 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20781 | yes | 3.99 | 0 |
| SoliSpirit-all | 7196 | yes | 3.71 | 0 |
| Epodonios-all | 6505 | yes | 3.47 | 0 |
| DeltaKronecker-all | 5897 | yes | 4.45 | 0 |
| Surfboard-tg-mixed | 5873 | yes | 3.0 | 0 |
| 10ium-ScrapeCategorize-Vless | 5219 | yes | 1.82 | 0 |
| xiaoji235-airport-v2ray-all | 5214 | yes | 1.71 | 0 |
| mahdibland-V2RayAggregator | 5212 | yes | 0.54 | 0 |
| barry-far-vless | 5049 | yes | 1.96 | 0 |
| Surfboard-tg-vless | 4677 | yes | 2.3 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 57 |
| 204 | 22 |
| cn-block | 16 |
| speed | 9 |
