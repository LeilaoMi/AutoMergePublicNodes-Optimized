# AutoNodes 每日报告

生成时间：2026-09-01 04:36:34

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79985 |
| 去重后节点数 | 22309 |
| TCP 可达数 | 3000 |
| 真测通过数 | 640 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22309 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 34.1 |
| geo | 1.3 |
| probe | 73.8 |
| real_test | 123.0 |
| tcp | 35.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 18 | 17 | 1 | 94.4% |
| shadowsocks | 169 | 165 | 4 | 97.6% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 61 | 39 | 22 | 63.9% |
| vless | 526 | 391 | 135 | 74.3% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 47 |
| geo:ClientOSError | 30 |
| cn-block:TimeoutError | 19 |
| speed:TimeoutError | 16 |
| speed:ClientOSError | 15 |
| 204:TimeoutError | 14 |
| 204:ProxyError | 8 |
| cn-block:ClientOSError | 7 |
| geo:ProxyError | 3 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4921 |
| ConnectionRefusedError | 898 |
| gaierror | 301 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Au1rxx-base64 | 0.959 | prefer | 366 | 0.899 | 1549 |
| mheidari-all | 0.913 | prefer | 88 | 0.841 | 15162 |
| Surfboard-tg-mixed | 0.829 | prefer | 237 | 0.751 | 6997 |
| DeltaKronecker-all | 0.494 | observe | 85 | 0.412 | 5904 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4657 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7837 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5908 |

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
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.412 | 35 | 50 | 85 |
| Surfboard-tg-mixed | 0.751 | 178 | 59 | 237 |
| mheidari-all | 0.841 | 74 | 14 | 88 |
| Au1rxx-base64 | 0.899 | 329 | 37 | 366 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15162 | yes | 3.16 | 0 |
| SoliSpirit-all | 7837 | yes | 1.54 | 0 |
| Epodonios-all | 7436 | yes | 1.97 | 0 |
| Surfboard-tg-mixed | 6997 | yes | 2.86 | 0 |
| barry-far-vless | 6067 | yes | 0.8 | 0 |
| Surfboard-tg-vless | 5908 | yes | 2.3 | 0 |
| DeltaKronecker-all | 5904 | yes | 3.12 | 0 |
| 10ium-ScrapeCategorize-Vless | 4657 | yes | 0.63 | 0 |
| mahdibland-V2RayAggregator | 4025 | yes | 0.47 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 0.87 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 80 |
| speed | 31 |
| cn-block | 28 |
| 204 | 24 |
