# AutoNodes 每日报告

生成时间：2026-10-31 12:52:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 18/0 |
| 清理建议：优先/观察 | 3/86 |
| 原始节点数 | 80647 |
| 去重后节点数 | 26392 |
| TCP 可达数 | 3000 |
| 真测通过数 | 399 |
| verified 输出数 | 146 |
| global 输出数 | 300 |
| all 输出数 | 26392 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 22.2 |
| fetch | 7.2 |
| generate | 14.6 |
| geo | 1.5 |
| probe | 91.7 |
| real_test | 81.1 |
| tcp | 72.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 22 | 20 | 2 | 90.9% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 126 | 114 | 12 | 90.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 160 | 128 | 32 | 80.0% |
| vless | 224 | 125 | 99 | 55.8% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 90 |
| geo:ClientOSError | 16 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 8 |
| cn-block:ProxyError | 7 |
| cn-block:TimeoutError | 6 |
| geo:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |
| speed:ClientOSError | 2 |
| cn-block:ClientOSError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5591 |
| ConnectionRefusedError | 973 |
| gaierror | 256 |
| OSError | 234 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.901 | prefer | 324 | 0.833 | 1751 |
| zhangkai | 0.877 | prefer | 19 | 0.947 | 43 |
| Surfboard-tg-mixed | 0.738 | prefer | 36 | 0.667 | 7861 |
| DeltaKronecker-all | 0.622 | observe | 15 | 0.667 | 2848 |
| mheidari-all | 0.587 | observe | 146 | 0.507 | 14723 |
| mahdibland-V2RayAggregator | 0.287 | observe | 2 | 0.5 | 4635 |
| ermaozi-get_subscribe | 0.271 | observe | 1 | 1.0 | 412 |
| xiaoji235-airport-v2ray-all | 0.259 | observe | 3 | 0.333 | 6752 |
| ermaozi | 0.258 | observe | 1 | 1.0 | 79 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4970 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Epodonios-all | 0.025 | observe | 0 | None | 1 | 0 |
| MatinGhanbari-super-sub | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 2 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 11 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 519 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 410 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 405 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 288 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 266 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 265 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 257 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 235 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 230 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 154 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| MatinGhanbari-super-sub | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.333 | 1 | 2 | 3 |
| mahdibland-V2RayAggregator | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.507 | 74 | 72 | 146 |
| DeltaKronecker-all | 0.667 | 10 | 5 | 15 |
| Surfboard-tg-mixed | 0.667 | 24 | 12 | 36 |
| Au1rxx-base64 | 0.833 | 270 | 54 | 324 |
| zhangkai | 0.947 | 18 | 1 | 19 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| ermaozi | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14723 | yes | 5.98 | 0 |
| SoliSpirit-all | 10576 | yes | 3.87 | 0 |
| Surfboard-tg-mixed | 7861 | yes | 4.59 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.69 | 0 |
| barry-far-vless | 5912 | yes | 1.46 | 0 |
| Surfboard-tg-vless | 5698 | yes | 3.83 | 0 |
| 10ium-ScrapeCategorize-Vless | 4970 | yes | 1.74 | 0 |
| mahdibland-V2RayAggregator | 4635 | yes | 0.15 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.9 | 0 |
| DeltaKronecker-all | 2848 | yes | 6.49 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 90 |
| geo | 21 |
| 204 | 19 |
| cn-block | 15 |
| speed | 3 |
