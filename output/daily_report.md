# AutoNodes 每日报告

生成时间：2026-08-26 01:47:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 79196 |
| 去重后节点数 | 22570 |
| TCP 可达数 | 3000 |
| 真测通过数 | 550 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22570 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.2 |
| generate | 43.2 |
| geo | 1.4 |
| probe | 78.0 |
| real_test | 195.1 |
| tcp | 36.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 29 | 29 | 0 | 100.0% |
| shadowsocks | 204 | 194 | 10 | 95.1% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 69 | 53 | 16 | 76.8% |
| vless | 886 | 245 | 641 | 27.7% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 392 |
| speed:ClientOSError | 115 |
| geo:ClientOSError | 72 |
| speed:TimeoutError | 37 |
| cn-block:TimeoutError | 16 |
| 204:ProxyError | 12 |
| 204:TimeoutError | 12 |
| geo:ProxyError | 4 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4704 |
| ConnectionRefusedError | 883 |
| gaierror | 390 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 115 | 0.983 | 1944 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.873 | prefer | 114 | 0.798 | 6470 |
| mheidari-all | 0.856 | prefer | 47 | 0.787 | 14587 |
| DeltaKronecker-all | 0.391 | observe | 912 | 0.31 | 6340 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 191 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4912 |
| Epodonios-all | 0.255 | observe | 0 | None | 7017 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3987 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.31 | 283 | 629 | 912 |
| mheidari-all | 0.787 | 37 | 10 | 47 |
| Surfboard-tg-mixed | 0.798 | 91 | 23 | 114 |
| Au1rxx-base64 | 0.983 | 113 | 2 | 115 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14587 | yes | 5.16 | 0 |
| SoliSpirit-all | 7048 | yes | 3.74 | 0 |
| Epodonios-all | 7017 | yes | 3.42 | 0 |
| Surfboard-tg-mixed | 6470 | yes | 3.77 | 0 |
| DeltaKronecker-all | 6340 | yes | 5.29 | 0 |
| barry-far-vless | 5579 | yes | 3.05 | 0 |
| Surfboard-tg-vless | 5307 | yes | 3.99 | 0 |
| 10ium-ScrapeCategorize-Vless | 4912 | yes | 3.13 | 0 |
| mahdibland-V2RayAggregator | 4119 | yes | 3.16 | 0 |
| MatinGhanbari-all-sub | 3987 | yes | 2.86 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 468 |
| speed | 152 |
| 204 | 27 |
| cn-block | 21 |
