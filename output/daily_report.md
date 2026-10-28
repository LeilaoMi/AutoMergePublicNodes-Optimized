# AutoNodes 每日报告

生成时间：2026-10-28 06:00:49

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/1 |
| 清理建议：优先/观察 | 4/87 |
| 原始节点数 | 97707 |
| 去重后节点数 | 26826 |
| TCP 可达数 | 3000 |
| 真测通过数 | 527 |
| verified 输出数 | 68 |
| global 输出数 | 300 |
| all 输出数 | 26826 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 25.2 |
| fetch | 6.7 |
| generate | 13.6 |
| geo | 1.5 |
| probe | 99.3 |
| real_test | 92.0 |
| tcp | 79.1 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 92 | 90 | 2 | 97.8% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 167 | 156 | 11 | 93.4% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 77 | 68 | 9 | 88.3% |
| vless | 327 | 202 | 125 | 61.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 94 |
| geo:ClientOSError | 32 |
| 204:ProxyError | 6 |
| cn-block:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| 204:TimeoutError | 3 |
| speed:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6432 |
| ConnectionRefusedError | 1101 |
| gaierror | 301 |
| OSError | 241 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi-get_subscribe | 0.966 | prefer | 74 | 0.959 | 467 |
| Au1rxx-base64 | 0.946 | prefer | 334 | 0.88 | 1707 |
| zhangkai | 0.923 | prefer | 19 | 1.0 | 43 |
| Surfboard-tg-mixed | 0.755 | prefer | 161 | 0.677 | 7522 |
| roosterkid-openproxylist-v2ray | 0.494 | observe | 8 | 0.875 | 150 |
| mheidari-all | 0.46 | observe | 77 | 0.377 | 24790 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 10431 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 52 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4988 |
| Epodonios-all | 0.255 | observe | 0 | None | 8008 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigV2rayNG | 0.135 | observe | 1 | 0.0 | 0 | 200 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 509 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 400 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 395 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 278 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 256 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 255 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 247 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 225 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 144 | 连续死亡次数 >= 2 |
| downweight | DeltaKronecker-all | 0.208 | 7 | 0.143 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-ConfigV2rayNG | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.143 | 1 | 6 | 7 |
| mheidari-all | 0.377 | 29 | 48 | 77 |
| Surfboard-tg-mixed | 0.677 | 109 | 52 | 161 |
| roosterkid-openproxylist-v2ray | 0.875 | 7 | 1 | 8 |
| Au1rxx-base64 | 0.88 | 294 | 40 | 334 |
| ermaozi-get_subscribe | 0.959 | 71 | 3 | 74 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 19 | 0 | 19 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24790 | yes | 6.0 | 0 |
| SoliSpirit-all | 10431 | yes | 4.86 | 0 |
| Epodonios-all | 8008 | yes | 5.29 | 0 |
| Surfboard-tg-mixed | 7522 | yes | 0.45 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.53 | 0 |
| barry-far-vless | 5751 | yes | 0.32 | 0 |
| Surfboard-tg-vless | 5538 | yes | 3.71 | 0 |
| 10ium-ScrapeCategorize-Vless | 4988 | yes | 3.69 | 0 |
| mahdibland-V2RayAggregator | 4500 | yes | 0.2 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.84 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 94 |
| geo | 33 |
| cn-block | 11 |
| 204 | 10 |
| speed | 3 |
