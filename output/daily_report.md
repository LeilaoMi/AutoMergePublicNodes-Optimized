# AutoNodes 每日报告

生成时间：2026-09-22 21:14:50

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 84314 |
| 去重后节点数 | 23820 |
| TCP 可达数 | 3000 |
| 真测通过数 | 484 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23820 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 82.9 |
| geo | 1.4 |
| probe | 182.3 |
| real_test | 201.8 |
| tcp | 39.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 35 | 26 | 9 | 74.3% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 163 | 155 | 8 | 95.1% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 26 | 17 | 9 | 65.4% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 394 | 260 | 134 | 66.0% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 61 |
| geo:TimeoutError | 22 |
| geo:ClientOSError | 18 |
| 204:ProxyError | 16 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 11 |
| speed:TimeoutError | 7 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5628 |
| ConnectionRefusedError | 818 |
| gaierror | 229 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.967 | prefer | 60 | 0.9 | 7279 |
| Au1rxx-base64 | 0.876 | prefer | 299 | 0.809 | 1718 |
| mheidari-all | 0.804 | prefer | 85 | 0.729 | 15951 |
| ermaozi | 0.787 | prefer | 29 | 0.793 | 325 |
| DeltaKronecker-all | 0.671 | observe | 162 | 0.593 | 6324 |
| tg-oneclickvpnkeys | 0.363 | observe | 3 | 1.0 | 116 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4915 |
| Epodonios-all | 0.255 | observe | 0 | None | 7749 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.233 | 5 | 0.4 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.4 | 2 | 3 | 5 |
| DeltaKronecker-all | 0.593 | 96 | 66 | 162 |
| mheidari-all | 0.729 | 62 | 23 | 85 |
| ermaozi | 0.793 | 23 | 6 | 29 |
| Au1rxx-base64 | 0.809 | 242 | 57 | 299 |
| Surfboard-tg-mixed | 0.9 | 54 | 6 | 60 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15951 | yes | 3.75 | 0 |
| SoliSpirit-all | 9217 | yes | 2.9 | 0 |
| Epodonios-all | 7749 | yes | 2.37 | 0 |
| Surfboard-tg-mixed | 7279 | yes | 2.8 | 0 |
| DeltaKronecker-all | 6324 | yes | 3.96 | 0 |
| Surfboard-tg-vless | 5930 | yes | 3.18 | 0 |
| barry-far-vless | 5928 | yes | 2.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 4915 | yes | 2.03 | 0 |
| mahdibland-V2RayAggregator | 4252 | yes | 0.83 | 0 |
| xiaoji235-airport-v2ray-all | 4242 | yes | 3.99 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| tuic | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 69 |
| geo | 41 |
| 204 | 31 |
| cn-block | 22 |
