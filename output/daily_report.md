# AutoNodes 每日报告

生成时间：2026-07-09 19:58:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78644 |
| 去重后节点数 | 23912 |
| TCP 可达数 | 3000 |
| 真测通过数 | 279 |
| verified 输出数 | 279 |
| global 输出数 | 293 |
| all 输出数 | 23912 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 38.6 |
| geo | 1.3 |
| probe | 57.3 |
| real_test | 103.1 |
| tcp | 32.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 3 | 2 | 60.0% |
| shadowsocks | 103 | 87 | 16 | 84.5% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 67 | 26 | 41 | 38.8% |
| vless | 374 | 120 | 254 | 32.1% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 155 |
| geo:TimeoutError | 61 |
| 204:ProxyError | 24 |
| 204:TimeoutError | 22 |
| cn-block:TimeoutError | 16 |
| geo:ClientOSError | 13 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 5 |
| cn-block:ProxyError | 4 |
| speed:TimeoutError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4489 |
| ConnectionRefusedError | 824 |
| gaierror | 213 |
| OSError | 174 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Au1rxx-base64 | 0.854 | prefer | 25 | 0.88 | 66 |
| Surfboard-tg-mixed | 0.591 | observe | 260 | 0.512 | 5585 |
| mheidari-all | 0.407 | observe | 215 | 0.326 | 16918 |
| nscl5-all | 0.364 | observe | 2 | 1.0 | 1319 |
| DeltaKronecker-all | 0.358 | observe | 52 | 0.269 | 7533 |
| xiaoji235-airport-v2ray-all | 0.349 | observe | 3 | 0.667 | 2703 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4306 |
| Epodonios-all | 0.255 | observe | 0 | None | 6500 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ermaozi | 0.175 | observe | 0 | None | 0 | 8 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.269 | 14 | 38 | 52 |
| mheidari-all | 0.326 | 70 | 145 | 215 |
| Surfboard-tg-mixed | 0.512 | 133 | 127 | 260 |
| xiaoji235-airport-v2ray-all | 0.667 | 2 | 1 | 3 |
| Au1rxx-base64 | 0.88 | 22 | 3 | 25 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16918 | yes | 3.87 | 0 |
| DeltaKronecker-all | 7533 | yes | 3.84 | 0 |
| SoliSpirit-all | 6851 | yes | 1.8 | 0 |
| Epodonios-all | 6500 | yes | 1.6 | 0 |
| Surfboard-tg-mixed | 5585 | yes | 2.89 | 0 |
| mahdibland-V2RayAggregator | 5403 | yes | 1.7 | 0 |
| barry-far-vless | 4613 | yes | 1.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4306 | yes | 0.88 | 0 |
| Surfboard-tg-vless | 4106 | yes | 2.45 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.31 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 159 |
| geo | 79 |
| 204 | 51 |
| cn-block | 26 |
