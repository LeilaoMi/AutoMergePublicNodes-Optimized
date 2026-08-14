# AutoNodes 每日报告

生成时间：2026-08-14 19:06:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78247 |
| 去重后节点数 | 22446 |
| TCP 可达数 | 3000 |
| 真测通过数 | 837 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22446 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 13.2 |
| generate | 37.6 |
| geo | 1.3 |
| probe | 59.6 |
| real_test | 165.6 |
| tcp | 34.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 20 | 18 | 2 | 90.0% |
| shadowsocks | 145 | 131 | 14 | 90.3% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 367 | 350 | 17 | 95.4% |
| vless | 262 | 206 | 56 | 78.6% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 35 |
| geo:TimeoutError | 11 |
| speed:TimeoutError | 9 |
| cn-block:TimeoutError | 9 |
| geo:ClientOSError | 6 |
| 204:ProxyError | 6 |
| speed:ClientOSError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4112 |
| ConnectionRefusedError | 835 |
| gaierror | 415 |
| OSError | 32 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 673 | 0.938 | 1715 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.717 | prefer | 78 | 0.641 | 5725 |
| DeltaKronecker-all | 0.648 | observe | 42 | 0.571 | 5969 |
| mheidari-all | 0.4 | observe | 4 | 0.75 | 15859 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 160 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5157 |
| Epodonios-all | 0.255 | observe | 0 | None | 6388 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3995 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.571 | 24 | 18 | 42 |
| Surfboard-tg-mixed | 0.641 | 50 | 28 | 78 |
| mheidari-all | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.938 | 631 | 42 | 673 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15859 | yes | 4.36 | 0 |
| SoliSpirit-all | 7685 | yes | 4.15 | 0 |
| Epodonios-all | 6388 | yes | 4.53 | 0 |
| DeltaKronecker-all | 5969 | yes | 4.91 | 0 |
| Surfboard-tg-mixed | 5725 | yes | 3.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 5157 | yes | 2.88 | 0 |
| barry-far-vless | 4814 | yes | 1.24 | 0 |
| Surfboard-tg-vless | 4488 | yes | 3.16 | 0 |
| MatinGhanbari-all-sub | 3995 | yes | 1.35 | 0 |
| mahdibland-V2RayAggregator | 3992 | yes | 2.64 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 45 |
| geo | 17 |
| cn-block | 14 |
| speed | 14 |
