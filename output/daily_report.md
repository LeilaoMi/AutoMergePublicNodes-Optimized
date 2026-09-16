# AutoNodes 每日报告

生成时间：2026-09-16 11:25:51

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 87785 |
| 去重后节点数 | 24305 |
| TCP 可达数 | 3000 |
| 真测通过数 | 455 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24305 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 135.6 |
| geo | 1.4 |
| probe | 276.4 |
| real_test | 232.8 |
| tcp | 41.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 74 | 50 | 24 | 67.6% |
| hysteria2 | 23 | 20 | 3 | 87.0% |
| shadowsocks | 157 | 145 | 12 | 92.4% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 13 | 7 | 6 | 53.8% |
| vless | 319 | 230 | 89 | 72.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 28 |
| 204:ProxyError | 26 |
| cn-block:TimeoutError | 18 |
| 204:TimeoutError | 15 |
| speed:ClientOSError | 12 |
| cn-block:ClientOSError | 11 |
| speed:TimeoutError | 11 |
| geo:TimeoutError | 10 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5608 |
| ConnectionRefusedError | 916 |
| gaierror | 416 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.916 | prefer | 301 | 0.85 | 1687 |
| mheidari-all | 0.811 | prefer | 65 | 0.738 | 16003 |
| DeltaKronecker-all | 0.777 | prefer | 31 | 0.71 | 6081 |
| ermaozi | 0.775 | prefer | 56 | 0.768 | 407 |
| Surfboard-tg-mixed | 0.735 | prefer | 114 | 0.658 | 7446 |
| ermaozi-get_subscribe | 0.427 | observe | 20 | 0.4 | 438 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 178 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 8003 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.4 | 8 | 12 | 20 |
| Surfboard-tg-mixed | 0.658 | 75 | 39 | 114 |
| DeltaKronecker-all | 0.71 | 22 | 9 | 31 |
| mheidari-all | 0.738 | 48 | 17 | 65 |
| ermaozi | 0.768 | 43 | 13 | 56 |
| Au1rxx-base64 | 0.85 | 256 | 45 | 301 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16003 | yes | 4.32 | 0 |
| SoliSpirit-all | 9052 | yes | 4.17 | 0 |
| Epodonios-all | 8003 | yes | 4.64 | 0 |
| Surfboard-tg-mixed | 7446 | yes | 5.91 | 0 |
| barry-far-vless | 6340 | yes | 2.63 | 0 |
| DeltaKronecker-all | 6081 | yes | 4.52 | 0 |
| Surfboard-tg-vless | 6044 | yes | 3.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 5115 | yes | 3.89 | 0 |
| mahdibland-V2RayAggregator | 4206 | yes | 0.17 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 4.23 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 44 |
| geo | 39 |
| cn-block | 31 |
| speed | 23 |
