# AutoNodes 每日报告

生成时间：2026-09-21 22:02:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 88299 |
| 去重后节点数 | 25177 |
| TCP 可达数 | 3000 |
| 真测通过数 | 511 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25177 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 85.6 |
| geo | 1.5 |
| probe | 268.4 |
| real_test | 201.2 |
| tcp | 42.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 37 | 26 | 11 | 70.3% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 159 | 152 | 7 | 95.6% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 11 | 7 | 4 | 63.6% |
| vless | 483 | 303 | 180 | 62.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 56 |
| geo:ClientOSError | 35 |
| geo:TimeoutError | 27 |
| speed:ClientOSError | 27 |
| 204:ProxyError | 17 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 12 |
| speed:TimeoutError | 10 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6199 |
| ConnectionRefusedError | 912 |
| gaierror | 282 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.937 | prefer | 277 | 0.87 | 1752 |
| Surfboard-tg-mixed | 0.891 | prefer | 72 | 0.819 | 7121 |
| ermaozi | 0.698 | observe | 36 | 0.694 | 350 |
| mheidari-all | 0.638 | observe | 319 | 0.558 | 20197 |
| DeltaKronecker-all | 0.489 | observe | 9 | 0.667 | 6181 |
| ermaozi-get_subscribe | 0.27 | observe | 1 | 1.0 | 377 |
| tg-oneclickvpnkeys | 0.261 | observe | 1 | 1.0 | 138 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5290 |
| Epodonios-all | 0.255 | observe | 0 | None | 7717 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

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

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.558 | 178 | 141 | 319 |
| DeltaKronecker-all | 0.667 | 6 | 3 | 9 |
| ermaozi | 0.694 | 25 | 11 | 36 |
| Surfboard-tg-mixed | 0.819 | 59 | 13 | 72 |
| Au1rxx-base64 | 0.87 | 241 | 36 | 277 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20197 | yes | 5.09 | 0 |
| SoliSpirit-all | 8749 | yes | 1.69 | 0 |
| Epodonios-all | 7717 | yes | 3.97 | 0 |
| Surfboard-tg-mixed | 7121 | yes | 4.18 | 0 |
| DeltaKronecker-all | 6181 | yes | 5.24 | 0 |
| barry-far-vless | 6075 | yes | 0.61 | 0 |
| Surfboard-tg-vless | 5672 | yes | 3.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 5290 | yes | 0.93 | 0 |
| mahdibland-V2RayAggregator | 4344 | yes | 2.92 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 0.72 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 75 |
| geo | 62 |
| speed | 37 |
| 204 | 31 |
