# AutoNodes 每日报告

生成时间：2026-08-26 13:06:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 78650 |
| 去重后节点数 | 22232 |
| TCP 可达数 | 3000 |
| 真测通过数 | 518 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22232 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 33.7 |
| geo | 1.4 |
| probe | 56.9 |
| real_test | 118.6 |
| tcp | 36.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 24 | 1 | 96.0% |
| hysteria2 | 24 | 24 | 0 | 100.0% |
| shadowsocks | 174 | 160 | 14 | 92.0% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 32 | 23 | 9 | 71.9% |
| vless | 375 | 285 | 90 | 76.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 45 |
| 204:TimeoutError | 20 |
| cn-block:TimeoutError | 19 |
| 204:ProxyError | 8 |
| speed:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| geo:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 2 |
| geo:TimeoutError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:49471: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5172 |
| ConnectionRefusedError | 851 |
| gaierror | 224 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.978 | prefer | 323 | 0.901 | 1988 |
| DeltaKronecker-all | 0.933 | prefer | 32 | 0.875 | 6107 |
| zhangkai | 0.926 | prefer | 23 | 0.957 | 144 |
| Surfboard-tg-mixed | 0.8 | prefer | 166 | 0.723 | 6535 |
| mheidari-all | 0.692 | observe | 83 | 0.614 | 14222 |
| nscl5-all | 0.435 | observe | 4 | 1.0 | 887 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 206 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4825 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1992 |
| Epodonios-all | 0.255 | observe | 0 | None | 7011 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.614 | 51 | 32 | 83 |
| Surfboard-tg-mixed | 0.723 | 120 | 46 | 166 |
| DeltaKronecker-all | 0.875 | 28 | 4 | 32 |
| Au1rxx-base64 | 0.901 | 291 | 32 | 323 |
| zhangkai | 0.957 | 22 | 1 | 23 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| nscl5-all | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14222 | yes | 6.69 | 0 |
| SoliSpirit-all | 7145 | yes | 5.76 | 0 |
| Epodonios-all | 7011 | yes | 0.95 | 0 |
| Surfboard-tg-mixed | 6535 | yes | 4.31 | 0 |
| DeltaKronecker-all | 6107 | yes | 4.46 | 0 |
| barry-far-vless | 5628 | yes | 5.08 | 0 |
| Surfboard-tg-vless | 5395 | yes | 4.11 | 0 |
| 10ium-ScrapeCategorize-Vless | 4825 | yes | 3.43 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 3.19 | 0 |
| mahdibland-V2RayAggregator | 3981 | yes | 1.77 | 0 |

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
| speed | 53 |
| 204 | 30 |
| cn-block | 26 |
| geo | 6 |
| sing-box exited 1 | 1 |
