# AutoNodes 每日报告

生成时间：2026-09-08 16:35:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 90488 |
| 去重后节点数 | 25021 |
| TCP 可达数 | 3000 |
| 真测通过数 | 458 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25021 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 90.2 |
| geo | 1.4 |
| probe | 285.3 |
| real_test | 269.2 |
| tcp | 42.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 36 | 22 | 14 | 61.1% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 164 | 141 | 23 | 86.0% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 19 | 16 | 3 | 84.2% |
| vless | 395 | 256 | 139 | 64.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 45 |
| geo:ClientOSError | 40 |
| 204:ProxyError | 27 |
| 204:TimeoutError | 20 |
| cn-block:TimeoutError | 18 |
| speed:ClientOSError | 10 |
| 204:ClientOSError | 10 |
| speed:TimeoutError | 5 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5948 |
| ConnectionRefusedError | 980 |
| gaierror | 451 |
| OSError | 239 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.965 | prefer | 305 | 0.902 | 1658 |
| Surfboard-tg-mixed | 0.721 | prefer | 90 | 0.644 | 7484 |
| ermaozi | 0.674 | observe | 33 | 0.667 | 409 |
| mheidari-all | 0.573 | observe | 205 | 0.493 | 21582 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 212 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4657 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 6097 |
| Epodonios-all | 0.255 | observe | 0 | None | 7932 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 4 | 4 |
| mheidari-all | 0.493 | 101 | 104 | 205 |
| Surfboard-tg-mixed | 0.644 | 58 | 32 | 90 |
| ermaozi | 0.667 | 22 | 11 | 33 |
| Au1rxx-base64 | 0.902 | 275 | 30 | 305 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21582 | yes | 5.33 | 0 |
| SoliSpirit-all | 8703 | yes | 4.04 | 0 |
| Epodonios-all | 7932 | yes | 0.36 | 0 |
| Surfboard-tg-mixed | 7484 | yes | 2.98 | 0 |
| barry-far-vless | 6501 | yes | 3.25 | 0 |
| Surfboard-tg-vless | 6283 | yes | 4.12 | 0 |
| DeltaKronecker-all | 6097 | yes | 4.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 4657 | yes | 3.49 | 0 |
| mahdibland-V2RayAggregator | 4209 | yes | 0.15 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.32 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 65 |
| 204 | 57 |
| geo | 45 |
| speed | 15 |
