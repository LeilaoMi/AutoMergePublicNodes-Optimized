# AutoNodes 每日报告

生成时间：2026-06-28 04:25:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76091 |
| 去重后节点数 | 23164 |
| TCP 可达数 | 3000 |
| 真测通过数 | 547 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23164 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.5 |
| generate | 33.3 |
| geo | 1.4 |
| probe | 57.0 |
| real_test | 133.9 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 136 | 113 | 23 | 83.1% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 95 | 83 | 12 | 87.4% |
| vless | 736 | 305 | 431 | 41.4% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 189 |
| speed:ClientOSError | 150 |
| geo:ClientOSError | 48 |
| cn-block:TimeoutError | 31 |
| cn-block:ClientOSError | 10 |
| speed:TimeoutError | 9 |
| 204:ClientOSError | 9 |
| 204:TimeoutError | 9 |
| 204:ProxyError | 7 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4513 |
| ConnectionRefusedError | 649 |
| gaierror | 132 |
| OSError | 126 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.866 | prefer | 279 | 0.789 | 5004 |
| Au1rxx-base64 | 0.744 | prefer | 67 | 0.746 | 117 |
| mheidari-all | 0.686 | observe | 178 | 0.607 | 16017 |
| DeltaKronecker-all | 0.37 | observe | 450 | 0.289 | 6822 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4579 |
| Epodonios-all | 0.255 | observe | 0 | None | 7564 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3980 |

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
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.289 | 130 | 320 | 450 |
| mheidari-all | 0.607 | 108 | 70 | 178 |
| Au1rxx-base64 | 0.746 | 50 | 17 | 67 |
| Surfboard-tg-mixed | 0.789 | 220 | 59 | 279 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16017 | yes | 2.31 | 0 |
| Epodonios-all | 7564 | yes | 1.55 | 0 |
| SoliSpirit-all | 7009 | yes | 2.35 | 0 |
| DeltaKronecker-all | 6822 | yes | 2.62 | 0 |
| mahdibland-V2RayAggregator | 5287 | yes | 0.64 | 0 |
| Surfboard-tg-mixed | 5004 | yes | 1.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 4579 | yes | 1.18 | 0 |
| barry-far-vless | 4479 | yes | 1.41 | 0 |
| MatinGhanbari-all-sub | 3980 | yes | 1.55 | 0 |
| Surfboard-tg-vless | 3679 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 239 |
| speed | 161 |
| cn-block | 41 |
| 204 | 25 |
