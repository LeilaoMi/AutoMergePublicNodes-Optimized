# AutoNodes 每日报告

生成时间：2026-08-25 01:41:37

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 83410 |
| 去重后节点数 | 23892 |
| TCP 可达数 | 3000 |
| 真测通过数 | 787 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23892 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.3 |
| generate | 26.5 |
| geo | 1.5 |
| probe | 59.2 |
| real_test | 180.4 |
| tcp | 38.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 23 | 23 | 0 | 100.0% |
| shadowsocks | 224 | 209 | 15 | 93.3% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 57 | 40 | 17 | 70.2% |
| vless | 979 | 489 | 490 | 49.9% |
| vmess | 4 | 3 | 1 | 75.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 223 |
| speed:TimeoutError | 99 |
| geo:ClientOSError | 97 |
| speed:ClientOSError | 59 |
| cn-block:ClientOSError | 13 |
| 204:TimeoutError | 12 |
| cn-block:TimeoutError | 9 |
| 204:ProxyError | 5 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| speed:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:33184: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5347 |
| ConnectionRefusedError | 892 |
| gaierror | 262 |
| OSError | 230 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.979 | prefer | 87 | 0.908 | 6540 |
| Au1rxx-base64 | 0.975 | prefer | 471 | 0.909 | 1713 |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| mheidari-all | 0.436 | observe | 669 | 0.356 | 19487 |
| DeltaKronecker-all | 0.397 | observe | 58 | 0.31 | 5914 |
| ninja-vless | 0.279 | observe | 2 | 0.5 | 1791 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4899 |
| Epodonios-all | 0.255 | observe | 0 | None | 7074 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3989 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.31 | 18 | 40 | 58 |
| mheidari-all | 0.356 | 238 | 431 | 669 |
| ninja-vless | 0.5 | 1 | 1 | 2 |
| Surfboard-tg-mixed | 0.908 | 79 | 8 | 87 |
| Au1rxx-base64 | 0.909 | 428 | 43 | 471 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19487 | yes | 4.08 | 0 |
| Epodonios-all | 7074 | yes | 4.33 | 0 |
| SoliSpirit-all | 7047 | yes | 3.81 | 0 |
| Surfboard-tg-mixed | 6540 | yes | 3.62 | 0 |
| DeltaKronecker-all | 5914 | yes | 4.34 | 0 |
| barry-far-vless | 5640 | yes | 0.5 | 0 |
| Surfboard-tg-vless | 5352 | yes | 3.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 4899 | yes | 0.68 | 0 |
| mahdibland-V2RayAggregator | 4132 | yes | 2.55 | 0 |
| MatinGhanbari-all-sub | 3989 | yes | 0.75 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 320 |
| speed | 160 |
| cn-block | 24 |
| 204 | 19 |
| sing-box exited 1 | 1 |
