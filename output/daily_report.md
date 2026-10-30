# AutoNodes 每日报告

生成时间：2026-10-30 06:06:09

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 19/0 |
| 清理建议：优先/观察 | 3/85 |
| 原始节点数 | 99789 |
| 去重后节点数 | 27982 |
| TCP 可达数 | 3000 |
| 真测通过数 | 499 |
| verified 输出数 | 91 |
| global 输出数 | 300 |
| all 输出数 | 27982 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 26.5 |
| fetch | 6.8 |
| generate | 12.9 |
| geo | 1.5 |
| probe | 91.7 |
| real_test | 91.8 |
| tcp | 86.4 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 21 | 20 | 1 | 95.2% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 177 | 152 | 25 | 85.9% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 177 | 157 | 20 | 88.7% |
| vless | 301 | 156 | 145 | 51.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 122 |
| geo:ClientOSError | 31 |
| 204:ProxyError | 10 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 6 |
| speed:ClientOSError | 6 |
| cn-block:ProxyError | 4 |
| cn-block:TimeoutError | 3 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6863 |
| ConnectionRefusedError | 1125 |
| gaierror | 276 |
| OSError | 244 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.934 | prefer | 21 | 0.952 | 515 |
| Au1rxx-base64 | 0.926 | prefer | 332 | 0.858 | 1735 |
| Surfboard-tg-mixed | 0.708 | prefer | 146 | 0.63 | 7756 |
| mheidari-all | 0.612 | observe | 188 | 0.532 | 34034 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 2709 |
| xiaoji235-airport-v2ray-all | 0.3 | observe | 5 | 0.4 | 6752 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5005 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 10500 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5729 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ShadowsocksM | 0.175 | observe | 0 | None | 0 | 2 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 515 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 406 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 401 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 284 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 262 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 261 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 253 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 231 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 226 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 150 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.4 | 2 | 3 | 5 |
| mheidari-all | 0.532 | 100 | 88 | 188 |
| Surfboard-tg-mixed | 0.63 | 92 | 54 | 146 |
| Au1rxx-base64 | 0.858 | 285 | 47 | 332 |
| ermaozi | 0.952 | 20 | 1 | 21 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 34034 | yes | 6.11 | 0 |
| SoliSpirit-all | 10500 | yes | 4.02 | 0 |
| Surfboard-tg-mixed | 7756 | yes | 3.77 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.23 | 0 |
| barry-far-vless | 5941 | yes | 0.7 | 0 |
| Surfboard-tg-vless | 5729 | yes | 3.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 5005 | yes | 0.51 | 0 |
| mahdibland-V2RayAggregator | 4444 | yes | 2.82 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.78 | 0 |
| DeltaKronecker-all | 2709 | yes | 5.97 | 0 |

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
| test_one_timeout | 122 |
| geo | 33 |
| 204 | 19 |
| cn-block | 13 |
| speed | 6 |
