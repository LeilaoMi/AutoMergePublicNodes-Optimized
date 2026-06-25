# AutoNodes 每日报告

生成时间：2026-06-25 14:51:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83018 |
| 去重后节点数 | 23108 |
| TCP 可达数 | 3000 |
| 真测通过数 | 375 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23108 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 30.0 |
| geo | 1.4 |
| probe | 53.5 |
| real_test | 94.1 |
| tcp | 31.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 127 | 102 | 25 | 80.3% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 107 | 63 | 44 | 58.9% |
| vless | 269 | 166 | 103 | 61.7% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 75 |
| 204:TimeoutError | 28 |
| 204:ClientOSError | 16 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 8 |
| cn-block:TimeoutError | 8 |
| cn-block:ProxyError | 8 |
| geo:TimeoutError | 7 |
| speed:TimeoutError | 4 |
| speed:ProxyError | 3 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4469 |
| ConnectionRefusedError | 622 |
| OSError | 111 |
| gaierror | 109 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Au1rxx-base64 | 0.841 | prefer | 47 | 0.851 | 101 |
| Surfboard-tg-mixed | 0.778 | prefer | 240 | 0.7 | 5257 |
| mheidari-all | 0.673 | observe | 170 | 0.594 | 16105 |
| DeltaKronecker-all | 0.617 | observe | 52 | 0.538 | 12590 |
| nscl5-all | 0.3 | observe | 1 | 1.0 | 1136 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4787 |
| Epodonios-all | 0.255 | observe | 0 | None | 7910 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3977 |

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
| DeltaKronecker-all | 0.538 | 28 | 24 | 52 |
| mheidari-all | 0.594 | 101 | 69 | 170 |
| Surfboard-tg-mixed | 0.7 | 168 | 72 | 240 |
| Au1rxx-base64 | 0.851 | 40 | 7 | 47 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16105 | yes | 3.95 | 0 |
| DeltaKronecker-all | 12590 | yes | 4.42 | 0 |
| Epodonios-all | 7910 | yes | 2.51 | 0 |
| SoliSpirit-all | 7492 | yes | 2.34 | 0 |
| Surfboard-tg-mixed | 5257 | yes | 2.7 | 0 |
| mahdibland-V2RayAggregator | 5133 | yes | 1.79 | 0 |
| 10ium-ScrapeCategorize-Vless | 4787 | yes | 1.1 | 0 |
| barry-far-vless | 4673 | yes | 1.89 | 0 |
| MatinGhanbari-all-sub | 3977 | yes | 1.99 | 0 |
| Surfboard-tg-vless | 3824 | yes | 2.84 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 82 |
| 204 | 56 |
| cn-block | 24 |
| geo | 10 |
