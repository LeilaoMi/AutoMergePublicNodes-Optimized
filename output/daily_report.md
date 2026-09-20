# AutoNodes 每日报告

生成时间：2026-09-20 15:57:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84264 |
| 去重后节点数 | 23485 |
| TCP 可达数 | 3000 |
| 真测通过数 | 504 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23485 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 71.0 |
| geo | 1.5 |
| probe | 199.9 |
| real_test | 201.6 |
| tcp | 37.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 29 | 24 | 5 | 82.8% |
| hysteria2 | 18 | 16 | 2 | 88.9% |
| shadowsocks | 153 | 138 | 15 | 90.2% |
| trojan | 7 | 5 | 2 | 71.4% |
| vless | 436 | 318 | 118 | 72.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 37 |
| cn-block:TimeoutError | 20 |
| 204:ProxyError | 19 |
| 204:TimeoutError | 19 |
| geo:TimeoutError | 16 |
| cn-block:ClientOSError | 14 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| speed:ClientOSError | 4 |
| speed:ProxyError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5074 |
| ConnectionRefusedError | 809 |
| gaierror | 463 |
| OSError | 18 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.979 | prefer | 301 | 0.917 | 1617 |
| ermaozi | 0.897 | prefer | 24 | 0.917 | 314 |
| Surfboard-tg-mixed | 0.772 | prefer | 212 | 0.693 | 7133 |
| mheidari-all | 0.65 | observe | 91 | 0.571 | 16459 |
| DeltaKronecker-all | 0.385 | observe | 8 | 0.5 | 6092 |
| tg-oneclickvpnkeys | 0.315 | observe | 2 | 1.0 | 103 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7577 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9286 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Pawdroid | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.0 | 0 | 3 | 3 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.5 | 4 | 4 | 8 |
| mheidari-all | 0.571 | 52 | 39 | 91 |
| Surfboard-tg-mixed | 0.693 | 147 | 65 | 212 |
| ermaozi | 0.917 | 22 | 2 | 24 |
| Au1rxx-base64 | 0.917 | 276 | 25 | 301 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16459 | yes | 3.45 | 0 |
| SoliSpirit-all | 9286 | yes | 1.59 | 0 |
| Epodonios-all | 7577 | yes | 2.24 | 0 |
| Surfboard-tg-mixed | 7133 | yes | 2.58 | 0 |
| DeltaKronecker-all | 6092 | yes | 3.51 | 0 |
| barry-far-vless | 5918 | yes | 0.65 | 0 |
| Surfboard-tg-vless | 5703 | yes | 2.93 | 0 |
| 10ium-ScrapeCategorize-Vless | 5238 | yes | 1.01 | 0 |
| mahdibland-V2RayAggregator | 4315 | yes | 0.51 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 0.71 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 54 |
| 204 | 42 |
| cn-block | 34 |
| speed | 12 |
