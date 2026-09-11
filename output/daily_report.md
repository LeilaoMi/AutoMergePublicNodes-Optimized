# AutoNodes 每日报告

生成时间：2026-09-11 04:20:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83660 |
| 去重后节点数 | 22960 |
| TCP 可达数 | 3000 |
| 真测通过数 | 539 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22960 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| generate | 87.6 |
| geo | 1.4 |
| probe | 401.0 |
| real_test | 581.7 |
| tcp | 37.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 60 | 43 | 17 | 71.7% |
| hysteria2 | 14 | 13 | 1 | 92.9% |
| shadowsocks | 145 | 134 | 11 | 92.4% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 64 | 27 | 37 | 42.2% |
| vless | 735 | 319 | 416 | 43.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 204 |
| speed:ClientOSError | 85 |
| geo:ClientOSError | 83 |
| speed:TimeoutError | 46 |
| 204:ProxyError | 25 |
| cn-block:TimeoutError | 18 |
| cn-block:ClientOSError | 8 |
| 204:TimeoutError | 7 |
| 204:ClientOSError | 3 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41389: bind: address already in use | 1 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4669 |
| ConnectionRefusedError | 900 |
| gaierror | 426 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.9 | prefer | 332 | 0.837 | 1613 |
| ermaozi | 0.813 | prefer | 42 | 0.81 | 431 |
| Surfboard-tg-mixed | 0.73 | prefer | 101 | 0.653 | 7301 |
| ermaozi-get_subscribe | 0.486 | observe | 18 | 0.5 | 461 |
| DeltaKronecker-all | 0.365 | observe | 514 | 0.284 | 5853 |
| mheidari-all | 0.305 | observe | 10 | 0.3 | 15718 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 168 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4995 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.284 | 146 | 368 | 514 |
| mheidari-all | 0.3 | 3 | 7 | 10 |
| ermaozi-get_subscribe | 0.5 | 9 | 9 | 18 |
| Surfboard-tg-mixed | 0.653 | 66 | 35 | 101 |
| ermaozi | 0.81 | 34 | 8 | 42 |
| Au1rxx-base64 | 0.837 | 278 | 54 | 332 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15718 | yes | 4.91 | 0 |
| SoliSpirit-all | 8799 | yes | 3.9 | 0 |
| Epodonios-all | 7793 | yes | 5.22 | 0 |
| Surfboard-tg-mixed | 7301 | yes | 4.22 | 0 |
| barry-far-vless | 6145 | yes | 2.1 | 0 |
| Surfboard-tg-vless | 5909 | yes | 3.89 | 0 |
| DeltaKronecker-all | 5853 | yes | 5.65 | 0 |
| 10ium-ScrapeCategorize-Vless | 4995 | yes | 1.34 | 0 |
| mahdibland-V2RayAggregator | 4255 | yes | 0.37 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.66 | 0 |

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
| geo | 288 |
| speed | 133 |
| 204 | 35 |
| cn-block | 27 |
| sing-box exited 1 | 1 |
