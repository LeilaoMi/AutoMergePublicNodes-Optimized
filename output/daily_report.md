# AutoNodes 每日报告

生成时间：2026-08-31 13:19:54

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 79273 |
| 去重后节点数 | 22282 |
| TCP 可达数 | 3000 |
| 真测通过数 | 503 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22282 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 40.0 |
| geo | 1.5 |
| probe | 81.9 |
| real_test | 95.4 |
| tcp | 35.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 19 | 4 | 82.6% |
| hysteria2 | 19 | 16 | 3 | 84.2% |
| shadowsocks | 165 | 150 | 15 | 90.9% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 20 | 15 | 5 | 75.0% |
| vless | 349 | 298 | 51 | 85.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 19 |
| 204:TimeoutError | 18 |
| geo:ClientOSError | 11 |
| geo:TimeoutError | 10 |
| 204:ProxyConnectionError | 4 |
| 204:ClientOSError | 4 |
| 204:ProxyError | 4 |
| speed:ClientOSError | 3 |
| cn-block:ClientOSError | 2 |
| speed:TimeoutError | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4851 |
| ConnectionRefusedError | 907 |
| gaierror | 336 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 306 | 0.938 | 1804 |
| mheidari-all | 0.937 | prefer | 33 | 0.879 | 14620 |
| Surfboard-tg-mixed | 0.845 | prefer | 168 | 0.768 | 6828 |
| DeltaKronecker-all | 0.845 | prefer | 49 | 0.776 | 5904 |
| zhangkai | 0.806 | prefer | 23 | 0.826 | 144 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7174 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7956 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5768 |

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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.768 | 129 | 39 | 168 |
| DeltaKronecker-all | 0.776 | 38 | 11 | 49 |
| zhangkai | 0.826 | 19 | 4 | 23 |
| mheidari-all | 0.879 | 29 | 4 | 33 |
| Au1rxx-base64 | 0.938 | 287 | 19 | 306 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14620 | yes | 4.34 | 0 |
| SoliSpirit-all | 7956 | yes | 3.34 | 0 |
| Epodonios-all | 7174 | yes | 1.51 | 0 |
| Surfboard-tg-mixed | 6828 | yes | 3.93 | 0 |
| DeltaKronecker-all | 5904 | yes | 4.77 | 0 |
| barry-far-vless | 5864 | yes | 2.24 | 0 |
| Surfboard-tg-vless | 5768 | yes | 3.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4657 | yes | 2.47 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.3 | 0 |
| mahdibland-V2RayAggregator | 3987 | yes | 1.32 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| cn-block | 22 |
| geo | 21 |
| speed | 5 |
