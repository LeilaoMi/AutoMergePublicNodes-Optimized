# AutoNodes 每日报告

生成时间：2026-08-24 18:52:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 84125 |
| 去重后节点数 | 23818 |
| TCP 可达数 | 3000 |
| 真测通过数 | 494 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23818 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 46.7 |
| geo | 1.4 |
| probe | 56.8 |
| real_test | 107.5 |
| tcp | 38.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 20 | 20 | 0 | 100.0% |
| shadowsocks | 123 | 110 | 13 | 89.4% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 37 | 29 | 8 | 78.4% |
| vless | 435 | 308 | 127 | 70.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 41 |
| cn-block:TimeoutError | 24 |
| 204:TimeoutError | 21 |
| speed:ClientOSError | 16 |
| geo:TimeoutError | 15 |
| speed:TimeoutError | 10 |
| 204:ClientOSError | 8 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| 204:ProxyError | 3 |
| speed:ClientPayloadError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5499 |
| ConnectionRefusedError | 887 |
| OSError | 233 |
| gaierror | 206 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.953 | prefer | 354 | 0.884 | 1779 |
| zhangkai | 0.929 | prefer | 24 | 0.958 | 144 |
| mheidari-all | 0.677 | observe | 224 | 0.598 | 19577 |
| DeltaKronecker-all | 0.58 | observe | 32 | 0.5 | 5914 |
| Surfboard-tg-mixed | 0.568 | observe | 8 | 0.875 | 6457 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4899 |
| Epodonios-all | 0.255 | observe | 0 | None | 6977 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7298 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.5 | 16 | 16 | 32 |
| mheidari-all | 0.598 | 134 | 90 | 224 |
| Surfboard-tg-mixed | 0.875 | 7 | 1 | 8 |
| Au1rxx-base64 | 0.884 | 313 | 41 | 354 |
| zhangkai | 0.958 | 23 | 1 | 24 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19577 | yes | 4.14 | 0 |
| SoliSpirit-all | 7298 | yes | 4.0 | 0 |
| Epodonios-all | 6977 | yes | 5.17 | 0 |
| Surfboard-tg-mixed | 6457 | yes | 3.5 | 0 |
| DeltaKronecker-all | 5914 | yes | 4.87 | 0 |
| barry-far-vless | 5662 | yes | 5.07 | 0 |
| Surfboard-tg-vless | 5373 | yes | 4.68 | 0 |
| 10ium-ScrapeCategorize-Vless | 4899 | yes | 2.93 | 0 |
| mahdibland-V2RayAggregator | 4132 | yes | 0.9 | 0 |
| MatinGhanbari-all-sub | 3987 | yes | 3.2 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 56 |
| cn-block | 34 |
| 204 | 32 |
| speed | 28 |
