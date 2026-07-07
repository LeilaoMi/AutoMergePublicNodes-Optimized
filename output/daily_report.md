# AutoNodes 每日报告

生成时间：2026-07-07 03:59:13

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 84264 |
| 去重后节点数 | 24819 |
| TCP 可达数 | 3000 |
| 真测通过数 | 422 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24819 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 21.5 |
| geo | 1.3 |
| probe | 45.2 |
| real_test | 73.7 |
| tcp | 31.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 153 | 138 | 15 | 90.2% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 219 | 202 | 17 | 92.2% |
| vless | 129 | 33 | 96 | 25.6% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 55 |
| speed:ClientOSError | 28 |
| geo:ClientOSError | 13 |
| 204:ClientOSError | 11 |
| speed:TimeoutError | 9 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4636 |
| ConnectionRefusedError | 812 |
| OSError | 166 |
| gaierror | 104 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.953 | prefer | 132 | 0.879 | 6047 |
| Au1rxx-base64 | 0.846 | prefer | 61 | 0.852 | 111 |
| mheidari-all | 0.772 | prefer | 128 | 0.695 | 18366 |
| DeltaKronecker-all | 0.741 | prefer | 190 | 0.663 | 8330 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 3626 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7041 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7168 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.663 | 126 | 64 | 190 |
| mheidari-all | 0.695 | 89 | 39 | 128 |
| Au1rxx-base64 | 0.852 | 52 | 9 | 61 |
| Surfboard-tg-mixed | 0.879 | 116 | 16 | 132 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18366 | yes | 3.4 | 0 |
| DeltaKronecker-all | 8330 | yes | 3.45 | 0 |
| SoliSpirit-all | 7168 | yes | 2.02 | 0 |
| Epodonios-all | 7041 | yes | 1.94 | 0 |
| Surfboard-tg-mixed | 6047 | yes | 2.29 | 0 |
| mahdibland-V2RayAggregator | 5338 | yes | 1.38 | 0 |
| barry-far-vless | 5184 | yes | 1.71 | 0 |
| Surfboard-tg-vless | 4526 | yes | 2.12 | 0 |
| 10ium-ScrapeCategorize-Vless | 4358 | yes | 0.82 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.56 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 68 |
| speed | 37 |
| 204 | 16 |
| cn-block | 9 |
