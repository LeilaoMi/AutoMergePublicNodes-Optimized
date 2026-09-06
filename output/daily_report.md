# AutoNodes 每日报告

生成时间：2026-09-06 20:20:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 94324 |
| 去重后节点数 | 24687 |
| TCP 可达数 | 3000 |
| 真测通过数 | 515 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24687 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 39.9 |
| geo | 1.4 |
| probe | 92.5 |
| real_test | 124.7 |
| tcp | 41.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 6 | 2 | 4 | 33.3% |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 21 | 20 | 1 | 95.2% |
| shadowsocks | 169 | 153 | 16 | 90.5% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 33 | 25 | 8 | 75.8% |
| vless | 410 | 288 | 122 | 70.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 50 |
| geo:ClientOSError | 33 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 14 |
| 204:ProxyConnectionError | 9 |
| 204:ProxyError | 8 |
| speed:TimeoutError | 7 |
| geo:TimeoutError | 6 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 2 |
| speed:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5339 |
| ConnectionRefusedError | 1013 |
| gaierror | 407 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.975 | prefer | 311 | 0.904 | 1862 |
| zhangkai | 0.96 | prefer | 20 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.826 | prefer | 171 | 0.749 | 7274 |
| mheidari-all | 0.596 | observe | 153 | 0.516 | 21188 |
| DeltaKronecker-all | 0.391 | observe | 2 | 1.0 | 5856 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 5750 |
| tg-oneclickvpnkeys | 0.298 | observe | 5 | 0.6 | 134 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4791 |
| Epodonios-all | 0.255 | observe | 0 | None | 7817 |
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
| tg-LonUp_M | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.516 | 79 | 74 | 153 |
| tg-oneclickvpnkeys | 0.6 | 3 | 2 | 5 |
| Surfboard-tg-mixed | 0.749 | 128 | 43 | 171 |
| Au1rxx-base64 | 0.904 | 281 | 30 | 311 |
| DeltaKronecker-all | 1.0 | 2 | 0 | 2 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21188 | yes | 5.51 | 0 |
| SoliSpirit-all | 8616 | yes | 5.34 | 0 |
| Epodonios-all | 7817 | yes | 1.66 | 0 |
| Surfboard-tg-mixed | 7274 | yes | 3.81 | 0 |
| barry-far-vless | 6306 | yes | 4.26 | 0 |
| Surfboard-tg-vless | 6019 | yes | 4.3 | 0 |
| DeltaKronecker-all | 5856 | yes | 6.11 | 0 |
| xiaoji235-airport-v2ray-all | 5750 | yes | 3.24 | 0 |
| 10ium-ScrapeCategorize-Vless | 4791 | yes | 3.37 | 0 |
| mahdibland-V2RayAggregator | 4138 | yes | 1.73 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 68 |
| geo | 39 |
| 204 | 34 |
| speed | 11 |
