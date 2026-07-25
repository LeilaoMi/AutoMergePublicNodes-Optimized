# AutoNodes 每日报告

生成时间：2026-07-25 03:22:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 80289 |
| 去重后节点数 | 22838 |
| TCP 可达数 | 3000 |
| 真测通过数 | 826 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22838 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| generate | 29.7 |
| geo | 1.3 |
| probe | 61.5 |
| real_test | 189.9 |
| tcp | 32.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 35 | 1 | 97.2% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 145 | 130 | 15 | 89.7% |
| socks | 14 | 9 | 5 | 64.3% |
| trojan | 481 | 460 | 21 | 95.6% |
| vless | 635 | 188 | 447 | 29.6% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 167 |
| speed:ClientOSError | 145 |
| speed:TimeoutError | 59 |
| geo:ClientOSError | 54 |
| cn-block:TimeoutError | 41 |
| cn-block:ClientOSError | 9 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 4 |
| 204:TimeoutError | 4 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4168 |
| ConnectionRefusedError | 706 |
| gaierror | 414 |
| OSError | 219 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.95 | prefer | 36 | 0.972 | 61 |
| Au1rxx-base64 | 0.924 | prefer | 138 | 0.913 | 432 |
| Surfboard-tg-mixed | 0.729 | prefer | 320 | 0.65 | 5472 |
| mheidari-all | 0.664 | observe | 734 | 0.584 | 19397 |
| DeltaKronecker-all | 0.406 | observe | 84 | 0.321 | 5559 |
| tg-ConfigV2rayNG | 0.263 | observe | 1 | 1.0 | 200 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4588 |
| Epodonios-all | 0.255 | observe | 0 | None | 6656 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3970 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6389 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.321 | 27 | 57 | 84 |
| mheidari-all | 0.584 | 429 | 305 | 734 |
| Surfboard-tg-mixed | 0.65 | 208 | 112 | 320 |
| Au1rxx-base64 | 0.913 | 126 | 12 | 138 |
| zhangkai | 0.972 | 35 | 1 | 36 |
| tg-ConfigV2rayNG | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19397 | yes | 3.1 | 0 |
| Epodonios-all | 6656 | yes | 3.33 | 0 |
| SoliSpirit-all | 6389 | yes | 3.56 | 0 |
| DeltaKronecker-all | 5559 | yes | 3.24 | 0 |
| Surfboard-tg-mixed | 5472 | yes | 1.75 | 0 |
| mahdibland-V2RayAggregator | 5027 | yes | 1.82 | 0 |
| barry-far-vless | 4847 | yes | 0.64 | 0 |
| 10ium-ScrapeCategorize-Vless | 4588 | yes | 2.01 | 0 |
| Surfboard-tg-vless | 4180 | yes | 2.39 | 0 |
| MatinGhanbari-all-sub | 3970 | yes | 0.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 221 |
| speed | 204 |
| cn-block | 50 |
| 204 | 14 |
