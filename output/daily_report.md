# AutoNodes 每日报告

生成时间：2026-09-04 04:00:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 82420 |
| 去重后节点数 | 22769 |
| TCP 可达数 | 3000 |
| 真测通过数 | 612 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22769 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.0 |
| generate | 31.3 |
| geo | 1.5 |
| probe | 89.9 |
| real_test | 145.6 |
| tcp | 37.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 25 | 23 | 2 | 92.0% |
| hysteria2 | 22 | 19 | 3 | 86.4% |
| shadowsocks | 111 | 111 | 0 | 100.0% |
| socks | 1 | 0 | 1 | 0.0% |
| trojan | 60 | 41 | 19 | 68.3% |
| vless | 638 | 414 | 224 | 64.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 99 |
| speed:TimeoutError | 39 |
| geo:ClientOSError | 32 |
| speed:ClientOSError | 29 |
| cn-block:TimeoutError | 18 |
| cn-block:ClientOSError | 9 |
| 204:ProxyError | 9 |
| 204:TimeoutError | 6 |
| 204:ProxyConnectionError | 2 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ClientPayloadError | 1 |
| 204:ServerDisconnectedError | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41601: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4619 |
| ConnectionRefusedError | 920 |
| gaierror | 366 |
| OSError | 18 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 381 | 0.945 | 1753 |
| zhangkai | 0.922 | prefer | 22 | 0.955 | 144 |
| mheidari-all | 0.686 | observe | 186 | 0.608 | 15793 |
| DeltaKronecker-all | 0.517 | observe | 252 | 0.437 | 6335 |
| Surfboard-tg-mixed | 0.385 | observe | 8 | 0.5 | 7237 |
| tg-oneclickvpnkeys | 0.323 | observe | 4 | 0.75 | 71 |
| Epodonios-all | 0.255 | observe | 0 | None | 7701 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7955 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6022 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | 10ium-ScrapeCategorize-Vless | 0.226 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| 10ium-ScrapeCategorize-Vless | 0.2 | 1 | 4 | 5 |
| DeltaKronecker-all | 0.437 | 110 | 142 | 252 |
| Surfboard-tg-mixed | 0.5 | 4 | 4 | 8 |
| mheidari-all | 0.608 | 113 | 73 | 186 |
| tg-oneclickvpnkeys | 0.75 | 3 | 1 | 4 |
| Au1rxx-base64 | 0.945 | 360 | 21 | 381 |
| zhangkai | 0.955 | 21 | 1 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15793 | yes | 4.99 | 0 |
| SoliSpirit-all | 7955 | yes | 3.31 | 0 |
| Epodonios-all | 7701 | yes | 3.16 | 0 |
| Surfboard-tg-mixed | 7237 | yes | 3.71 | 0 |
| DeltaKronecker-all | 6335 | yes | 3.02 | 0 |
| barry-far-vless | 6237 | yes | 2.01 | 0 |
| Surfboard-tg-vless | 6022 | yes | 3.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 4671 | yes | 2.29 | 0 |
| mahdibland-V2RayAggregator | 4133 | yes | 2.27 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.08 | 0 |

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
| geo | 131 |
| speed | 69 |
| cn-block | 28 |
| 204 | 20 |
| sing-box exited 1 | 1 |
