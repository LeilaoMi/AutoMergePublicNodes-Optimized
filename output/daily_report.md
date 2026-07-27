# AutoNodes 每日报告

生成时间：2026-07-27 10:07:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84235 |
| 去重后节点数 | 22876 |
| TCP 可达数 | 3000 |
| 真测通过数 | 733 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22876 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 40.6 |
| geo | 1.5 |
| probe | 78.1 |
| real_test | 212.2 |
| tcp | 32.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 5 | 0 | 100.0% |
| http | 76 | 76 | 0 | 100.0% |
| hysteria2 | 11 | 7 | 4 | 63.6% |
| shadowsocks | 122 | 106 | 16 | 86.9% |
| socks | 25 | 21 | 4 | 84.0% |
| trojan | 376 | 327 | 49 | 87.0% |
| vless | 717 | 190 | 527 | 26.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 202 |
| speed:ClientOSError | 177 |
| 204:ProxyError | 54 |
| geo:ClientOSError | 50 |
| cn-block:TimeoutError | 34 |
| 204:TimeoutError | 26 |
| speed:TimeoutError | 25 |
| cn-block:ProxyError | 15 |
| cn-block:ClientOSError | 9 |
| geo:ProxyError | 5 |
| 204:ClientOSError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4420 |
| ConnectionRefusedError | 706 |
| gaierror | 249 |
| OSError | 220 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.991 | prefer | 76 | 1.0 | 86 |
| Au1rxx-base64 | 0.975 | prefer | 426 | 0.92 | 1407 |
| Surfboard-tg-mixed | 0.705 | prefer | 54 | 0.63 | 5483 |
| tg-oneclickvpnkeys | 0.445 | observe | 5 | 1.0 | 132 |
| mheidari-all | 0.413 | observe | 52 | 0.327 | 19339 |
| DeltaKronecker-all | 0.369 | observe | 714 | 0.289 | 5643 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 3959 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 174 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4831 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.289 | 206 | 508 | 714 |
| mheidari-all | 0.327 | 17 | 35 | 52 |
| Surfboard-tg-mixed | 0.63 | 34 | 20 | 54 |
| Au1rxx-base64 | 0.92 | 392 | 34 | 426 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19339 | yes | 4.22 | 0 |
| Epodonios-all | 6410 | yes | 2.27 | 0 |
| SoliSpirit-all | 6188 | yes | 2.8 | 0 |
| DeltaKronecker-all | 5643 | yes | 4.22 | 0 |
| Surfboard-tg-mixed | 5483 | yes | 2.95 | 0 |
| mahdibland-V2RayAggregator | 5017 | yes | 2.35 | 0 |
| 10ium-ScrapeCategorize-Vless | 4831 | yes | 0.82 | 0 |
| barry-far-vless | 4692 | yes | 1.16 | 0 |
| Surfboard-tg-vless | 4173 | yes | 2.58 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 1.78 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 257 |
| speed | 202 |
| 204 | 83 |
| cn-block | 58 |
