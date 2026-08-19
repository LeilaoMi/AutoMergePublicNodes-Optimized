# AutoNodes 每日报告

生成时间：2026-08-19 13:02:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82409 |
| 去重后节点数 | 22576 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1142 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22576 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 45.3 |
| geo | 1.1 |
| probe | 63.2 |
| real_test | 189.2 |
| tcp | 35.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 18 | 15 | 3 | 83.3% |
| shadowsocks | 133 | 121 | 12 | 91.0% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 740 | 735 | 5 | 99.3% |
| vless | 216 | 156 | 60 | 72.2% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 13 |
| geo:ClientOSError | 11 |
| 204:ProxyError | 9 |
| cn-block:TimeoutError | 9 |
| geo:TimeoutError | 9 |
| speed:TimeoutError | 8 |
| speed:ClientOSError | 7 |
| 204:ClientOSError | 6 |
| cn-block:ClientOSError | 6 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4452 |
| ConnectionRefusedError | 874 |
| gaierror | 516 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 619 | 0.976 | 1765 |
| zhangkai | 0.997 | prefer | 112 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.954 | prefer | 173 | 0.879 | 6304 |
| mheidari-all | 0.946 | prefer | 312 | 0.869 | 16605 |
| nscl5-all | 0.349 | observe | 3 | 0.667 | 3330 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5067 |
| Epodonios-all | 0.255 | observe | 0 | None | 7081 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7049 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 4858 |

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
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.25 | 1 | 3 | 4 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| mheidari-all | 0.869 | 271 | 41 | 312 |
| Surfboard-tg-mixed | 0.879 | 152 | 21 | 173 |
| Au1rxx-base64 | 0.976 | 604 | 15 | 619 |
| zhangkai | 1.0 | 112 | 0 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16605 | yes | 3.4 | 0 |
| Epodonios-all | 7081 | yes | 0.23 | 0 |
| SoliSpirit-all | 7049 | yes | 2.2 | 0 |
| DeltaKronecker-all | 6390 | yes | 3.47 | 0 |
| Surfboard-tg-mixed | 6304 | yes | 2.9 | 0 |
| barry-far-vless | 5240 | yes | 1.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 5067 | yes | 1.78 | 0 |
| Surfboard-tg-vless | 4858 | yes | 2.22 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.86 | 0 |
| mahdibland-V2RayAggregator | 3995 | yes | 0.29 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 28 |
| geo | 21 |
| cn-block | 17 |
| speed | 16 |
