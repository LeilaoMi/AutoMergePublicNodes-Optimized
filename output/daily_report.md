# AutoNodes 每日报告

生成时间：2026-09-15 04:39:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 90171 |
| 去重后节点数 | 25748 |
| TCP 可达数 | 3000 |
| 真测通过数 | 510 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25748 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| generate | 84.8 |
| geo | 1.5 |
| probe | 372.1 |
| real_test | 583.8 |
| tcp | 41.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 43 | 23 | 20 | 53.5% |
| hysteria2 | 28 | 27 | 1 | 96.4% |
| shadowsocks | 163 | 153 | 10 | 93.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 5 | 4 | 1 | 80.0% |
| vless | 859 | 301 | 558 | 35.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 204 |
| geo:ClientOSError | 99 |
| speed:TimeoutError | 96 |
| cn-block:ClientOSError | 65 |
| speed:ClientOSError | 59 |
| cn-block:TimeoutError | 28 |
| 204:ProxyError | 25 |
| 204:TimeoutError | 12 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5489 |
| ConnectionRefusedError | 972 |
| gaierror | 496 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.879 | prefer | 286 | 0.818 | 1584 |
| Surfboard-tg-mixed | 0.767 | prefer | 164 | 0.689 | 7572 |
| ermaozi | 0.531 | observe | 35 | 0.514 | 425 |
| ermaozi-get_subscribe | 0.384 | observe | 8 | 0.625 | 447 |
| DeltaKronecker-all | 0.322 | observe | 16 | 0.25 | 5972 |
| mheidari-all | 0.309 | observe | 588 | 0.228 | 21540 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 120 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4914 |
| Epodonios-all | 0.255 | observe | 0 | None | 8044 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.228 | 134 | 454 | 588 |
| DeltaKronecker-all | 0.25 | 4 | 12 | 16 |
| ermaozi | 0.514 | 18 | 17 | 35 |
| ermaozi-get_subscribe | 0.625 | 5 | 3 | 8 |
| Surfboard-tg-mixed | 0.689 | 113 | 51 | 164 |
| Au1rxx-base64 | 0.818 | 234 | 52 | 286 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21540 | yes | 5.03 | 0 |
| SoliSpirit-all | 8754 | yes | 4.88 | 0 |
| Epodonios-all | 8044 | yes | 5.24 | 0 |
| Surfboard-tg-mixed | 7572 | yes | 3.62 | 0 |
| barry-far-vless | 6333 | yes | 1.0 | 0 |
| Surfboard-tg-vless | 6105 | yes | 3.84 | 0 |
| DeltaKronecker-all | 5972 | yes | 5.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 4914 | yes | 1.3 | 0 |
| mahdibland-V2RayAggregator | 4099 | yes | 0.49 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.08 | 0 |

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
| geo | 303 |
| speed | 156 |
| cn-block | 95 |
| 204 | 37 |
