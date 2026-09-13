# AutoNodes 每日报告

生成时间：2026-09-13 11:38:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 94200 |
| 去重后节点数 | 25224 |
| TCP 可达数 | 3000 |
| 真测通过数 | 342 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25224 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 80.2 |
| geo | 1.4 |
| probe | 252.5 |
| real_test | 202.4 |
| tcp | 41.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 1 | 1 | 50.0% |
| http | 52 | 31 | 21 | 59.6% |
| hysteria2 | 22 | 17 | 5 | 77.3% |
| shadowsocks | 100 | 88 | 12 | 88.0% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 20 | 15 | 5 | 75.0% |
| vless | 264 | 187 | 77 | 70.8% |
| vmess | 2 | 0 | 2 | 0.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 24 |
| speed:ClientOSError | 22 |
| 204:ProxyError | 20 |
| 204:ProxyConnectionError | 16 |
| 204:TimeoutError | 12 |
| cn-block:TimeoutError | 9 |
| cn-block:ClientOSError | 5 |
| geo:TimeoutError | 5 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5013 |
| ConnectionRefusedError | 1000 |
| gaierror | 633 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.885 | prefer | 248 | 0.823 | 1633 |
| Surfboard-tg-mixed | 0.842 | prefer | 99 | 0.768 | 7439 |
| ermaozi | 0.684 | observe | 43 | 0.674 | 436 |
| mheidari-all | 0.509 | observe | 47 | 0.426 | 20485 |
| DeltaKronecker-all | 0.441 | observe | 13 | 0.462 | 5892 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 5301 |
| Au1rxx-clash | 0.32 | observe | 1 | 1.0 | 1633 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 102 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4839 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.244 | 10 | 0.3 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| roosterkid-openproxylist-v2ray | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.3 | 3 | 7 | 10 |
| mheidari-all | 0.426 | 20 | 27 | 47 |
| DeltaKronecker-all | 0.462 | 6 | 7 | 13 |
| ermaozi | 0.674 | 29 | 14 | 43 |
| Surfboard-tg-mixed | 0.768 | 76 | 23 | 99 |
| Au1rxx-base64 | 0.823 | 204 | 44 | 248 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20485 | yes | 5.53 | 0 |
| SoliSpirit-all | 8920 | yes | 4.31 | 0 |
| Epodonios-all | 7887 | yes | 3.51 | 0 |
| Surfboard-tg-mixed | 7439 | yes | 3.86 | 0 |
| barry-far-vless | 6291 | yes | 2.27 | 0 |
| Surfboard-tg-vless | 6075 | yes | 5.81 | 0 |
| DeltaKronecker-all | 5892 | yes | 5.72 | 0 |
| xiaoji235-airport-v2ray-all | 5301 | yes | 3.15 | 0 |
| 10ium-ScrapeCategorize-Vless | 4839 | yes | 2.56 | 0 |
| mahdibland-V2RayAggregator | 4221 | yes | 0.85 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 低通过率协议
| 协议 | 通过率 |
| --- | --- |
| vmess | 0.0 |

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 51 |
| geo | 29 |
| speed | 29 |
| cn-block | 15 |
