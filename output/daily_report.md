# AutoNodes 每日报告

生成时间：2026-09-15 21:13:49

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 84752 |
| 去重后节点数 | 23104 |
| TCP 可达数 | 3000 |
| 真测通过数 | 417 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23104 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 79.4 |
| geo | 1.4 |
| probe | 187.2 |
| real_test | 182.1 |
| tcp | 38.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 39 | 29 | 10 | 74.4% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 139 | 131 | 8 | 94.2% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 12 | 7 | 5 | 58.3% |
| vless | 305 | 234 | 71 | 76.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 19 |
| cn-block:TimeoutError | 16 |
| cn-block:ClientOSError | 13 |
| 204:TimeoutError | 13 |
| 204:ProxyError | 11 |
| speed:ClientOSError | 11 |
| speed:TimeoutError | 6 |
| cn-block:ProxyError | 3 |
| geo:TimeoutError | 3 |
| 204:ClientOSError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5383 |
| ConnectionRefusedError | 841 |
| gaierror | 357 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.989 | prefer | 31 | 0.935 | 15952 |
| Au1rxx-base64 | 0.948 | prefer | 305 | 0.889 | 1553 |
| ermaozi | 0.779 | prefer | 36 | 0.778 | 406 |
| Surfboard-tg-mixed | 0.702 | prefer | 125 | 0.624 | 7516 |
| DeltaKronecker-all | 0.633 | observe | 14 | 0.714 | 5932 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5015 |
| Epodonios-all | 0.255 | observe | 0 | None | 7982 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8946 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6065 |

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
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.624 | 78 | 47 | 125 |
| DeltaKronecker-all | 0.714 | 10 | 4 | 14 |
| ermaozi | 0.778 | 28 | 8 | 36 |
| Au1rxx-base64 | 0.889 | 271 | 34 | 305 |
| mheidari-all | 0.935 | 29 | 2 | 31 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15952 | yes | 4.81 | 0 |
| SoliSpirit-all | 8946 | yes | 4.91 | 0 |
| Epodonios-all | 7982 | yes | 5.05 | 0 |
| Surfboard-tg-mixed | 7516 | yes | 4.05 | 0 |
| barry-far-vless | 6289 | yes | 1.34 | 0 |
| Surfboard-tg-vless | 6065 | yes | 3.53 | 0 |
| DeltaKronecker-all | 5932 | yes | 5.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 5015 | yes | 0.77 | 0 |
| mahdibland-V2RayAggregator | 4258 | yes | 3.08 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.13 | 0 |

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
| cn-block | 32 |
| 204 | 27 |
| geo | 22 |
| speed | 17 |
