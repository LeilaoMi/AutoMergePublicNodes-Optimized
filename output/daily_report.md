# AutoNodes 每日报告

生成时间：2026-07-11 08:08:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 75954 |
| 去重后节点数 | 23903 |
| TCP 可达数 | 3000 |
| 真测通过数 | 403 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23903 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| generate | 24.3 |
| geo | 1.4 |
| probe | 46.0 |
| real_test | 102.4 |
| tcp | 32.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 131 | 111 | 20 | 84.7% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 258 | 219 | 39 | 84.9% |
| vless | 105 | 27 | 78 | 25.7% |
| vmess | 7 | 7 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 43 |
| speed:ClientOSError | 25 |
| geo:ClientOSError | 16 |
| cn-block:ClientOSError | 12 |
| 204:ClientOSError | 7 |
| cn-block:TimeoutError | 7 |
| 204:ProxyError | 7 |
| speed:TimeoutError | 6 |
| geo:ProxyError | 6 |
| 204:TimeoutError | 5 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4446 |
| ConnectionRefusedError | 661 |
| gaierror | 235 |
| OSError | 188 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.911 | prefer | 63 | 0.841 | 16239 |
| Surfboard-tg-mixed | 0.865 | prefer | 128 | 0.789 | 5476 |
| DeltaKronecker-all | 0.759 | prefer | 250 | 0.68 | 7969 |
| Au1rxx-base64 | 0.682 | observe | 60 | 0.683 | 111 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 3953 |
| Epodonios-all | 0.255 | observe | 0 | None | 6366 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6404 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4097 |

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
| ninja-vless | 0.333 | 1 | 2 | 3 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.68 | 170 | 80 | 250 |
| Au1rxx-base64 | 0.683 | 41 | 19 | 60 |
| Surfboard-tg-mixed | 0.789 | 101 | 27 | 128 |
| mheidari-all | 0.841 | 53 | 10 | 63 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16239 | yes | 2.82 | 0 |
| DeltaKronecker-all | 7969 | yes | 2.94 | 0 |
| SoliSpirit-all | 6404 | yes | 1.87 | 0 |
| Epodonios-all | 6366 | yes | 1.34 | 0 |
| Surfboard-tg-mixed | 5476 | yes | 2.13 | 0 |
| mahdibland-V2RayAggregator | 5423 | yes | 1.44 | 0 |
| barry-far-vless | 4653 | yes | 1.44 | 0 |
| Surfboard-tg-vless | 4097 | yes | 2.95 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 1.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 3953 | yes | 1.28 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 65 |
| speed | 34 |
| cn-block | 22 |
| 204 | 19 |
