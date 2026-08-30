# AutoNodes 每日报告

生成时间：2026-08-30 20:54:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79345 |
| 去重后节点数 | 21873 |
| TCP 可达数 | 3000 |
| 真测通过数 | 573 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21873 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 38.3 |
| geo | 1.5 |
| probe | 56.3 |
| real_test | 109.0 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 141 | 126 | 15 | 89.4% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 22 | 20 | 2 | 90.9% |
| vless | 466 | 383 | 83 | 82.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 30 |
| 204:TimeoutError | 20 |
| 204:ProxyError | 12 |
| geo:ClientOSError | 10 |
| cn-block:ProxyError | 7 |
| speed:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| geo:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4684 |
| ConnectionRefusedError | 887 |
| gaierror | 414 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 327 | 0.942 | 1804 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.84 | prefer | 173 | 0.763 | 6963 |
| DeltaKronecker-all | 0.794 | prefer | 138 | 0.717 | 5576 |
| mheidari-all | 0.714 | prefer | 12 | 0.917 | 14482 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4762 |
| Epodonios-all | 0.255 | observe | 0 | None | 7411 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7545 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5857 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.717 | 99 | 39 | 138 |
| Surfboard-tg-mixed | 0.763 | 132 | 41 | 173 |
| mheidari-all | 0.917 | 11 | 1 | 12 |
| Au1rxx-base64 | 0.942 | 308 | 19 | 327 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14482 | yes | 5.24 | 0 |
| SoliSpirit-all | 7545 | yes | 4.35 | 0 |
| Epodonios-all | 7411 | yes | 4.91 | 0 |
| Surfboard-tg-mixed | 6963 | yes | 3.77 | 0 |
| barry-far-vless | 6057 | yes | 3.47 | 0 |
| Surfboard-tg-vless | 5857 | yes | 3.43 | 0 |
| DeltaKronecker-all | 5576 | yes | 5.15 | 0 |
| 10ium-ScrapeCategorize-Vless | 4762 | yes | 3.69 | 0 |
| mahdibland-V2RayAggregator | 4041 | yes | 0.62 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 3.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 40 |
| 204 | 35 |
| geo | 14 |
| speed | 12 |
