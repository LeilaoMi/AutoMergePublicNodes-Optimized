# AutoNodes 每日报告

生成时间：2026-08-22 18:42:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 86102 |
| 去重后节点数 | 23834 |
| TCP 可达数 | 3000 |
| 真测通过数 | 721 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23834 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.2 |
| generate | 36.3 |
| geo | 1.5 |
| probe | 60.2 |
| real_test | 155.6 |
| tcp | 40.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 113 | 113 | 0 | 100.0% |
| hysteria2 | 21 | 20 | 1 | 95.2% |
| shadowsocks | 171 | 159 | 12 | 93.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 161 | 156 | 5 | 96.9% |
| vless | 353 | 272 | 81 | 77.1% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 29 |
| cn-block:TimeoutError | 18 |
| geo:TimeoutError | 15 |
| speed:TimeoutError | 11 |
| geo:ClientOSError | 8 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| speed:ClientOSError | 4 |
| 204:ProxyError | 4 |
| 204:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4995 |
| ConnectionRefusedError | 1021 |
| gaierror | 721 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 487 | 0.936 | 1853 |
| zhangkai | 0.997 | prefer | 112 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.784 | prefer | 123 | 0.707 | 6394 |
| mheidari-all | 0.78 | prefer | 88 | 0.705 | 14443 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5974 |
| DeltaKronecker-all | 0.272 | observe | 7 | 0.286 | 5015 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 176 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5096 |
| Epodonios-all | 0.255 | observe | 0 | None | 6972 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-OutlineReleasedKey | 0.13 | observe | 1 | 0.0 | 0 | 58 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-OutlineReleasedKey | 0.0 | 0 | 1 | 1 |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.286 | 2 | 5 | 7 |
| mheidari-all | 0.705 | 62 | 26 | 88 |
| Surfboard-tg-mixed | 0.707 | 87 | 36 | 123 |
| Au1rxx-base64 | 0.936 | 456 | 31 | 487 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 112 | 0 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14443 | yes | 5.54 | 0 |
| SoliSpirit-all | 7145 | yes | 4.15 | 0 |
| Epodonios-all | 6972 | yes | 5.97 | 0 |
| Surfboard-tg-mixed | 6394 | yes | 3.97 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 3.79 | 0 |
| barry-far-vless | 5526 | yes | 3.11 | 0 |
| Surfboard-tg-vless | 5216 | yes | 1.73 | 0 |
| 10ium-ScrapeCategorize-Vless | 5096 | yes | 3.32 | 0 |
| DeltaKronecker-all | 5015 | yes | 5.14 | 0 |
| mahdibland-V2RayAggregator | 4074 | yes | 0.38 | 0 |

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
| 204 | 34 |
| cn-block | 28 |
| geo | 23 |
| speed | 16 |
