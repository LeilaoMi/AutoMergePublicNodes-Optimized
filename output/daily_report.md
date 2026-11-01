# AutoNodes 每日报告

生成时间：2026-11-01 22:16:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 17/0 |
| 清理建议：优先/观察 | 4/86 |
| 原始节点数 | 82958 |
| 去重后节点数 | 26789 |
| TCP 可达数 | 3000 |
| 真测通过数 | 429 |
| verified 输出数 | 74 |
| global 输出数 | 300 |
| all 输出数 | 26789 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 26.1 |
| fetch | 7.5 |
| generate | 14.8 |
| geo | 1.5 |
| probe | 94.9 |
| real_test | 83.9 |
| tcp | 77.7 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 48 | 46 | 2 | 95.8% |
| hysteria2 | 17 | 16 | 1 | 94.1% |
| shadowsocks | 170 | 123 | 47 | 72.4% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 123 | 116 | 7 | 94.3% |
| vless | 215 | 129 | 86 | 60.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 73 |
| geo:ClientOSError | 23 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 10 |
| cn-block:ClientOSError | 6 |
| geo:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| 204:TimeoutError | 3 |
| speed:ClientOSError | 2 |
| speed:TimeoutError | 2 |
| 204:ClientOSError | 1 |
| 204:ProxyConnectionError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5887 |
| ConnectionRefusedError | 948 |
| OSError | 234 |
| gaierror | 174 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.923 | prefer | 19 | 1.0 | 43 |
| ermaozi-get_subscribe | 0.92 | prefer | 28 | 0.929 | 499 |
| Au1rxx-base64 | 0.868 | prefer | 320 | 0.8 | 1751 |
| mheidari-all | 0.866 | prefer | 54 | 0.796 | 15206 |
| Surfboard-tg-mixed | 0.643 | observe | 149 | 0.564 | 8273 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4800 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| DeltaKronecker-all | 0.287 | observe | 2 | 0.5 | 3716 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4976 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 414 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 409 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 292 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 270 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 269 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 261 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 239 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 234 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 158 | 连续死亡次数 >= 2 |
| disable | tg-AzadNet | 0.0 | 0 | None | 145 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.564 | 84 | 65 | 149 |
| mheidari-all | 0.796 | 43 | 11 | 54 |
| Au1rxx-base64 | 0.8 | 256 | 64 | 320 |
| ermaozi-get_subscribe | 0.929 | 26 | 2 | 28 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15206 | yes | 6.57 | 0 |
| SoliSpirit-all | 10673 | yes | 5.53 | 0 |
| Surfboard-tg-mixed | 8273 | yes | 4.56 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.64 | 0 |
| barry-far-vless | 5986 | yes | 1.97 | 0 |
| Surfboard-tg-vless | 5823 | yes | 4.77 | 0 |
| 10ium-ScrapeCategorize-Vless | 4976 | yes | 2.33 | 0 |
| mahdibland-V2RayAggregator | 4800 | yes | 2.06 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.06 | 0 |
| DeltaKronecker-all | 3716 | yes | 6.71 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 73 |
| geo | 27 |
| 204 | 20 |
| cn-block | 19 |
| speed | 4 |
