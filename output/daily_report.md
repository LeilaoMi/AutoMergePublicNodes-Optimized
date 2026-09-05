# AutoNodes 每日报告

生成时间：2026-09-05 15:00:02

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83843 |
| 去重后节点数 | 22680 |
| TCP 可达数 | 3000 |
| 真测通过数 | 606 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22680 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 32.7 |
| geo | 1.6 |
| probe | 68.7 |
| real_test | 114.4 |
| tcp | 37.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 30 | 30 | 0 | 100.0% |
| hysteria2 | 13 | 12 | 1 | 92.3% |
| shadowsocks | 163 | 156 | 7 | 95.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 47 | 40 | 7 | 85.1% |
| vless | 459 | 364 | 95 | 79.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 28 |
| geo:ClientOSError | 24 |
| cn-block:TimeoutError | 19 |
| cn-block:ClientOSError | 13 |
| speed:ClientOSError | 9 |
| 204:ProxyError | 7 |
| speed:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| 204:ServerDisconnectedError | 1 |
| geo:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5011 |
| ConnectionRefusedError | 899 |
| gaierror | 452 |
| OSError | 18 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Au1rxx-base64 | 0.963 | prefer | 400 | 0.897 | 1685 |
| Surfboard-tg-mixed | 0.859 | prefer | 143 | 0.783 | 7365 |
| mheidari-all | 0.794 | prefer | 131 | 0.718 | 16245 |
| DeltaKronecker-all | 0.664 | observe | 9 | 1.0 | 6212 |
| tg-oneclickvpnkeys | 0.518 | observe | 7 | 1.0 | 118 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| Epodonios-all | 0.255 | observe | 0 | None | 7776 |
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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.718 | 94 | 37 | 131 |
| Surfboard-tg-mixed | 0.783 | 112 | 31 | 143 |
| Au1rxx-base64 | 0.897 | 359 | 41 | 400 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 7 | 0 | 7 |
| DeltaKronecker-all | 1.0 | 9 | 0 | 9 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16245 | yes | 3.33 | 0 |
| SoliSpirit-all | 8453 | yes | 2.49 | 0 |
| Epodonios-all | 7776 | yes | 1.19 | 0 |
| Surfboard-tg-mixed | 7365 | yes | 2.6 | 0 |
| barry-far-vless | 6414 | yes | 1.74 | 0 |
| DeltaKronecker-all | 6212 | yes | 3.5 | 0 |
| Surfboard-tg-vless | 6206 | yes | 2.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 4887 | yes | 1.88 | 0 |
| mahdibland-V2RayAggregator | 4095 | yes | 0.23 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.94 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 38 |
| cn-block | 33 |
| geo | 27 |
| speed | 13 |
