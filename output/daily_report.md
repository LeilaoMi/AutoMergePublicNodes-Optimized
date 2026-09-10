# AutoNodes 每日报告

生成时间：2026-09-10 11:11:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 91201 |
| 去重后节点数 | 24193 |
| TCP 可达数 | 3000 |
| 真测通过数 | 451 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24193 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 88.0 |
| geo | 1.4 |
| probe | 272.2 |
| real_test | 266.2 |
| tcp | 40.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 53 | 32 | 21 | 60.4% |
| hysteria2 | 22 | 22 | 0 | 100.0% |
| shadowsocks | 160 | 149 | 11 | 93.1% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 44 | 19 | 25 | 43.2% |
| vless | 297 | 224 | 73 | 75.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 26 |
| 204:TimeoutError | 26 |
| 204:ProxyError | 19 |
| geo:TimeoutError | 13 |
| 204:ProxyConnectionError | 12 |
| cn-block:TimeoutError | 10 |
| speed:ClientOSError | 10 |
| cn-block:ClientOSError | 8 |
| speed:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4988 |
| ConnectionRefusedError | 959 |
| gaierror | 477 |
| OSError | 244 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.973 | prefer | 268 | 0.91 | 1628 |
| Surfboard-tg-mixed | 0.848 | prefer | 166 | 0.771 | 7439 |
| mheidari-all | 0.628 | observe | 71 | 0.549 | 19290 |
| ermaozi | 0.618 | observe | 53 | 0.604 | 449 |
| DeltaKronecker-all | 0.372 | observe | 22 | 0.273 | 5853 |
| ermaozi-get_subscribe | 0.274 | observe | 1 | 1.0 | 469 |
| tg-oneclickvpnkeys | 0.264 | observe | 1 | 1.0 | 214 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4995 |
| Epodonios-all | 0.255 | observe | 0 | None | 7808 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| DeltaKronecker-all | 0.273 | 6 | 16 | 22 |
| mheidari-all | 0.549 | 39 | 32 | 71 |
| ermaozi | 0.604 | 32 | 21 | 53 |
| Surfboard-tg-mixed | 0.771 | 128 | 38 | 166 |
| Au1rxx-base64 | 0.91 | 244 | 24 | 268 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19290 | yes | 5.26 | 0 |
| SoliSpirit-all | 8703 | yes | 5.62 | 0 |
| Epodonios-all | 7808 | yes | 3.51 | 0 |
| Surfboard-tg-mixed | 7439 | yes | 4.15 | 0 |
| barry-far-vless | 6215 | yes | 3.59 | 0 |
| Surfboard-tg-vless | 6025 | yes | 3.87 | 0 |
| DeltaKronecker-all | 5853 | yes | 5.62 | 0 |
| 10ium-ScrapeCategorize-Vless | 4995 | yes | 3.37 | 0 |
| mahdibland-V2RayAggregator | 4358 | yes | 0.31 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 60 |
| geo | 39 |
| cn-block | 19 |
| speed | 14 |
