# AutoNodes 每日报告

生成时间：2026-10-27 05:22:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 15/0 |
| 清理建议：优先/观察 | 3/89 |
| 原始节点数 | 96396 |
| 去重后节点数 | 26562 |
| TCP 可达数 | 3000 |
| 真测通过数 | 479 |
| verified 输出数 | 129 |
| global 输出数 | 300 |
| all 输出数 | 26562 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.8 |
| fetch | 7.3 |
| generate | 14.5 |
| geo | 1.5 |
| probe | 104.0 |
| real_test | 100.2 |
| tcp | 81.9 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 89 | 65 | 24 | 73.0% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 141 | 111 | 30 | 78.7% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 81 | 71 | 10 | 87.7% |
| vless | 392 | 215 | 177 | 54.8% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 115 |
| geo:ClientOSError | 42 |
| speed:ClientOSError | 33 |
| 204:ProxyError | 15 |
| cn-block:ProxyError | 12 |
| geo:ProxyError | 8 |
| cn-block:ClientOSError | 6 |
| 204:TimeoutError | 5 |
| cn-block:TimeoutError | 2 |
| 204:ClientOSError | 2 |
| geo:TimeoutError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6472 |
| ConnectionRefusedError | 1088 |
| gaierror | 268 |
| OSError | 238 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.81 | prefer | 401 | 0.743 | 1700 |
| ermaozi | 0.742 | prefer | 90 | 0.722 | 603 |
| Surfboard-tg-mixed | 0.728 | prefer | 123 | 0.65 | 7143 |
| mheidari-all | 0.425 | observe | 85 | 0.341 | 24431 |
| ninja-vless | 0.327 | observe | 1 | 1.0 | 1791 |
| DeltaKronecker-all | 0.322 | observe | 16 | 0.25 | 3004 |
| roosterkid-openproxylist-v2ray | 0.275 | observe | 3 | 0.667 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7632 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5408 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 506 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 397 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 392 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 275 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 253 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 252 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 244 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 222 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 141 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| SoliSpirit-all | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.25 | 4 | 12 | 16 |
| mheidari-all | 0.341 | 29 | 56 | 85 |
| Surfboard-tg-mixed | 0.65 | 80 | 43 | 123 |
| roosterkid-openproxylist-v2ray | 0.667 | 2 | 1 | 3 |
| ermaozi | 0.722 | 65 | 25 | 90 |
| Au1rxx-base64 | 0.743 | 298 | 103 | 401 |
| ninja-vless | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24431 | yes | 6.54 | 0 |
| SoliSpirit-all | 10267 | yes | 4.14 | 0 |
| Epodonios-all | 7632 | yes | 2.02 | 0 |
| Surfboard-tg-mixed | 7143 | yes | 4.5 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.35 | 0 |
| barry-far-vless | 5620 | yes | 2.49 | 0 |
| Surfboard-tg-vless | 5408 | yes | 4.18 | 0 |
| 10ium-ScrapeCategorize-Vless | 4919 | yes | 4.39 | 0 |
| mahdibland-V2RayAggregator | 4466 | yes | 2.1 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.82 | 0 |

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
| test_one_timeout | 115 |
| geo | 51 |
| speed | 34 |
| 204 | 22 |
| cn-block | 20 |
