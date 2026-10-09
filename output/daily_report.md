# AutoNodes 每日报告

生成时间：2026-10-09 05:50:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 98042 |
| 去重后节点数 | 27766 |
| TCP 可达数 | 3000 |
| 真测通过数 | 495 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27766 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.6 |
| generate | 80.8 |
| geo | 1.5 |
| probe | 344.6 |
| real_test | 558.2 |
| tcp | 47.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 9 | 5 | 4 | 55.6% |
| http | 51 | 35 | 16 | 68.6% |
| hysteria2 | 27 | 27 | 0 | 100.0% |
| shadowsocks | 129 | 117 | 12 | 90.7% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 116 | 105 | 11 | 90.5% |
| vless | 508 | 203 | 305 | 40.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 158 |
| speed:TimeoutError | 64 |
| 204:ProxyError | 33 |
| geo:ClientOSError | 30 |
| speed:ClientOSError | 28 |
| cn-block:TimeoutError | 16 |
| 204:TimeoutError | 15 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6700 |
| ConnectionRefusedError | 1007 |
| gaierror | 358 |
| OSError | 238 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.982 | prefer | 370 | 0.914 | 1763 |
| DeltaKronecker-all | 0.78 | prefer | 28 | 0.714 | 5197 |
| ermaozi-get_subscribe | 0.642 | observe | 53 | 0.623 | 607 |
| zhangkai | 0.555 | observe | 8 | 1.0 | 144 |
| Au1rxx-clash | 0.325 | observe | 1 | 1.0 | 1761 |
| mheidari-all | 0.323 | observe | 372 | 0.242 | 23125 |
| Surfboard-tg-mixed | 0.305 | observe | 10 | 0.3 | 7069 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5081 |

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
| ninja-vless | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.242 | 90 | 282 | 372 |
| Surfboard-tg-mixed | 0.3 | 3 | 7 | 10 |
| ermaozi-get_subscribe | 0.623 | 33 | 20 | 53 |
| DeltaKronecker-all | 0.714 | 20 | 8 | 28 |
| Au1rxx-base64 | 0.914 | 338 | 32 | 370 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| Au1rxx-clash | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23125 | yes | 3.79 | 0 |
| SoliSpirit-all | 9901 | yes | 1.85 | 0 |
| Epodonios-all | 7569 | yes | 2.1 | 0 |
| Surfboard-tg-mixed | 7069 | yes | 3.1 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 1.44 | 0 |
| barry-far-vless | 5823 | yes | 0.86 | 0 |
| Surfboard-tg-vless | 5581 | yes | 2.61 | 0 |
| DeltaKronecker-all | 5197 | yes | 4.02 | 0 |
| 10ium-ScrapeCategorize-Vless | 5081 | yes | 0.76 | 0 |
| mahdibland-V2RayAggregator | 4362 | yes | 2.17 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 188 |
| speed | 92 |
| 204 | 50 |
| cn-block | 21 |
