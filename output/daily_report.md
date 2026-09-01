# AutoNodes 每日报告

生成时间：2026-09-01 11:31:14

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 4/102 |
| 原始节点数 | 83205 |
| 去重后节点数 | 24567 |
| TCP 可达数 | 3000 |
| 真测通过数 | 616 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24567 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 40.7 |
| geo | 1.6 |
| probe | 88.6 |
| real_test | 144.9 |
| tcp | 40.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 142 | 130 | 12 | 91.5% |
| socks | 5 | 4 | 1 | 80.0% |
| trojan | 23 | 16 | 7 | 69.6% |
| vless | 552 | 429 | 123 | 77.7% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 25 |
| speed:TimeoutError | 25 |
| cn-block:TimeoutError | 20 |
| geo:ClientOSError | 18 |
| cn-block:ClientOSError | 17 |
| geo:TimeoutError | 14 |
| 204:ProxyError | 13 |
| 204:ClientOSError | 8 |
| cn-block:ProxyError | 2 |
| speed:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5765 |
| ConnectionRefusedError | 1009 |
| gaierror | 325 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Au1rxx-base64 | 0.918 | prefer | 338 | 0.852 | 1711 |
| Surfboard-tg-mixed | 0.862 | prefer | 177 | 0.785 | 6921 |
| mheidari-all | 0.853 | prefer | 209 | 0.775 | 17148 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 49 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4708 |
| Epodonios-all | 0.255 | observe | 0 | None | 7334 |
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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.197 | 9 | 0.111 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.111 | 1 | 8 | 9 |
| mheidari-all | 0.775 | 162 | 47 | 209 |
| Surfboard-tg-mixed | 0.785 | 139 | 38 | 177 |
| Au1rxx-base64 | 0.852 | 288 | 50 | 338 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17148 | yes | 5.26 | 0 |
| SoliSpirit-all | 7625 | yes | 1.25 | 0 |
| Epodonios-all | 7334 | yes | 5.61 | 0 |
| DeltaKronecker-all | 7294 | yes | 4.5 | 0 |
| Surfboard-tg-mixed | 6921 | yes | 3.49 | 0 |
| barry-far-vless | 6092 | yes | 0.61 | 0 |
| Surfboard-tg-vless | 5831 | yes | 4.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 4708 | yes | 0.42 | 0 |
| mahdibland-V2RayAggregator | 4013 | yes | 2.75 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.68 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 46 |
| cn-block | 39 |
| geo | 32 |
| speed | 27 |
