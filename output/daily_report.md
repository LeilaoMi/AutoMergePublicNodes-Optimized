# AutoNodes 每日报告

生成时间：2026-10-23 17:22:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 88/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 95347 |
| 去重后节点数 | 26845 |
| TCP 可达数 | 3000 |
| 真测通过数 | 306 |
| verified 输出数 | 140 |
| global 输出数 | 300 |
| all 输出数 | 26845 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 29.1 |
| fetch | 8.1 |
| generate | 13.6 |
| geo | 1.5 |
| probe | 100.8 |
| real_test | 66.5 |
| tcp | 82.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 53 | 50 | 3 | 94.3% |
| hysteria2 | 12 | 12 | 0 | 100.0% |
| shadowsocks | 140 | 119 | 21 | 85.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 21 | 14 | 7 | 66.7% |
| vless | 171 | 112 | 59 | 65.5% |
| vmess | 1 | 0 | 1 | 0.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 53 |
| 204:TimeoutError | 8 |
| 204:ProxyError | 8 |
| cn-block:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 5 |
| geo:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6642 |
| ConnectionRefusedError | 1046 |
| OSError | 236 |
| gaierror | 159 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.965 | prefer | 50 | 0.96 | 555 |
| Au1rxx-base64 | 0.875 | prefer | 242 | 0.814 | 1588 |
| mheidari-all | 0.854 | prefer | 29 | 0.793 | 23793 |
| Surfboard-tg-mixed | 0.573 | observe | 67 | 0.493 | 6855 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6752 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| tg-oneclickvpnkeys | 0.272 | observe | 3 | 0.667 | 98 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 175 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 53 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4911 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Barabama-we | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-nodefree | 0.025 | observe | 0 | None | 1 | 0 |
| barabama-yudou66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| peasoft-NoMoreWalls | 0.109 | observe | 2 | 0.0 | 0 | 126 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 493 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 384 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 379 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 262 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 240 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 239 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 231 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 209 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 128 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| SoliSpirit-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| peasoft-NoMoreWalls | 0.0 | 0 | 2 | 2 |
| Surfboard-tg-mixed | 0.493 | 33 | 34 | 67 |
| tg-oneclickvpnkeys | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.793 | 23 | 6 | 29 |
| Au1rxx-base64 | 0.814 | 197 | 45 | 242 |
| ermaozi | 0.96 | 48 | 2 | 50 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23793 | yes | 6.95 | 0 |
| SoliSpirit-all | 10123 | yes | 1.8 | 0 |
| Epodonios-all | 7353 | yes | 5.9 | 0 |
| Surfboard-tg-mixed | 6855 | yes | 3.68 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.65 | 0 |
| barry-far-vless | 5545 | yes | 2.01 | 0 |
| Surfboard-tg-vless | 5326 | yes | 5.54 | 0 |
| 10ium-ScrapeCategorize-Vless | 4911 | yes | 1.39 | 0 |
| mahdibland-V2RayAggregator | 4230 | yes | 3.22 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.84 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vmess | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 53 |
| 204 | 21 |
| cn-block | 13 |
| geo | 5 |
| speed | 1 |
