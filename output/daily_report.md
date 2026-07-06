# AutoNodes 每日报告

生成时间：2026-07-06 15:48:42

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79704 |
| 去重后节点数 | 24484 |
| TCP 可达数 | 3000 |
| 真测通过数 | 375 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24484 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 26.1 |
| geo | 1.3 |
| probe | 42.9 |
| real_test | 73.9 |
| tcp | 31.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 5 | 5 | 0 | 100.0% |
| shadowsocks | 133 | 107 | 26 | 80.5% |
| socks | 13 | 9 | 4 | 69.2% |
| trojan | 237 | 203 | 34 | 85.7% |
| vless | 49 | 11 | 38 | 22.4% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 22 |
| speed:ClientOSError | 17 |
| 204:ProxyError | 11 |
| 204:TimeoutError | 11 |
| geo:TimeoutError | 9 |
| speed:ProxyError | 8 |
| geo:ClientOSError | 5 |
| geo:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| speed:TimeoutError | 3 |
| cn-block:TimeoutError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4409 |
| ConnectionRefusedError | 779 |
| OSError | 161 |
| gaierror | 137 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.887 | prefer | 107 | 0.813 | 5986 |
| DeltaKronecker-all | 0.852 | prefer | 187 | 0.775 | 8330 |
| mheidari-all | 0.796 | prefer | 114 | 0.719 | 16268 |
| Au1rxx-base64 | 0.753 | prefer | 22 | 0.773 | 84 |
| nscl5-all | 0.424 | observe | 3 | 1.0 | 1651 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| ermaozi | 0.256 | observe | 1 | 1.0 | 26 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4358 |

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
| tg-LonUp_M | 0.5 | 2 | 2 | 4 |
| mheidari-all | 0.719 | 82 | 32 | 114 |
| Au1rxx-base64 | 0.773 | 17 | 5 | 22 |
| DeltaKronecker-all | 0.775 | 145 | 42 | 187 |
| Surfboard-tg-mixed | 0.813 | 87 | 20 | 107 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16268 | yes | 3.04 | 0 |
| DeltaKronecker-all | 8330 | yes | 3.42 | 0 |
| SoliSpirit-all | 7108 | yes | 2.48 | 0 |
| Epodonios-all | 6989 | yes | 2.44 | 0 |
| Surfboard-tg-mixed | 5986 | yes | 2.61 | 0 |
| mahdibland-V2RayAggregator | 5349 | yes | 1.4 | 0 |
| barry-far-vless | 5099 | yes | 1.36 | 0 |
| Surfboard-tg-vless | 4436 | yes | 1.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 4358 | yes | 1.14 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.43 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 44 |
| speed | 28 |
| geo | 19 |
| cn-block | 11 |
