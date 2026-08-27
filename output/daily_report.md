# AutoNodes 每日报告

生成时间：2026-08-27 08:40:20

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 88922 |
| 去重后节点数 | 24473 |
| TCP 可达数 | 3000 |
| 真测通过数 | 508 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24473 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 38.2 |
| geo | 1.5 |
| probe | 50.5 |
| real_test | 106.4 |
| tcp | 40.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 183 | 169 | 14 | 92.3% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 40 | 37 | 3 | 92.5% |
| vless | 345 | 255 | 90 | 73.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 31 |
| cn-block:TimeoutError | 17 |
| 204:TimeoutError | 15 |
| geo:ClientOSError | 14 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| 204:ProxyError | 7 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5608 |
| ConnectionRefusedError | 950 |
| gaierror | 323 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.972 | prefer | 350 | 0.906 | 1712 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.873 | prefer | 143 | 0.797 | 6600 |
| mheidari-all | 0.807 | prefer | 53 | 0.736 | 19260 |
| DeltaKronecker-all | 0.407 | observe | 47 | 0.319 | 6107 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4825 |
| Epodonios-all | 0.255 | observe | 0 | None | 7097 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7132 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5353 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.319 | 15 | 32 | 47 |
| mheidari-all | 0.736 | 39 | 14 | 53 |
| Surfboard-tg-mixed | 0.797 | 114 | 29 | 143 |
| Au1rxx-base64 | 0.906 | 317 | 33 | 350 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19260 | yes | 5.61 | 0 |
| SoliSpirit-all | 7132 | yes | 4.24 | 0 |
| Epodonios-all | 7097 | yes | 3.2 | 0 |
| Surfboard-tg-mixed | 6600 | yes | 3.9 | 0 |
| DeltaKronecker-all | 6107 | yes | 5.4 | 0 |
| barry-far-vless | 5696 | yes | 2.89 | 0 |
| xiaoji235-airport-v2ray-all | 5418 | yes | 1.65 | 0 |
| Surfboard-tg-vless | 5353 | yes | 3.43 | 0 |
| 10ium-ScrapeCategorize-Vless | 4825 | yes | 3.98 | 0 |
| mahdibland-V2RayAggregator | 4011 | yes | 0.79 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 45 |
| 204 | 24 |
| cn-block | 24 |
| speed | 18 |
