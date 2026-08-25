# AutoNodes 每日报告

生成时间：2026-08-25 18:50:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78004 |
| 去重后节点数 | 22569 |
| TCP 可达数 | 3000 |
| 真测通过数 | 564 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22569 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| generate | 24.6 |
| geo | 1.3 |
| probe | 55.0 |
| real_test | 118.5 |
| tcp | 37.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 23 | 21 | 2 | 91.3% |
| shadowsocks | 167 | 158 | 9 | 94.6% |
| socks | 11 | 10 | 1 | 90.9% |
| trojan | 47 | 44 | 3 | 93.6% |
| vless | 399 | 307 | 92 | 76.9% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 34 |
| geo:TimeoutError | 20 |
| 204:TimeoutError | 19 |
| cn-block:TimeoutError | 15 |
| speed:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ProxyError | 4 |
| 204:ClientOSError | 3 |
| geo:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5424 |
| ConnectionRefusedError | 843 |
| gaierror | 129 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| DeltaKronecker-all | 0.943 | prefer | 49 | 0.878 | 6340 |
| Surfboard-tg-mixed | 0.908 | prefer | 97 | 0.835 | 6487 |
| Au1rxx-base64 | 0.902 | prefer | 427 | 0.843 | 1502 |
| mheidari-all | 0.843 | prefer | 74 | 0.77 | 14446 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 6936 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7007 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5327 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
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
| mheidari-all | 0.77 | 57 | 17 | 74 |
| Surfboard-tg-mixed | 0.835 | 81 | 16 | 97 |
| Au1rxx-base64 | 0.843 | 360 | 67 | 427 |
| DeltaKronecker-all | 0.878 | 43 | 6 | 49 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14446 | yes | 2.81 | 0 |
| SoliSpirit-all | 7007 | yes | 3.95 | 0 |
| Epodonios-all | 6936 | yes | 4.0 | 0 |
| Surfboard-tg-mixed | 6487 | yes | 2.48 | 0 |
| DeltaKronecker-all | 6340 | yes | 3.43 | 0 |
| barry-far-vless | 5601 | yes | 0.66 | 0 |
| Surfboard-tg-vless | 5327 | yes | 3.16 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 2.66 | 0 |
| mahdibland-V2RayAggregator | 4119 | yes | 2.0 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.74 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 39 |
| 204 | 26 |
| geo | 22 |
| cn-block | 20 |
