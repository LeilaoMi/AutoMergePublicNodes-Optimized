# AutoNodes 每日报告

生成时间：2026-09-10 20:52:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 83486 |
| 去重后节点数 | 22847 |
| TCP 可达数 | 3000 |
| 真测通过数 | 371 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22847 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 98.9 |
| geo | 1.4 |
| probe | 275.6 |
| real_test | 215.4 |
| tcp | 38.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 20 | 5 | 80.0% |
| hysteria2 | 18 | 12 | 6 | 66.7% |
| shadowsocks | 141 | 126 | 15 | 89.4% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 20 | 14 | 6 | 70.0% |
| vless | 263 | 198 | 65 | 75.3% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 24 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 15 |
| cn-block:ClientOSError | 11 |
| 204:ProxyError | 9 |
| 204:ClientOSError | 6 |
| speed:TimeoutError | 5 |
| speed:ClientOSError | 4 |
| geo:TimeoutError | 4 |
| 204:ProxyConnectionError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5153 |
| ConnectionRefusedError | 899 |
| gaierror | 369 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.94 | prefer | 237 | 0.878 | 1642 |
| DeltaKronecker-all | 0.819 | prefer | 21 | 0.762 | 5853 |
| Surfboard-tg-mixed | 0.78 | prefer | 128 | 0.703 | 7221 |
| ermaozi | 0.776 | prefer | 23 | 0.783 | 405 |
| mheidari-all | 0.705 | prefer | 54 | 0.63 | 15823 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 194 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4995 |
| Epodonios-all | 0.255 | observe | 0 | None | 7677 |

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
| mheidari-all | 0.63 | 34 | 20 | 54 |
| Surfboard-tg-mixed | 0.703 | 90 | 38 | 128 |
| DeltaKronecker-all | 0.762 | 16 | 5 | 21 |
| ermaozi | 0.783 | 18 | 5 | 23 |
| Au1rxx-base64 | 0.878 | 208 | 29 | 237 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15823 | yes | 5.29 | 0 |
| SoliSpirit-all | 8881 | yes | 2.22 | 0 |
| Epodonios-all | 7677 | yes | 6.41 | 0 |
| Surfboard-tg-mixed | 7221 | yes | 3.73 | 0 |
| barry-far-vless | 6058 | yes | 2.42 | 0 |
| DeltaKronecker-all | 5853 | yes | 5.37 | 0 |
| Surfboard-tg-vless | 5840 | yes | 3.94 | 0 |
| 10ium-ScrapeCategorize-Vless | 4995 | yes | 1.85 | 0 |
| mahdibland-V2RayAggregator | 4255 | yes | 3.39 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 32 |
| cn-block | 29 |
| geo | 28 |
| speed | 9 |
