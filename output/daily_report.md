# AutoNodes 每日报告

生成时间：2026-08-24 13:04:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78546 |
| 去重后节点数 | 21951 |
| TCP 可达数 | 3000 |
| 真测通过数 | 572 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21951 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 32.3 |
| geo | 1.5 |
| probe | 54.4 |
| real_test | 120.0 |
| tcp | 35.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 215 | 198 | 17 | 92.1% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 54 | 49 | 5 | 90.7% |
| vless | 374 | 278 | 96 | 74.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 33 |
| geo:TimeoutError | 24 |
| 204:TimeoutError | 21 |
| geo:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| speed:ClientOSError | 7 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 5 |
| 204:ProxyError | 5 |
| cn-block:ProxyError | 4 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4873 |
| ConnectionRefusedError | 844 |
| gaierror | 325 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Au1rxx-base64 | 0.937 | prefer | 357 | 0.874 | 1628 |
| mheidari-all | 0.878 | prefer | 87 | 0.805 | 14541 |
| DeltaKronecker-all | 0.871 | prefer | 65 | 0.8 | 5914 |
| Surfboard-tg-mixed | 0.791 | prefer | 157 | 0.713 | 6395 |
| nscl5-all | 0.352 | observe | 2 | 1.0 | 1008 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 4899 |
| Epodonios-all | 0.255 | observe | 0 | None | 6919 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7302 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.713 | 112 | 45 | 157 |
| DeltaKronecker-all | 0.8 | 52 | 13 | 65 |
| mheidari-all | 0.805 | 70 | 17 | 87 |
| Au1rxx-base64 | 0.874 | 312 | 45 | 357 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14541 | yes | 5.69 | 0 |
| SoliSpirit-all | 7302 | yes | 3.21 | 0 |
| Epodonios-all | 6919 | yes | 3.73 | 0 |
| Surfboard-tg-mixed | 6395 | yes | 4.26 | 0 |
| DeltaKronecker-all | 5914 | yes | 4.93 | 0 |
| barry-far-vless | 5633 | yes | 2.65 | 0 |
| Surfboard-tg-vless | 5345 | yes | 4.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 4899 | yes | 3.88 | 0 |
| mahdibland-V2RayAggregator | 4097 | yes | 3.18 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 4.41 | 0 |

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
| cn-block | 42 |
| geo | 33 |
| 204 | 31 |
| speed | 15 |
