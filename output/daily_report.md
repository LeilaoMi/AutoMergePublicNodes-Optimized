# AutoNodes 每日报告

生成时间：2026-06-25 20:13:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 82829 |
| 去重后节点数 | 22935 |
| TCP 可达数 | 3000 |
| 真测通过数 | 287 |
| verified 输出数 | 287 |
| global 输出数 | 293 |
| all 输出数 | 22935 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 42.4 |
| geo | 1.3 |
| probe | 60.6 |
| real_test | 97.4 |
| tcp | 30.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 2 | 1 | 66.7% |
| shadowsocks | 103 | 80 | 23 | 77.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 87 | 34 | 53 | 39.1% |
| vless | 204 | 129 | 75 | 63.2% |
| vmess | 5 | 5 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 45 |
| 204:TimeoutError | 32 |
| 204:ProxyError | 21 |
| 204:ClientOSError | 13 |
| cn-block:TimeoutError | 12 |
| geo:TimeoutError | 11 |
| speed:TimeoutError | 7 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| geo:ClientOSError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4236 |
| ConnectionRefusedError | 703 |
| gaierror | 201 |
| OSError | 112 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Au1rxx-base64 | 0.82 | prefer | 47 | 0.83 | 104 |
| Surfboard-tg-mixed | 0.785 | prefer | 181 | 0.707 | 5178 |
| mheidari-all | 0.588 | observe | 120 | 0.508 | 16098 |
| DeltaKronecker-all | 0.487 | observe | 52 | 0.404 | 12590 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4787 |
| Epodonios-all | 0.255 | observe | 0 | None | 7883 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7637 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 7 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.404 | 21 | 31 | 52 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.508 | 61 | 59 | 120 |
| Surfboard-tg-mixed | 0.707 | 128 | 53 | 181 |
| Au1rxx-base64 | 0.83 | 39 | 8 | 47 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16098 | yes | 3.55 | 0 |
| DeltaKronecker-all | 12590 | yes | 3.86 | 0 |
| Epodonios-all | 7883 | yes | 2.31 | 0 |
| SoliSpirit-all | 7637 | yes | 2.42 | 0 |
| Surfboard-tg-mixed | 5178 | yes | 2.51 | 0 |
| mahdibland-V2RayAggregator | 5117 | yes | 1.81 | 0 |
| 10ium-ScrapeCategorize-Vless | 4787 | yes | 1.5 | 0 |
| barry-far-vless | 4620 | yes | 1.28 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.59 | 0 |
| Surfboard-tg-vless | 3800 | yes | 1.64 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 66 |
| speed | 53 |
| cn-block | 19 |
| geo | 14 |
