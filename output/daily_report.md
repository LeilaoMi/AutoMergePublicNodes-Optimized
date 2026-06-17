# AutoNodes 每日报告

生成时间：2026-06-17 18:01:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 1/43 |
| 原始节点数 | 43727 |
| 去重后节点数 | 18109 |
| TCP 可达数 | 1500 |
| 真测通过数 | 51 |
| verified 输出数 | 51 |
| global 输出数 | 51 |
| all 输出数 | 18109 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.1 |
| generate | 20.3 |
| geo | 1.2 |
| probe | 26.4 |
| real_test | 40.3 |
| tcp | 19.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 2 | 1 | 1 | 50.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 72 | 20 | 52 | 27.8% |
| vless | 6 | 2 | 4 | 33.3% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 16 |
| 204:ProxyError | 11 |
| 204:TimeoutError | 11 |
| geo:status | 6 |
| cn-block:ClientOSError | 3 |
| speed:ProxyError | 3 |
| cn-block:TimeoutError | 3 |
| geo:ProxyError | 2 |
| geo:status | 1 |
| speed:TimeoutError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2717 |
| ConnectionRefusedError | 439 |
| gaierror | 63 |
| OSError | 29 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.964 | prefer | 24 | 1.0 | 73 |
| DeltaKronecker-all | 0.38 | observe | 78 | 0.295 | 7763 |
| Surfboard-tg-mixed | 0.32 | observe | 4 | 0.5 | 4729 |
| Au1rxx-base64 | 0.26 | observe | 1 | 1.0 | 118 |
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

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.295 | 23 | 55 | 78 |
| Barabama-yudou | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.5 | 2 | 2 | 4 |
| Au1rxx-base64 | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 7763 | yes | 3.06 | 0 |
| Surfboard-tg-mixed | 4729 | yes | 1.88 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 1.46 | 0 |
| Surfboard-tg-vless | 3741 | yes | 1.38 | 0 |
| Epodonios-all | 3000 | yes | 1.75 | 0 |
| SoliSpirit-all | 3000 | yes | 2.27 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.29 | 0 |
| mheidari-all | 2000 | yes | 2.9 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.86 | 0 |
| barry-far-vless | 2000 | yes | 1.02 | 0 |

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
| 204 | 22 |
| speed | 20 |
| geo | 9 |
| cn-block | 7 |
