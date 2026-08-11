# AutoNodes 每日报告

生成时间：2026-08-11 13:21:36

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84618 |
| 去重后节点数 | 24389 |
| TCP 可达数 | 3000 |
| 真测通过数 | 537 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24389 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 26.3 |
| geo | 1.4 |
| probe | 49.9 |
| real_test | 113.5 |
| tcp | 36.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 159 | 140 | 19 | 88.1% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 123 | 117 | 6 | 95.1% |
| vless | 210 | 132 | 78 | 62.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 23 |
| 204:ProxyError | 18 |
| 204:TimeoutError | 17 |
| geo:ClientOSError | 16 |
| speed:ClientOSError | 10 |
| geo:TimeoutError | 8 |
| cn-block:TimeoutError | 4 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4434 |
| ConnectionRefusedError | 832 |
| gaierror | 349 |
| OSError | 228 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Au1rxx-base64 | 0.912 | prefer | 391 | 0.854 | 1501 |
| Surfboard-tg-mixed | 0.721 | prefer | 90 | 0.644 | 6195 |
| mheidari-all | 0.602 | observe | 17 | 0.588 | 20194 |
| DeltaKronecker-all | 0.389 | observe | 13 | 0.385 | 5522 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5419 |
| Epodonios-all | 0.255 | observe | 0 | None | 6769 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.385 | 5 | 8 | 13 |
| mheidari-all | 0.588 | 10 | 7 | 17 |
| Surfboard-tg-mixed | 0.644 | 58 | 32 | 90 |
| Au1rxx-base64 | 0.854 | 334 | 57 | 391 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20194 | yes | 4.44 | 0 |
| SoliSpirit-all | 7602 | yes | 3.76 | 0 |
| Epodonios-all | 6769 | yes | 2.75 | 0 |
| Surfboard-tg-mixed | 6195 | yes | 3.53 | 0 |
| DeltaKronecker-all | 5522 | yes | 4.58 | 0 |
| 10ium-ScrapeCategorize-Vless | 5419 | yes | 2.28 | 0 |
| barry-far-vless | 5245 | yes | 1.98 | 0 |
| mahdibland-V2RayAggregator | 5209 | yes | 3.87 | 0 |
| Surfboard-tg-vless | 5048 | yes | 3.7 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.74 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 39 |
| speed | 34 |
| geo | 25 |
| cn-block | 8 |
