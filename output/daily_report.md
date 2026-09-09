# AutoNodes 每日报告

生成时间：2026-09-09 04:20:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 85797 |
| 去重后节点数 | 22922 |
| TCP 可达数 | 3000 |
| 真测通过数 | 530 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22922 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 87.5 |
| geo | 1.4 |
| probe | 340.4 |
| real_test | 406.1 |
| tcp | 39.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 52 | 29 | 23 | 55.8% |
| hysteria2 | 10 | 10 | 0 | 100.0% |
| shadowsocks | 178 | 157 | 21 | 88.2% |
| socks | 11 | 6 | 5 | 54.5% |
| trojan | 23 | 15 | 8 | 65.2% |
| vless | 520 | 312 | 208 | 60.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 67 |
| geo:ClientOSError | 43 |
| 204:ProxyError | 41 |
| speed:TimeoutError | 35 |
| speed:ClientOSError | 28 |
| cn-block:TimeoutError | 20 |
| 204:TimeoutError | 15 |
| cn-block:ClientOSError | 4 |
| 204:ProxyConnectionError | 3 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:37096: bind: address already in use | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5472 |
| ConnectionRefusedError | 886 |
| gaierror | 404 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.962 | prefer | 263 | 0.897 | 1690 |
| Surfboard-tg-mixed | 0.824 | prefer | 205 | 0.746 | 7520 |
| mheidari-all | 0.672 | observe | 74 | 0.595 | 16648 |
| ermaozi-get_subscribe | 0.61 | observe | 20 | 0.6 | 473 |
| ermaozi | 0.573 | observe | 34 | 0.559 | 442 |
| DeltaKronecker-all | 0.412 | observe | 194 | 0.33 | 6097 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 176 |
| Epodonios-all | 0.255 | observe | 0 | None | 7969 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.33 | 64 | 130 | 194 |
| ermaozi | 0.559 | 19 | 15 | 34 |
| mheidari-all | 0.595 | 44 | 30 | 74 |
| ermaozi-get_subscribe | 0.6 | 12 | 8 | 20 |
| Surfboard-tg-mixed | 0.746 | 153 | 52 | 205 |
| Au1rxx-base64 | 0.897 | 236 | 27 | 263 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16648 | yes | 6.02 | 0 |
| SoliSpirit-all | 8963 | yes | 3.11 | 0 |
| Epodonios-all | 7969 | yes | 3.94 | 0 |
| Surfboard-tg-mixed | 7520 | yes | 3.47 | 0 |
| barry-far-vless | 6393 | yes | 4.21 | 0 |
| Surfboard-tg-vless | 6208 | yes | 3.7 | 0 |
| DeltaKronecker-all | 6097 | yes | 4.61 | 0 |
| 10ium-ScrapeCategorize-Vless | 4657 | yes | 3.93 | 0 |
| mahdibland-V2RayAggregator | 4219 | yes | 3.21 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 4.3 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 112 |
| speed | 64 |
| 204 | 62 |
| cn-block | 26 |
| sing-box exited 1 | 1 |
