# AutoNodes 每日报告

生成时间：2026-10-14 03:44:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 93/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 98590 |
| 去重后节点数 | 27432 |
| TCP 可达数 | 3000 |
| 真测通过数 | 55 |
| verified 输出数 | 55 |
| global 输出数 | 70 |
| all 输出数 | 27432 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 104.5 |
| geo | 1.5 |
| probe | 322.3 |
| real_test | 443.3 |
| tcp | 96.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 59 | 26 | 33 | 44.1% |
| hysteria2 | 9 | 9 | 0 | 100.0% |
| shadowsocks | 152 | 147 | 5 | 96.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 111 | 103 | 8 | 92.8% |
| vless | 445 | 230 | 215 | 51.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 110 |
| 204:ProxyError | 41 |
| geo:ClientOSError | 36 |
| speed:ClientOSError | 33 |
| speed:TimeoutError | 15 |
| cn-block:TimeoutError | 10 |
| 204:TimeoutError | 8 |
| cn-block:ClientOSError | 7 |
| 204:ClientOSError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6612 |
| ConnectionRefusedError | 928 |
| gaierror | 499 |
| OSError | 228 |
| SSRFBlocked | 4 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 1.0 | prefer | 72 | 0.944 | 7113 |
| Au1rxx-base64 | 0.961 | prefer | 345 | 0.893 | 1771 |
| ermaozi-get_subscribe | 0.468 | observe | 61 | 0.443 | 598 |
| mheidari-all | 0.461 | observe | 300 | 0.38 | 24076 |
| zhangkai | 0.261 | observe | 1 | 1.0 | 144 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5076 |
| Epodonios-all | 0.255 | observe | 0 | None | 7613 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9824 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5621 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ArV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.38 | 114 | 186 | 300 |
| ermaozi-get_subscribe | 0.443 | 27 | 34 | 61 |
| Au1rxx-base64 | 0.893 | 308 | 37 | 345 |
| Surfboard-tg-mixed | 0.944 | 68 | 4 | 72 |
| zhangkai | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 24076 | yes | 5.54 | 0 |
| SoliSpirit-all | 9824 | yes | 3.7 | 0 |
| Epodonios-all | 7613 | yes | 4.97 | 0 |
| Surfboard-tg-mixed | 7113 | yes | 3.88 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.95 | 0 |
| barry-far-vless | 5866 | yes | 0.71 | 0 |
| Surfboard-tg-vless | 5621 | yes | 3.66 | 0 |
| 10ium-ScrapeCategorize-Vless | 5086 | yes | 2.49 | 0 |
| DeltaKronecker-all | 5076 | yes | 5.74 | 0 |
| mahdibland-V2RayAggregator | 4216 | yes | 2.81 | 0 |

## 趋势报警

| 类型 | 信息 |
| --- | --- |
| verified_drop_50pct | verified output dropped from 300 to 55 |
| real_ok_drop_50pct | real-test ok dropped from 412 to 55 |

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 146 |
| 204 | 51 |
| speed | 48 |
| cn-block | 17 |
