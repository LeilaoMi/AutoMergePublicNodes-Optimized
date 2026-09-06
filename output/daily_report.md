# AutoNodes 每日报告

生成时间：2026-09-06 15:20:32

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 94591 |
| 去重后节点数 | 24561 |
| TCP 可达数 | 3000 |
| 真测通过数 | 515 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24561 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 37.6 |
| geo | 1.3 |
| probe | 67.4 |
| real_test | 116.6 |
| tcp | 41.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 24 | 23 | 1 | 95.8% |
| shadowsocks | 167 | 153 | 14 | 91.6% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 34 | 27 | 7 | 79.4% |
| vless | 416 | 281 | 135 | 67.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 42 |
| geo:ClientOSError | 36 |
| 204:TimeoutError | 29 |
| cn-block:TimeoutError | 18 |
| 204:ProxyError | 10 |
| speed:TimeoutError | 9 |
| cn-block:ProxyError | 6 |
| speed:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| geo:TimeoutError | 2 |
| 204:ServerDisconnectedError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5293 |
| ConnectionRefusedError | 988 |
| gaierror | 338 |
| OSError | 232 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.974 | prefer | 346 | 0.902 | 1876 |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.804 | prefer | 161 | 0.727 | 7393 |
| mheidari-all | 0.512 | observe | 137 | 0.431 | 21148 |
| xiaoji235-airport-v2ray-all | 0.391 | observe | 2 | 1.0 | 5750 |
| tg-oneclickvpnkeys | 0.363 | observe | 3 | 1.0 | 133 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4791 |
| Epodonios-all | 0.255 | observe | 0 | None | 7776 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8812 |

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
| DeltaKronecker-all | 0.0 | 0 | 1 | 1 |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.431 | 59 | 78 | 137 |
| Surfboard-tg-mixed | 0.727 | 117 | 44 | 161 |
| Au1rxx-base64 | 0.902 | 312 | 34 | 346 |
| xiaoji235-airport-v2ray-all | 1.0 | 2 | 0 | 2 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21148 | yes | 4.2 | 0 |
| SoliSpirit-all | 8812 | yes | 2.22 | 0 |
| Epodonios-all | 7776 | yes | 3.69 | 0 |
| Surfboard-tg-mixed | 7393 | yes | 2.39 | 0 |
| barry-far-vless | 6226 | yes | 1.28 | 0 |
| Surfboard-tg-vless | 6147 | yes | 2.25 | 0 |
| DeltaKronecker-all | 5856 | yes | 2.81 | 0 |
| xiaoji235-airport-v2ray-all | 5750 | yes | 2.47 | 0 |
| 10ium-ScrapeCategorize-Vless | 4791 | yes | 1.4 | 0 |
| mahdibland-V2RayAggregator | 4111 | yes | 0.88 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 66 |
| 204 | 42 |
| geo | 38 |
| speed | 12 |
