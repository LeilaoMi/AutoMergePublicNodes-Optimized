# AutoNodes 每日报告

生成时间：2026-09-24 11:38:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 96310 |
| 去重后节点数 | 26222 |
| TCP 可达数 | 3000 |
| 真测通过数 | 380 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26222 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| generate | 91.4 |
| geo | 1.4 |
| probe | 306.1 |
| real_test | 171.7 |
| tcp | 42.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 67 | 40 | 27 | 59.7% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 160 | 147 | 13 | 91.9% |
| socks | 7 | 4 | 3 | 57.1% |
| trojan | 27 | 23 | 4 | 85.2% |
| vless | 234 | 144 | 90 | 61.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 26 |
| 204:TimeoutError | 23 |
| cn-block:ClientOSError | 21 |
| cn-block:TimeoutError | 18 |
| speed:TimeoutError | 16 |
| geo:TimeoutError | 16 |
| geo:ClientOSError | 9 |
| 204:ProxyConnectionError | 3 |
| 204:ClientOSError | 2 |
| speed:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6069 |
| ConnectionRefusedError | 970 |
| gaierror | 353 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.922 | prefer | 99 | 0.848 | 7027 |
| Au1rxx-base64 | 0.916 | prefer | 218 | 0.853 | 1658 |
| ermaozi | 0.625 | observe | 52 | 0.615 | 339 |
| mheidari-all | 0.617 | observe | 121 | 0.537 | 22399 |
| ermaozi-get_subscribe | 0.49 | observe | 17 | 0.529 | 373 |
| DeltaKronecker-all | 0.401 | observe | 7 | 0.571 | 5845 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5307 |
| Epodonios-all | 0.255 | observe | 0 | None | 7495 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8857 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.529 | 9 | 8 | 17 |
| mheidari-all | 0.537 | 65 | 56 | 121 |
| DeltaKronecker-all | 0.571 | 4 | 3 | 7 |
| ermaozi | 0.615 | 32 | 20 | 52 |
| Surfboard-tg-mixed | 0.848 | 84 | 15 | 99 |
| Au1rxx-base64 | 0.853 | 186 | 32 | 218 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22399 | yes | 5.94 | 0 |
| SoliSpirit-all | 8857 | yes | 3.25 | 0 |
| Epodonios-all | 7495 | yes | 3.27 | 0 |
| Surfboard-tg-mixed | 7027 | yes | 3.7 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.22 | 0 |
| barry-far-vless | 5899 | yes | 4.83 | 0 |
| DeltaKronecker-all | 5845 | yes | 6.01 | 0 |
| Surfboard-tg-vless | 5676 | yes | 3.93 | 0 |
| 10ium-ScrapeCategorize-Vless | 5307 | yes | 2.85 | 0 |
| mahdibland-V2RayAggregator | 4305 | yes | 1.4 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 54 |
| cn-block | 40 |
| geo | 25 |
| speed | 18 |
