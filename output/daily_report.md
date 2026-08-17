# AutoNodes 每日报告

生成时间：2026-08-17 01:45:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 80829 |
| 去重后节点数 | 22248 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1311 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22248 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 30.2 |
| geo | 1.0 |
| probe | 76.1 |
| real_test | 244.4 |
| tcp | 33.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 127 | 1 | 99.2% |
| hysteria2 | 24 | 24 | 0 | 100.0% |
| shadowsocks | 136 | 131 | 5 | 96.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 687 | 675 | 12 | 98.3% |
| vless | 585 | 352 | 233 | 60.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 105 |
| speed:TimeoutError | 44 |
| cn-block:TimeoutError | 40 |
| geo:ClientOSError | 22 |
| speed:ClientOSError | 16 |
| 204:TimeoutError | 7 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:45089: bind: address already in use | 1 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4304 |
| ConnectionRefusedError | 819 |
| gaierror | 314 |
| OSError | 14 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 913 | 0.966 | 1994 |
| zhangkai | 0.991 | prefer | 127 | 0.992 | 159 |
| Surfboard-tg-mixed | 0.908 | prefer | 132 | 0.833 | 5916 |
| mheidari-all | 0.651 | observe | 324 | 0.571 | 17074 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 3043 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 129 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4990 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1994 |
| Epodonios-all | 0.255 | observe | 0 | None | 6595 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.186 | 64 | 0.094 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.094 | 6 | 58 | 64 |
| mheidari-all | 0.571 | 185 | 139 | 324 |
| Surfboard-tg-mixed | 0.833 | 110 | 22 | 132 |
| Au1rxx-base64 | 0.966 | 882 | 31 | 913 |
| zhangkai | 0.992 | 126 | 1 | 127 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17074 | yes | 4.56 | 0 |
| SoliSpirit-all | 7537 | yes | 4.89 | 0 |
| Epodonios-all | 6595 | yes | 4.82 | 0 |
| Surfboard-tg-mixed | 5916 | yes | 3.44 | 0 |
| DeltaKronecker-all | 5092 | yes | 5.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 4990 | yes | 2.76 | 0 |
| barry-far-vless | 4905 | yes | 2.41 | 0 |
| Surfboard-tg-vless | 4572 | yes | 3.6 | 0 |
| mahdibland-V2RayAggregator | 4025 | yes | 0.3 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 2.5 | 0 |

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
| geo | 128 |
| speed | 60 |
| cn-block | 45 |
| 204 | 18 |
| sing-box exited 1 | 1 |
