# AutoNodes 每日报告

生成时间：2026-10-17 15:48:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 14/0 |
| 清理建议：优先/观察 | 3/90 |
| 原始节点数 | 99259 |
| 去重后节点数 | 27641 |
| TCP 可达数 | 3000 |
| 真测通过数 | 373 |
| verified 输出数 | 121 |
| global 输出数 | 300 |
| all 输出数 | 27641 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| china_check | 30.7 |
| fetch | 5.9 |
| generate | 10.8 |
| geo | 1.5 |
| probe | 88.1 |
| real_test | 80.8 |
| tcp | 87.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 29 | 27 | 2 | 93.1% |
| hysteria2 | 14 | 12 | 2 | 85.7% |
| shadowsocks | 145 | 124 | 21 | 85.5% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 32 | 26 | 6 | 81.2% |
| vless | 271 | 184 | 87 | 67.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| test_one_timeout:15.0s | 49 |
| geo:ClientOSError | 15 |
| 204:ProxyError | 12 |
| speed:ClientOSError | 11 |
| 204:TimeoutError | 9 |
| speed:ProxyError | 6 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| cn-block:TimeoutError | 2 |
| geo:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7173 |
| ConnectionRefusedError | 1010 |
| OSError | 234 |
| gaierror | 182 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 0.928 | prefer | 29 | 0.931 | 623 |
| Au1rxx-base64 | 0.871 | prefer | 400 | 0.792 | 1993 |
| mheidari-all | 0.817 | prefer | 19 | 0.789 | 23770 |
| ninja-vless | 0.43 | observe | 3 | 1.0 | 1791 |
| Surfboard-tg-mixed | 0.374 | observe | 32 | 0.281 | 7171 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| DeltaKronecker-all | 0.272 | observe | 7 | 0.286 | 4999 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4986 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1993 |
| Epodonios-all | 0.255 | observe | 0 | None | 7678 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Pawdroid | 0.128 | observe | 1 | 0.0 | 0 | 12 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 4 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 470 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 361 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 356 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 239 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 217 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 216 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 208 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 186 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 181 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 105 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.281 | 9 | 23 | 32 |
| DeltaKronecker-all | 0.286 | 2 | 5 | 7 |
| mheidari-all | 0.789 | 15 | 4 | 19 |
| Au1rxx-base64 | 0.792 | 317 | 83 | 400 |
| ermaozi | 0.931 | 27 | 2 | 29 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |
| ninja-vless | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23770 | yes | 3.98 | 0 |
| SoliSpirit-all | 10049 | yes | 2.12 | 0 |
| Epodonios-all | 7678 | yes | 4.9 | 0 |
| Surfboard-tg-mixed | 7171 | yes | 3.25 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.88 | 0 |
| barry-far-vless | 5865 | yes | 0.88 | 0 |
| Surfboard-tg-vless | 5617 | yes | 2.94 | 0 |
| DeltaKronecker-all | 4999 | yes | 4.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 4986 | yes | 0.53 | 0 |
| mahdibland-V2RayAggregator | 4255 | yes | 2.6 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| output_guard_preserved | output shrink guard preserved previous files |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| test_one_timeout | 49 |
| 204 | 25 |
| geo | 19 |
| speed | 17 |
| cn-block | 9 |
