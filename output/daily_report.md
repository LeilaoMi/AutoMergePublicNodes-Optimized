# AutoNodes 每日报告

生成时间：2026-07-03 03:52:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 103/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77844 |
| 去重后节点数 | 23404 |
| TCP 可达数 | 3000 |
| 真测通过数 | 512 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23404 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 36.8 |
| geo | 1.4 |
| probe | 50.4 |
| real_test | 108.8 |
| tcp | 30.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 136 | 128 | 8 | 94.1% |
| socks | 25 | 21 | 4 | 84.0% |
| trojan | 125 | 115 | 10 | 92.0% |
| vless | 545 | 206 | 339 | 37.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 149 |
| geo:TimeoutError | 115 |
| geo:ClientOSError | 52 |
| speed:TimeoutError | 14 |
| cn-block:ClientOSError | 8 |
| cn-block:TimeoutError | 7 |
| 204:ClientOSError | 5 |
| 204:ProxyError | 4 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4188 |
| ConnectionRefusedError | 712 |
| gaierror | 237 |
| OSError | 154 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.813 | prefer | 324 | 0.735 | 6047 |
| Au1rxx-base64 | 0.725 | prefer | 34 | 0.735 | 73 |
| mheidari-all | 0.649 | observe | 230 | 0.57 | 16051 |
| DeltaKronecker-all | 0.409 | observe | 244 | 0.328 | 7467 |
| nscl5-all | 0.3 | observe | 1 | 1.0 | 1114 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4254 |
| Epodonios-all | 0.255 | observe | 0 | None | 7006 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.141 | observe | 3 | 0.0 | 0 | 1289 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.328 | 80 | 164 | 244 |
| mheidari-all | 0.57 | 131 | 99 | 230 |
| Au1rxx-base64 | 0.735 | 25 | 9 | 34 |
| Surfboard-tg-mixed | 0.735 | 238 | 86 | 324 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16051 | yes | 3.4 | 0 |
| DeltaKronecker-all | 7467 | yes | 3.91 | 0 |
| Epodonios-all | 7006 | yes | 1.68 | 0 |
| SoliSpirit-all | 6800 | yes | 2.74 | 0 |
| Surfboard-tg-mixed | 6047 | yes | 2.07 | 0 |
| mahdibland-V2RayAggregator | 5372 | yes | 1.06 | 0 |
| barry-far-vless | 5102 | yes | 1.68 | 0 |
| Surfboard-tg-vless | 4559 | yes | 2.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 4254 | yes | 1.96 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 167 |
| speed | 163 |
| cn-block | 18 |
| 204 | 13 |
