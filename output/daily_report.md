# AutoNodes 每日报告

生成时间：2026-09-21 04:35:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 83915 |
| 去重后节点数 | 23652 |
| TCP 可达数 | 3000 |
| 真测通过数 | 672 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23652 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 79.4 |
| geo | 1.4 |
| probe | 272.9 |
| real_test | 449.0 |
| tcp | 39.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 54 | 38 | 16 | 70.4% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 185 | 177 | 8 | 95.7% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 44 | 27 | 17 | 61.4% |
| vless | 772 | 408 | 364 | 52.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 168 |
| geo:ClientOSError | 71 |
| speed:TimeoutError | 54 |
| speed:ClientOSError | 46 |
| 204:ProxyError | 25 |
| cn-block:ClientOSError | 16 |
| cn-block:TimeoutError | 12 |
| cn-block:ProxyError | 5 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 3 |
| 204:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5295 |
| ConnectionRefusedError | 795 |
| gaierror | 334 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.933 | prefer | 332 | 0.867 | 1693 |
| Surfboard-tg-mixed | 0.736 | prefer | 123 | 0.659 | 7202 |
| ermaozi | 0.7 | prefer | 49 | 0.694 | 355 |
| mheidari-all | 0.57 | observe | 100 | 0.49 | 15960 |
| DeltaKronecker-all | 0.551 | observe | 450 | 0.471 | 6092 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4315 |
| ermaozi-get_subscribe | 0.297 | observe | 10 | 0.4 | 382 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 74 |
| Epodonios-all | 0.255 | observe | 0 | None | 7661 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | 10ium-ScrapeCategorize-Vless | 0.202 | 8 | 0.125 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| 10ium-ScrapeCategorize-Vless | 0.125 | 1 | 7 | 8 |
| ermaozi-get_subscribe | 0.4 | 4 | 6 | 10 |
| DeltaKronecker-all | 0.471 | 212 | 238 | 450 |
| mheidari-all | 0.49 | 49 | 51 | 100 |
| Surfboard-tg-mixed | 0.659 | 81 | 42 | 123 |
| ermaozi | 0.694 | 34 | 15 | 49 |
| Au1rxx-base64 | 0.867 | 288 | 44 | 332 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15960 | yes | 4.95 | 0 |
| SoliSpirit-all | 8828 | yes | 2.12 | 0 |
| Epodonios-all | 7661 | yes | 3.45 | 0 |
| Surfboard-tg-mixed | 7202 | yes | 3.71 | 0 |
| DeltaKronecker-all | 6092 | yes | 5.69 | 0 |
| barry-far-vless | 6015 | yes | 1.38 | 0 |
| Surfboard-tg-vless | 5800 | yes | 3.98 | 0 |
| 10ium-ScrapeCategorize-Vless | 5238 | yes | 1.18 | 0 |
| mahdibland-V2RayAggregator | 4315 | yes | 3.2 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.95 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 242 |
| speed | 100 |
| cn-block | 33 |
| 204 | 32 |
