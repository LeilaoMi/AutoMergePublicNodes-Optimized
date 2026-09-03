# AutoNodes 每日报告

生成时间：2026-09-03 11:03:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82567 |
| 去重后节点数 | 22929 |
| TCP 可达数 | 3000 |
| 真测通过数 | 553 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22929 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.0 |
| generate | 38.0 |
| geo | 1.5 |
| probe | 89.6 |
| real_test | 126.3 |
| tcp | 37.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 22 | 1 | 95.7% |
| hysteria2 | 12 | 11 | 1 | 91.7% |
| shadowsocks | 159 | 149 | 10 | 93.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 35 | 30 | 5 | 85.7% |
| vless | 427 | 337 | 90 | 78.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 22 |
| 204:TimeoutError | 20 |
| geo:ClientOSError | 19 |
| speed:TimeoutError | 13 |
| 204:ProxyError | 9 |
| geo:TimeoutError | 5 |
| speed:ClientOSError | 5 |
| 204:ProxyConnectionError | 4 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5216 |
| ConnectionRefusedError | 908 |
| gaierror | 317 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.976 | prefer | 329 | 0.909 | 1751 |
| zhangkai | 0.922 | prefer | 22 | 0.955 | 144 |
| mheidari-all | 0.84 | prefer | 123 | 0.764 | 16145 |
| Surfboard-tg-mixed | 0.82 | prefer | 171 | 0.743 | 7139 |
| DeltaKronecker-all | 0.684 | observe | 14 | 0.786 | 6335 |
| tg-oneclickvpnkeys | 0.258 | observe | 1 | 1.0 | 87 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4671 |
| Epodonios-all | 0.255 | observe | 0 | None | 7527 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8132 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.743 | 127 | 44 | 171 |
| mheidari-all | 0.764 | 94 | 29 | 123 |
| DeltaKronecker-all | 0.786 | 11 | 3 | 14 |
| Au1rxx-base64 | 0.909 | 299 | 30 | 329 |
| zhangkai | 0.955 | 21 | 1 | 22 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16145 | yes | 4.7 | 0 |
| SoliSpirit-all | 8132 | yes | 3.21 | 0 |
| Epodonios-all | 7527 | yes | 3.03 | 0 |
| Surfboard-tg-mixed | 7139 | yes | 3.3 | 0 |
| DeltaKronecker-all | 6335 | yes | 4.36 | 0 |
| barry-far-vless | 6217 | yes | 2.74 | 0 |
| Surfboard-tg-vless | 6006 | yes | 4.01 | 0 |
| 10ium-ScrapeCategorize-Vless | 4671 | yes | 2.44 | 0 |
| mahdibland-V2RayAggregator | 4081 | yes | 2.64 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.55 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 36 |
| cn-block | 28 |
| geo | 25 |
| speed | 20 |
