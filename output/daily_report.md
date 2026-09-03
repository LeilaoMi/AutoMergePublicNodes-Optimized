# AutoNodes 每日报告

生成时间：2026-09-03 16:16:16

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 82139 |
| 去重后节点数 | 22600 |
| TCP 可达数 | 3000 |
| 真测通过数 | 554 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22600 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 41.4 |
| geo | 1.6 |
| probe | 84.5 |
| real_test | 112.2 |
| tcp | 36.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 23 | 22 | 1 | 95.7% |
| hysteria2 | 22 | 21 | 1 | 95.5% |
| shadowsocks | 152 | 145 | 7 | 95.4% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 27 | 22 | 5 | 81.5% |
| vless | 406 | 339 | 67 | 83.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 17 |
| geo:ClientOSError | 16 |
| 204:TimeoutError | 16 |
| 204:ProxyError | 9 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 4 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| 204:ProxyConnectionError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4629 |
| ConnectionRefusedError | 929 |
| gaierror | 352 |
| OSError | 28 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 334 | 0.946 | 1770 |
| zhangkai | 0.915 | prefer | 20 | 0.95 | 144 |
| mheidari-all | 0.893 | prefer | 105 | 0.819 | 15770 |
| DeltaKronecker-all | 0.875 | prefer | 18 | 0.889 | 6335 |
| Surfboard-tg-mixed | 0.807 | prefer | 152 | 0.73 | 7139 |
| tg-oneclickvpnkeys | 0.406 | observe | 4 | 1.0 | 145 |
| SoliSpirit-all | 0.335 | observe | 1 | 1.0 | 7991 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4671 |
| Epodonios-all | 0.255 | observe | 0 | None | 7586 |

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
| Surfboard-tg-mixed | 0.73 | 111 | 41 | 152 |
| mheidari-all | 0.819 | 86 | 19 | 105 |
| DeltaKronecker-all | 0.889 | 16 | 2 | 18 |
| Au1rxx-base64 | 0.946 | 316 | 18 | 334 |
| zhangkai | 0.95 | 19 | 1 | 20 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| SoliSpirit-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15770 | yes | 5.21 | 0 |
| SoliSpirit-all | 7991 | yes | 4.32 | 0 |
| Epodonios-all | 7586 | yes | 3.32 | 0 |
| Surfboard-tg-mixed | 7139 | yes | 3.67 | 0 |
| DeltaKronecker-all | 6335 | yes | 4.98 | 0 |
| barry-far-vless | 6219 | yes | 1.79 | 0 |
| Surfboard-tg-vless | 6006 | yes | 4.44 | 0 |
| 10ium-ScrapeCategorize-Vless | 4671 | yes | 3.42 | 0 |
| mahdibland-V2RayAggregator | 4081 | yes | 3.39 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.55 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 29 |
| cn-block | 22 |
| geo | 18 |
| speed | 13 |
