# AutoNodes 每日报告

生成时间：2026-10-14 13:17:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 4/90 |
| 原始节点数 | 97972 |
| 去重后节点数 | 27169 |
| TCP 可达数 | 3000 |
| 真测通过数 | 66 |
| verified 输出数 | 66 |
| global 输出数 | 72 |
| all 输出数 | 27169 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.6 |
| fetch | 5.8 |
| generate | 10.1 |
| geo | 1.5 |
| probe | 92.0 |
| real_test | 70.0 |
| tcp | 89.6 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 26 | 26 | 0 | 100.0% |
| hysteria2 | 9 | 7 | 2 | 77.8% |
| shadowsocks | 136 | 119 | 17 | 87.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 2 | 1 | 1 | 50.0% |
| vless | 190 | 116 | 74 | 61.1% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 49 |
| speed:ClientOSError | 13 |
| 204:ProxyError | 8 |
| geo:ClientOSError | 6 |
| cn-block:TimeoutError | 5 |
| 204:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7488 |
| ConnectionRefusedError | 999 |
| OSError | 230 |
| gaierror | 86 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.927 | prefer | 19 | 1.0 | 144 |
| Au1rxx-base64 | 0.814 | prefer | 200 | 0.745 | 1782 |
| mheidari-all | 0.78 | prefer | 78 | 0.705 | 23983 |
| Surfboard-tg-mixed | 0.736 | prefer | 59 | 0.661 | 7056 |
| ermaozi-get_subscribe | 0.534 | observe | 7 | 1.0 | 515 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5125 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 4803 |
| Epodonios-all | 0.255 | observe | 0 | None | 7542 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 450 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 341 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 336 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 197 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 196 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 188 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 166 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 161 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 85 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.661 | 39 | 20 | 59 |
| mheidari-all | 0.705 | 55 | 23 | 78 |
| Au1rxx-base64 | 0.745 | 149 | 51 | 200 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 7 | 0 | 7 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23983 | yes | 5.05 | 0 |
| SoliSpirit-all | 9829 | yes | 2.18 | 0 |
| Epodonios-all | 7542 | yes | 3.99 | 0 |
| Surfboard-tg-mixed | 7056 | yes | 3.28 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.0 | 0 |
| barry-far-vless | 5831 | yes | 1.55 | 0 |
| Surfboard-tg-vless | 5579 | yes | 3.46 | 0 |
| 10ium-ScrapeCategorize-Vless | 5125 | yes | 1.4 | 0 |
| DeltaKronecker-all | 4803 | yes | 3.74 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 2.59 | 0 |

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
| test_one_timeout | 49 |
| 204 | 17 |
| speed | 13 |
| cn-block | 10 |
| geo | 6 |
