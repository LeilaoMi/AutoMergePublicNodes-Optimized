# AutoNodes 每日报告

生成时间：2026-10-22 05:07:44

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 91/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 96990 |
| 去重后节点数 | 27063 |
| TCP 可达数 | 3000 |
| 真测通过数 | 425 |
| verified 输出数 | 117 |
| global 输出数 | 300 |
| all 输出数 | 27063 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 33.9 |
| fetch | 5.6 |
| generate | 10.3 |
| geo | 1.5 |
| probe | 72.7 |
| real_test | 97.6 |
| tcp | 85.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 95 | 87 | 8 | 91.6% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 123 | 116 | 7 | 94.3% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 56 | 49 | 7 | 87.5% |
| vless | 300 | 158 | 142 | 52.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 105 |
| speed:ClientOSError | 18 |
| geo:ClientOSError | 14 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 7 |
| cn-block:TimeoutError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:TimeoutError | 2 |
| speed:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6755 |
| ConnectionRefusedError | 1021 |
| OSError | 236 |
| gaierror | 149 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 26 | 1.0 | 31 |
| ermaozi-get_subscribe | 0.933 | prefer | 66 | 0.924 | 523 |
| Au1rxx-base64 | 0.868 | prefer | 288 | 0.806 | 1615 |
| mheidari-all | 0.577 | observe | 179 | 0.497 | 24252 |
| Surfboard-tg-mixed | 0.568 | observe | 8 | 0.875 | 7097 |
| DeltaKronecker-all | 0.474 | observe | 15 | 0.467 | 4067 |
| ninja-vless | 0.364 | observe | 5 | 0.6 | 1791 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4925 |
| Epodonios-all | 0.255 | observe | 0 | None | 7591 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-oneclickvpnkeys | 0.084 | observe | 4 | 0.0 | 0 | 107 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 487 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 378 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 373 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 256 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 234 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 233 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 225 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 122 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-oneclickvpnkeys | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.467 | 7 | 8 | 15 |
| mheidari-all | 0.497 | 89 | 90 | 179 |
| ninja-vless | 0.6 | 3 | 2 | 5 |
| Au1rxx-base64 | 0.806 | 232 | 56 | 288 |
| Surfboard-tg-mixed | 0.875 | 7 | 1 | 8 |
| ermaozi-get_subscribe | 0.924 | 61 | 5 | 66 |
| zhangkai | 1.0 | 26 | 0 | 26 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24252 | yes | 5.02 | 0 |
| SoliSpirit-all | 10126 | yes | 2.11 | 0 |
| Epodonios-all | 7591 | yes | 3.89 | 0 |
| Surfboard-tg-mixed | 7097 | yes | 2.9 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.09 | 0 |
| barry-far-vless | 5773 | yes | 1.51 | 0 |
| Surfboard-tg-vless | 5559 | yes | 3.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 4925 | yes | 0.65 | 0 |
| mahdibland-V2RayAggregator | 4164 | yes | 2.37 | 0 |
| DeltaKronecker-all | 4067 | yes | 4.3 | 0 |

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
| test_one_timeout | 105 |
| speed | 21 |
| 204 | 17 |
| geo | 14 |
| cn-block | 9 |
