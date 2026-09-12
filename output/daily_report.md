# AutoNodes 每日报告

生成时间：2026-09-12 15:30:46

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83067 |
| 去重后节点数 | 22816 |
| TCP 可达数 | 3000 |
| 真测通过数 | 470 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22816 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 76.7 |
| geo | 1.4 |
| probe | 254.2 |
| real_test | 239.0 |
| tcp | 38.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 41 | 27 | 14 | 65.9% |
| hysteria2 | 25 | 20 | 5 | 80.0% |
| shadowsocks | 157 | 149 | 8 | 94.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 50 | 46 | 4 | 92.0% |
| vless | 339 | 226 | 113 | 66.7% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 53 |
| cn-block:TimeoutError | 20 |
| 204:ProxyError | 18 |
| cn-block:ClientOSError | 14 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 9 |
| speed:TimeoutError | 9 |
| geo:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5248 |
| ConnectionRefusedError | 873 |
| gaierror | 500 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.93 | prefer | 303 | 0.875 | 1455 |
| DeltaKronecker-all | 0.791 | prefer | 43 | 0.721 | 5970 |
| Surfboard-tg-mixed | 0.765 | prefer | 144 | 0.688 | 7345 |
| mheidari-all | 0.646 | observe | 81 | 0.568 | 15620 |
| ermaozi | 0.637 | observe | 35 | 0.629 | 393 |
| ermaozi-get_subscribe | 0.425 | observe | 6 | 0.833 | 408 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7743 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.568 | 46 | 35 | 81 |
| ermaozi | 0.629 | 22 | 13 | 35 |
| Surfboard-tg-mixed | 0.688 | 99 | 45 | 144 |
| DeltaKronecker-all | 0.721 | 31 | 12 | 43 |
| ermaozi-get_subscribe | 0.833 | 5 | 1 | 6 |
| Au1rxx-base64 | 0.875 | 265 | 38 | 303 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15620 | yes | 3.59 | 0 |
| SoliSpirit-all | 8959 | yes | 1.44 | 0 |
| Epodonios-all | 7743 | yes | 2.46 | 0 |
| Surfboard-tg-mixed | 7345 | yes | 5.21 | 0 |
| barry-far-vless | 6112 | yes | 1.21 | 0 |
| DeltaKronecker-all | 5970 | yes | 3.04 | 0 |
| Surfboard-tg-vless | 5912 | yes | 3.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4793 | yes | 0.96 | 0 |
| mahdibland-V2RayAggregator | 4207 | yes | 2.07 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.01 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 57 |
| cn-block | 36 |
| 204 | 30 |
| speed | 23 |
