# AutoNodes 每日报告

生成时间：2026-09-17 11:32:56

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 86889 |
| 去重后节点数 | 24175 |
| TCP 可达数 | 3000 |
| 真测通过数 | 421 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24175 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 7.7 |
| generate | 84.0 |
| geo | 1.4 |
| probe | 234.4 |
| real_test | 256.2 |
| tcp | 40.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 81 | 49 | 32 | 60.5% |
| hysteria2 | 15 | 12 | 3 | 80.0% |
| shadowsocks | 177 | 152 | 25 | 85.9% |
| socks | 6 | 6 | 0 | 100.0% |
| trojan | 25 | 3 | 22 | 12.0% |
| vless | 307 | 195 | 112 | 63.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 38 |
| 204:TimeoutError | 30 |
| geo:ClientOSError | 28 |
| cn-block:TimeoutError | 22 |
| speed:TimeoutError | 21 |
| geo:TimeoutError | 19 |
| cn-block:ClientOSError | 14 |
| speed:ClientOSError | 10 |
| 204:ClientOSError | 8 |
| geo:ProxyError | 2 |
| 204:ProxyConnectionError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4975 |
| ConnectionRefusedError | 915 |
| gaierror | 468 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.882 | prefer | 274 | 0.818 | 1663 |
| mheidari-all | 0.756 | prefer | 66 | 0.682 | 16008 |
| ermaozi | 0.753 | prefer | 55 | 0.745 | 396 |
| DeltaKronecker-all | 0.617 | observe | 39 | 0.538 | 5931 |
| Surfboard-tg-mixed | 0.61 | observe | 149 | 0.53 | 7408 |
| ermaozi-get_subscribe | 0.362 | observe | 27 | 0.333 | 431 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 129 |
| Epodonios-all | 0.255 | observe | 0 | None | 7867 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.333 | 9 | 18 | 27 |
| Surfboard-tg-mixed | 0.53 | 79 | 70 | 149 |
| DeltaKronecker-all | 0.538 | 21 | 18 | 39 |
| mheidari-all | 0.682 | 45 | 21 | 66 |
| ermaozi | 0.745 | 41 | 14 | 55 |
| Au1rxx-base64 | 0.818 | 224 | 50 | 274 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16008 | yes | 6.05 | 0 |
| SoliSpirit-all | 8871 | yes | 6.2 | 0 |
| Epodonios-all | 7867 | yes | 4.63 | 0 |
| Surfboard-tg-mixed | 7408 | yes | 3.45 | 0 |
| barry-far-vless | 6149 | yes | 1.74 | 0 |
| DeltaKronecker-all | 5931 | yes | 5.21 | 0 |
| Surfboard-tg-vless | 5925 | yes | 4.04 | 0 |
| 10ium-ScrapeCategorize-Vless | 5093 | yes | 3.29 | 0 |
| mahdibland-V2RayAggregator | 4179 | yes | 0.57 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.62 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 77 |
| geo | 49 |
| cn-block | 36 |
| speed | 32 |
