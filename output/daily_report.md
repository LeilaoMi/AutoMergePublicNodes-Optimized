# AutoNodes 每日报告

生成时间：2026-08-15 18:42:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 78636 |
| 去重后节点数 | 22463 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1055 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22463 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 10.7 |
| generate | 41.9 |
| geo | 0.8 |
| probe | 74.1 |
| real_test | 189.5 |
| tcp | 34.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 157 | 142 | 15 | 90.4% |
| socks | 7 | 5 | 2 | 71.4% |
| trojan | 592 | 583 | 9 | 98.5% |
| vless | 228 | 181 | 47 | 79.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 19 |
| speed:TimeoutError | 13 |
| cn-block:TimeoutError | 9 |
| 204:ClientOSError | 7 |
| geo:TimeoutError | 7 |
| cn-block:ClientOSError | 6 |
| geo:ClientOSError | 5 |
| speed:ClientOSError | 4 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4714 |
| ConnectionRefusedError | 791 |
| gaierror | 307 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 699 | 0.967 | 1997 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| mheidari-all | 0.951 | prefer | 192 | 0.875 | 16339 |
| Surfboard-tg-mixed | 0.896 | prefer | 74 | 0.824 | 5684 |
| DeltaKronecker-all | 0.663 | observe | 34 | 0.588 | 5773 |
| nscl5-all | 0.349 | observe | 3 | 0.667 | 2081 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 160 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5113 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1997 |
| Epodonios-all | 0.255 | observe | 0 | None | 6266 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.588 | 20 | 14 | 34 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.824 | 61 | 13 | 74 |
| mheidari-all | 0.875 | 168 | 24 | 192 |
| Au1rxx-base64 | 0.967 | 676 | 23 | 699 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16339 | yes | 5.31 | 0 |
| SoliSpirit-all | 7464 | yes | 1.65 | 0 |
| Epodonios-all | 6266 | yes | 3.9 | 0 |
| DeltaKronecker-all | 5773 | yes | 4.11 | 0 |
| Surfboard-tg-mixed | 5684 | yes | 3.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 5113 | yes | 0.86 | 0 |
| barry-far-vless | 4694 | yes | 0.6 | 0 |
| Surfboard-tg-vless | 4350 | yes | 3.05 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 0.67 | 0 |
| mahdibland-V2RayAggregator | 3935 | yes | 2.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| speed | 17 |
| cn-block | 16 |
| geo | 12 |
