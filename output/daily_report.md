# AutoNodes 每日报告

生成时间：2026-06-24 09:45:39

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76985 |
| 去重后节点数 | 22299 |
| TCP 可达数 | 3000 |
| 真测通过数 | 414 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22299 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.7 |
| generate | 43.1 |
| geo | 1.4 |
| probe | 57.6 |
| real_test | 124.3 |
| tcp | 29.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 50 | 50 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 134 | 114 | 20 | 85.1% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 130 | 72 | 58 | 55.4% |
| vless | 328 | 171 | 157 | 52.1% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 70 |
| 204:TimeoutError | 34 |
| geo:TimeoutError | 26 |
| cn-block:TimeoutError | 24 |
| 204:ProxyError | 21 |
| 204:ClientOSError | 16 |
| geo:ClientOSError | 14 |
| cn-block:ProxyError | 7 |
| cn-block:ClientOSError | 7 |
| speed:TimeoutError | 7 |
| geo:ProxyError | 6 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4146 |
| ConnectionRefusedError | 620 |
| gaierror | 160 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | prefer | 50 | 1.0 | 73 |
| Surfboard-tg-mixed | 0.778 | prefer | 243 | 0.7 | 5405 |
| Au1rxx-base64 | 0.766 | prefer | 65 | 0.769 | 117 |
| mheidari-all | 0.622 | observe | 164 | 0.543 | 15611 |
| DeltaKronecker-all | 0.504 | observe | 123 | 0.423 | 6644 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1140 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4745 |
| Epodonios-all | 0.255 | observe | 0 | None | 8238 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3980 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 10 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.423 | 52 | 71 | 123 |
| mheidari-all | 0.543 | 89 | 75 | 164 |
| Surfboard-tg-mixed | 0.7 | 170 | 73 | 243 |
| Au1rxx-base64 | 0.769 | 50 | 15 | 65 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 50 | 0 | 50 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15611 | yes | 2.58 | 0 |
| Epodonios-all | 8238 | yes | 1.3 | 0 |
| SoliSpirit-all | 7317 | yes | 2.08 | 0 |
| DeltaKronecker-all | 6644 | yes | 2.78 | 0 |
| Surfboard-tg-mixed | 5405 | yes | 1.64 | 0 |
| barry-far-vless | 4922 | yes | 1.01 | 0 |
| 10ium-ScrapeCategorize-Vless | 4745 | yes | 0.89 | 0 |
| mahdibland-V2RayAggregator | 4710 | yes | 1.1 | 0 |
| Surfboard-tg-vless | 4121 | yes | 1.77 | 0 |
| MatinGhanbari-all-sub | 3980 | yes | 1.06 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 80 |
| 204 | 71 |
| geo | 46 |
| cn-block | 38 |
