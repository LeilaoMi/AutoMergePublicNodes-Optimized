# AutoNodes 每日报告

生成时间：2026-06-25 09:37:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 82741 |
| 去重后节点数 | 22707 |
| TCP 可达数 | 3000 |
| 真测通过数 | 393 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22707 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 18.6 |
| generate | 37.0 |
| geo | 1.3 |
| probe | 54.7 |
| real_test | 107.3 |
| tcp | 30.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 123 | 100 | 23 | 81.3% |
| socks | 12 | 11 | 1 | 91.7% |
| trojan | 234 | 132 | 102 | 56.4% |
| vless | 186 | 108 | 78 | 58.1% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 72 |
| 204:ProxyError | 32 |
| geo:TimeoutError | 22 |
| 204:TimeoutError | 18 |
| 204:ClientOSError | 12 |
| geo:ClientOSError | 11 |
| cn-block:ClientOSError | 11 |
| cn-block:TimeoutError | 8 |
| geo:ProxyError | 6 |
| cn-block:ProxyError | 5 |
| speed:TimeoutError | 4 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4283 |
| ConnectionRefusedError | 606 |
| gaierror | 152 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Au1rxx-base64 | 0.973 | prefer | 30 | 1.0 | 111 |
| Surfboard-tg-mixed | 0.794 | prefer | 250 | 0.716 | 5237 |
| mheidari-all | 0.65 | observe | 77 | 0.571 | 15925 |
| DeltaKronecker-all | 0.582 | observe | 201 | 0.502 | 12590 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.3 | observe | 1 | 1.0 | 1136 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4787 |
| Epodonios-all | 0.255 | observe | 0 | None | 7823 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 10 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.502 | 101 | 100 | 201 |
| mheidari-all | 0.571 | 44 | 33 | 77 |
| Surfboard-tg-mixed | 0.716 | 179 | 71 | 250 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| Au1rxx-base64 | 1.0 | 30 | 0 | 30 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15925 | yes | 3.27 | 0 |
| DeltaKronecker-all | 12590 | yes | 3.16 | 0 |
| Epodonios-all | 7823 | yes | 1.87 | 0 |
| SoliSpirit-all | 7435 | yes | 1.98 | 0 |
| Surfboard-tg-mixed | 5237 | yes | 2.4 | 0 |
| mahdibland-V2RayAggregator | 5133 | yes | 1.62 | 0 |
| 10ium-ScrapeCategorize-Vless | 4787 | yes | 1.31 | 0 |
| barry-far-vless | 4701 | yes | 1.29 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.59 | 0 |
| Surfboard-tg-vless | 3919 | yes | 1.98 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 79 |
| 204 | 62 |
| geo | 39 |
| cn-block | 24 |
