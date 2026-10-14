# AutoNodes 每日报告

生成时间：2026-10-14 04:30:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 13/0 |
| 清理建议：优先/观察 | 2/92 |
| 原始节点数 | 98590 |
| 去重后节点数 | 27454 |
| TCP 可达数 | 3000 |
| 真测通过数 | 57 |
| verified 输出数 | 57 |
| global 输出数 | 75 |
| all 输出数 | 27454 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 106.5 |
| geo | 1.5 |
| probe | 298.5 |
| real_test | 370.4 |
| tcp | 117.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 43 | 27 | 16 | 62.8% |
| hysteria2 | 17 | 14 | 3 | 82.4% |
| shadowsocks | 156 | 144 | 12 | 92.3% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 92 | 86 | 6 | 93.5% |
| vless | 401 | 231 | 170 | 57.6% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 90 |
| geo:ClientOSError | 30 |
| 204:ProxyError | 28 |
| speed:ClientOSError | 17 |
| 204:TimeoutError | 12 |
| cn-block:TimeoutError | 12 |
| cn-block:ClientOSError | 7 |
| speed:TimeoutError | 7 |
| 204:ProxyConnectionError | 2 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6407 |
| ConnectionRefusedError | 1057 |
| gaierror | 343 |
| OSError | 243 |
| SSRFBlocked | 3 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.941 | prefer | 328 | 0.872 | 1771 |
| Surfboard-tg-mixed | 0.807 | prefer | 137 | 0.73 | 7113 |
| ermaozi-get_subscribe | 0.577 | observe | 36 | 0.556 | 598 |
| zhangkai | 0.555 | observe | 8 | 1.0 | 144 |
| mheidari-all | 0.529 | observe | 205 | 0.449 | 24076 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5086 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5076 |
| Epodonios-all | 0.255 | observe | 0 | None | 7613 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9825 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Mr8AHAL | 0.175 | observe | 0 | None | 0 | 1 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-DarkVPNpro | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-VmessProtocol | 0.175 | observe | 0 | None | 0 | 5 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| disable | tg-V2rayngVpn | 0.0 | 0 | None | 445 | 连续死亡次数 >= 2 |
| disable | tg-Letiranbreath | 0.0 | 0 | None | 336 | 连续死亡次数 >= 2 |
| disable | snakem982 | 0.0 | 0 | None | 331 | 连续死亡次数 >= 2 |
| disable | tg-ernoxin_shop | 0.0 | 0 | None | 214 | 连续死亡次数 >= 2 |
| disable | abc-configs-readme-latest30 | 0.0 | 0 | None | 192 | 连续死亡次数 >= 2 |
| disable | tg-abc_configs | 0.0 | 0 | None | 191 | 连续死亡次数 >= 2 |
| disable | tg-Parsashonam | 0.0 | 0 | None | 183 | 连续死亡次数 >= 2 |
| disable | nscl5-all | 0.0 | 0 | None | 161 | 连续死亡次数 >= 2 |
| disable | mfuu-v2ray | 0.0 | 0 | None | 156 | 连续死亡次数 >= 2 |
| disable | tg-CaV2ray | 0.0 | 0 | None | 80 | 连续死亡次数 >= 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.449 | 92 | 113 | 205 |
| ermaozi-get_subscribe | 0.556 | 20 | 16 | 36 |
| Surfboard-tg-mixed | 0.73 | 100 | 37 | 137 |
| Au1rxx-base64 | 0.872 | 286 | 42 | 328 |
| zhangkai | 1.0 | 8 | 0 | 8 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24076 | yes | 4.8 | 0 |
| SoliSpirit-all | 9825 | yes | 4.83 | 0 |
| Epodonios-all | 7613 | yes | 6.01 | 0 |
| Surfboard-tg-mixed | 7113 | yes | 5.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.76 | 0 |
| barry-far-vless | 5866 | yes | 2.71 | 0 |
| Surfboard-tg-vless | 5621 | yes | 5.06 | 0 |
| 10ium-ScrapeCategorize-Vless | 5086 | yes | 2.97 | 0 |
| DeltaKronecker-all | 5076 | yes | 5.78 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 0.93 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 120 |
| 204 | 44 |
| speed | 24 |
| cn-block | 21 |
