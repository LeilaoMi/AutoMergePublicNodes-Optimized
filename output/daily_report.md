# AutoNodes 每日报告

生成时间：2026-10-16 04:06:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 99761 |
| 去重后节点数 | 27999 |
| TCP 可达数 | 3000 |
| 真测通过数 | 99 |
| verified 输出数 | 99 |
| global 输出数 | 106 |
| all 输出数 | 27999 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 28.4 |
| fetch | 5.9 |
| generate | 9.4 |
| geo | 1.5 |
| probe | 95.5 |
| real_test | 99.4 |
| tcp | 86.3 |
| write_verified | 0.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 87 | 84 | 3 | 96.6% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 141 | 137 | 4 | 97.2% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 10 | 5 | 5 | 50.0% |
| vless | 435 | 225 | 210 | 51.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 148 |
| speed:ClientOSError | 36 |
| geo:ClientOSError | 19 |
| cn-block:ClientOSError | 7 |
| 204:TimeoutError | 4 |
| 204:ProxyError | 2 |
| 204:ClientOSError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound: start inbound/socks[socks-in]: listen tcp 127.0.0.1:43955: bind: address already in use | 1 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |
| cn-block:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7087 |
| ConnectionRefusedError | 1023 |
| OSError | 237 |
| gaierror | 183 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.983 | prefer | 87 | 0.966 | 693 |
| Au1rxx-base64 | 0.804 | prefer | 459 | 0.725 | 1991 |
| mheidari-all | 0.436 | observe | 144 | 0.354 | 23985 |
| Surfboard-tg-mixed | 0.391 | observe | 2 | 1.0 | 7135 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5089 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1991 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5147 |
| Epodonios-all | 0.255 | observe | 0 | None | 7647 |
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
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 457 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 348 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 343 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 226 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 204 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 203 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 195 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 173 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 168 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 92 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.354 | 51 | 93 | 144 |
| Au1rxx-base64 | 0.725 | 333 | 126 | 459 |
| ermaozi | 0.966 | 84 | 3 | 87 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23985 | yes | 5.43 | 0 |
| SoliSpirit-all | 9903 | yes | 3.67 | 0 |
| Epodonios-all | 7647 | yes | 4.85 | 0 |
| Surfboard-tg-mixed | 7135 | yes | 3.95 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.61 | 0 |
| barry-far-vless | 5878 | yes | 2.09 | 0 |
| Surfboard-tg-vless | 5628 | yes | 3.12 | 0 |
| DeltaKronecker-all | 5147 | yes | 4.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 5089 | yes | 2.3 | 0 |
| mahdibland-V2RayAggregator | 4235 | yes | 2.59 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 148 |
| speed | 37 |
| geo | 20 |
| cn-block | 9 |
| 204 | 8 |
| sing-box exited 1 | 1 |
