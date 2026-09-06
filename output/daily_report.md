# AutoNodes 每日报告

生成时间：2026-09-06 04:02:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 97417 |
| 去重后节点数 | 25569 |
| TCP 可达数 | 3000 |
| 真测通过数 | 577 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25569 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 22.8 |
| geo | 1.4 |
| probe | 67.2 |
| real_test | 139.3 |
| tcp | 42.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 29 | 28 | 1 | 96.6% |
| hysteria2 | 25 | 24 | 1 | 96.0% |
| shadowsocks | 184 | 166 | 18 | 90.2% |
| socks | 5 | 3 | 2 | 60.0% |
| trojan | 52 | 34 | 18 | 65.4% |
| vless | 675 | 319 | 356 | 47.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 158 |
| geo:ClientOSError | 77 |
| speed:TimeoutError | 48 |
| speed:ClientOSError | 32 |
| cn-block:ClientOSError | 31 |
| 204:TimeoutError | 19 |
| cn-block:TimeoutError | 12 |
| 204:ProxyError | 9 |
| speed:ClientPayloadError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |
| 204:ServerDisconnectedError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5837 |
| ConnectionRefusedError | 1008 |
| gaierror | 360 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Au1rxx-base64 | 0.959 | prefer | 314 | 0.889 | 1827 |
| Surfboard-tg-mixed | 0.821 | prefer | 199 | 0.744 | 7381 |
| tg-oneclickvpnkeys | 0.414 | observe | 6 | 0.833 | 132 |
| mheidari-all | 0.363 | observe | 425 | 0.282 | 22409 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 6965 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4887 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 6212 |
| Epodonios-all | 0.255 | observe | 0 | None | 7876 |

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
| mheidari-all | 0.282 | 120 | 305 | 425 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.744 | 148 | 51 | 199 |
| tg-oneclickvpnkeys | 0.833 | 5 | 1 | 6 |
| Au1rxx-base64 | 0.889 | 279 | 35 | 314 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22409 | yes | 3.57 | 0 |
| SoliSpirit-all | 8608 | yes | 3.31 | 0 |
| Epodonios-all | 7876 | yes | 3.18 | 0 |
| Surfboard-tg-mixed | 7381 | yes | 2.94 | 0 |
| xiaoji235-airport-v2ray-all | 6965 | yes | 1.07 | 0 |
| barry-far-vless | 6398 | yes | 0.72 | 0 |
| DeltaKronecker-all | 6212 | yes | 2.71 | 0 |
| Surfboard-tg-vless | 6075 | yes | 2.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 4887 | yes | 0.36 | 0 |
| mahdibland-V2RayAggregator | 4087 | yes | 1.79 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 236 |
| speed | 85 |
| cn-block | 44 |
| 204 | 31 |
