# AutoNodes 每日报告

生成时间：2026-09-14 12:31:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 84799 |
| 去重后节点数 | 23007 |
| TCP 可达数 | 3000 |
| 真测通过数 | 447 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23007 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 86.5 |
| geo | 1.4 |
| probe | 209.4 |
| real_test | 241.4 |
| tcp | 37.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 69 | 47 | 22 | 68.1% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 145 | 139 | 6 | 95.9% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 16 | 14 | 2 | 87.5% |
| vless | 315 | 226 | 89 | 71.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 27 |
| 204:ProxyError | 24 |
| cn-block:TimeoutError | 22 |
| speed:ClientOSError | 16 |
| 204:TimeoutError | 9 |
| cn-block:ClientOSError | 8 |
| geo:TimeoutError | 6 |
| speed:TimeoutError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5101 |
| ConnectionRefusedError | 875 |
| gaierror | 450 |
| OSError | 15 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.927 | prefer | 299 | 0.863 | 1668 |
| mheidari-all | 0.844 | prefer | 53 | 0.774 | 15903 |
| Surfboard-tg-mixed | 0.793 | prefer | 127 | 0.717 | 7478 |
| ermaozi | 0.715 | prefer | 51 | 0.706 | 417 |
| ermaozi-get_subscribe | 0.617 | observe | 19 | 0.632 | 444 |
| DeltaKronecker-all | 0.515 | observe | 16 | 0.5 | 5972 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 131 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4914 |
| Epodonios-all | 0.255 | observe | 0 | None | 7910 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.5 | 8 | 8 | 16 |
| ermaozi-get_subscribe | 0.632 | 12 | 7 | 19 |
| ermaozi | 0.706 | 36 | 15 | 51 |
| Surfboard-tg-mixed | 0.717 | 91 | 36 | 127 |
| mheidari-all | 0.774 | 41 | 12 | 53 |
| Au1rxx-base64 | 0.863 | 258 | 41 | 299 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15903 | yes | 4.6 | 0 |
| SoliSpirit-all | 9127 | yes | 3.94 | 0 |
| Epodonios-all | 7910 | yes | 5.32 | 0 |
| Surfboard-tg-mixed | 7478 | yes | 3.35 | 0 |
| barry-far-vless | 6310 | yes | 1.46 | 0 |
| Surfboard-tg-vless | 6074 | yes | 3.92 | 0 |
| DeltaKronecker-all | 5972 | yes | 4.68 | 0 |
| 10ium-ScrapeCategorize-Vless | 4914 | yes | 0.95 | 0 |
| mahdibland-V2RayAggregator | 4176 | yes | 2.88 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.55 | 0 |

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
| 204 | 35 |
| geo | 33 |
| cn-block | 32 |
| speed | 20 |
