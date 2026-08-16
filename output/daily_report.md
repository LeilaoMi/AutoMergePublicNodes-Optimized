# AutoNodes 每日报告

生成时间：2026-08-16 18:42:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79897 |
| 去重后节点数 | 21949 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1043 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21949 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 43.5 |
| geo | 0.6 |
| probe | 77.0 |
| real_test | 244.7 |
| tcp | 33.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 122 | 111 | 11 | 91.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 589 | 588 | 1 | 99.8% |
| vless | 261 | 195 | 66 | 74.7% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 18 |
| cn-block:TimeoutError | 13 |
| speed:TimeoutError | 12 |
| geo:TimeoutError | 9 |
| geo:ClientOSError | 7 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| speed:ClientOSError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4341 |
| ConnectionRefusedError | 815 |
| gaierror | 333 |
| OSError | 15 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 748 | 0.967 | 1994 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| mheidari-all | 0.859 | prefer | 152 | 0.783 | 17005 |
| Surfboard-tg-mixed | 0.835 | prefer | 92 | 0.761 | 5798 |
| nscl5-all | 0.391 | observe | 2 | 1.0 | 2601 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 174 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4990 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1994 |
| Epodonios-all | 0.255 | observe | 0 | None | 6468 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3982 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.25 | 1 | 3 | 4 |
| Surfboard-tg-mixed | 0.761 | 70 | 22 | 92 |
| mheidari-all | 0.783 | 119 | 33 | 152 |
| Au1rxx-base64 | 0.967 | 723 | 25 | 748 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17005 | yes | 4.33 | 0 |
| SoliSpirit-all | 7449 | yes | 1.41 | 0 |
| Epodonios-all | 6468 | yes | 4.5 | 0 |
| Surfboard-tg-mixed | 5798 | yes | 3.87 | 0 |
| DeltaKronecker-all | 5092 | yes | 4.24 | 0 |
| 10ium-ScrapeCategorize-Vless | 4990 | yes | 1.15 | 0 |
| barry-far-vless | 4856 | yes | 0.8 | 0 |
| Surfboard-tg-vless | 4549 | yes | 3.26 | 0 |
| mahdibland-V2RayAggregator | 4025 | yes | 2.43 | 0 |
| MatinGhanbari-all-sub | 3982 | yes | 0.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 29 |
| cn-block | 23 |
| geo | 16 |
| speed | 15 |
