# AutoNodes 每日报告

生成时间：2026-06-27 04:02:30

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 75900 |
| 去重后节点数 | 22867 |
| TCP 可达数 | 3000 |
| 真测通过数 | 515 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22867 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.8 |
| generate | 38.2 |
| geo | 1.4 |
| probe | 52.0 |
| real_test | 108.5 |
| tcp | 30.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 18 | 18 | 0 | 100.0% |
| hysteria2 | 5 | 3 | 2 | 60.0% |
| shadowsocks | 132 | 117 | 15 | 88.6% |
| socks | 24 | 23 | 1 | 95.8% |
| trojan | 154 | 134 | 20 | 87.0% |
| vless | 489 | 217 | 272 | 44.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 131 |
| geo:TimeoutError | 103 |
| geo:ClientOSError | 31 |
| cn-block:TimeoutError | 12 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 7 |
| speed:TimeoutError | 6 |
| 204:TimeoutError | 5 |
| 204:ProxyError | 5 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4404 |
| ConnectionRefusedError | 637 |
| gaierror | 153 |
| OSError | 139 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.92 | prefer | 330 | 0.842 | 5149 |
| snakem982 | 0.89 | prefer | 18 | 1.0 | 39 |
| mheidari-all | 0.742 | prefer | 193 | 0.663 | 16221 |
| Au1rxx-base64 | 0.663 | observe | 42 | 0.667 | 101 |
| nscl5-all | 0.359 | observe | 2 | 1.0 | 1186 |
| DeltaKronecker-all | 0.343 | observe | 234 | 0.261 | 6283 |
| Epodonios-all | 0.255 | observe | 0 | None | 7720 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3980 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7047 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3785 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.147 | observe | 2 | 0.0 | 0 | 1084 |
| 10ium-ScrapeCategorize-Vless | 0.16 | observe | 4 | 0.0 | 0 | 4567 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 2 | 2 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.261 | 61 | 173 | 234 |
| mheidari-all | 0.663 | 128 | 65 | 193 |
| Au1rxx-base64 | 0.667 | 28 | 14 | 42 |
| Surfboard-tg-mixed | 0.842 | 278 | 52 | 330 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 18 | 0 | 18 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16221 | yes | 3.66 | 0 |
| Epodonios-all | 7720 | yes | 1.94 | 0 |
| SoliSpirit-all | 7047 | yes | 1.91 | 0 |
| DeltaKronecker-all | 6283 | yes | 3.8 | 0 |
| mahdibland-V2RayAggregator | 5248 | yes | 2.03 | 0 |
| Surfboard-tg-mixed | 5149 | yes | 3.2 | 0 |
| 10ium-ScrapeCategorize-Vless | 4567 | yes | 1.36 | 0 |
| barry-far-vless | 4565 | yes | 1.54 | 0 |
| MatinGhanbari-all-sub | 3980 | yes | 1.63 | 0 |
| Surfboard-tg-vless | 3785 | yes | 2.24 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 137 |
| geo | 134 |
| cn-block | 22 |
| 204 | 17 |
