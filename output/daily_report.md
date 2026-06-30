# AutoNodes 每日报告

生成时间：2026-06-30 04:11:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75411 |
| 去重后节点数 | 23011 |
| TCP 可达数 | 3000 |
| 真测通过数 | 602 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23011 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 40.7 |
| geo | 1.4 |
| probe | 55.6 |
| real_test | 143.3 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 127 | 72 | 55 | 56.7% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 149 | 119 | 30 | 79.9% |
| vless | 708 | 364 | 344 | 51.4% |
| vmess | 5 | 4 | 1 | 80.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 139 |
| speed:ClientOSError | 130 |
| geo:ClientOSError | 45 |
| speed:TimeoutError | 42 |
| cn-block:TimeoutError | 30 |
| 204:ProxyError | 23 |
| 204:ClientOSError | 9 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4446 |
| ConnectionRefusedError | 631 |
| gaierror | 164 |
| OSError | 132 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.789 | prefer | 324 | 0.71 | 5456 |
| mheidari-all | 0.775 | prefer | 336 | 0.696 | 15873 |
| Au1rxx-base64 | 0.671 | observe | 55 | 0.673 | 101 |
| DeltaKronecker-all | 0.312 | observe | 278 | 0.23 | 7004 |
| xiaoji235-airport-v2ray-all | 0.303 | observe | 1 | 1.0 | 1204 |
| Epodonios-all | 0.255 | observe | 0 | None | 6395 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6638 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4008 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.23 | 64 | 214 | 278 |
| Au1rxx-base64 | 0.673 | 37 | 18 | 55 |
| mheidari-all | 0.696 | 234 | 102 | 336 |
| Surfboard-tg-mixed | 0.71 | 230 | 94 | 324 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15873 | yes | 3.88 | 0 |
| DeltaKronecker-all | 7004 | yes | 3.21 | 0 |
| SoliSpirit-all | 6638 | yes | 2.56 | 0 |
| Epodonios-all | 6395 | yes | 3.15 | 0 |
| Surfboard-tg-mixed | 5456 | yes | 1.96 | 0 |
| mahdibland-V2RayAggregator | 5353 | yes | 1.59 | 0 |
| 10ium-ScrapeCategorize-Vless | 4653 | yes | 1.3 | 0 |
| barry-far-vless | 4588 | yes | 0.98 | 0 |
| Surfboard-tg-vless | 4008 | yes | 2.18 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.1 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 184 |
| speed | 173 |
| cn-block | 37 |
| 204 | 37 |
