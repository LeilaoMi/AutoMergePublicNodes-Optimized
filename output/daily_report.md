# AutoNodes 每日报告

生成时间：2026-06-28 14:06:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 104/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76210 |
| 去重后节点数 | 22925 |
| TCP 可达数 | 3000 |
| 真测通过数 | 566 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22925 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 29.6 |
| geo | 1.4 |
| probe | 62.0 |
| real_test | 159.9 |
| tcp | 30.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 2 | 1 | 66.7% |
| shadowsocks | 107 | 89 | 18 | 83.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 130 | 69 | 61 | 53.1% |
| vless | 493 | 366 | 127 | 74.2% |
| vmess | 4 | 3 | 1 | 75.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 88 |
| 204:TimeoutError | 26 |
| geo:ClientOSError | 16 |
| cn-block:TimeoutError | 15 |
| speed:TimeoutError | 12 |
| geo:TimeoutError | 12 |
| 204:ProxyError | 10 |
| cn-block:ClientOSError | 8 |
| cn-block:ProxyError | 7 |
| speed:ProxyError | 6 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4370 |
| ConnectionRefusedError | 638 |
| gaierror | 176 |
| OSError | 122 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.865 | prefer | 333 | 0.787 | 16291 |
| Surfboard-tg-mixed | 0.794 | prefer | 243 | 0.716 | 5019 |
| Au1rxx-base64 | 0.794 | prefer | 55 | 0.8 | 109 |
| DeltaKronecker-all | 0.538 | observe | 105 | 0.457 | 6788 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1174 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7519 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.457 | 48 | 57 | 105 |
| Surfboard-tg-mixed | 0.716 | 174 | 69 | 243 |
| mheidari-all | 0.787 | 262 | 71 | 333 |
| Au1rxx-base64 | 0.8 | 44 | 11 | 55 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16291 | yes | 3.63 | 0 |
| Epodonios-all | 7519 | yes | 2.03 | 0 |
| SoliSpirit-all | 7282 | yes | 2.48 | 0 |
| DeltaKronecker-all | 6788 | yes | 3.9 | 0 |
| mahdibland-V2RayAggregator | 5325 | yes | 1.59 | 0 |
| Surfboard-tg-mixed | 5019 | yes | 2.44 | 0 |
| barry-far-vless | 4502 | yes | 1.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 4327 | yes | 1.94 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.78 | 0 |
| Surfboard-tg-vless | 3723 | yes | 2.25 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 106 |
| 204 | 41 |
| geo | 32 |
| cn-block | 30 |
