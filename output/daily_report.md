# AutoNodes 每日报告

生成时间：2026-09-03 03:58:52

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 83558 |
| 去重后节点数 | 23576 |
| TCP 可达数 | 3000 |
| 真测通过数 | 575 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23576 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 42.3 |
| geo | 1.7 |
| probe | 87.3 |
| real_test | 140.9 |
| tcp | 38.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 123 | 120 | 3 | 97.6% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 67 | 34 | 33 | 50.7% |
| vless | 638 | 371 | 267 | 58.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 126 |
| speed:TimeoutError | 48 |
| geo:ClientOSError | 41 |
| speed:ClientOSError | 38 |
| cn-block:TimeoutError | 20 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 8 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5134 |
| ConnectionRefusedError | 895 |
| gaierror | 326 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.973 | prefer | 371 | 0.9 | 1874 |
| zhangkai | 0.967 | prefer | 24 | 1.0 | 144 |
| mheidari-all | 0.56 | observe | 365 | 0.479 | 16261 |
| Surfboard-tg-mixed | 0.492 | observe | 13 | 0.538 | 7080 |
| DeltaKronecker-all | 0.404 | observe | 100 | 0.32 | 7295 |
| tg-oneclickvpnkeys | 0.316 | observe | 2 | 1.0 | 131 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4765 |
| Epodonios-all | 0.255 | observe | 0 | None | 7558 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.32 | 32 | 68 | 100 |
| mheidari-all | 0.479 | 175 | 190 | 365 |
| Surfboard-tg-mixed | 0.538 | 7 | 6 | 13 |
| Au1rxx-base64 | 0.9 | 334 | 37 | 371 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16261 | yes | 6.03 | 0 |
| SoliSpirit-all | 7927 | yes | 4.01 | 0 |
| Epodonios-all | 7558 | yes | 3.93 | 0 |
| DeltaKronecker-all | 7295 | yes | 4.42 | 0 |
| Surfboard-tg-mixed | 7080 | yes | 5.43 | 0 |
| barry-far-vless | 6145 | yes | 3.62 | 0 |
| Surfboard-tg-vless | 5956 | yes | 3.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 4765 | yes | 2.81 | 0 |
| mahdibland-V2RayAggregator | 4066 | yes | 2.9 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 168 |
| speed | 88 |
| cn-block | 26 |
| 204 | 22 |
