# AutoNodes 每日报告

生成时间：2026-08-13 19:14:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80087 |
| 去重后节点数 | 22489 |
| TCP 可达数 | 3000 |
| 真测通过数 | 838 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22489 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 48.3 |
| geo | 1.0 |
| probe | 70.0 |
| real_test | 161.1 |
| tcp | 33.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 127 | 127 | 0 | 100.0% |
| hysteria2 | 21 | 17 | 4 | 81.0% |
| shadowsocks | 159 | 145 | 14 | 91.2% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 330 | 328 | 2 | 99.4% |
| vless | 294 | 215 | 79 | 73.1% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 19 |
| cn-block:TimeoutError | 18 |
| geo:TimeoutError | 17 |
| 204:ProxyError | 11 |
| 204:ClientOSError | 10 |
| geo:ClientOSError | 7 |
| speed:ClientOSError | 7 |
| speed:TimeoutError | 5 |
| geo:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4382 |
| ConnectionRefusedError | 803 |
| gaierror | 361 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Au1rxx-base64 | 0.983 | prefer | 616 | 0.919 | 1639 |
| mheidari-all | 0.91 | prefer | 110 | 0.836 | 16814 |
| Surfboard-tg-mixed | 0.715 | prefer | 72 | 0.639 | 6036 |
| DeltaKronecker-all | 0.461 | observe | 11 | 0.545 | 4878 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5203 |
| Epodonios-all | 0.255 | observe | 0 | None | 6692 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7502 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-proxy_kafee | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.545 | 6 | 5 | 11 |
| Surfboard-tg-mixed | 0.639 | 46 | 26 | 72 |
| mheidari-all | 0.836 | 92 | 18 | 110 |
| Au1rxx-base64 | 0.919 | 566 | 50 | 616 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16814 | yes | 4.05 | 0 |
| SoliSpirit-all | 7502 | yes | 2.67 | 0 |
| Epodonios-all | 6692 | yes | 4.42 | 0 |
| Surfboard-tg-mixed | 6036 | yes | 3.43 | 0 |
| 10ium-ScrapeCategorize-Vless | 5203 | yes | 0.92 | 0 |
| mahdibland-V2RayAggregator | 5197 | yes | 2.78 | 0 |
| barry-far-vless | 5103 | yes | 1.12 | 0 |
| DeltaKronecker-all | 4878 | yes | 2.81 | 0 |
| Surfboard-tg-vless | 4739 | yes | 4.23 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 1.4 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 40 |
| geo | 26 |
| cn-block | 21 |
| speed | 13 |
