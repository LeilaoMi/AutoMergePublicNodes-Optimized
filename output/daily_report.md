# AutoNodes 每日报告

生成时间：2026-09-09 16:30:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 84876 |
| 去重后节点数 | 22038 |
| TCP 可达数 | 3000 |
| 真测通过数 | 402 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22038 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 79.4 |
| geo | 1.4 |
| probe | 271.3 |
| real_test | 261.7 |
| tcp | 36.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 31 | 17 | 14 | 54.8% |
| hysteria2 | 19 | 16 | 3 | 84.2% |
| shadowsocks | 125 | 109 | 16 | 87.2% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 24 | 19 | 5 | 79.2% |
| vless | 338 | 240 | 98 | 71.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 39 |
| cn-block:TimeoutError | 27 |
| 204:ProxyError | 23 |
| 204:TimeoutError | 19 |
| cn-block:ClientOSError | 10 |
| 204:ProxyConnectionError | 6 |
| geo:TimeoutError | 5 |
| speed:TimeoutError | 4 |
| speed:ClientOSError | 4 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4511 |
| ConnectionRefusedError | 892 |
| gaierror | 418 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.916 | prefer | 225 | 0.853 | 1634 |
| Surfboard-tg-mixed | 0.82 | prefer | 148 | 0.743 | 7428 |
| DeltaKronecker-all | 0.749 | prefer | 13 | 0.923 | 5187 |
| mheidari-all | 0.662 | observe | 120 | 0.583 | 16618 |
| ermaozi | 0.609 | observe | 25 | 0.6 | 410 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 205 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4795 |
| Epodonios-all | 0.255 | observe | 0 | None | 7926 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9327 |

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
| downweight | ermaozi-get_subscribe | 0.163 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.2 | 1 | 4 | 5 |
| mheidari-all | 0.583 | 70 | 50 | 120 |
| ermaozi | 0.6 | 15 | 10 | 25 |
| Surfboard-tg-mixed | 0.743 | 110 | 38 | 148 |
| Au1rxx-base64 | 0.853 | 192 | 33 | 225 |
| DeltaKronecker-all | 0.923 | 12 | 1 | 13 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16618 | yes | 5.23 | 0 |
| SoliSpirit-all | 9327 | yes | 2.47 | 0 |
| Epodonios-all | 7926 | yes | 5.49 | 0 |
| Surfboard-tg-mixed | 7428 | yes | 3.88 | 0 |
| barry-far-vless | 6336 | yes | 1.9 | 0 |
| Surfboard-tg-vless | 6118 | yes | 4.44 | 0 |
| DeltaKronecker-all | 5187 | yes | 5.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 4795 | yes | 1.32 | 0 |
| mahdibland-V2RayAggregator | 4219 | yes | 1.83 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.65 | 0 |

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
| 204 | 49 |
| geo | 44 |
| cn-block | 37 |
| speed | 8 |
