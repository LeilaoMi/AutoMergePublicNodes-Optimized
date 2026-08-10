# AutoNodes 每日报告

生成时间：2026-08-10 13:24:35

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 3/103 |
| 原始节点数 | 86629 |
| 去重后节点数 | 24807 |
| TCP 可达数 | 3000 |
| 真测通过数 | 506 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24807 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.9 |
| generate | 28.8 |
| geo | 1.3 |
| probe | 55.8 |
| real_test | 121.5 |
| tcp | 36.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 53 | 53 | 0 | 100.0% |
| hysteria2 | 17 | 15 | 2 | 88.2% |
| shadowsocks | 153 | 135 | 18 | 88.2% |
| socks | 6 | 2 | 4 | 33.3% |
| trojan | 133 | 119 | 14 | 89.5% |
| vless | 239 | 180 | 59 | 75.3% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 19 |
| 204:TimeoutError | 18 |
| speed:TimeoutError | 15 |
| 204:ProxyError | 11 |
| geo:ClientOSError | 9 |
| geo:TimeoutError | 9 |
| speed:ClientOSError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4216 |
| ConnectionRefusedError | 860 |
| gaierror | 394 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.969 | prefer | 437 | 0.904 | 1668 |
| zhangkai | 0.964 | prefer | 50 | 0.98 | 67 |
| Surfboard-tg-mixed | 0.724 | prefer | 71 | 0.648 | 6388 |
| mheidari-all | 0.497 | observe | 22 | 0.409 | 20526 |
| tg-oneclickvpnkeys | 0.405 | observe | 4 | 1.0 | 122 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7165 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7747 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5219 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | DeltaKronecker-all | 0.222 | 17 | 0.118 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.118 | 2 | 15 | 17 |
| mheidari-all | 0.409 | 9 | 13 | 22 |
| Surfboard-tg-mixed | 0.648 | 46 | 25 | 71 |
| Au1rxx-base64 | 0.904 | 395 | 42 | 437 |
| zhangkai | 0.98 | 49 | 1 | 50 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20526 | yes | 3.41 | 0 |
| SoliSpirit-all | 7747 | yes | 1.14 | 0 |
| Epodonios-all | 7165 | yes | 1.97 | 0 |
| Surfboard-tg-mixed | 6388 | yes | 3.57 | 0 |
| DeltaKronecker-all | 5881 | yes | 3.5 | 0 |
| barry-far-vless | 5695 | yes | 0.9 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 0.69 | 0 |
| Surfboard-tg-vless | 5219 | yes | 2.35 | 0 |
| mahdibland-V2RayAggregator | 5191 | yes | 2.03 | 0 |
| MatinGhanbari-all-sub | 3996 | yes | 0.77 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 34 |
| cn-block | 24 |
| speed | 21 |
| geo | 18 |
