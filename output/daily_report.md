# AutoNodes 每日报告

生成时间：2026-08-29 06:40:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 76898 |
| 去重后节点数 | 20895 |
| TCP 可达数 | 3000 |
| 真测通过数 | 630 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 20895 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 29.8 |
| geo | 1.5 |
| probe | 58.6 |
| real_test | 130.6 |
| tcp | 35.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 27 | 26 | 1 | 96.3% |
| hysteria2 | 24 | 21 | 3 | 87.5% |
| shadowsocks | 180 | 168 | 12 | 93.3% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 34 | 32 | 2 | 94.1% |
| vless | 500 | 379 | 121 | 75.8% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 26 |
| geo:ClientOSError | 25 |
| cn-block:TimeoutError | 21 |
| 204:TimeoutError | 16 |
| geo:TimeoutError | 15 |
| cn-block:ClientOSError | 11 |
| 204:ProxyError | 9 |
| cn-block:ProxyError | 6 |
| speed:ClientOSError | 6 |
| geo:ProxyError | 3 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4808 |
| ConnectionRefusedError | 860 |
| gaierror | 344 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Au1rxx-base64 | 0.959 | prefer | 379 | 0.889 | 1789 |
| mheidari-all | 0.852 | prefer | 99 | 0.778 | 14598 |
| DeltaKronecker-all | 0.801 | prefer | 170 | 0.724 | 4065 |
| Surfboard-tg-mixed | 0.794 | prefer | 89 | 0.719 | 6733 |
| tg-oneclickvpnkeys | 0.326 | observe | 4 | 0.75 | 139 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7084 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.719 | 64 | 25 | 89 |
| DeltaKronecker-all | 0.724 | 123 | 47 | 170 |
| tg-oneclickvpnkeys | 0.75 | 3 | 1 | 4 |
| mheidari-all | 0.778 | 77 | 22 | 99 |
| Au1rxx-base64 | 0.889 | 337 | 42 | 379 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14598 | yes | 3.96 | 0 |
| SoliSpirit-all | 7191 | yes | 4.34 | 0 |
| Epodonios-all | 7084 | yes | 3.08 | 0 |
| Surfboard-tg-mixed | 6733 | yes | 4.8 | 0 |
| barry-far-vless | 5694 | yes | 4.12 | 0 |
| Surfboard-tg-vless | 5530 | yes | 0.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 4725 | yes | 2.44 | 0 |
| mahdibland-V2RayAggregator | 4093 | yes | 2.48 | 0 |
| DeltaKronecker-all | 4065 | yes | 3.95 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 43 |
| cn-block | 38 |
| speed | 32 |
| 204 | 27 |
