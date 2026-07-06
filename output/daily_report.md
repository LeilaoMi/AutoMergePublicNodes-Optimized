# AutoNodes 每日报告

生成时间：2026-07-06 04:08:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78913 |
| 去重后节点数 | 24116 |
| TCP 可达数 | 3000 |
| 真测通过数 | 448 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24116 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 21.5 |
| geo | 1.3 |
| probe | 42.6 |
| real_test | 79.2 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 144 | 136 | 8 | 94.4% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 260 | 239 | 21 | 91.9% |
| vless | 103 | 28 | 75 | 27.2% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 34 |
| speed:ClientOSError | 27 |
| geo:ClientOSError | 16 |
| 204:ClientOSError | 10 |
| 204:ProxyError | 8 |
| speed:TimeoutError | 3 |
| cn-block:ClientOSError | 3 |
| cn-block:TimeoutError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4445 |
| ConnectionRefusedError | 760 |
| gaierror | 165 |
| OSError | 158 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.987 | prefer | 127 | 0.913 | 5914 |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.969 | prefer | 97 | 0.897 | 16346 |
| Au1rxx-base64 | 0.831 | prefer | 44 | 0.841 | 133 |
| DeltaKronecker-all | 0.77 | prefer | 243 | 0.691 | 7739 |
| nscl5-all | 0.321 | observe | 1 | 1.0 | 1651 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Pawdroid | 0.256 | observe | 1 | 1.0 | 20 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4662 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.691 | 168 | 75 | 243 |
| Au1rxx-base64 | 0.841 | 37 | 7 | 44 |
| mheidari-all | 0.897 | 87 | 10 | 97 |
| Surfboard-tg-mixed | 0.913 | 116 | 11 | 127 |
| Pawdroid | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16346 | yes | 4.22 | 0 |
| DeltaKronecker-all | 7739 | yes | 3.23 | 0 |
| Epodonios-all | 7009 | yes | 0.84 | 0 |
| SoliSpirit-all | 6809 | yes | 2.55 | 0 |
| Surfboard-tg-mixed | 5914 | yes | 2.74 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 0.93 | 0 |
| barry-far-vless | 5045 | yes | 2.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 4662 | yes | 1.81 | 0 |
| Surfboard-tg-vless | 4330 | yes | 2.19 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.72 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 50 |
| speed | 30 |
| 204 | 18 |
| cn-block | 7 |
