# AutoNodes 每日报告

生成时间：2026-10-16 06:35:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 99735 |
| 去重后节点数 | 27902 |
| TCP 可达数 | 3000 |
| 真测通过数 | 494 |
| verified 输出数 | 34 |
| global 输出数 | 300 |
| all 输出数 | 27902 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 24.0 |
| fetch | 8.0 |
| generate | 14.1 |
| geo | 1.5 |
| probe | 93.4 |
| real_test | 97.2 |
| tcp | 86.2 |
| write_verified | 0.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 0 | 2 | 0.0% |
| http | 90 | 89 | 1 | 98.9% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 148 | 138 | 10 | 93.2% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 50 | 36 | 14 | 72.0% |
| vless | 371 | 215 | 156 | 58.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 111 |
| geo:ClientOSError | 23 |
| speed:ClientOSError | 20 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 6 |
| 204:ClientOSError | 5 |
| 204:ProxyError | 5 |
| cn-block:ProxyError | 4 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6970 |
| ConnectionRefusedError | 1025 |
| gaierror | 240 |
| OSError | 238 |
| SSRFBlocked | 2 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 89 | 0.989 | 693 |
| Au1rxx-base64 | 0.887 | prefer | 470 | 0.809 | 1992 |
| Surfboard-tg-mixed | 0.4 | observe | 4 | 0.75 | 7054 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| mheidari-all | 0.276 | observe | 110 | 0.191 | 23985 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 79 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5024 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1992 |
| Epodonios-all | 0.255 | observe | 0 | None | 7651 |
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
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 460 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 351 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 346 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 229 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 207 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 206 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 198 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 176 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 171 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 95 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.191 | 21 | 89 | 110 |
| Surfboard-tg-mixed | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.809 | 380 | 90 | 470 |
| ermaozi | 0.989 | 88 | 1 | 89 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23985 | yes | 7.86 | 0 |
| SoliSpirit-all | 10060 | yes | 3.62 | 0 |
| Epodonios-all | 7651 | yes | 6.66 | 0 |
| Surfboard-tg-mixed | 7054 | yes | 4.45 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.99 | 0 |
| barry-far-vless | 5882 | yes | 1.22 | 0 |
| Surfboard-tg-vless | 5573 | yes | 4.98 | 0 |
| DeltaKronecker-all | 5147 | yes | 4.27 | 0 |
| 10ium-ScrapeCategorize-Vless | 5024 | yes | 2.01 | 0 |
| mahdibland-V2RayAggregator | 4265 | yes | 2.74 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 111 |
| geo | 25 |
| speed | 20 |
| 204 | 18 |
| cn-block | 10 |
