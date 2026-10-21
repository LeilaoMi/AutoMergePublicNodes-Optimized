# AutoNodes 每日报告

生成时间：2026-10-21 21:54:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 91/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 96046 |
| 去重后节点数 | 27003 |
| TCP 可达数 | 3000 |
| 真测通过数 | 332 |
| verified 输出数 | 74 |
| global 输出数 | 300 |
| all 输出数 | 27003 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 19.3 |
| fetch | 7.2 |
| generate | 14.3 |
| geo | 1.5 |
| probe | 98.4 |
| real_test | 62.6 |
| tcp | 85.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 31 | 27 | 4 | 87.1% |
| hysteria2 | 11 | 10 | 1 | 90.9% |
| shadowsocks | 116 | 108 | 8 | 93.1% |
| socks | 3 | 0 | 3 | 0.0% |
| trojan | 54 | 49 | 5 | 90.7% |
| vless | 207 | 138 | 69 | 66.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 40 |
| speed:ClientOSError | 18 |
| 204:ProxyError | 7 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| speed:ProxyError | 4 |
| geo:ClientOSError | 4 |
| cn-block:TimeoutError | 3 |
| cn-block:ProxyError | 1 |
| speed:TimeoutError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6873 |
| ConnectionRefusedError | 1043 |
| OSError | 236 |
| gaierror | 103 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.932 | prefer | 27 | 0.963 | 31 |
| mheidari-all | 0.899 | prefer | 103 | 0.825 | 23903 |
| Au1rxx-base64 | 0.873 | prefer | 255 | 0.812 | 1596 |
| DeltaKronecker-all | 0.454 | observe | 18 | 0.389 | 4067 |
| ninja-vless | 0.412 | observe | 6 | 0.667 | 1791 |
| Surfboard-tg-mixed | 0.32 | observe | 4 | 0.5 | 7033 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4925 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10005 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5488 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ermaozi-get_subscribe | 0.143 | observe | 1 | 0.0 | 0 | 385 |
| tg-oneclickvpnkeys | 0.164 | observe | 4 | 0.25 | 0 | 92 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 486 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 377 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 372 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 255 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 233 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 232 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 224 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 202 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 121 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.25 | 1 | 3 | 4 |
| DeltaKronecker-all | 0.389 | 7 | 11 | 18 |
| roosterkid-openproxylist-v2ray | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.5 | 2 | 2 | 4 |
| ninja-vless | 0.667 | 4 | 2 | 6 |
| Au1rxx-base64 | 0.812 | 207 | 48 | 255 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23903 | yes | 5.52 | 0 |
| SoliSpirit-all | 10005 | yes | 3.38 | 0 |
| Epodonios-all | 7500 | yes | 4.85 | 0 |
| Surfboard-tg-mixed | 7033 | yes | 4.17 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.01 | 0 |
| barry-far-vless | 5734 | yes | 1.05 | 0 |
| Surfboard-tg-vless | 5488 | yes | 3.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 4925 | yes | 1.29 | 0 |
| mahdibland-V2RayAggregator | 4164 | yes | 0.6 | 0 |
| DeltaKronecker-all | 4067 | yes | 6.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 40 |
| speed | 23 |
| 204 | 14 |
| cn-block | 9 |
| geo | 4 |
