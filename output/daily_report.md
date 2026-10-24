# AutoNodes 每日报告

生成时间：2026-10-24 04:53:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 86/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 92457 |
| 去重后节点数 | 24506 |
| TCP 可达数 | 3000 |
| 真测通过数 | 449 |
| verified 输出数 | 161 |
| global 输出数 | 300 |
| all 输出数 | 24506 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 32.7 |
| fetch | 6.8 |
| generate | 11.3 |
| geo | 1.5 |
| probe | 91.4 |
| real_test | 88.7 |
| tcp | 77.1 |
| write_verified | 0.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 82 | 79 | 3 | 96.3% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 161 | 147 | 14 | 91.3% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 35 | 32 | 3 | 91.4% |
| vless | 303 | 177 | 126 | 58.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 90 |
| geo:ClientOSError | 19 |
| speed:ClientOSError | 12 |
| cn-block:TimeoutError | 9 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 3 |
| 204:TimeoutError | 3 |
| speed:ProxyError | 3 |
| cn-block:ProxyError | 1 |
| geo:TimeoutError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6294 |
| ConnectionRefusedError | 1048 |
| OSError | 235 |
| gaierror | 193 |
| SSRFBlocked | 1 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 79 | 0.987 | 608 |
| Au1rxx-base64 | 0.958 | prefer | 270 | 0.9 | 1532 |
| Surfboard-tg-mixed | 0.942 | prefer | 56 | 0.875 | 7159 |
| mheidari-all | 0.469 | observe | 173 | 0.387 | 23800 |
| roosterkid-openproxylist-v2ray | 0.406 | observe | 4 | 1.0 | 150 |
| SoliSpirit-all | 0.349 | observe | 3 | 0.667 | 10227 |
| 10ium-HighSpeed | 0.345 | observe | 2 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.287 | observe | 2 | 0.5 | 4911 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| ermaozi-get_subscribe | 0.276 | observe | 1 | 1.0 | 515 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| DeltaKronecker-all | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 495 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 386 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 381 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 264 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 242 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 241 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 233 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 211 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 130 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.387 | 67 | 106 | 173 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| 10ium-ScrapeCategorize-Vless | 0.5 | 1 | 1 | 2 |
| tg-oneclickvpnkeys | 0.5 | 2 | 2 | 4 |
| SoliSpirit-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.875 | 49 | 7 | 56 |
| Au1rxx-base64 | 0.9 | 243 | 27 | 270 |
| ermaozi | 0.987 | 78 | 1 | 79 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23800 | yes | 5.55 | 0 |
| SoliSpirit-all | 10227 | yes | 5.5 | 0 |
| Epodonios-all | 7650 | yes | 3.2 | 0 |
| Surfboard-tg-mixed | 7159 | yes | 4.89 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.62 | 0 |
| barry-far-vless | 5734 | yes | 0.73 | 0 |
| Surfboard-tg-vless | 5520 | yes | 3.95 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 3.1 | 0 |
| mahdibland-V2RayAggregator | 4117 | yes | 2.92 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.23 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 90 |
| geo | 20 |
| speed | 15 |
| cn-block | 13 |
| 204 | 9 |
