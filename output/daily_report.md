# AutoNodes 每日报告

生成时间：2026-09-30 22:12:31

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 97982 |
| 去重后节点数 | 27241 |
| TCP 可达数 | 3000 |
| 真测通过数 | 362 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27241 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.5 |
| generate | 77.1 |
| geo | 1.6 |
| probe | 203.0 |
| real_test | 126.8 |
| tcp | 45.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 27 | 7 | 20 | 25.9% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 141 | 133 | 8 | 94.3% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 14 | 13 | 1 | 92.9% |
| vless | 252 | 195 | 57 | 77.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 38 |
| 204:ProxyConnectionError | 22 |
| cn-block:TimeoutError | 6 |
| 204:ProxyError | 5 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 4 |
| geo:TimeoutError | 2 |
| 204:ClientOSError | 1 |
| speed:TimeoutError | 1 |
| geo:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6071 |
| ConnectionRefusedError | 1014 |
| gaierror | 440 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.94 | prefer | 41 | 0.878 | 7200 |
| Au1rxx-base64 | 0.914 | prefer | 302 | 0.844 | 1803 |
| mheidari-all | 0.892 | prefer | 78 | 0.821 | 22901 |
| zhangkai | 0.338 | observe | 17 | 0.353 | 144 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7696 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9724 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5833 |
| barry-far-vless | 0.255 | observe | 0 | None | 6072 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.131 | 9 | 0.111 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| tg-oneclickvpnkeys | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.0 | 0 | 2 | 2 |
| ermaozi-get_subscribe | 0.111 | 1 | 8 | 9 |
| zhangkai | 0.353 | 6 | 11 | 17 |
| mheidari-all | 0.821 | 64 | 14 | 78 |
| Au1rxx-base64 | 0.844 | 255 | 47 | 302 |
| Surfboard-tg-mixed | 0.878 | 36 | 5 | 41 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22901 | yes | 6.36 | 0 |
| SoliSpirit-all | 9724 | yes | 4.83 | 0 |
| Epodonios-all | 7696 | yes | 5.65 | 0 |
| Surfboard-tg-mixed | 7200 | yes | 4.17 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.77 | 0 |
| barry-far-vless | 6072 | yes | 0.54 | 0 |
| Surfboard-tg-vless | 5833 | yes | 5.01 | 0 |
| DeltaKronecker-all | 5434 | yes | 6.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 0.79 | 0 |
| mahdibland-V2RayAggregator | 4183 | yes | 3.11 | 0 |

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
| speed | 39 |
| 204 | 33 |
| cn-block | 14 |
| geo | 3 |
