# AutoNodes 每日报告

生成时间：2026-08-12 19:12:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 79820 |
| 去重后节点数 | 22379 |
| TCP 可达数 | 3000 |
| 真测通过数 | 604 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22379 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 14.5 |
| generate | 39.4 |
| geo | 1.3 |
| probe | 56.4 |
| real_test | 119.8 |
| tcp | 32.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 19 | 19 | 0 | 100.0% |
| shadowsocks | 163 | 146 | 17 | 89.6% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 116 | 110 | 6 | 94.8% |
| vless | 266 | 198 | 68 | 74.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 22 |
| speed:TimeoutError | 16 |
| geo:ClientOSError | 15 |
| speed:ClientOSError | 11 |
| cn-block:TimeoutError | 7 |
| 204:ProxyError | 7 |
| geo:TimeoutError | 6 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4245 |
| ConnectionRefusedError | 794 |
| gaierror | 368 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.999 | prefer | 128 | 1.0 | 159 |
| Au1rxx-base64 | 0.928 | prefer | 468 | 0.861 | 1703 |
| Surfboard-tg-mixed | 0.855 | prefer | 69 | 0.783 | 5991 |
| DeltaKronecker-all | 0.622 | observe | 22 | 0.545 | 4975 |
| mheidari-all | 0.529 | observe | 7 | 0.857 | 16743 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 5328 |
| Epodonios-all | 0.255 | observe | 0 | None | 6597 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7349 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4839 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.545 | 12 | 10 | 22 |
| Surfboard-tg-mixed | 0.783 | 54 | 15 | 69 |
| mheidari-all | 0.857 | 6 | 1 | 7 |
| Au1rxx-base64 | 0.861 | 403 | 65 | 468 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 128 | 0 | 128 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16743 | yes | 4.76 | 0 |
| SoliSpirit-all | 7349 | yes | 3.32 | 0 |
| Epodonios-all | 6597 | yes | 2.88 | 0 |
| Surfboard-tg-mixed | 5991 | yes | 3.61 | 0 |
| 10ium-ScrapeCategorize-Vless | 5328 | yes | 2.36 | 0 |
| mahdibland-V2RayAggregator | 5209 | yes | 3.07 | 0 |
| barry-far-vless | 5121 | yes | 2.83 | 0 |
| DeltaKronecker-all | 4975 | yes | 4.12 | 0 |
| Surfboard-tg-vless | 4839 | yes | 4.0 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 2.44 | 0 |

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
| 204 | 32 |
| speed | 27 |
| geo | 22 |
| cn-block | 11 |
