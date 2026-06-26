# AutoNodes 每日报告

生成时间：2026-06-26 04:16:29

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 82567 |
| 去重后节点数 | 22943 |
| TCP 可达数 | 3000 |
| 真测通过数 | 527 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22943 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 35.3 |
| geo | 1.3 |
| probe | 57.6 |
| real_test | 123.8 |
| tcp | 30.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 137 | 123 | 14 | 89.8% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 105 | 90 | 15 | 85.7% |
| vless | 731 | 270 | 461 | 36.9% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 213 |
| geo:TimeoutError | 180 |
| geo:ClientOSError | 26 |
| speed:TimeoutError | 25 |
| cn-block:TimeoutError | 15 |
| 204:ClientOSError | 10 |
| 204:ProxyError | 8 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 5 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4238 |
| ConnectionRefusedError | 641 |
| gaierror | 195 |
| OSError | 118 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Surfboard-tg-mixed | 0.856 | prefer | 284 | 0.778 | 5079 |
| Au1rxx-base64 | 0.759 | prefer | 55 | 0.764 | 110 |
| mheidari-all | 0.69 | observe | 234 | 0.611 | 16097 |
| nscl5-all | 0.358 | observe | 2 | 1.0 | 1175 |
| DeltaKronecker-all | 0.286 | observe | 401 | 0.204 | 12590 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7810 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3981 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7388 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.204 | 82 | 319 | 401 |
| mheidari-all | 0.611 | 143 | 91 | 234 |
| Au1rxx-base64 | 0.764 | 42 | 13 | 55 |
| Surfboard-tg-mixed | 0.778 | 221 | 63 | 284 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16097 | yes | 3.52 | 0 |
| DeltaKronecker-all | 12590 | yes | 3.63 | 0 |
| Epodonios-all | 7810 | yes | 2.75 | 0 |
| SoliSpirit-all | 7388 | yes | 2.28 | 0 |
| mahdibland-V2RayAggregator | 5117 | yes | 1.82 | 0 |
| Surfboard-tg-mixed | 5079 | yes | 2.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 4787 | yes | 1.17 | 0 |
| barry-far-vless | 4580 | yes | 1.34 | 0 |
| MatinGhanbari-all-sub | 3981 | yes | 1.41 | 0 |
| Surfboard-tg-vless | 3792 | yes | 1.74 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 238 |
| geo | 206 |
| 204 | 26 |
| cn-block | 20 |
