# AutoNodes 每日报告

生成时间：2026-09-17 04:42:33

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 89183 |
| 去重后节点数 | 24536 |
| TCP 可达数 | 3000 |
| 真测通过数 | 537 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24536 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 70.5 |
| geo | 1.6 |
| probe | 429.1 |
| real_test | 610.6 |
| tcp | 42.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 37 | 26 | 11 | 70.3% |
| hysteria2 | 24 | 22 | 2 | 91.7% |
| shadowsocks | 128 | 123 | 5 | 96.1% |
| socks | 6 | 5 | 1 | 83.3% |
| trojan | 53 | 30 | 23 | 56.6% |
| vless | 755 | 327 | 428 | 43.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 255 |
| geo:ClientOSError | 70 |
| speed:TimeoutError | 55 |
| speed:ClientOSError | 44 |
| 204:ProxyError | 22 |
| cn-block:TimeoutError | 10 |
| 204:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| 204:ClientOSError | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6064 |
| ConnectionRefusedError | 901 |
| gaierror | 318 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.939 | prefer | 279 | 0.878 | 1590 |
| Surfboard-tg-mixed | 0.83 | prefer | 22 | 0.773 | 7408 |
| ermaozi | 0.774 | prefer | 27 | 0.778 | 396 |
| mheidari-all | 0.577 | observe | 165 | 0.497 | 17792 |
| DeltaKronecker-all | 0.411 | observe | 497 | 0.33 | 6081 |
| ermaozi-get_subscribe | 0.398 | observe | 11 | 0.545 | 431 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 130 |
| Epodonios-all | 0.255 | observe | 0 | None | 7930 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9115 |

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
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.33 | 164 | 333 | 497 |
| ninja-vless | 0.333 | 1 | 2 | 3 |
| mheidari-all | 0.497 | 82 | 83 | 165 |
| ermaozi-get_subscribe | 0.545 | 6 | 5 | 11 |
| Surfboard-tg-mixed | 0.773 | 17 | 5 | 22 |
| ermaozi | 0.778 | 21 | 6 | 27 |
| Au1rxx-base64 | 0.878 | 245 | 34 | 279 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17792 | yes | 3.77 | 0 |
| SoliSpirit-all | 9115 | yes | 2.48 | 0 |
| Epodonios-all | 7930 | yes | 4.21 | 0 |
| Surfboard-tg-mixed | 7408 | yes | 2.41 | 0 |
| barry-far-vless | 6194 | yes | 1.32 | 0 |
| DeltaKronecker-all | 6081 | yes | 1.89 | 0 |
| Surfboard-tg-vless | 5925 | yes | 2.57 | 0 |
| 10ium-ScrapeCategorize-Vless | 5115 | yes | 1.17 | 0 |
| mahdibland-V2RayAggregator | 4234 | yes | 2.1 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.61 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 325 |
| speed | 100 |
| 204 | 29 |
| cn-block | 16 |
