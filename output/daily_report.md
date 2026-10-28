# AutoNodes 每日报告

生成时间：2026-10-28 13:18:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 3/89 |
| 原始节点数 | 97874 |
| 去重后节点数 | 26563 |
| TCP 可达数 | 3000 |
| 真测通过数 | 394 |
| verified 输出数 | 66 |
| global 输出数 | 300 |
| all 输出数 | 26563 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 21.4 |
| fetch | 7.2 |
| generate | 13.8 |
| geo | 1.6 |
| probe | 98.2 |
| real_test | 79.7 |
| tcp | 82.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 28 | 27 | 1 | 96.4% |
| hysteria2 | 13 | 11 | 2 | 84.6% |
| shadowsocks | 142 | 119 | 23 | 83.8% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 95 | 63 | 32 | 66.3% |
| vless | 251 | 173 | 78 | 68.9% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 79 |
| geo:ClientOSError | 20 |
| 204:ProxyError | 11 |
| cn-block:TimeoutError | 8 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 3 |
| geo:TimeoutError | 2 |
| 204:ClientOSError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6589 |
| ConnectionRefusedError | 1085 |
| OSError | 240 |
| gaierror | 229 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.939 | prefer | 35 | 0.943 | 513 |
| Au1rxx-base64 | 0.901 | prefer | 315 | 0.832 | 1778 |
| mheidari-all | 0.794 | prefer | 33 | 0.727 | 24702 |
| Surfboard-tg-mixed | 0.6 | observe | 123 | 0.52 | 7544 |
| roosterkid-openproxylist-v2ray | 0.372 | observe | 5 | 0.8 | 150 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| DeltaKronecker-all | 0.324 | observe | 8 | 0.375 | 2801 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| Epodonios-all | 0.272 | observe | 7 | 0.286 | 8008 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| chromego_merge | 0.137 | observe | 1 | 0.0 | 0 | 233 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 510 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 401 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 396 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 279 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 257 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 256 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 248 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 226 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 145 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| chromego_merge | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.286 | 2 | 5 | 7 |
| DeltaKronecker-all | 0.375 | 3 | 5 | 8 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.52 | 64 | 59 | 123 |
| mheidari-all | 0.727 | 24 | 9 | 33 |
| roosterkid-openproxylist-v2ray | 0.8 | 4 | 1 | 5 |
| Au1rxx-base64 | 0.832 | 262 | 53 | 315 |
| ermaozi | 0.943 | 33 | 2 | 35 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24702 | yes | 5.84 | 0 |
| SoliSpirit-all | 10344 | yes | 3.83 | 0 |
| Epodonios-all | 8035 | yes | 6.18 | 0 |
| Surfboard-tg-mixed | 7544 | yes | 3.93 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.35 | 0 |
| barry-far-vless | 5789 | yes | 1.38 | 0 |
| Surfboard-tg-vless | 5575 | yes | 3.68 | 0 |
| 10ium-ScrapeCategorize-Vless | 5004 | yes | 1.61 | 0 |
| mahdibland-V2RayAggregator | 4500 | yes | 2.93 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.7 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 79 |
| geo | 25 |
| 204 | 18 |
| cn-block | 14 |
