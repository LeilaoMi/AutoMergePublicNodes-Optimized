# AutoNodes 每日报告

生成时间：2026-10-25 11:51:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 5/87 |
| 原始节点数 | 97033 |
| 去重后节点数 | 27210 |
| TCP 可达数 | 3000 |
| 真测通过数 | 474 |
| verified 输出数 | 172 |
| global 输出数 | 300 |
| all 输出数 | 27210 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 31.9 |
| fetch | 7.1 |
| generate | 13.5 |
| geo | 1.5 |
| probe | 92.7 |
| real_test | 88.4 |
| tcp | 84.9 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 105 | 105 | 0 | 100.0% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 155 | 136 | 19 | 87.7% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 68 | 47 | 21 | 69.1% |
| vless | 238 | 174 | 64 | 73.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 72 |
| 204:TimeoutError | 12 |
| geo:ClientOSError | 7 |
| 204:ClientOSError | 5 |
| 204:ProxyError | 3 |
| cn-block:TimeoutError | 2 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6888 |
| ConnectionRefusedError | 1037 |
| OSError | 235 |
| gaierror | 151 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 83 | 0.988 | 604 |
| zhangkai | 0.964 | prefer | 24 | 1.0 | 59 |
| Au1rxx-base64 | 0.893 | prefer | 307 | 0.831 | 1618 |
| Surfboard-tg-mixed | 0.805 | prefer | 89 | 0.73 | 7259 |
| mheidari-all | 0.802 | prefer | 34 | 0.735 | 24013 |
| DeltaKronecker-all | 0.638 | observe | 41 | 0.561 | 3849 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| tg-oneclickvpnkeys | 0.316 | observe | 2 | 1.0 | 112 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 11 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 500 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 391 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 386 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 269 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 247 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 246 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 238 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 135 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.561 | 23 | 18 | 41 |
| Surfboard-tg-mixed | 0.73 | 65 | 24 | 89 |
| mheidari-all | 0.735 | 25 | 9 | 34 |
| Au1rxx-base64 | 0.831 | 255 | 52 | 307 |
| ermaozi | 0.988 | 82 | 1 | 83 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24013 | yes | 6.88 | 0 |
| SoliSpirit-all | 10577 | yes | 2.29 | 0 |
| Epodonios-all | 7583 | yes | 3.48 | 0 |
| Surfboard-tg-mixed | 7259 | yes | 5.69 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.85 | 0 |
| barry-far-vless | 5633 | yes | 0.53 | 0 |
| Surfboard-tg-vless | 5481 | yes | 4.01 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 1.08 | 0 |
| mahdibland-V2RayAggregator | 4186 | yes | 1.1 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.63 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 72 |
| 204 | 20 |
| geo | 7 |
| cn-block | 5 |
| speed | 1 |
