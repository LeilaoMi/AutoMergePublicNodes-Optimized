# AutoNodes 每日报告

生成时间：2026-06-17 18:40:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 0/43 |
| 原始节点数 | 43687 |
| 去重后节点数 | 18013 |
| TCP 可达数 | 1500 |
| 真测通过数 | 190 |
| verified 输出数 | 190 |
| global 输出数 | 199 |
| all 输出数 | 18013 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.4 |
| generate | 31.7 |
| geo | 1.2 |
| probe | 40.8 |
| real_test | 89.9 |
| tcp | 19.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 29 | 14 | 15 | 48.3% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 12 | 4 | 8 | 33.3% |
| vless | 579 | 141 | 438 | 24.4% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:status | 351 |
| speed:ClientOSError | 40 |
| geo:status | 18 |
| 204:ProxyError | 13 |
| speed:TimeoutError | 12 |
| cn-block:TimeoutError | 8 |
| 204:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 1 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2636 |
| ConnectionRefusedError | 438 |
| gaierror | 61 |
| OSError | 28 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.459 | observe | 55 | 0.455 | 73 |
| DeltaKronecker-all | 0.355 | observe | 590 | 0.275 | 7763 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Au1rxx-base64 | 0.259 | observe | 1 | 1.0 | 108 |
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
| abc-configs-readme-latest30 | 0.176 | observe | 0 | None | 0 | 17 |
| barabama-nodefree | 0.176 | observe | 0 | None | 0 | 23 |
| ermaozi | 0.176 | observe | 0 | None | 0 | 29 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | Surfboard-tg-mixed | 0.226 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.2 | 1 | 4 | 5 |
| DeltaKronecker-all | 0.275 | 162 | 428 | 590 |
| snakem982 | 0.455 | 25 | 30 | 55 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| Au1rxx-base64 | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 7763 | yes | 3.3 | 0 |
| Surfboard-tg-mixed | 4729 | yes | 1.83 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 1.58 | 0 |
| Surfboard-tg-vless | 3741 | yes | 1.5 | 0 |
| Epodonios-all | 3000 | yes | 2.52 | 0 |
| SoliSpirit-all | 3000 | yes | 2.6 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.43 | 0 |
| mheidari-all | 2000 | yes | 2.93 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.98 | 0 |
| barry-far-vless | 2000 | yes | 1.13 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| socks | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 374 |
| speed | 52 |
| 204 | 23 |
| cn-block | 13 |
