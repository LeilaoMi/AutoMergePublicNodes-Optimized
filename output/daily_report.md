# AutoNodes 每日报告

生成时间：2026-10-10 05:35:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 97887 |
| 去重后节点数 | 27738 |
| TCP 可达数 | 3000 |
| 真测通过数 | 510 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27738 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.7 |
| generate | 102.6 |
| geo | 1.5 |
| probe | 344.3 |
| real_test | 559.4 |
| tcp | 49.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 4 | 0 | 4 | 0.0% |
| http | 44 | 36 | 8 | 81.8% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 163 | 153 | 10 | 93.9% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 114 | 106 | 8 | 93.0% |
| vless | 465 | 195 | 270 | 41.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 148 |
| speed:TimeoutError | 39 |
| geo:ClientOSError | 34 |
| 204:ProxyError | 23 |
| speed:ClientOSError | 22 |
| cn-block:TimeoutError | 12 |
| 204:TimeoutError | 9 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 7307 |
| ConnectionRefusedError | 986 |
| OSError | 229 |
| gaierror | 108 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.997 | prefer | 319 | 0.928 | 1786 |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.759 | prefer | 82 | 0.683 | 7155 |
| ermaozi-get_subscribe | 0.578 | observe | 27 | 0.556 | 653 |
| DeltaKronecker-all | 0.467 | observe | 16 | 0.438 | 5154 |
| mheidari-all | 0.411 | observe | 339 | 0.33 | 23395 |
| 10ium-ScrapeCategorize-Vless | 0.335 | observe | 1 | 1.0 | 4984 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7634 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.33 | 112 | 227 | 339 |
| DeltaKronecker-all | 0.438 | 7 | 9 | 16 |
| ermaozi-get_subscribe | 0.556 | 15 | 12 | 27 |
| Surfboard-tg-mixed | 0.683 | 56 | 26 | 82 |
| Au1rxx-base64 | 0.928 | 296 | 23 | 319 |
| 10ium-ScrapeCategorize-Vless | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23395 | yes | 4.88 | 0 |
| SoliSpirit-all | 9590 | yes | 2.67 | 0 |
| Epodonios-all | 7634 | yes | 2.94 | 0 |
| Surfboard-tg-mixed | 7155 | yes | 3.63 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.39 | 0 |
| barry-far-vless | 5793 | yes | 1.66 | 0 |
| Surfboard-tg-vless | 5643 | yes | 3.24 | 0 |
| DeltaKronecker-all | 5154 | yes | 4.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 4984 | yes | 1.39 | 0 |
| mahdibland-V2RayAggregator | 4346 | yes | 2.67 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| anytls | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 183 |
| speed | 61 |
| 204 | 37 |
| cn-block | 20 |
