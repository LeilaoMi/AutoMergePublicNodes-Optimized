# AutoNodes 每日报告

生成时间：2026-08-10 07:54:44

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 87298 |
| 去重后节点数 | 24723 |
| TCP 可达数 | 3000 |
| 真测通过数 | 470 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24723 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.7 |
| generate | 27.2 |
| geo | 1.3 |
| probe | 55.4 |
| real_test | 109.6 |
| tcp | 35.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 20 | 20 | 0 | 100.0% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 150 | 144 | 6 | 96.0% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 143 | 121 | 22 | 84.6% |
| vless | 273 | 161 | 112 | 59.0% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 40 |
| geo:TimeoutError | 28 |
| 204:TimeoutError | 14 |
| cn-block:TimeoutError | 14 |
| speed:ClientOSError | 13 |
| 204:ProxyError | 13 |
| geo:ClientOSError | 12 |
| 204:ClientOSError | 6 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4268 |
| ConnectionRefusedError | 820 |
| gaierror | 364 |
| OSError | 231 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.956 | prefer | 20 | 1.0 | 25 |
| Au1rxx-base64 | 0.908 | prefer | 436 | 0.839 | 1742 |
| Surfboard-tg-mixed | 0.733 | prefer | 99 | 0.657 | 6647 |
| DeltaKronecker-all | 0.424 | observe | 30 | 0.333 | 5881 |
| mheidari-all | 0.413 | observe | 25 | 0.32 | 20373 |
| nscl5-all | 0.313 | observe | 1 | 1.0 | 1442 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7338 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3994 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7807 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| mheidari-all | 0.32 | 8 | 17 | 25 |
| DeltaKronecker-all | 0.333 | 10 | 20 | 30 |
| Surfboard-tg-mixed | 0.657 | 65 | 34 | 99 |
| Au1rxx-base64 | 0.839 | 366 | 70 | 436 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 20 | 0 | 20 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 20373 | yes | 3.58 | 0 |
| SoliSpirit-all | 7807 | yes | 2.1 | 0 |
| Epodonios-all | 7338 | yes | 1.86 | 0 |
| Surfboard-tg-mixed | 6647 | yes | 2.82 | 0 |
| DeltaKronecker-all | 5881 | yes | 3.11 | 0 |
| barry-far-vless | 5713 | yes | 1.57 | 0 |
| Surfboard-tg-vless | 5394 | yes | 2.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 5327 | yes | 1.37 | 0 |
| mahdibland-V2RayAggregator | 5191 | yes | 2.02 | 0 |
| MatinGhanbari-all-sub | 3994 | yes | 1.43 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 53 |
| geo | 41 |
| 204 | 33 |
| cn-block | 17 |
