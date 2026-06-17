# AutoNodes 每日报告

生成时间：2026-06-17 18:48:00

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 44/44 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 1/43 |
| 原始节点数 | 43687 |
| 去重后节点数 | 18013 |
| TCP 可达数 | 1500 |
| 真测通过数 | 102 |
| verified 输出数 | 102 |
| global 输出数 | 112 |
| all 输出数 | 18013 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 1.9 |
| generate | 38.9 |
| geo | 1.2 |
| probe | 37.6 |
| real_test | 60.4 |
| tcp | 21.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 5 | 2 | 3 | 40.0% |
| shadowsocks | 30 | 23 | 7 | 76.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 93 | 16 | 77 | 17.2% |
| vless | 57 | 30 | 27 | 52.6% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 55 |
| 204:TimeoutError | 18 |
| 204:ProxyError | 10 |
| cn-block:TimeoutError | 9 |
| geo:ClientOSError | 7 |
| cn-block:ProxyError | 7 |
| cn-block:ClientOSError | 3 |
| geo:TimeoutError | 3 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 2534 |
| ConnectionRefusedError | 452 |
| gaierror | 95 |
| OSError | 29 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.884 | prefer | 57 | 0.895 | 73 |
| Au1rxx-base64 | 0.404 | observe | 4 | 1.0 | 108 |
| DeltaKronecker-all | 0.377 | observe | 146 | 0.295 | 7763 |
| Surfboard-tg-mixed | 0.349 | observe | 3 | 0.667 | 4729 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 2000 |
| Epodonios-all | 0.255 | observe | 0 | None | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 3000 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.113 | observe | 3 | 0.0 | 0 | 588 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tonykong-base64 | 0.175 | observe | 0 | None | 0 | 5 |
| tonykong-clash | 0.175 | observe | 0 | None | 0 | 5 |
| Barabama-we | 0.176 | observe | 0 | None | 0 | 23 |
| Mr8AHAL | 0.176 | observe | 0 | None | 0 | 26 |
| abc-configs-readme-latest30 | 0.176 | observe | 0 | None | 0 | 17 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.295 | 43 | 103 | 146 |
| Surfboard-tg-mixed | 0.667 | 2 | 1 | 3 |
| snakem982 | 0.895 | 51 | 6 | 57 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| Au1rxx-base64 | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 7763 | yes | 2.03 | 0 |
| Surfboard-tg-mixed | 4729 | yes | 1.25 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 0.67 | 0 |
| Surfboard-tg-vless | 3741 | yes | 1.31 | 0 |
| Epodonios-all | 3000 | yes | 1.09 | 0 |
| SoliSpirit-all | 3000 | yes | 1.18 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 0.9 | 0 |
| mheidari-all | 2000 | yes | 1.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 0.71 | 0 |
| barry-far-vless | 2000 | yes | 0.63 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 56 |
| 204 | 28 |
| cn-block | 19 |
| geo | 11 |
