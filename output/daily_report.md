# AutoNodes 每日报告

生成时间：2026-09-04 11:03:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83808 |
| 去重后节点数 | 23398 |
| TCP 可达数 | 3000 |
| 真测通过数 | 514 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23398 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 44.2 |
| geo | 1.4 |
| probe | 84.2 |
| real_test | 108.5 |
| tcp | 37.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 27 | 25 | 2 | 92.6% |
| hysteria2 | 20 | 17 | 3 | 85.0% |
| shadowsocks | 159 | 145 | 14 | 91.2% |
| socks | 2 | 0 | 2 | 0.0% |
| trojan | 40 | 20 | 20 | 50.0% |
| vless | 410 | 303 | 107 | 73.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 33 |
| geo:TimeoutError | 28 |
| 204:TimeoutError | 17 |
| speed:TimeoutError | 17 |
| cn-block:TimeoutError | 14 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 11 |
| speed:ClientOSError | 7 |
| 204:ClientOSError | 4 |
| 204:ProxyConnectionError | 2 |
| cn-block:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:31239: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5143 |
| ConnectionRefusedError | 898 |
| gaierror | 394 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.966 | prefer | 357 | 0.899 | 1736 |
| zhangkai | 0.886 | prefer | 23 | 0.913 | 144 |
| Surfboard-tg-mixed | 0.838 | prefer | 64 | 0.766 | 7244 |
| mheidari-all | 0.795 | prefer | 142 | 0.718 | 15923 |
| tg-oneclickvpnkeys | 0.443 | observe | 5 | 1.0 | 87 |
| DeltaKronecker-all | 0.326 | observe | 67 | 0.239 | 7089 |
| Epodonios-all | 0.255 | observe | 0 | None | 7763 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7993 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6120 |

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
| ninja-vless | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.239 | 16 | 51 | 67 |
| mheidari-all | 0.718 | 102 | 40 | 142 |
| Surfboard-tg-mixed | 0.766 | 49 | 15 | 64 |
| Au1rxx-base64 | 0.899 | 321 | 36 | 357 |
| zhangkai | 0.913 | 21 | 2 | 23 |
| tg-oneclickvpnkeys | 1.0 | 5 | 0 | 5 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15923 | yes | 4.58 | 0 |
| SoliSpirit-all | 7993 | yes | 3.87 | 0 |
| Epodonios-all | 7763 | yes | 2.82 | 0 |
| Surfboard-tg-mixed | 7244 | yes | 3.3 | 0 |
| DeltaKronecker-all | 7089 | yes | 4.78 | 0 |
| barry-far-vless | 6426 | yes | 2.36 | 0 |
| Surfboard-tg-vless | 6120 | yes | 3.92 | 0 |
| 10ium-ScrapeCategorize-Vless | 4810 | yes | 2.53 | 0 |
| mahdibland-V2RayAggregator | 4123 | yes | 0.45 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.91 | 0 |

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
| geo | 61 |
| 204 | 35 |
| cn-block | 27 |
| speed | 24 |
| sing-box exited 1 | 1 |
