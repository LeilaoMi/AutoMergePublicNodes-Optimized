# AutoNodes 每日报告

生成时间：2026-09-13 20:43:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 84974 |
| 去重后节点数 | 23272 |
| TCP 可达数 | 3000 |
| 真测通过数 | 455 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23272 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.1 |
| generate | 78.5 |
| geo | 1.5 |
| probe | 229.4 |
| real_test | 180.3 |
| tcp | 39.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 37 | 22 | 15 | 59.5% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 173 | 158 | 15 | 91.3% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 22 | 17 | 5 | 77.3% |
| vless | 302 | 237 | 65 | 78.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 24 |
| cn-block:TimeoutError | 19 |
| geo:ClientOSError | 18 |
| speed:ClientOSError | 11 |
| cn-block:ClientOSError | 8 |
| speed:TimeoutError | 8 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 2 |
| geo:exit-country | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5213 |
| ConnectionRefusedError | 927 |
| gaierror | 497 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.96 | prefer | 304 | 0.891 | 1781 |
| mheidari-all | 0.869 | prefer | 36 | 0.806 | 16210 |
| Surfboard-tg-mixed | 0.822 | prefer | 153 | 0.745 | 7511 |
| DeltaKronecker-all | 0.8 | prefer | 23 | 0.739 | 5892 |
| ermaozi | 0.626 | observe | 34 | 0.618 | 382 |
| mahdibland-V2RayAggregator | 0.335 | observe | 1 | 1.0 | 4222 |
| roosterkid-openproxylist-v2ray | 0.275 | observe | 3 | 0.667 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4839 |
| Epodonios-all | 0.255 | observe | 0 | None | 8029 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 3 | 3 |
| ermaozi | 0.618 | 21 | 13 | 34 |
| roosterkid-openproxylist-v2ray | 0.667 | 2 | 1 | 3 |
| DeltaKronecker-all | 0.739 | 17 | 6 | 23 |
| Surfboard-tg-mixed | 0.745 | 114 | 39 | 153 |
| mheidari-all | 0.806 | 29 | 7 | 36 |
| Au1rxx-base64 | 0.891 | 271 | 33 | 304 |
| mahdibland-V2RayAggregator | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16210 | yes | 4.66 | 0 |
| SoliSpirit-all | 8804 | yes | 3.63 | 0 |
| Epodonios-all | 8029 | yes | 3.27 | 0 |
| Surfboard-tg-mixed | 7511 | yes | 3.93 | 0 |
| barry-far-vless | 6390 | yes | 4.01 | 0 |
| Surfboard-tg-vless | 6079 | yes | 3.64 | 0 |
| DeltaKronecker-all | 5892 | yes | 4.48 | 0 |
| 10ium-ScrapeCategorize-Vless | 4839 | yes | 3.71 | 0 |
| mahdibland-V2RayAggregator | 4222 | yes | 1.67 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.11 | 0 |

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
| 204 | 34 |
| cn-block | 29 |
| geo | 22 |
| speed | 19 |
