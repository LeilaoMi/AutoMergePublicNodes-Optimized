# AutoNodes 每日报告

生成时间：2026-08-02 03:33:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/2 |
| 清理建议：优先/观察 | 2/103 |
| 原始节点数 | 78379 |
| 去重后节点数 | 23363 |
| TCP 可达数 | 3000 |
| 真测通过数 | 730 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23363 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 20.2 |
| geo | 1.3 |
| probe | 60.0 |
| real_test | 190.0 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 146 | 146 | 0 | 100.0% |
| hysteria2 | 21 | 20 | 1 | 95.2% |
| shadowsocks | 161 | 150 | 11 | 93.2% |
| socks | 8 | 5 | 3 | 62.5% |
| trojan | 53 | 35 | 18 | 66.0% |
| vless | 829 | 373 | 456 | 45.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 270 |
| speed:ClientOSError | 64 |
| geo:ClientOSError | 58 |
| speed:TimeoutError | 52 |
| cn-block:TimeoutError | 22 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 4 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4863 |
| ConnectionRefusedError | 786 |
| gaierror | 229 |
| OSError | 222 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | prefer | 147 | 1.0 | 194 |
| Au1rxx-base64 | 0.948 | prefer | 501 | 0.886 | 1590 |
| Surfboard-tg-mixed | 0.647 | observe | 118 | 0.568 | 5146 |
| nscl5-all | 0.262 | observe | 2 | 0.5 | 1354 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 57 |
| mheidari-all | 0.255 | observe | 9 | 0.222 | 16695 |
| Epodonios-all | 0.255 | observe | 0 | None | 5783 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3973 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6873 |

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
| ninja-vless | 0.136 | downweight | 7 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ninja-vless | 0.136 | 7 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |
| downweight | DeltaKronecker-all | 0.237 | 430 | 0.156 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 7 | 7 |
| DeltaKronecker-all | 0.156 | 67 | 363 | 430 |
| mheidari-all | 0.222 | 2 | 7 | 9 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.568 | 67 | 51 | 118 |
| Au1rxx-base64 | 0.886 | 444 | 57 | 501 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16695 | yes | 3.78 | 0 |
| SoliSpirit-all | 6873 | yes | 2.21 | 0 |
| Epodonios-all | 5783 | yes | 4.02 | 0 |
| DeltaKronecker-all | 5497 | yes | 2.41 | 0 |
| 10ium-ScrapeCategorize-Vless | 5391 | yes | 1.72 | 0 |
| Surfboard-tg-mixed | 5146 | yes | 2.44 | 0 |
| mahdibland-V2RayAggregator | 5071 | yes | 1.91 | 0 |
| barry-far-vless | 4431 | yes | 1.15 | 0 |
| Surfboard-tg-vless | 4069 | yes | 2.83 | 0 |
| MatinGhanbari-all-sub | 3973 | yes | 1.76 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 328 |
| speed | 117 |
| cn-block | 30 |
| 204 | 14 |
