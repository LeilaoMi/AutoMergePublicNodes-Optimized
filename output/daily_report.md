# AutoNodes 每日报告

生成时间：2026-08-24 07:13:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 78696 |
| 去重后节点数 | 21962 |
| TCP 可达数 | 3000 |
| 真测通过数 | 715 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21962 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 35.0 |
| geo | 1.4 |
| probe | 61.2 |
| real_test | 169.3 |
| tcp | 34.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 21 | 20 | 1 | 95.2% |
| shadowsocks | 212 | 200 | 12 | 94.3% |
| socks | 5 | 2 | 3 | 40.0% |
| trojan | 79 | 66 | 13 | 83.5% |
| vless | 588 | 312 | 276 | 53.1% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 126 |
| geo:ClientOSError | 53 |
| speed:ClientOSError | 33 |
| speed:TimeoutError | 32 |
| 204:TimeoutError | 22 |
| cn-block:TimeoutError | 15 |
| 204:ProxyError | 12 |
| cn-block:ClientOSError | 11 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4435 |
| ConnectionRefusedError | 857 |
| gaierror | 430 |
| OSError | 22 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | prefer | 113 | 1.0 | 144 |
| Au1rxx-base64 | 0.97 | prefer | 382 | 0.903 | 1718 |
| mheidari-all | 0.922 | prefer | 36 | 0.861 | 14629 |
| Surfboard-tg-mixed | 0.844 | prefer | 155 | 0.768 | 6484 |
| DeltaKronecker-all | 0.4 | observe | 329 | 0.319 | 5914 |
| nscl5-all | 0.309 | observe | 3 | 0.667 | 1008 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4899 |
| Epodonios-all | 0.255 | observe | 0 | None | 6867 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7231 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.319 | 105 | 224 | 329 |
| nscl5-all | 0.667 | 2 | 1 | 3 |
| Surfboard-tg-mixed | 0.768 | 119 | 36 | 155 |
| mheidari-all | 0.861 | 31 | 5 | 36 |
| Au1rxx-base64 | 0.903 | 345 | 37 | 382 |
| zhangkai | 1.0 | 113 | 0 | 113 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14629 | yes | 4.41 | 0 |
| SoliSpirit-all | 7231 | yes | 3.55 | 0 |
| Epodonios-all | 6867 | yes | 4.65 | 0 |
| Surfboard-tg-mixed | 6484 | yes | 0.29 | 0 |
| DeltaKronecker-all | 5914 | yes | 4.77 | 0 |
| barry-far-vless | 5530 | yes | 2.07 | 0 |
| Surfboard-tg-vless | 5385 | yes | 3.53 | 0 |
| 10ium-ScrapeCategorize-Vless | 4899 | yes | 2.4 | 0 |
| mahdibland-V2RayAggregator | 4097 | yes | 1.73 | 0 |
| MatinGhanbari-all-sub | 3988 | yes | 2.15 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 179 |
| speed | 65 |
| 204 | 34 |
| cn-block | 27 |
