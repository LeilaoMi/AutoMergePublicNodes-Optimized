# AutoNodes 每日报告

生成时间：2026-06-17 17:08:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/42 |
| 原始节点数 | 43696 |
| 去重后节点数 | 18208 |
| TCP 可达数 | 1500 |
| 真测通过数 | 78 |
| verified 输出数 | 78 |
| global 输出数 | 81 |
| all 输出数 | 18208 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| generate | 25.0 |
| geo | 1.2 |
| probe | 34.8 |
| real_test | 36.6 |
| tcp | 19.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 14 | 14 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 28 | 13 | 15 | 46.4% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 54 | 43 | 11 | 79.6% |
| vless | 8 | 1 | 7 | 12.5% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 10 |
| speed:ClientOSError | 7 |
| geo:status | 5 |
| speed:TimeoutError | 4 |
| cn-block:TimeoutError | 4 |
| 204:TimeoutError | 3 |
| 204:ProxyError | 1 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2643 |
| ConnectionRefusedError | 448 |
| gaierror | 75 |
| OSError | 31 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.791 | prefer | 15 | 1.0 | 73 |
| DeltaKronecker-all | 0.732 | prefer | 90 | 0.656 | 7763 |
| Surfboard-tg-mixed | 0.3 | observe | 5 | 0.4 | 4729 |
| nscl5-all | 0.294 | observe | 1 | 1.0 | 967 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 2000 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3741 |
| barry-far-vless | 0.255 | observe | 0 | None | 2000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tonykong-base64 | 0.175 | observe | 0 | None | 0 | 5 |
| tonykong-clash | 0.175 | observe | 0 | None | 0 | 5 |
| Barabama-we | 0.176 | observe | 0 | None | 0 | 23 |
| Mr8AHAL | 0.176 | observe | 0 | None | 0 | 26 |
| abc-configs-readme-latest30 | 0.176 | observe | 0 | None | 0 | 19 |
| barabama-nodefree | 0.176 | observe | 0 | None | 0 | 23 |
| ermaozi | 0.176 | observe | 0 | None | 0 | 29 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.4 | 2 | 3 | 5 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| DeltaKronecker-all | 0.656 | 59 | 31 | 90 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 15 | 0 | 15 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 7763 | yes | 3.08 | 0 |
| Surfboard-tg-mixed | 4729 | yes | 1.38 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 1.45 | 0 |
| Surfboard-tg-vless | 3741 | yes | 2.1 | 0 |
| Epodonios-all | 3000 | yes | 1.88 | 0 |
| SoliSpirit-all | 3000 | yes | 1.86 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.3 | 0 |
| mheidari-all | 2000 | yes | 2.84 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.24 | 0 |
| barry-far-vless | 2000 | yes | 1.05 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_downtrend_4_runs | verified output decreased for 4 consecutive runs |

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 15 |
| speed | 11 |
| cn-block | 5 |
| 204 | 4 |
