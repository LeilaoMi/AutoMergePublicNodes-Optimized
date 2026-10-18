# AutoNodes 每日报告

生成时间：2026-10-18 11:28:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 2/91 |
| 原始节点数 | 98405 |
| 去重后节点数 | 27711 |
| TCP 可达数 | 3000 |
| 真测通过数 | 470 |
| verified 输出数 | 143 |
| global 输出数 | 300 |
| all 输出数 | 27711 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 23.2 |
| fetch | 7.9 |
| generate | 13.9 |
| geo | 1.5 |
| probe | 95.2 |
| real_test | 100.3 |
| tcp | 86.2 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 100 | 97 | 3 | 97.0% |
| hysteria2 | 23 | 17 | 6 | 73.9% |
| shadowsocks | 147 | 126 | 21 | 85.7% |
| socks | 7 | 4 | 3 | 57.1% |
| trojan | 39 | 27 | 12 | 69.2% |
| vless | 332 | 204 | 128 | 61.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 78 |
| geo:ClientOSError | 30 |
| 204:TimeoutError | 16 |
| 204:ProxyError | 14 |
| speed:ClientOSError | 10 |
| cn-block:ProxyError | 6 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 5 |
| speed:TimeoutError | 3 |
| geo:TimeoutError | 2 |
| cn-block:TimeoutError | 2 |
| speed:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7129 |
| ConnectionRefusedError | 1050 |
| gaierror | 257 |
| OSError | 237 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.98 | prefer | 102 | 0.961 | 710 |
| Au1rxx-base64 | 0.879 | prefer | 378 | 0.804 | 1920 |
| Surfboard-tg-mixed | 0.58 | observe | 52 | 0.5 | 7030 |
| DeltaKronecker-all | 0.478 | observe | 101 | 0.396 | 4750 |
| mheidari-all | 0.418 | observe | 10 | 0.5 | 23769 |
| tg-LonUp_M | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4983 |
| Epodonios-all | 0.255 | observe | 0 | None | 7561 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9785 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Surfboard-tg-vless | 0.17 | observe | 3 | 0.0 | 0 | 5615 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-PrivateVPNs | 0.175 | observe | 0 | None | 0 | 12 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 473 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 364 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 359 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 242 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 220 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 219 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 189 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 184 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 108 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.396 | 40 | 61 | 101 |
| mheidari-all | 0.5 | 5 | 5 | 10 |
| Surfboard-tg-mixed | 0.5 | 26 | 26 | 52 |
| Au1rxx-base64 | 0.804 | 304 | 74 | 378 |
| ermaozi | 0.961 | 98 | 4 | 102 |
| tg-LonUp_M | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23769 | yes | 6.56 | 0 |
| SoliSpirit-all | 9785 | yes | 4.96 | 0 |
| Epodonios-all | 7561 | yes | 5.86 | 0 |
| Surfboard-tg-mixed | 7030 | yes | 4.37 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.53 | 0 |
| barry-far-vless | 5830 | yes | 2.48 | 0 |
| Surfboard-tg-vless | 5615 | yes | 4.15 | 0 |
| 10ium-ScrapeCategorize-Vless | 4983 | yes | 2.72 | 0 |
| DeltaKronecker-all | 4750 | yes | 6.8 | 0 |
| mahdibland-V2RayAggregator | 4246 | yes | 3.66 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 78 |
| 204 | 35 |
| geo | 33 |
| speed | 14 |
| cn-block | 13 |
