# AutoNodes 每日报告

生成时间：2026-08-25 13:00:43

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78389 |
| 去重后节点数 | 22412 |
| TCP 可达数 | 3000 |
| 真测通过数 | 580 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22412 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 43.3 |
| geo | 1.4 |
| probe | 54.5 |
| real_test | 112.9 |
| tcp | 36.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 28 | 27 | 1 | 96.4% |
| shadowsocks | 209 | 189 | 20 | 90.4% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 54 | 44 | 10 | 81.5% |
| vless | 383 | 294 | 89 | 76.8% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 24 |
| 204:TimeoutError | 23 |
| cn-block:TimeoutError | 22 |
| speed:TimeoutError | 14 |
| speed:ClientOSError | 10 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 7 |
| 204:ProxyError | 5 |
| geo:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4931 |
| ConnectionRefusedError | 852 |
| gaierror | 291 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.967 | prefer | 24 | 1.0 | 144 |
| mheidari-all | 0.933 | prefer | 73 | 0.863 | 14402 |
| Au1rxx-base64 | 0.915 | prefer | 389 | 0.853 | 1581 |
| Surfboard-tg-mixed | 0.825 | prefer | 155 | 0.748 | 6520 |
| DeltaKronecker-all | 0.822 | prefer | 60 | 0.75 | 6340 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 7010 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7084 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5377 |

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
| Surfboard-tg-mixed | 0.748 | 116 | 39 | 155 |
| DeltaKronecker-all | 0.75 | 45 | 15 | 60 |
| Au1rxx-base64 | 0.853 | 332 | 57 | 389 |
| mheidari-all | 0.863 | 63 | 10 | 73 |
| zhangkai | 1.0 | 24 | 0 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14402 | yes | 4.48 | 0 |
| SoliSpirit-all | 7084 | yes | 4.09 | 0 |
| Epodonios-all | 7010 | yes | 3.05 | 0 |
| Surfboard-tg-mixed | 6520 | yes | 3.3 | 0 |
| DeltaKronecker-all | 6340 | yes | 4.95 | 0 |
| barry-far-vless | 5577 | yes | 3.19 | 0 |
| Surfboard-tg-vless | 5377 | yes | 3.5 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 2.95 | 0 |
| mahdibland-V2RayAggregator | 4119 | yes | 0.67 | 0 |
| MatinGhanbari-all-sub | 3987 | yes | 3.28 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 35 |
| cn-block | 33 |
| geo | 29 |
| speed | 24 |
