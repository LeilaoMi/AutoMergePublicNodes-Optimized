# AutoNodes 每日报告

生成时间：2026-09-29 22:14:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 96969 |
| 去重后节点数 | 27166 |
| TCP 可达数 | 3000 |
| 真测通过数 | 402 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27166 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 88.1 |
| geo | 1.4 |
| probe | 227.0 |
| real_test | 155.7 |
| tcp | 45.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 3 | 2 | 1 | 66.7% |
| http | 32 | 28 | 4 | 87.5% |
| hysteria2 | 23 | 23 | 0 | 100.0% |
| shadowsocks | 158 | 146 | 12 | 92.4% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 11 | 6 | 5 | 54.5% |
| vless | 253 | 194 | 59 | 76.7% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 30 |
| cn-block:TimeoutError | 18 |
| 204:ProxyError | 8 |
| speed:TimeoutError | 7 |
| geo:TimeoutError | 6 |
| 204:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6412 |
| ConnectionRefusedError | 1000 |
| gaierror | 287 |
| OSError | 235 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.98 | prefer | 28 | 0.929 | 7082 |
| mheidari-all | 0.916 | prefer | 114 | 0.842 | 22763 |
| Au1rxx-base64 | 0.882 | prefer | 304 | 0.812 | 1792 |
| ermaozi | 0.86 | prefer | 31 | 0.871 | 291 |
| tg-oneclickvpnkeys | 0.36 | observe | 3 | 1.0 | 62 |
| DeltaKronecker-all | 0.335 | observe | 1 | 1.0 | 5528 |
| ermaozi-get_subscribe | 0.323 | observe | 2 | 1.0 | 293 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5314 |
| Epodonios-all | 0.255 | observe | 0 | None | 7556 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Au1rxx-base64 | 0.812 | 247 | 57 | 304 |
| mheidari-all | 0.842 | 96 | 18 | 114 |
| ermaozi | 0.871 | 27 | 4 | 31 |
| Surfboard-tg-mixed | 0.929 | 26 | 2 | 28 |
| DeltaKronecker-all | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 2 | 0 | 2 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22763 | yes | 4.5 | 0 |
| SoliSpirit-all | 9172 | yes | 3.34 | 0 |
| Epodonios-all | 7556 | yes | 2.36 | 0 |
| Surfboard-tg-mixed | 7082 | yes | 2.74 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.61 | 0 |
| barry-far-vless | 5942 | yes | 2.4 | 0 |
| Surfboard-tg-vless | 5695 | yes | 3.1 | 0 |
| DeltaKronecker-all | 5528 | yes | 3.94 | 0 |
| 10ium-ScrapeCategorize-Vless | 5314 | yes | 2.0 | 0 |
| mahdibland-V2RayAggregator | 4338 | yes | 2.16 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 37 |
| cn-block | 23 |
| 204 | 15 |
| geo | 7 |
