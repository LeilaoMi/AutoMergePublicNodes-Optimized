# AutoNodes 每日报告

生成时间：2026-09-02 11:03:52

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 82681 |
| 去重后节点数 | 23587 |
| TCP 可达数 | 3000 |
| 真测通过数 | 602 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23587 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 26.0 |
| geo | 1.3 |
| probe | 73.2 |
| real_test | 123.4 |
| tcp | 38.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 141 | 131 | 10 | 92.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 27 | 19 | 8 | 70.4% |
| vless | 516 | 406 | 110 | 78.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 24 |
| geo:ClientOSError | 23 |
| 204:TimeoutError | 22 |
| speed:TimeoutError | 19 |
| geo:TimeoutError | 12 |
| 204:ClientOSError | 8 |
| speed:ClientOSError | 8 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:44424: bind: address already in use | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5072 |
| ConnectionRefusedError | 895 |
| gaierror | 316 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.968 | prefer | 409 | 0.897 | 1826 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| mheidari-all | 0.809 | prefer | 127 | 0.732 | 15813 |
| Surfboard-tg-mixed | 0.8 | prefer | 159 | 0.723 | 7112 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 102 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 47 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4765 |
| Epodonios-all | 0.255 | observe | 0 | None | 7428 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7727 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.239 | 12 | 0.167 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.167 | 2 | 10 | 12 |
| Surfboard-tg-mixed | 0.723 | 115 | 44 | 159 |
| mheidari-all | 0.732 | 93 | 34 | 127 |
| Au1rxx-base64 | 0.897 | 367 | 42 | 409 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15813 | yes | 3.21 | 0 |
| SoliSpirit-all | 7727 | yes | 2.82 | 0 |
| Epodonios-all | 7428 | yes | 3.61 | 0 |
| DeltaKronecker-all | 7295 | yes | 4.06 | 0 |
| Surfboard-tg-mixed | 7112 | yes | 2.88 | 0 |
| barry-far-vless | 6070 | yes | 2.04 | 0 |
| Surfboard-tg-vless | 5992 | yes | 3.84 | 0 |
| 10ium-ScrapeCategorize-Vless | 4765 | yes | 1.89 | 0 |
| mahdibland-V2RayAggregator | 4066 | yes | 0.96 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.74 | 0 |

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
| 204 | 36 |
| geo | 35 |
| cn-block | 31 |
| speed | 28 |
| sing-box exited 1 | 1 |
