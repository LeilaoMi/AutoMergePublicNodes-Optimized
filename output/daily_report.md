# AutoNodes 每日报告

生成时间：2026-07-23 08:44:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83067 |
| 去重后节点数 | 22726 |
| TCP 可达数 | 3000 |
| 真测通过数 | 837 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22726 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 31.6 |
| geo | 1.3 |
| probe | 66.6 |
| real_test | 207.4 |
| tcp | 32.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 141 | 120 | 21 | 85.1% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 665 | 597 | 68 | 89.8% |
| vless | 390 | 77 | 313 | 19.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 194 |
| cn-block:TimeoutError | 64 |
| speed:ClientOSError | 57 |
| geo:ClientOSError | 26 |
| speed:TimeoutError | 25 |
| 204:TimeoutError | 15 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 4 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4256 |
| ConnectionRefusedError | 699 |
| gaierror | 312 |
| OSError | 218 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| DeltaKronecker-all | 0.902 | prefer | 245 | 0.824 | 5572 |
| Surfboard-tg-mixed | 0.841 | prefer | 86 | 0.767 | 5330 |
| Au1rxx-base64 | 0.792 | prefer | 193 | 0.777 | 432 |
| mheidari-all | 0.642 | observe | 676 | 0.562 | 19639 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 4399 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4757 |
| Epodonios-all | 0.255 | observe | 0 | None | 6489 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3968 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.562 | 380 | 296 | 676 |
| Surfboard-tg-mixed | 0.767 | 66 | 20 | 86 |
| Au1rxx-base64 | 0.777 | 150 | 43 | 193 |
| DeltaKronecker-all | 0.824 | 202 | 43 | 245 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19639 | yes | 3.86 | 0 |
| SoliSpirit-all | 6912 | yes | 2.1 | 0 |
| Epodonios-all | 6489 | yes | 1.38 | 0 |
| DeltaKronecker-all | 5572 | yes | 3.13 | 0 |
| Surfboard-tg-mixed | 5330 | yes | 1.77 | 0 |
| mahdibland-V2RayAggregator | 4954 | yes | 1.85 | 0 |
| 10ium-ScrapeCategorize-Vless | 4757 | yes | 1.55 | 0 |
| barry-far-vless | 4690 | yes | 1.38 | 0 |
| xiaoji235-airport-v2ray-all | 4399 | yes | 1.65 | 0 |
| Surfboard-tg-vless | 4154 | yes | 2.21 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 221 |
| speed | 84 |
| cn-block | 72 |
| 204 | 26 |
