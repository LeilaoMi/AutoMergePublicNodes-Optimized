# AutoNodes 每日报告

生成时间：2026-08-17 07:11:47

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 101/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 82922 |
| 去重后节点数 | 23092 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1340 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23092 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 31.4 |
| geo | 1.2 |
| probe | 67.9 |
| real_test | 229.6 |
| tcp | 34.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 128 | 128 | 0 | 100.0% |
| hysteria2 | 25 | 23 | 2 | 92.0% |
| shadowsocks | 125 | 116 | 9 | 92.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 780 | 756 | 24 | 96.9% |
| vless | 453 | 314 | 139 | 69.3% |
| vmess | 2 | 1 | 1 | 50.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 50 |
| cn-block:TimeoutError | 26 |
| 204:TimeoutError | 24 |
| speed:TimeoutError | 21 |
| geo:ClientOSError | 19 |
| speed:ClientOSError | 16 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4263 |
| ConnectionRefusedError | 818 |
| gaierror | 343 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 867 | 0.942 | 1991 |
| mheidari-all | 1.0 | prefer | 246 | 0.959 | 17400 |
| zhangkai | 0.999 | prefer | 127 | 1.0 | 159 |
| Surfboard-tg-mixed | 0.767 | prefer | 215 | 0.688 | 5925 |
| nscl5-all | 0.335 | observe | 1 | 1.0 | 3043 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 164 |
| Au1rxx-clash | 0.255 | observe | 0 | None | 1991 |
| Epodonios-all | 0.255 | observe | 0 | None | 6602 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.161 | 9 | 47 | 56 |
| Surfboard-tg-mixed | 0.688 | 148 | 67 | 215 |
| Au1rxx-base64 | 0.942 | 817 | 50 | 867 |
| mheidari-all | 0.959 | 236 | 10 | 246 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 127 | 0 | 127 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 17400 | yes | 3.63 | 0 |
| SoliSpirit-all | 7808 | yes | 2.23 | 0 |
| Epodonios-all | 6602 | yes | 3.83 | 0 |
| DeltaKronecker-all | 6368 | yes | 3.78 | 0 |
| Surfboard-tg-mixed | 5925 | yes | 2.61 | 0 |
| 10ium-ScrapeCategorize-Vless | 5085 | yes | 1.94 | 0 |
| barry-far-vless | 4931 | yes | 1.72 | 0 |
| Surfboard-tg-vless | 4592 | yes | 2.43 | 0 |
| mahdibland-V2RayAggregator | 4046 | yes | 2.12 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 2.03 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 69 |
| speed | 37 |
| cn-block | 35 |
| 204 | 35 |
