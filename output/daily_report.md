# AutoNodes 每日报告

生成时间：2026-08-30 16:31:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79914 |
| 去重后节点数 | 21856 |
| TCP 可达数 | 3000 |
| 真测通过数 | 582 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21856 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 34.1 |
| geo | 1.6 |
| probe | 58.2 |
| real_test | 137.9 |
| tcp | 35.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 19 | 17 | 2 | 89.5% |
| shadowsocks | 150 | 139 | 11 | 92.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 27 | 21 | 6 | 77.8% |
| vless | 463 | 377 | 86 | 81.4% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 27 |
| geo:TimeoutError | 19 |
| geo:ClientOSError | 14 |
| cn-block:TimeoutError | 12 |
| speed:TimeoutError | 11 |
| 204:ProxyError | 9 |
| speed:ClientOSError | 7 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4982 |
| ConnectionRefusedError | 885 |
| gaierror | 224 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.967 | prefer | 341 | 0.897 | 1804 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.862 | prefer | 163 | 0.785 | 7004 |
| DeltaKronecker-all | 0.842 | prefer | 149 | 0.765 | 5576 |
| mheidari-all | 0.679 | observe | 11 | 0.909 | 15115 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 163 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4762 |
| Epodonios-all | 0.255 | observe | 0 | None | 7409 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7601 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.765 | 114 | 35 | 149 |
| Surfboard-tg-mixed | 0.785 | 128 | 35 | 163 |
| Au1rxx-base64 | 0.897 | 306 | 35 | 341 |
| mheidari-all | 0.909 | 10 | 1 | 11 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15115 | yes | 2.91 | 0 |
| SoliSpirit-all | 7601 | yes | 1.68 | 0 |
| Epodonios-all | 7409 | yes | 2.21 | 0 |
| Surfboard-tg-mixed | 7004 | yes | 2.58 | 0 |
| barry-far-vless | 6056 | yes | 1.24 | 0 |
| Surfboard-tg-vless | 5872 | yes | 2.0 | 0 |
| DeltaKronecker-all | 5576 | yes | 2.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 4762 | yes | 1.04 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.12 | 0 |
| mahdibland-V2RayAggregator | 3949 | yes | 1.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 38 |
| geo | 35 |
| speed | 18 |
| cn-block | 15 |
