# AutoNodes 每日报告

生成时间：2026-08-30 11:44:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79168 |
| 去重后节点数 | 21765 |
| TCP 可达数 | 3000 |
| 真测通过数 | 602 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21765 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 41.3 |
| geo | 1.5 |
| probe | 58.0 |
| real_test | 140.7 |
| tcp | 34.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 148 | 136 | 12 | 91.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 27 | 24 | 3 | 88.9% |
| vless | 491 | 395 | 96 | 80.4% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 26 |
| 204:TimeoutError | 19 |
| geo:ClientOSError | 16 |
| speed:TimeoutError | 13 |
| geo:TimeoutError | 9 |
| speed:ClientOSError | 9 |
| 204:ProxyError | 8 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4502 |
| ConnectionRefusedError | 893 |
| gaierror | 407 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.997 | prefer | 345 | 0.928 | 1804 |
| zhangkai | 0.967 | prefer | 24 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.844 | prefer | 142 | 0.768 | 6846 |
| DeltaKronecker-all | 0.8 | prefer | 191 | 0.723 | 5576 |
| mheidari-all | 0.699 | observe | 10 | 1.0 | 15081 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4762 |
| Epodonios-all | 0.255 | observe | 0 | None | 7251 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3991 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7584 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| chromego_merge | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.723 | 138 | 53 | 191 |
| Surfboard-tg-mixed | 0.768 | 109 | 33 | 142 |
| Au1rxx-base64 | 0.928 | 320 | 25 | 345 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| mheidari-all | 1.0 | 10 | 0 | 10 |
| zhangkai | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15081 | yes | 3.21 | 0 |
| SoliSpirit-all | 7584 | yes | 3.12 | 0 |
| Epodonios-all | 7251 | yes | 3.44 | 0 |
| Surfboard-tg-mixed | 6846 | yes | 2.81 | 0 |
| barry-far-vless | 5864 | yes | 1.94 | 0 |
| Surfboard-tg-vless | 5683 | yes | 2.61 | 0 |
| DeltaKronecker-all | 5576 | yes | 3.77 | 0 |
| 10ium-ScrapeCategorize-Vless | 4762 | yes | 2.4 | 0 |
| MatinGhanbari-all-sub | 3991 | yes | 1.81 | 0 |
| mahdibland-V2RayAggregator | 3949 | yes | 0.16 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 33 |
| 204 | 31 |
| geo | 26 |
| speed | 22 |
