# AutoNodes 每日报告

生成时间：2026-06-24 14:48:25

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 77241 |
| 去重后节点数 | 22530 |
| TCP 可达数 | 3000 |
| 真测通过数 | 457 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22530 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 38.2 |
| geo | 1.5 |
| probe | 60.7 |
| real_test | 126.2 |
| tcp | 29.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 50 | 50 | 0 | 100.0% |
| hysteria2 | 3 | 2 | 1 | 66.7% |
| shadowsocks | 137 | 119 | 18 | 86.9% |
| trojan | 142 | 100 | 42 | 70.4% |
| vless | 275 | 182 | 93 | 66.2% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 60 |
| cn-block:TimeoutError | 23 |
| 204:TimeoutError | 21 |
| 204:ProxyError | 9 |
| cn-block:ClientOSError | 8 |
| geo:TimeoutError | 8 |
| geo:ClientOSError | 7 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 3 |
| speed:ProxyError | 3 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4201 |
| ConnectionRefusedError | 609 |
| gaierror | 191 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.984 | prefer | 50 | 1.0 | 73 |
| Surfboard-tg-mixed | 0.821 | prefer | 264 | 0.742 | 5407 |
| Au1rxx-base64 | 0.805 | prefer | 63 | 0.81 | 114 |
| mheidari-all | 0.793 | prefer | 162 | 0.716 | 15574 |
| DeltaKronecker-all | 0.677 | observe | 70 | 0.6 | 6644 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4745 |
| Epodonios-all | 0.255 | observe | 0 | None | 8169 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3983 |

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
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 9 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.6 | 42 | 28 | 70 |
| mheidari-all | 0.716 | 116 | 46 | 162 |
| Surfboard-tg-mixed | 0.742 | 196 | 68 | 264 |
| Au1rxx-base64 | 0.81 | 51 | 12 | 63 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 50 | 0 | 50 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15574 | yes | 2.97 | 0 |
| Epodonios-all | 8169 | yes | 3.8 | 0 |
| SoliSpirit-all | 7672 | yes | 2.72 | 0 |
| DeltaKronecker-all | 6644 | yes | 4.35 | 0 |
| Surfboard-tg-mixed | 5407 | yes | 2.16 | 0 |
| barry-far-vless | 4921 | yes | 2.49 | 0 |
| 10ium-ScrapeCategorize-Vless | 4745 | yes | 1.49 | 0 |
| mahdibland-V2RayAggregator | 4710 | yes | 1.7 | 0 |
| Surfboard-tg-vless | 4121 | yes | 1.99 | 0 |
| MatinGhanbari-all-sub | 3983 | yes | 1.24 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 68 |
| 204 | 35 |
| cn-block | 33 |
| geo | 18 |
