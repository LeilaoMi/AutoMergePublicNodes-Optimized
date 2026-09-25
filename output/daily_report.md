# AutoNodes 每日报告

生成时间：2026-09-25 21:29:44

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 97258 |
| 去重后节点数 | 26464 |
| TCP 可达数 | 3000 |
| 真测通过数 | 402 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26464 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.0 |
| generate | 92.2 |
| geo | 1.4 |
| probe | 186.3 |
| real_test | 158.3 |
| tcp | 43.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 2 | 2 | 0 | 100.0% |
| http | 34 | 24 | 10 | 70.6% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 157 | 144 | 13 | 91.7% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 25 | 23 | 2 | 92.0% |
| vless | 231 | 186 | 45 | 80.5% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 21 |
| cn-block:TimeoutError | 17 |
| 204:ProxyError | 15 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 3 |
| speed:ClientOSError | 2 |
| geo:ClientOSError | 2 |
| speed:ProxyError | 2 |
| geo:TimeoutError | 2 |
| speed:TimeoutError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6221 |
| ConnectionRefusedError | 964 |
| gaierror | 362 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.949 | prefer | 241 | 0.884 | 1701 |
| mheidari-all | 0.903 | prefer | 77 | 0.831 | 22345 |
| Surfboard-tg-mixed | 0.901 | prefer | 121 | 0.826 | 7370 |
| ermaozi | 0.689 | observe | 32 | 0.688 | 304 |
| tg-oneclickvpnkeys | 0.314 | observe | 2 | 1.0 | 69 |
| ermaozi-get_subscribe | 0.268 | observe | 1 | 1.0 | 314 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5293 |
| DeltaKronecker-all | 0.255 | observe | 0 | None | 5452 |
| Epodonios-all | 0.255 | observe | 0 | None | 7740 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| ermaozi | 0.688 | 22 | 10 | 32 |
| Surfboard-tg-mixed | 0.826 | 100 | 21 | 121 |
| mheidari-all | 0.831 | 64 | 13 | 77 |
| Au1rxx-base64 | 0.884 | 213 | 28 | 241 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22345 | yes | 2.86 | 0 |
| SoliSpirit-all | 9253 | yes | 1.15 | 0 |
| Epodonios-all | 7740 | yes | 1.61 | 0 |
| Surfboard-tg-mixed | 7370 | yes | 2.09 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.86 | 0 |
| barry-far-vless | 6190 | yes | 0.64 | 0 |
| Surfboard-tg-vless | 5959 | yes | 2.23 | 0 |
| DeltaKronecker-all | 5452 | yes | 3.25 | 0 |
| 10ium-ScrapeCategorize-Vless | 5293 | yes | 0.49 | 0 |
| mahdibland-V2RayAggregator | 4304 | yes | 1.37 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 39 |
| cn-block | 25 |
| speed | 5 |
| geo | 4 |
