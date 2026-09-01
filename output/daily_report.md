# AutoNodes 每日报告

生成时间：2026-09-01 16:28:12

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83812 |
| 去重后节点数 | 24692 |
| TCP 可达数 | 3000 |
| 真测通过数 | 657 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24692 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 35.0 |
| geo | 1.4 |
| probe | 89.4 |
| real_test | 125.8 |
| tcp | 40.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 19 | 1 | 95.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 152 | 138 | 14 | 90.8% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 37 | 35 | 2 | 94.6% |
| vless | 538 | 459 | 79 | 85.3% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 19 |
| cn-block:ClientOSError | 16 |
| cn-block:TimeoutError | 15 |
| 204:ProxyError | 11 |
| 204:ProxyConnectionError | 10 |
| geo:ClientOSError | 9 |
| speed:ClientOSError | 6 |
| speed:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| geo:TimeoutError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5109 |
| ConnectionRefusedError | 982 |
| gaierror | 351 |
| OSError | 241 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 0.984 | prefer | 144 | 0.91 | 17557 |
| Au1rxx-base64 | 0.98 | prefer | 398 | 0.912 | 1760 |
| zhangkai | 0.875 | prefer | 21 | 0.905 | 144 |
| Surfboard-tg-mixed | 0.835 | prefer | 186 | 0.758 | 6964 |
| DeltaKronecker-all | 0.3 | observe | 5 | 0.4 | 7294 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4708 |
| Epodonios-all | 0.255 | observe | 0 | None | 7367 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7657 |

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
| DeltaKronecker-all | 0.4 | 2 | 3 | 5 |
| Surfboard-tg-mixed | 0.758 | 141 | 45 | 186 |
| zhangkai | 0.905 | 19 | 2 | 21 |
| mheidari-all | 0.91 | 131 | 13 | 144 |
| Au1rxx-base64 | 0.912 | 363 | 35 | 398 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17557 | yes | 4.67 | 0 |
| SoliSpirit-all | 7657 | yes | 4.45 | 0 |
| Epodonios-all | 7367 | yes | 1.72 | 0 |
| DeltaKronecker-all | 7294 | yes | 5.21 | 0 |
| Surfboard-tg-mixed | 6964 | yes | 3.9 | 0 |
| barry-far-vless | 6013 | yes | 3.16 | 0 |
| Surfboard-tg-vless | 5838 | yes | 5.21 | 0 |
| 10ium-ScrapeCategorize-Vless | 4708 | yes | 3.14 | 0 |
| mahdibland-V2RayAggregator | 4013 | yes | 0.55 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.24 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 43 |
| cn-block | 33 |
| geo | 13 |
| speed | 10 |
