# AutoNodes 每日报告

生成时间：2026-08-12 13:25:58

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 80149 |
| 去重后节点数 | 22315 |
| TCP 可达数 | 3000 |
| 真测通过数 | 587 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22315 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.6 |
| generate | 35.4 |
| geo | 1.4 |
| probe | 54.3 |
| real_test | 125.9 |
| tcp | 33.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 17 | 17 | 0 | 100.0% |
| shadowsocks | 161 | 151 | 10 | 93.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 125 | 121 | 4 | 96.8% |
| vless | 265 | 167 | 98 | 63.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 28 |
| speed:TimeoutError | 27 |
| geo:TimeoutError | 16 |
| speed:ClientOSError | 13 |
| 204:TimeoutError | 11 |
| 204:ClientOSError | 5 |
| 204:ProxyError | 5 |
| cn-block:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4402 |
| ConnectionRefusedError | 784 |
| gaierror | 325 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Au1rxx-base64 | 0.952 | prefer | 428 | 0.888 | 1660 |
| Surfboard-tg-mixed | 0.796 | prefer | 65 | 0.723 | 6099 |
| DeltaKronecker-all | 0.464 | observe | 71 | 0.38 | 4975 |
| mheidari-all | 0.4 | observe | 4 | 0.75 | 16658 |
| Au1rxx-clash | 0.322 | observe | 1 | 1.0 | 1669 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5328 |
| Epodonios-all | 0.255 | observe | 0 | None | 6671 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| ermaozi | 0.175 | observe | 0 | None | 0 | 8 |
| ermaozi-get_subscribe | 0.175 | observe | 0 | None | 0 | 8 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.38 | 27 | 44 | 71 |
| Surfboard-tg-mixed | 0.723 | 47 | 18 | 65 |
| mheidari-all | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.888 | 380 | 48 | 428 |
| Au1rxx-clash | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16658 | yes | 4.88 | 0 |
| SoliSpirit-all | 7502 | yes | 2.97 | 0 |
| Epodonios-all | 6671 | yes | 2.99 | 0 |
| Surfboard-tg-mixed | 6099 | yes | 4.11 | 0 |
| 10ium-ScrapeCategorize-Vless | 5328 | yes | 2.18 | 0 |
| barry-far-vless | 5264 | yes | 1.94 | 0 |
| mahdibland-V2RayAggregator | 5196 | yes | 2.8 | 0 |
| DeltaKronecker-all | 4975 | yes | 4.69 | 0 |
| Surfboard-tg-vless | 4929 | yes | 3.79 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.44 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 44 |
| speed | 40 |
| 204 | 21 |
| cn-block | 8 |
