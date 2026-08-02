# AutoNodes 每日报告

生成时间：2026-08-02 13:45:10

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 78156 |
| 去重后节点数 | 22890 |
| TCP 可达数 | 3000 |
| 真测通过数 | 673 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22890 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 40.8 |
| geo | 1.4 |
| probe | 60.0 |
| real_test | 160.4 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 143 | 143 | 0 | 100.0% |
| hysteria2 | 23 | 18 | 5 | 78.3% |
| shadowsocks | 145 | 109 | 36 | 75.2% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 28 | 24 | 4 | 85.7% |
| vless | 604 | 375 | 229 | 62.1% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 100 |
| speed:TimeoutError | 48 |
| 204:TimeoutError | 37 |
| cn-block:TimeoutError | 24 |
| speed:ClientOSError | 23 |
| geo:ClientOSError | 17 |
| 204:ProxyError | 13 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |
| geo:parse | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4652 |
| ConnectionRefusedError | 790 |
| gaierror | 282 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 1.0 | prefer | 143 | 1.0 | 344 |
| Au1rxx-base64 | 0.797 | prefer | 555 | 0.732 | 1667 |
| Surfboard-tg-mixed | 0.66 | observe | 117 | 0.581 | 5249 |
| DeltaKronecker-all | 0.488 | observe | 123 | 0.407 | 4549 |
| mheidari-all | 0.373 | observe | 5 | 0.6 | 16891 |
| xiaoji235-airport-v2ray-all | 0.282 | observe | 2 | 0.5 | 1861 |
| nscl5-all | 0.262 | observe | 2 | 0.5 | 1354 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 57 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5486 |
| Epodonios-all | 0.255 | observe | 0 | None | 5857 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.407 | 50 | 73 | 123 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.581 | 68 | 49 | 117 |
| mheidari-all | 0.6 | 3 | 2 | 5 |
| Au1rxx-base64 | 0.732 | 406 | 149 | 555 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 143 | 0 | 143 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16891 | yes | 5.55 | 0 |
| SoliSpirit-all | 6807 | yes | 3.85 | 0 |
| Epodonios-all | 5857 | yes | 3.33 | 0 |
| 10ium-ScrapeCategorize-Vless | 5486 | yes | 2.7 | 0 |
| Surfboard-tg-mixed | 5249 | yes | 4.59 | 0 |
| mahdibland-V2RayAggregator | 5071 | yes | 5.08 | 0 |
| DeltaKronecker-all | 4549 | yes | 4.72 | 0 |
| barry-far-vless | 4517 | yes | 3.12 | 0 |
| Surfboard-tg-vless | 4007 | yes | 4.98 | 0 |
| MatinGhanbari-all-sub | 3972 | yes | 3.25 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 118 |
| speed | 72 |
| 204 | 53 |
| cn-block | 33 |
