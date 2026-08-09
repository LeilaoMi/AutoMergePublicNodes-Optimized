# AutoNodes 每日报告

生成时间：2026-08-09 18:53:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 86184 |
| 去重后节点数 | 24016 |
| TCP 可达数 | 3000 |
| 真测通过数 | 432 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24016 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.6 |
| generate | 38.9 |
| geo | 1.4 |
| probe | 52.3 |
| real_test | 92.6 |
| tcp | 35.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 21 | 21 | 0 | 100.0% |
| hysteria2 | 21 | 21 | 0 | 100.0% |
| shadowsocks | 142 | 125 | 17 | 88.0% |
| socks | 4 | 4 | 0 | 100.0% |
| trojan | 120 | 117 | 3 | 97.5% |
| vless | 205 | 142 | 63 | 69.3% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 18 |
| geo:ClientOSError | 15 |
| cn-block:TimeoutError | 12 |
| speed:TimeoutError | 10 |
| 204:ProxyError | 7 |
| geo:TimeoutError | 7 |
| speed:ClientOSError | 6 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4784 |
| ConnectionRefusedError | 835 |
| gaierror | 333 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.987 | prefer | 371 | 0.922 | 1688 |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Surfboard-tg-mixed | 0.718 | prefer | 92 | 0.641 | 6634 |
| mheidari-all | 0.413 | observe | 28 | 0.321 | 20206 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 107 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5505 |
| Epodonios-all | 0.255 | observe | 0 | None | 7178 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7585 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 9 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.321 | 9 | 19 | 28 |
| Surfboard-tg-mixed | 0.641 | 59 | 33 | 92 |
| Au1rxx-base64 | 0.922 | 342 | 29 | 371 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20206 | yes | 4.46 | 0 |
| SoliSpirit-all | 7585 | yes | 4.43 | 0 |
| Epodonios-all | 7178 | yes | 4.66 | 0 |
| Surfboard-tg-mixed | 6634 | yes | 3.9 | 0 |
| barry-far-vless | 5784 | yes | 2.74 | 0 |
| 10ium-ScrapeCategorize-Vless | 5505 | yes | 2.98 | 0 |
| Surfboard-tg-vless | 5470 | yes | 3.1 | 0 |
| mahdibland-V2RayAggregator | 5189 | yes | 2.68 | 0 |
| DeltaKronecker-all | 4998 | yes | 4.76 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.08 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 28 |
| geo | 24 |
| speed | 17 |
| cn-block | 14 |
