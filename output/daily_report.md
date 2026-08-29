# AutoNodes 每日报告

生成时间：2026-08-29 20:50:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79290 |
| 去重后节点数 | 21340 |
| TCP 可达数 | 3000 |
| 真测通过数 | 659 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21340 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 33.6 |
| geo | 1.4 |
| probe | 59.2 |
| real_test | 142.1 |
| tcp | 34.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 26 | 26 | 0 | 100.0% |
| hysteria2 | 23 | 21 | 2 | 91.3% |
| shadowsocks | 172 | 159 | 13 | 92.4% |
| socks | 8 | 4 | 4 | 50.0% |
| trojan | 17 | 12 | 5 | 70.6% |
| vless | 524 | 433 | 91 | 82.6% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 30 |
| 204:TimeoutError | 28 |
| geo:ClientOSError | 18 |
| speed:ClientOSError | 10 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 6 |
| geo:TimeoutError | 5 |
| 204:ProxyError | 4 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4576 |
| ConnectionRefusedError | 885 |
| gaierror | 471 |
| OSError | 25 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 362 | 0.945 | 1753 |
| zhangkai | 0.926 | prefer | 23 | 0.957 | 144 |
| mheidari-all | 0.872 | prefer | 104 | 0.798 | 14908 |
| Surfboard-tg-mixed | 0.835 | prefer | 157 | 0.758 | 6924 |
| DeltaKronecker-all | 0.798 | prefer | 122 | 0.721 | 4926 |
| tg-oneclickvpnkeys | 0.406 | observe | 4 | 1.0 | 155 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 178 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4635 |
| Epodonios-all | 0.255 | observe | 0 | None | 7291 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| DeltaKronecker-all | 0.721 | 88 | 34 | 122 |
| Surfboard-tg-mixed | 0.758 | 119 | 38 | 157 |
| mheidari-all | 0.798 | 83 | 21 | 104 |
| Au1rxx-base64 | 0.945 | 342 | 20 | 362 |
| zhangkai | 0.957 | 22 | 1 | 23 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14908 | yes | 5.37 | 0 |
| SoliSpirit-all | 7802 | yes | 2.77 | 0 |
| Epodonios-all | 7291 | yes | 3.25 | 0 |
| Surfboard-tg-mixed | 6924 | yes | 3.6 | 0 |
| barry-far-vless | 5901 | yes | 1.23 | 0 |
| Surfboard-tg-vless | 5706 | yes | 3.8 | 0 |
| DeltaKronecker-all | 4926 | yes | 4.71 | 0 |
| 10ium-ScrapeCategorize-Vless | 4635 | yes | 2.46 | 0 |
| mahdibland-V2RayAggregator | 4012 | yes | 2.94 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.02 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 41 |
| 204 | 33 |
| geo | 24 |
| speed | 17 |
