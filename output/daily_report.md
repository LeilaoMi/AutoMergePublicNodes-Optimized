# AutoNodes 每日报告

生成时间：2026-09-28 13:37:28

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 96149 |
| 去重后节点数 | 26789 |
| TCP 可达数 | 3000 |
| 真测通过数 | 463 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26789 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.4 |
| generate | 92.4 |
| geo | 1.4 |
| probe | 272.5 |
| real_test | 189.9 |
| tcp | 45.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 49 | 32 | 17 | 65.3% |
| hysteria2 | 20 | 16 | 4 | 80.0% |
| shadowsocks | 180 | 153 | 27 | 85.0% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 31 | 27 | 4 | 87.1% |
| vless | 293 | 232 | 61 | 79.2% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 27 |
| 204:ProxyError | 22 |
| 204:TimeoutError | 20 |
| speed:ClientOSError | 19 |
| speed:TimeoutError | 7 |
| geo:TimeoutError | 6 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 2 |
| geo:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6633 |
| ConnectionRefusedError | 961 |
| gaierror | 273 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.927 | prefer | 311 | 0.862 | 1677 |
| mheidari-all | 0.88 | prefer | 58 | 0.81 | 22474 |
| Surfboard-tg-mixed | 0.814 | prefer | 137 | 0.737 | 7046 |
| ermaozi | 0.72 | prefer | 49 | 0.714 | 344 |
| DeltaKronecker-all | 0.573 | observe | 15 | 0.6 | 5428 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 94 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5326 |
| Epodonios-all | 0.255 | observe | 0 | None | 7414 |

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
| ermaozi-get_subscribe | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.6 | 9 | 6 | 15 |
| ermaozi | 0.714 | 35 | 14 | 49 |
| Surfboard-tg-mixed | 0.737 | 101 | 36 | 137 |
| mheidari-all | 0.81 | 47 | 11 | 58 |
| Au1rxx-base64 | 0.862 | 268 | 43 | 311 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22474 | yes | 3.5 | 0 |
| SoliSpirit-all | 9420 | yes | 2.16 | 0 |
| Epodonios-all | 7414 | yes | 3.67 | 0 |
| Surfboard-tg-mixed | 7046 | yes | 2.84 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 0.99 | 0 |
| barry-far-vless | 5752 | yes | 2.8 | 0 |
| Surfboard-tg-vless | 5638 | yes | 2.25 | 0 |
| DeltaKronecker-all | 5428 | yes | 3.89 | 0 |
| 10ium-ScrapeCategorize-Vless | 5326 | yes | 1.1 | 0 |
| mahdibland-V2RayAggregator | 4185 | yes | 1.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 45 |
| cn-block | 34 |
| speed | 27 |
| geo | 9 |
