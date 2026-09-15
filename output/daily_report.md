# AutoNodes 每日报告

生成时间：2026-09-15 16:50:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 91321 |
| 去重后节点数 | 25727 |
| TCP 可达数 | 3000 |
| 真测通过数 | 424 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25727 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 77.4 |
| geo | 1.4 |
| probe | 261.7 |
| real_test | 212.7 |
| tcp | 42.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 24 | 18 | 6 | 75.0% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 163 | 148 | 15 | 90.8% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 6 | 6 | 0 | 100.0% |
| vless | 373 | 231 | 142 | 61.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 45 |
| 204:TimeoutError | 33 |
| geo:ClientOSError | 32 |
| cn-block:TimeoutError | 15 |
| speed:ClientOSError | 13 |
| 204:ProxyError | 12 |
| speed:TimeoutError | 6 |
| geo:TimeoutError | 5 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6093 |
| ConnectionRefusedError | 937 |
| gaierror | 347 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.928 | prefer | 312 | 0.869 | 1553 |
| Surfboard-tg-mixed | 0.783 | prefer | 72 | 0.708 | 7516 |
| ermaozi | 0.712 | prefer | 21 | 0.714 | 406 |
| mheidari-all | 0.538 | observe | 177 | 0.458 | 21913 |
| DeltaKronecker-all | 0.349 | observe | 3 | 0.667 | 5932 |
| ermaozi-get_subscribe | 0.328 | observe | 2 | 1.0 | 422 |
| tg-oneclickvpnkeys | 0.317 | observe | 2 | 1.0 | 149 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5015 |
| Epodonios-all | 0.255 | observe | 0 | None | 8076 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.458 | 81 | 96 | 177 |
| DeltaKronecker-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.708 | 51 | 21 | 72 |
| ermaozi | 0.714 | 15 | 6 | 21 |
| Au1rxx-base64 | 0.869 | 271 | 41 | 312 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21913 | yes | 4.0 | 0 |
| SoliSpirit-all | 9411 | yes | 3.28 | 0 |
| Epodonios-all | 8076 | yes | 4.37 | 0 |
| Surfboard-tg-mixed | 7516 | yes | 3.19 | 0 |
| barry-far-vless | 6401 | yes | 0.65 | 0 |
| Surfboard-tg-vless | 6065 | yes | 3.0 | 0 |
| DeltaKronecker-all | 5932 | yes | 4.51 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 1.44 | 0 |
| mahdibland-V2RayAggregator | 4258 | yes | 2.26 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.47 | 0 |

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
| cn-block | 61 |
| 204 | 47 |
| geo | 37 |
| speed | 20 |
