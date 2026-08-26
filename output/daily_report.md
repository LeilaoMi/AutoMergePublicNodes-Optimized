# AutoNodes 每日报告

生成时间：2026-08-26 07:02:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77824 |
| 去重后节点数 | 22072 |
| TCP 可达数 | 3000 |
| 真测通过数 | 591 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22072 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.5 |
| generate | 43.6 |
| geo | 1.5 |
| probe | 59.8 |
| real_test | 140.5 |
| tcp | 34.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 27 | 25 | 2 | 92.6% |
| shadowsocks | 178 | 165 | 13 | 92.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 51 | 38 | 13 | 74.5% |
| vless | 516 | 335 | 181 | 64.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 56 |
| geo:TimeoutError | 55 |
| geo:ClientOSError | 24 |
| cn-block:TimeoutError | 24 |
| 204:TimeoutError | 22 |
| speed:ClientOSError | 14 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4416 |
| ConnectionRefusedError | 864 |
| gaierror | 476 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.929 | prefer | 24 | 0.958 | 144 |
| Au1rxx-base64 | 0.912 | prefer | 375 | 0.835 | 1986 |
| Surfboard-tg-mixed | 0.787 | prefer | 165 | 0.709 | 6380 |
| mheidari-all | 0.705 | prefer | 126 | 0.627 | 14091 |
| DeltaKronecker-all | 0.58 | observe | 98 | 0.5 | 6107 |
| nscl5-all | 0.402 | observe | 5 | 0.8 | 887 |
| 10ium-ScrapeCategorize-Vless | 0.391 | observe | 2 | 1.0 | 4825 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 206 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
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
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.5 | 49 | 49 | 98 |
| mheidari-all | 0.627 | 79 | 47 | 126 |
| Surfboard-tg-mixed | 0.709 | 117 | 48 | 165 |
| nscl5-all | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.835 | 313 | 62 | 375 |
| zhangkai | 0.958 | 23 | 1 | 24 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14091 | yes | 5.37 | 0 |
| SoliSpirit-all | 6976 | yes | 3.35 | 0 |
| Epodonios-all | 6845 | yes | 4.98 | 0 |
| Surfboard-tg-mixed | 6380 | yes | 5.83 | 0 |
| DeltaKronecker-all | 6107 | yes | 4.96 | 0 |
| barry-far-vless | 5518 | yes | 2.98 | 0 |
| Surfboard-tg-vless | 5270 | yes | 3.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 4825 | yes | 2.75 | 0 |
| MatinGhanbari-all-sub | 3990 | yes | 3.06 | 0 |
| mahdibland-V2RayAggregator | 3981 | yes | 1.51 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 79 |
| speed | 71 |
| cn-block | 32 |
| 204 | 29 |
