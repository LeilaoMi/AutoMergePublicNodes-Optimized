# AutoNodes 每日报告

生成时间：2026-07-31 03:35:07

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78323 |
| 去重后节点数 | 23088 |
| TCP 可达数 | 3000 |
| 真测通过数 | 582 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23088 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 33.2 |
| geo | 1.4 |
| probe | 65.2 |
| real_test | 160.4 |
| tcp | 33.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 113 | 113 | 0 | 100.0% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 154 | 146 | 8 | 94.8% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 54 | 47 | 7 | 87.0% |
| vless | 669 | 257 | 412 | 38.4% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 250 |
| speed:ClientOSError | 51 |
| geo:ClientOSError | 50 |
| speed:TimeoutError | 40 |
| 204:TimeoutError | 12 |
| cn-block:TimeoutError | 12 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 4 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4547 |
| ConnectionRefusedError | 756 |
| gaierror | 296 |
| OSError | 227 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.996 | prefer | 113 | 1.0 | 129 |
| Au1rxx-base64 | 0.968 | prefer | 240 | 0.921 | 1272 |
| Surfboard-tg-mixed | 0.753 | prefer | 148 | 0.676 | 5223 |
| mheidari-all | 0.418 | observe | 10 | 0.5 | 16264 |
| ninja-vless | 0.381 | observe | 13 | 0.385 | 1791 |
| DeltaKronecker-all | 0.365 | observe | 483 | 0.284 | 5759 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 43 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5342 |
| Epodonios-all | 0.255 | observe | 0 | None | 6141 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| 10ium-HighSpeed | 0.161 | observe | 1 | 0.0 | 0 | 839 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 5 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.284 | 137 | 346 | 483 |
| ninja-vless | 0.385 | 5 | 8 | 13 |
| mheidari-all | 0.5 | 5 | 5 | 10 |
| Surfboard-tg-mixed | 0.676 | 100 | 48 | 148 |
| Au1rxx-base64 | 0.921 | 221 | 19 | 240 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 113 | 0 | 113 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16264 | yes | 3.21 | 0 |
| SoliSpirit-all | 7041 | yes | 3.19 | 0 |
| Epodonios-all | 6141 | yes | 2.2 | 0 |
| DeltaKronecker-all | 5759 | yes | 3.54 | 0 |
| 10ium-ScrapeCategorize-Vless | 5342 | yes | 1.03 | 0 |
| Surfboard-tg-mixed | 5223 | yes | 2.69 | 0 |
| mahdibland-V2RayAggregator | 5047 | yes | 1.78 | 0 |
| barry-far-vless | 4647 | yes | 0.86 | 0 |
| Surfboard-tg-vless | 4144 | yes | 2.85 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.7 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 301 |
| speed | 91 |
| 204 | 18 |
| cn-block | 17 |
