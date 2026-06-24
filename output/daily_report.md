# AutoNodes 每日报告

生成时间：2026-06-24 19:58:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76862 |
| 去重后节点数 | 22607 |
| TCP 可达数 | 3000 |
| 真测通过数 | 396 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22607 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 44.2 |
| geo | 1.4 |
| probe | 55.8 |
| real_test | 112.1 |
| tcp | 29.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 119 | 98 | 21 | 82.4% |
| trojan | 133 | 83 | 50 | 62.4% |
| vless | 291 | 173 | 118 | 59.5% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 71 |
| 204:TimeoutError | 31 |
| cn-block:TimeoutError | 27 |
| geo:TimeoutError | 12 |
| 204:ProxyError | 11 |
| 204:ClientOSError | 10 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 8 |
| geo:ClientOSError | 5 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4256 |
| ConnectionRefusedError | 625 |
| gaierror | 154 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Au1rxx-base64 | 0.801 | prefer | 62 | 0.806 | 114 |
| Surfboard-tg-mixed | 0.744 | prefer | 233 | 0.665 | 5375 |
| mheidari-all | 0.731 | prefer | 187 | 0.652 | 15681 |
| DeltaKronecker-all | 0.558 | observe | 65 | 0.477 | 6644 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1140 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4745 |
| Epodonios-all | 0.255 | observe | 0 | None | 8092 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3985 |

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
| DeltaKronecker-all | 0.477 | 31 | 34 | 65 |
| mheidari-all | 0.652 | 122 | 65 | 187 |
| Surfboard-tg-mixed | 0.665 | 155 | 78 | 233 |
| Au1rxx-base64 | 0.806 | 50 | 12 | 62 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15681 | yes | 3.81 | 0 |
| Epodonios-all | 8092 | yes | 3.05 | 0 |
| SoliSpirit-all | 7510 | yes | 2.84 | 0 |
| DeltaKronecker-all | 6644 | yes | 4.97 | 0 |
| Surfboard-tg-mixed | 5375 | yes | 2.75 | 0 |
| barry-far-vless | 4852 | yes | 0.97 | 0 |
| 10ium-ScrapeCategorize-Vless | 4745 | yes | 1.68 | 0 |
| mahdibland-V2RayAggregator | 4710 | yes | 1.69 | 0 |
| Surfboard-tg-vless | 4084 | yes | 2.05 | 0 |
| MatinGhanbari-all-sub | 3985 | yes | 1.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 79 |
| 204 | 52 |
| cn-block | 38 |
| geo | 20 |
