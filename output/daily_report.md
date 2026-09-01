# AutoNodes 每日报告

生成时间：2026-09-01 20:57:15

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 81580 |
| 去重后节点数 | 23552 |
| TCP 可达数 | 3000 |
| 真测通过数 | 646 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23552 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 41.7 |
| geo | 1.7 |
| probe | 87.2 |
| real_test | 134.7 |
| tcp | 38.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 23 | 0 | 100.0% |
| hysteria2 | 20 | 19 | 1 | 95.0% |
| shadowsocks | 149 | 134 | 15 | 89.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 32 | 26 | 6 | 81.2% |
| vless | 518 | 440 | 78 | 84.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 22 |
| cn-block:TimeoutError | 20 |
| cn-block:ClientOSError | 13 |
| geo:ClientOSError | 12 |
| 204:ProxyError | 11 |
| speed:ClientOSError | 7 |
| geo:TimeoutError | 4 |
| speed:TimeoutError | 4 |
| 204:ClientOSError | 3 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:42386: bind: address already in use | 1 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5113 |
| ConnectionRefusedError | 891 |
| gaierror | 318 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.977 | prefer | 413 | 0.91 | 1703 |
| zhangkai | 0.929 | prefer | 24 | 0.958 | 144 |
| mheidari-all | 0.875 | prefer | 130 | 0.8 | 15436 |
| Surfboard-tg-mixed | 0.86 | prefer | 166 | 0.783 | 6983 |
| DeltaKronecker-all | 0.784 | prefer | 14 | 0.929 | 7294 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4708 |
| Epodonios-all | 0.255 | observe | 0 | None | 7385 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7585 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5851 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.783 | 130 | 36 | 166 |
| mheidari-all | 0.8 | 104 | 26 | 130 |
| Au1rxx-base64 | 0.91 | 376 | 37 | 413 |
| DeltaKronecker-all | 0.929 | 13 | 1 | 14 |
| zhangkai | 0.958 | 23 | 1 | 24 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15436 | yes | 5.11 | 0 |
| SoliSpirit-all | 7585 | yes | 3.85 | 0 |
| Epodonios-all | 7385 | yes | 4.03 | 0 |
| DeltaKronecker-all | 7294 | yes | 4.18 | 0 |
| Surfboard-tg-mixed | 6983 | yes | 3.61 | 0 |
| barry-far-vless | 5987 | yes | 1.97 | 0 |
| Surfboard-tg-vless | 5851 | yes | 3.8 | 0 |
| 10ium-ScrapeCategorize-Vless | 4708 | yes | 1.78 | 0 |
| mahdibland-V2RayAggregator | 4159 | yes | 2.67 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.05 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 36 |
| cn-block | 34 |
| geo | 18 |
| speed | 12 |
| sing-box exited 1 | 1 |
