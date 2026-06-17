# AutoNodes 每日报告

生成时间：2026-06-17 16:49:18

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 0/44 |
| 原始节点数 | 43696 |
| 去重后节点数 | 18218 |
| TCP 可达数 | 272 |
| 真测通过数 | 140 |
| verified 输出数 | 140 |
| global 输出数 | 142 |
| all 输出数 | 18218 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| generate | 15.8 |
| geo | 1.2 |
| probe | 31.6 |
| real_test | 50.1 |
| tcp | 40.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 24 | 1 | 96.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 119 | 62 | 57 | 52.1% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 15 | 7 | 8 | 46.7% |
| vless | 104 | 40 | 64 | 38.5% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 55 |
| geo:status | 50 |
| speed:ClientOSError | 7 |
| cn-block:ClientOSError | 6 |
| 204:TimeoutError | 5 |
| cn-block:TimeoutError | 3 |
| 204:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 1906 |
| ConnectionRefusedError | 472 |
| gaierror | 198 |
| OSError | 38 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.699 | observe | 40 | 0.625 | 7763 |
| ninja-vless | 0.685 | observe | 29 | 0.621 | 1791 |
| roosterkid-openproxylist-v2ray | 0.683 | observe | 16 | 0.812 | 150 |
| Au1rxx-base64 | 0.519 | observe | 66 | 0.515 | 115 |
| snakem982 | 0.47 | observe | 58 | 0.466 | 73 |
| Surfboard-tg-mixed | 0.441 | observe | 34 | 0.353 | 4729 |
| mheidari-all | 0.426 | observe | 24 | 0.333 | 2000 |
| nscl5-all | 0.294 | observe | 1 | 1.0 | 967 |
| SoliSpirit-all | 0.287 | observe | 2 | 0.5 | 3000 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 2000 |

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
| abc-configs-readme-latest30 | 0.176 | observe | 0 | None | 0 | 18 |
| barabama-nodefree | 0.176 | observe | 0 | None | 0 | 23 |
| ermaozi | 0.176 | observe | 0 | None | 0 | 29 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.333 | 8 | 16 | 24 |
| Surfboard-tg-mixed | 0.353 | 12 | 22 | 34 |
| snakem982 | 0.466 | 27 | 31 | 58 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| SoliSpirit-all | 0.5 | 1 | 1 | 2 |
| Au1rxx-base64 | 0.515 | 34 | 32 | 66 |
| ninja-vless | 0.621 | 18 | 11 | 29 |
| DeltaKronecker-all | 0.625 | 25 | 15 | 40 |
| roosterkid-openproxylist-v2ray | 0.812 | 13 | 3 | 16 |
| nscl5-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 7763 | yes | 2.63 | 0 |
| Surfboard-tg-mixed | 4729 | yes | 1.97 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 1.3 | 0 |
| Surfboard-tg-vless | 3741 | yes | 1.45 | 0 |
| Epodonios-all | 3000 | yes | 1.72 | 0 |
| SoliSpirit-all | 3000 | yes | 1.62 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.1 | 0 |
| mheidari-all | 2000 | yes | 2.62 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.03 | 0 |
| barry-far-vless | 2000 | yes | 0.86 | 0 |

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
| geo | 107 |
| cn-block | 9 |
| speed | 8 |
| 204 | 8 |
