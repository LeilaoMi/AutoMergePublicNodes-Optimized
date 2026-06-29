# AutoNodes 每日报告

生成时间：2026-06-29 16:00:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77445 |
| 去重后节点数 | 23263 |
| TCP 可达数 | 3000 |
| 真测通过数 | 444 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23263 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| generate | 24.5 |
| geo | 1.4 |
| probe | 48.5 |
| real_test | 89.5 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 120 | 93 | 27 | 77.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 142 | 110 | 32 | 77.5% |
| vless | 320 | 198 | 122 | 61.9% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 89 |
| 204:ClientOSError | 16 |
| geo:ClientOSError | 15 |
| cn-block:TimeoutError | 14 |
| geo:TimeoutError | 12 |
| cn-block:ClientOSError | 11 |
| 204:TimeoutError | 11 |
| 204:ProxyError | 7 |
| speed:TimeoutError | 5 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4446 |
| ConnectionRefusedError | 652 |
| gaierror | 235 |
| OSError | 131 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.852 | prefer | 31 | 0.871 | 80 |
| mheidari-all | 0.805 | prefer | 169 | 0.728 | 15881 |
| Surfboard-tg-mixed | 0.799 | prefer | 279 | 0.72 | 5497 |
| DeltaKronecker-all | 0.589 | observe | 110 | 0.509 | 7004 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4653 |
| Epodonios-all | 0.255 | observe | 0 | None | 7616 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7472 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.509 | 56 | 54 | 110 |
| Surfboard-tg-mixed | 0.72 | 201 | 78 | 279 |
| mheidari-all | 0.728 | 123 | 46 | 169 |
| Au1rxx-base64 | 0.871 | 27 | 4 | 31 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15881 | yes | 3.3 | 0 |
| Epodonios-all | 7616 | yes | 2.41 | 0 |
| SoliSpirit-all | 7472 | yes | 2.39 | 0 |
| DeltaKronecker-all | 7004 | yes | 3.42 | 0 |
| Surfboard-tg-mixed | 5497 | yes | 2.83 | 0 |
| mahdibland-V2RayAggregator | 5278 | yes | 1.55 | 0 |
| 10ium-ScrapeCategorize-Vless | 4653 | yes | 1.91 | 0 |
| barry-far-vless | 4553 | yes | 1.7 | 0 |
| Surfboard-tg-vless | 3986 | yes | 1.77 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.56 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 94 |
| 204 | 34 |
| geo | 27 |
| cn-block | 27 |
