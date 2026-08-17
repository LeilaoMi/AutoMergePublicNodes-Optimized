# AutoNodes 每日报告

生成时间：2026-08-17 18:54:04

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80814 |
| 去重后节点数 | 22843 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1404 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22843 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.8 |
| generate | 39.2 |
| geo | 0.9 |
| probe | 73.3 |
| real_test | 268.9 |
| tcp | 35.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 129 | 115 | 14 | 89.1% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 823 | 818 | 5 | 99.4% |
| tuic | 1 | 1 | 0 | 100.0% |
| vless | 444 | 321 | 123 | 72.3% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ClientOSError | 50 |
| cn-block:TimeoutError | 24 |
| 204:TimeoutError | 19 |
| 204:ProxyError | 11 |
| geo:TimeoutError | 10 |
| speed:ClientOSError | 10 |
| geo:ClientOSError | 6 |
| speed:TimeoutError | 6 |
| cn-block:ClientOSError | 5 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4680 |
| ConnectionRefusedError | 824 |
| gaierror | 371 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| mheidari-all | 1.0 | prefer | 303 | 0.99 | 15619 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Au1rxx-base64 | 0.97 | prefer | 960 | 0.892 | 1983 |
| Surfboard-tg-mixed | 0.861 | prefer | 149 | 0.785 | 6228 |
| DeltaKronecker-all | 0.324 | observe | 8 | 0.375 | 6368 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 192 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5085 |
| Epodonios-all | 0.255 | observe | 0 | None | 6789 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3984 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6707 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 12 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.375 | 3 | 5 | 8 |
| Surfboard-tg-mixed | 0.785 | 117 | 32 | 149 |
| Au1rxx-base64 | 0.892 | 856 | 104 | 960 |
| mheidari-all | 0.99 | 300 | 3 | 303 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15619 | yes | 4.01 | 0 |
| Epodonios-all | 6789 | yes | 6.45 | 0 |
| SoliSpirit-all | 6707 | yes | 4.7 | 0 |
| DeltaKronecker-all | 6368 | yes | 3.78 | 0 |
| Surfboard-tg-mixed | 6228 | yes | 3.57 | 0 |
| barry-far-vless | 5131 | yes | 2.96 | 0 |
| 10ium-ScrapeCategorize-Vless | 5085 | yes | 3.19 | 0 |
| Surfboard-tg-vless | 4903 | yes | 5.49 | 0 |
| mahdibland-V2RayAggregator | 4027 | yes | 2.8 | 0 |
| MatinGhanbari-all-sub | 3984 | yes | 3.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 80 |
| cn-block | 31 |
| geo | 17 |
| speed | 16 |
