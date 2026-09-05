# AutoNodes 每日报告

生成时间：2026-09-05 20:14:59

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 97140 |
| 去重后节点数 | 25678 |
| TCP 可达数 | 3000 |
| 真测通过数 | 480 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25678 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 47.7 |
| geo | 1.4 |
| probe | 84.6 |
| real_test | 104.1 |
| tcp | 42.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 29 | 29 | 0 | 100.0% |
| hysteria2 | 24 | 22 | 2 | 91.7% |
| shadowsocks | 159 | 147 | 12 | 92.5% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 27 | 21 | 6 | 77.8% |
| vless | 360 | 255 | 105 | 70.8% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 40 |
| 204:TimeoutError | 23 |
| geo:ClientOSError | 19 |
| cn-block:TimeoutError | 18 |
| 204:ProxyError | 7 |
| speed:TimeoutError | 7 |
| speed:ClientOSError | 5 |
| geo:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5508 |
| ConnectionRefusedError | 1029 |
| gaierror | 408 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Au1rxx-base64 | 0.948 | prefer | 325 | 0.88 | 1764 |
| Surfboard-tg-mixed | 0.83 | prefer | 150 | 0.753 | 7292 |
| mheidari-all | 0.585 | observe | 99 | 0.505 | 22630 |
| tg-oneclickvpnkeys | 0.482 | observe | 6 | 1.0 | 132 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 6212 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6965 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4887 |
| Epodonios-all | 0.255 | observe | 0 | None | 7653 |
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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.505 | 50 | 49 | 99 |
| Surfboard-tg-mixed | 0.753 | 113 | 37 | 150 |
| Au1rxx-base64 | 0.88 | 286 | 39 | 325 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 6 | 0 | 6 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22630 | yes | 5.96 | 0 |
| SoliSpirit-all | 8694 | yes | 4.64 | 0 |
| Epodonios-all | 7653 | yes | 1.67 | 0 |
| Surfboard-tg-mixed | 7292 | yes | 3.61 | 0 |
| xiaoji235-airport-v2ray-all | 6965 | yes | 3.21 | 0 |
| barry-far-vless | 6249 | yes | 2.49 | 0 |
| DeltaKronecker-all | 6212 | yes | 6.04 | 0 |
| Surfboard-tg-vless | 6126 | yes | 4.17 | 0 |
| 10ium-ScrapeCategorize-Vless | 4887 | yes | 4.24 | 0 |
| mahdibland-V2RayAggregator | 4087 | yes | 0.71 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 59 |
| 204 | 32 |
| geo | 23 |
| speed | 13 |
