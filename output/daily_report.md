# AutoNodes 每日报告

生成时间：2026-09-23 04:30:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 96642 |
| 去重后节点数 | 26618 |
| TCP 可达数 | 3000 |
| 真测通过数 | 564 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26618 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 80.5 |
| geo | 1.8 |
| probe | 381.3 |
| real_test | 506.7 |
| tcp | 43.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 59 | 43 | 16 | 72.9% |
| hysteria2 | 25 | 25 | 0 | 100.0% |
| shadowsocks | 181 | 174 | 7 | 96.1% |
| socks | 14 | 7 | 7 | 50.0% |
| trojan | 31 | 25 | 6 | 80.6% |
| vless | 829 | 289 | 540 | 34.9% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 198 |
| speed:ClientOSError | 97 |
| geo:ClientOSError | 89 |
| speed:TimeoutError | 85 |
| cn-block:ClientOSError | 47 |
| 204:ProxyError | 19 |
| 204:TimeoutError | 18 |
| cn-block:TimeoutError | 14 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 2 |
| 204:ProxyConnectionError | 1 |
| geo:exit-country | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6214 |
| ConnectionRefusedError | 934 |
| gaierror | 251 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.904 | prefer | 331 | 0.843 | 1585 |
| ermaozi | 0.726 | prefer | 57 | 0.719 | 346 |
| Surfboard-tg-mixed | 0.633 | observe | 244 | 0.553 | 7168 |
| DeltaKronecker-all | 0.389 | observe | 13 | 0.385 | 6324 |
| mheidari-all | 0.289 | observe | 490 | 0.208 | 22274 |
| ermaozi-get_subscribe | 0.283 | observe | 3 | 0.667 | 372 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4915 |
| Epodonios-all | 0.255 | observe | 0 | None | 7633 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8890 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.208 | 102 | 388 | 490 |
| DeltaKronecker-all | 0.385 | 5 | 8 | 13 |
| Surfboard-tg-mixed | 0.553 | 135 | 109 | 244 |
| ermaozi-get_subscribe | 0.667 | 2 | 1 | 3 |
| ermaozi | 0.719 | 41 | 16 | 57 |
| Au1rxx-base64 | 0.843 | 279 | 52 | 331 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22274 | yes | 5.63 | 0 |
| SoliSpirit-all | 8890 | yes | 2.99 | 0 |
| Epodonios-all | 7633 | yes | 2.61 | 0 |
| Surfboard-tg-mixed | 7168 | yes | 3.4 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.24 | 0 |
| DeltaKronecker-all | 6324 | yes | 4.16 | 0 |
| barry-far-vless | 6054 | yes | 1.66 | 0 |
| Surfboard-tg-vless | 5836 | yes | 4.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 4915 | yes | 1.36 | 0 |
| mahdibland-V2RayAggregator | 4252 | yes | 2.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 288 |
| speed | 183 |
| cn-block | 65 |
| 204 | 40 |
