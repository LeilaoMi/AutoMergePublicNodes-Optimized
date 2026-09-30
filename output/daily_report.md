# AutoNodes 每日报告

生成时间：2026-09-30 12:25:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 96400 |
| 去重后节点数 | 26890 |
| TCP 可达数 | 3000 |
| 真测通过数 | 378 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26890 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 72.3 |
| geo | 1.4 |
| probe | 277.0 |
| real_test | 175.2 |
| tcp | 45.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 55 | 46 | 9 | 83.6% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 163 | 141 | 22 | 86.5% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 45 | 14 | 31 | 31.1% |
| vless | 257 | 158 | 99 | 61.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 52 |
| speed:ClientOSError | 46 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 15 |
| cn-block:ClientOSError | 10 |
| geo:TimeoutError | 8 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 6 |
| geo:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6350 |
| ConnectionRefusedError | 996 |
| gaierror | 273 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.931 | prefer | 45 | 0.867 | 22755 |
| Au1rxx-base64 | 0.842 | prefer | 274 | 0.774 | 1752 |
| ermaozi | 0.835 | prefer | 54 | 0.833 | 335 |
| Surfboard-tg-mixed | 0.587 | observe | 142 | 0.507 | 6952 |
| DeltaKronecker-all | 0.428 | observe | 21 | 0.333 | 5434 |
| tg-oneclickvpnkeys | 0.36 | observe | 3 | 1.0 | 53 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7458 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9148 |

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
| DeltaKronecker-all | 0.333 | 7 | 14 | 21 |
| Surfboard-tg-mixed | 0.507 | 72 | 70 | 142 |
| Au1rxx-base64 | 0.774 | 212 | 62 | 274 |
| ermaozi | 0.833 | 45 | 9 | 54 |
| mheidari-all | 0.867 | 39 | 6 | 45 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22755 | yes | 2.8 | 0 |
| SoliSpirit-all | 9148 | yes | 1.92 | 0 |
| Epodonios-all | 7458 | yes | 1.64 | 0 |
| Surfboard-tg-mixed | 6952 | yes | 1.98 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.67 | 0 |
| barry-far-vless | 5879 | yes | 1.22 | 0 |
| Surfboard-tg-vless | 5632 | yes | 2.08 | 0 |
| DeltaKronecker-all | 5434 | yes | 3.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 2.09 | 0 |
| mahdibland-V2RayAggregator | 4183 | yes | 1.67 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 73 |
| speed | 52 |
| cn-block | 26 |
| geo | 11 |
