# AutoNodes 每日报告

生成时间：2026-09-06 10:44:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 96057 |
| 去重后节点数 | 25365 |
| TCP 可达数 | 3000 |
| 真测通过数 | 491 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25365 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.1 |
| generate | 32.2 |
| geo | 1.4 |
| probe | 89.5 |
| real_test | 115.6 |
| tcp | 41.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 26 | 23 | 3 | 88.5% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 155 | 150 | 5 | 96.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 29 | 25 | 4 | 86.2% |
| vless | 381 | 271 | 110 | 71.1% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 42 |
| cn-block:TimeoutError | 20 |
| 204:TimeoutError | 19 |
| geo:ClientOSError | 13 |
| speed:TimeoutError | 10 |
| 204:ProxyError | 6 |
| 204:ProxyConnectionError | 4 |
| geo:TimeoutError | 3 |
| speed:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| 204:ServerDisconnectedError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5410 |
| ConnectionRefusedError | 1031 |
| gaierror | 429 |
| OSError | 240 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.932 | prefer | 335 | 0.863 | 1781 |
| Surfboard-tg-mixed | 0.862 | prefer | 145 | 0.786 | 7318 |
| zhangkai | 0.846 | prefer | 23 | 0.87 | 144 |
| mheidari-all | 0.661 | observe | 103 | 0.583 | 22388 |
| DeltaKronecker-all | 0.48 | observe | 4 | 1.0 | 5856 |
| tg-oneclickvpnkeys | 0.363 | observe | 3 | 1.0 | 133 |
| xiaoji235-airport-v2ray-all | 0.335 | observe | 1 | 1.0 | 6965 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4791 |
| Epodonios-all | 0.255 | observe | 0 | None | 7771 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |

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
| mheidari-all | 0.583 | 60 | 43 | 103 |
| Surfboard-tg-mixed | 0.786 | 114 | 31 | 145 |
| Au1rxx-base64 | 0.863 | 289 | 46 | 335 |
| zhangkai | 0.87 | 20 | 3 | 23 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |
| DeltaKronecker-all | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22388 | yes | 5.43 | 0 |
| SoliSpirit-all | 8223 | yes | 4.72 | 0 |
| Epodonios-all | 7771 | yes | 4.78 | 0 |
| Surfboard-tg-mixed | 7318 | yes | 4.03 | 0 |
| xiaoji235-airport-v2ray-all | 6965 | yes | 3.24 | 0 |
| barry-far-vless | 6223 | yes | 2.36 | 0 |
| Surfboard-tg-vless | 6005 | yes | 3.44 | 0 |
| DeltaKronecker-all | 5856 | yes | 5.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 4791 | yes | 4.35 | 0 |
| mahdibland-V2RayAggregator | 4111 | yes | 0.49 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 62 |
| 204 | 33 |
| geo | 16 |
| speed | 13 |
