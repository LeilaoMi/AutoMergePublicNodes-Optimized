# AutoNodes 每日报告

生成时间：2026-07-11 03:20:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 75798 |
| 去重后节点数 | 24018 |
| TCP 可达数 | 3000 |
| 真测通过数 | 517 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24018 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| generate | 22.4 |
| geo | 1.4 |
| probe | 44.0 |
| real_test | 91.5 |
| tcp | 31.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 134 | 125 | 9 | 93.3% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 209 | 199 | 10 | 95.2% |
| vless | 331 | 145 | 186 | 43.8% |
| vmess | 7 | 7 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 81 |
| geo:TimeoutError | 68 |
| speed:TimeoutError | 18 |
| geo:ClientOSError | 16 |
| cn-block:ClientOSError | 6 |
| cn-block:TimeoutError | 6 |
| 204:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| 204:ProxyError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4349 |
| ConnectionRefusedError | 680 |
| gaierror | 290 |
| OSError | 190 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.863 | prefer | 89 | 0.865 | 136 |
| DeltaKronecker-all | 0.814 | prefer | 242 | 0.736 | 7600 |
| mheidari-all | 0.72 | prefer | 48 | 0.646 | 16392 |
| Surfboard-tg-mixed | 0.714 | prefer | 304 | 0.635 | 5480 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4165 |
| Epodonios-all | 0.255 | observe | 0 | None | 6288 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3971 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6402 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.635 | 193 | 111 | 304 |
| mheidari-all | 0.646 | 31 | 17 | 48 |
| DeltaKronecker-all | 0.736 | 178 | 64 | 242 |
| Au1rxx-base64 | 0.865 | 77 | 12 | 89 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16392 | yes | 3.12 | 0 |
| DeltaKronecker-all | 7600 | yes | 3.06 | 0 |
| SoliSpirit-all | 6402 | yes | 2.28 | 0 |
| Epodonios-all | 6288 | yes | 2.19 | 0 |
| Surfboard-tg-mixed | 5480 | yes | 2.47 | 0 |
| mahdibland-V2RayAggregator | 5415 | yes | 1.36 | 0 |
| barry-far-vless | 4570 | yes | 1.28 | 0 |
| 10ium-ScrapeCategorize-Vless | 4165 | yes | 1.59 | 0 |
| Surfboard-tg-vless | 4087 | yes | 2.32 | 0 |
| MatinGhanbari-all-sub | 3971 | yes | 2.81 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 99 |
| geo | 84 |
| cn-block | 13 |
| 204 | 10 |
