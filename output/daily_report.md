# AutoNodes 每日报告

生成时间：2026-08-23 06:55:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 98/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 77609 |
| 去重后节点数 | 21148 |
| TCP 可达数 | 3000 |
| 真测通过数 | 797 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21148 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| generate | 35.9 |
| geo | 1.4 |
| probe | 61.9 |
| real_test | 160.4 |
| tcp | 33.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 113 | 113 | 0 | 100.0% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 221 | 210 | 11 | 95.0% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 145 | 137 | 8 | 94.5% |
| vless | 455 | 318 | 137 | 69.9% |
| vmess | 4 | 3 | 1 | 75.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 47 |
| speed:TimeoutError | 32 |
| speed:ClientOSError | 18 |
| cn-block:TimeoutError | 15 |
| geo:ClientOSError | 14 |
| 204:TimeoutError | 12 |
| 204:ProxyError | 11 |
| cn-block:ClientOSError | 7 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4576 |
| ConnectionRefusedError | 828 |
| gaierror | 351 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | prefer | 111 | 1.0 | 144 |
| Au1rxx-base64 | 0.996 | prefer | 494 | 0.925 | 1821 |
| Surfboard-tg-mixed | 0.896 | prefer | 150 | 0.82 | 6303 |
| mheidari-all | 0.618 | observe | 104 | 0.538 | 14434 |
| DeltaKronecker-all | 0.574 | observe | 81 | 0.494 | 5288 |
| nscl5-all | 0.428 | observe | 7 | 0.714 | 1082 |
| tg-oneclickvpnkeys | 0.316 | observe | 2 | 1.0 | 131 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.287 | observe | 2 | 0.5 | 4989 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| roosterkid-openproxylist-v2ray | 0.133 | observe | 1 | 0.0 | 0 | 150 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.494 | 40 | 41 | 81 |
| 10ium-ScrapeCategorize-Vless | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.538 | 56 | 48 | 104 |
| nscl5-all | 0.714 | 5 | 2 | 7 |
| Surfboard-tg-mixed | 0.82 | 123 | 27 | 150 |
| Au1rxx-base64 | 0.925 | 457 | 37 | 494 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14434 | yes | 4.63 | 0 |
| SoliSpirit-all | 7111 | yes | 4.45 | 0 |
| Epodonios-all | 6859 | yes | 4.9 | 0 |
| Surfboard-tg-mixed | 6303 | yes | 3.7 | 0 |
| barry-far-vless | 5430 | yes | 3.44 | 0 |
| DeltaKronecker-all | 5288 | yes | 5.34 | 0 |
| Surfboard-tg-vless | 5154 | yes | 3.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 4989 | yes | 3.21 | 0 |
| mahdibland-V2RayAggregator | 4094 | yes | 2.23 | 0 |
| MatinGhanbari-all-sub | 3985 | yes | 3.53 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 62 |
| speed | 50 |
| 204 | 24 |
| cn-block | 24 |
