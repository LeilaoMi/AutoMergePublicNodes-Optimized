# AutoNodes 每日报告

生成时间：2026-10-26 22:51:22

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 4/88 |
| 原始节点数 | 96962 |
| 去重后节点数 | 26586 |
| TCP 可达数 | 3000 |
| 真测通过数 | 446 |
| verified 输出数 | 96 |
| global 输出数 | 300 |
| all 输出数 | 26586 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 36.1 |
| fetch | 4.3 |
| generate | 8.4 |
| geo | 1.5 |
| probe | 74.7 |
| real_test | 91.3 |
| tcp | 84.0 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 35 | 35 | 0 | 100.0% |
| hysteria2 | 13 | 13 | 0 | 100.0% |
| shadowsocks | 149 | 117 | 32 | 78.5% |
| trojan | 61 | 58 | 3 | 95.1% |
| vless | 359 | 223 | 136 | 62.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 68 |
| speed:ClientOSError | 41 |
| geo:ClientOSError | 33 |
| cn-block:TimeoutError | 13 |
| cn-block:ClientOSError | 6 |
| 204:ProxyError | 5 |
| cn-block:ProxyError | 1 |
| 204:TimeoutError | 1 |
| geo:TimeoutError | 1 |
| speed:TimeoutError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6690 |
| ConnectionRefusedError | 1043 |
| OSError | 236 |
| gaierror | 223 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.996 | prefer | 35 | 1.0 | 564 |
| Surfboard-tg-mixed | 0.826 | prefer | 128 | 0.75 | 7052 |
| Au1rxx-base64 | 0.767 | prefer | 395 | 0.699 | 1735 |
| mheidari-all | 0.761 | prefer | 45 | 0.689 | 24769 |
| DeltaKronecker-all | 0.372 | observe | 9 | 0.444 | 3004 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| SoliSpirit-all | 0.287 | observe | 2 | 0.5 | 10741 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4919 |
| Epodonios-all | 0.255 | observe | 0 | None | 7537 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 10 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 505 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 396 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 391 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 274 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 252 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 251 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 243 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 221 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 140 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.444 | 4 | 5 | 9 |
| SoliSpirit-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.689 | 31 | 14 | 45 |
| Au1rxx-base64 | 0.699 | 276 | 119 | 395 |
| Surfboard-tg-mixed | 0.75 | 96 | 32 | 128 |
| ninja-vless | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |
| ermaozi | 1.0 | 35 | 0 | 35 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24769 | yes | 3.32 | 0 |
| SoliSpirit-all | 10741 | yes | 1.9 | 0 |
| Epodonios-all | 7537 | yes | 1.78 | 0 |
| Surfboard-tg-mixed | 7052 | yes | 2.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 0.58 | 0 |
| barry-far-vless | 5651 | yes | 0.74 | 0 |
| Surfboard-tg-vless | 5366 | yes | 2.52 | 0 |
| 10ium-ScrapeCategorize-Vless | 4919 | yes | 1.19 | 0 |
| mahdibland-V2RayAggregator | 4466 | yes | 0.33 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.17 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 68 |
| speed | 42 |
| geo | 35 |
| cn-block | 20 |
| 204 | 6 |
