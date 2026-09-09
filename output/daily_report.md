# AutoNodes 每日报告

生成时间：2026-09-09 20:55:23

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 83567 |
| 去重后节点数 | 22107 |
| TCP 可达数 | 3000 |
| 真测通过数 | 474 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22107 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 74.4 |
| geo | 1.4 |
| probe | 220.4 |
| real_test | 221.0 |
| tcp | 36.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 26 | 22 | 4 | 84.6% |
| hysteria2 | 21 | 18 | 3 | 85.7% |
| shadowsocks | 171 | 158 | 13 | 92.4% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 27 | 21 | 6 | 77.8% |
| vless | 312 | 251 | 61 | 80.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 17 |
| geo:ClientOSError | 16 |
| 204:TimeoutError | 14 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 8 |
| geo:TimeoutError | 7 |
| speed:ClientOSError | 7 |
| 204:ClientOSError | 4 |
| speed:TimeoutError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:31319: bind: address already in use | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4873 |
| ConnectionRefusedError | 877 |
| gaierror | 385 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.972 | prefer | 311 | 0.913 | 1527 |
| mheidari-all | 0.901 | prefer | 26 | 0.846 | 16196 |
| DeltaKronecker-all | 0.863 | prefer | 58 | 0.793 | 5187 |
| ermaozi | 0.802 | prefer | 26 | 0.808 | 410 |
| Surfboard-tg-mixed | 0.79 | prefer | 136 | 0.713 | 7393 |
| tg-oneclickvpnkeys | 0.317 | observe | 2 | 1.0 | 147 |
| ermaozi-get_subscribe | 0.272 | observe | 1 | 1.0 | 418 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4795 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
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
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.713 | 97 | 39 | 136 |
| DeltaKronecker-all | 0.793 | 46 | 12 | 58 |
| ermaozi | 0.808 | 21 | 5 | 26 |
| mheidari-all | 0.846 | 22 | 4 | 26 |
| Au1rxx-base64 | 0.913 | 284 | 27 | 311 |
| ermaozi-get_subscribe | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16196 | yes | 3.37 | 0 |
| SoliSpirit-all | 8955 | yes | 2.92 | 0 |
| Epodonios-all | 7839 | yes | 3.53 | 0 |
| Surfboard-tg-mixed | 7393 | yes | 3.01 | 0 |
| barry-far-vless | 6253 | yes | 1.76 | 0 |
| Surfboard-tg-vless | 6033 | yes | 2.46 | 0 |
| DeltaKronecker-all | 5187 | yes | 6.58 | 0 |
| 10ium-ScrapeCategorize-Vless | 4795 | yes | 2.0 | 0 |
| mahdibland-V2RayAggregator | 4247 | yes | 0.39 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.81 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| cn-block | 26 |
| geo | 23 |
| speed | 9 |
| sing-box exited 1 | 1 |
