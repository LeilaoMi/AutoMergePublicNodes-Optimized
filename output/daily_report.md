# AutoNodes 每日报告

生成时间：2026-07-18 08:06:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 98/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80195 |
| 去重后节点数 | 21663 |
| TCP 可达数 | 3000 |
| 真测通过数 | 835 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21663 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 34.8 |
| geo | 1.3 |
| probe | 67.7 |
| real_test | 207.3 |
| tcp | 31.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 157 | 132 | 25 | 84.1% |
| socks | 43 | 35 | 8 | 81.4% |
| trojan | 524 | 493 | 31 | 94.1% |
| vless | 520 | 136 | 384 | 26.2% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 232 |
| speed:ClientOSError | 103 |
| cn-block:TimeoutError | 30 |
| speed:TimeoutError | 26 |
| geo:ClientOSError | 16 |
| 204:TimeoutError | 15 |
| 204:ProxyError | 9 |
| cn-block:ProxyError | 6 |
| 204:ClientOSError | 6 |
| cn-block:ClientOSError | 5 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4185 |
| ConnectionRefusedError | 670 |
| gaierror | 222 |
| OSError | 216 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.909 | prefer | 173 | 0.832 | 5606 |
| nscl5-all | 0.904 | prefer | 55 | 0.836 | 1976 |
| Au1rxx-base64 | 0.887 | prefer | 133 | 0.887 | 150 |
| mheidari-all | 0.647 | observe | 834 | 0.567 | 19158 |
| DeltaKronecker-all | 0.44 | observe | 48 | 0.354 | 3620 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 4321 |
| Epodonios-all | 0.255 | observe | 0 | None | 6683 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6902 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-v2raying | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.354 | 17 | 31 | 48 |
| mheidari-all | 0.567 | 473 | 361 | 834 |
| Surfboard-tg-mixed | 0.832 | 144 | 29 | 173 |
| nscl5-all | 0.836 | 46 | 9 | 55 |
| Au1rxx-base64 | 0.887 | 118 | 15 | 133 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19158 | yes | 3.41 | 0 |
| SoliSpirit-all | 6902 | yes | 3.25 | 0 |
| Epodonios-all | 6683 | yes | 3.6 | 0 |
| Surfboard-tg-mixed | 5606 | yes | 1.6 | 0 |
| mahdibland-V2RayAggregator | 5334 | yes | 1.78 | 0 |
| barry-far-vless | 4807 | yes | 0.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 4371 | yes | 1.32 | 0 |
| xiaoji235-airport-v2ray-all | 4321 | yes | 1.43 | 0 |
| Surfboard-tg-vless | 4250 | yes | 2.1 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 1.12 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 248 |
| speed | 129 |
| cn-block | 41 |
| 204 | 30 |
