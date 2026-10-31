# AutoNodes 每日报告

生成时间：2026-10-31 06:00:53

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 4/85 |
| 原始节点数 | 80746 |
| 去重后节点数 | 26596 |
| TCP 可达数 | 3000 |
| 真测通过数 | 583 |
| verified 输出数 | 146 |
| global 输出数 | 300 |
| all 输出数 | 26596 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 31.3 |
| fetch | 4.1 |
| generate | 9.4 |
| geo | 1.4 |
| probe | 68.1 |
| real_test | 94.5 |
| tcp | 79.3 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 95 | 93 | 2 | 97.9% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 166 | 144 | 22 | 86.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 179 | 168 | 11 | 93.9% |
| vless | 267 | 165 | 102 | 61.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 71 |
| geo:ClientOSError | 31 |
| cn-block:ClientOSError | 7 |
| 204:TimeoutError | 6 |
| cn-block:TimeoutError | 6 |
| cn-block:ProxyError | 4 |
| 204:ProxyError | 4 |
| speed:ClientOSError | 3 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 2 |
| speed:TimeoutError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6152 |
| ConnectionRefusedError | 954 |
| OSError | 248 |
| gaierror | 123 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.994 | prefer | 95 | 0.979 | 622 |
| Au1rxx-base64 | 0.926 | prefer | 339 | 0.858 | 1751 |
| mheidari-all | 0.846 | prefer | 109 | 0.771 | 14594 |
| Surfboard-tg-mixed | 0.716 | prefer | 174 | 0.638 | 7827 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 6752 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 2724 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 94 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4960 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ShadowsocksM | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 518 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 409 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 404 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 287 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 265 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 264 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 256 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 234 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 229 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 153 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.638 | 111 | 63 | 174 |
| mheidari-all | 0.771 | 84 | 25 | 109 |
| Au1rxx-base64 | 0.858 | 291 | 48 | 339 |
| ermaozi | 0.979 | 93 | 2 | 95 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14594 | yes | 3.11 | 0 |
| SoliSpirit-all | 10524 | yes | 2.46 | 0 |
| Surfboard-tg-mixed | 7827 | yes | 2.87 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.02 | 0 |
| barry-far-vless | 5895 | yes | 0.59 | 0 |
| Surfboard-tg-vless | 5680 | yes | 2.13 | 0 |
| 10ium-ScrapeCategorize-Vless | 4960 | yes | 0.98 | 0 |
| mahdibland-V2RayAggregator | 4635 | yes | 1.7 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.34 | 0 |
| DeltaKronecker-all | 2724 | yes | 2.66 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 71 |
| geo | 32 |
| cn-block | 17 |
| 204 | 13 |
| speed | 6 |
