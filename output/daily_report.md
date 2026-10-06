# AutoNodes 每日报告

生成时间：2026-10-06 00:03:22

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 98529 |
| 去重后节点数 | 27355 |
| TCP 可达数 | 3000 |
| 真测通过数 | 512 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27355 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 79.7 |
| geo | 1.2 |
| probe | 185.9 |
| real_test | 155.2 |
| tcp | 46.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 60 | 37 | 23 | 61.7% |
| hysteria2 | 21 | 20 | 1 | 95.2% |
| shadowsocks | 162 | 160 | 2 | 98.8% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 88 | 87 | 1 | 98.9% |
| vless | 244 | 205 | 39 | 84.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 24 |
| cn-block:TimeoutError | 16 |
| geo:ClientOSError | 7 |
| cn-block:ClientOSError | 4 |
| 204:TimeoutError | 4 |
| geo:TimeoutError | 4 |
| speed:ProxyError | 3 |
| speed:TimeoutError | 3 |
| speed:ClientOSError | 2 |
| 204:ClientOSError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6698 |
| ConnectionRefusedError | 1055 |
| gaierror | 409 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 334 | 0.928 | 1862 |
| Surfboard-tg-mixed | 1.0 | prefer | 53 | 0.962 | 7145 |
| mheidari-all | 0.939 | prefer | 126 | 0.865 | 23213 |
| ermaozi | 0.641 | observe | 60 | 0.617 | 701 |
| DeltaKronecker-all | 0.391 | observe | 2 | 1.0 | 5300 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 177 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5111 |
| Epodonios-all | 0.255 | observe | 0 | None | 7624 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-OutlineReleasedKey | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| ermaozi | 0.617 | 37 | 23 | 60 |
| mheidari-all | 0.865 | 109 | 17 | 126 |
| Au1rxx-base64 | 0.928 | 310 | 24 | 334 |
| Surfboard-tg-mixed | 0.962 | 51 | 2 | 53 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23213 | yes | 3.17 | 0 |
| SoliSpirit-all | 9352 | yes | 2.47 | 0 |
| Epodonios-all | 7624 | yes | 1.94 | 0 |
| Surfboard-tg-mixed | 7145 | yes | 2.37 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 0.99 | 0 |
| barry-far-vless | 5871 | yes | 1.22 | 0 |
| Surfboard-tg-vless | 5642 | yes | 2.19 | 0 |
| DeltaKronecker-all | 5300 | yes | 2.72 | 0 |
| 10ium-ScrapeCategorize-Vless | 5111 | yes | 1.96 | 0 |
| mahdibland-V2RayAggregator | 4375 | yes | 0.88 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 29 |
| cn-block | 21 |
| geo | 11 |
| speed | 8 |
