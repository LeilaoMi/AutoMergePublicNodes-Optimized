# AutoNodes 每日报告

生成时间：2026-09-05 03:58:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 84346 |
| 去重后节点数 | 23686 |
| TCP 可达数 | 3000 |
| 真测通过数 | 647 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23686 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 37.1 |
| geo | 1.5 |
| probe | 87.9 |
| real_test | 143.4 |
| tcp | 39.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 29 | 27 | 2 | 93.1% |
| hysteria2 | 19 | 18 | 1 | 94.7% |
| shadowsocks | 174 | 170 | 4 | 97.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 85 | 57 | 28 | 67.1% |
| vless | 638 | 370 | 268 | 58.0% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 159 |
| geo:ClientOSError | 51 |
| speed:TimeoutError | 37 |
| speed:ClientOSError | 20 |
| 204:TimeoutError | 14 |
| cn-block:ClientOSError | 9 |
| cn-block:TimeoutError | 7 |
| 204:ProxyError | 4 |
| 204:ProxyConnectionError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5539 |
| ConnectionRefusedError | 890 |
| gaierror | 322 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.993 | prefer | 389 | 0.923 | 1796 |
| zhangkai | 0.881 | prefer | 22 | 0.909 | 144 |
| Surfboard-tg-mixed | 0.874 | prefer | 100 | 0.8 | 7291 |
| mheidari-all | 0.728 | prefer | 217 | 0.65 | 16194 |
| tg-oneclickvpnkeys | 0.554 | observe | 8 | 1.0 | 135 |
| DeltaKronecker-all | 0.269 | observe | 210 | 0.186 | 7089 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8350 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 6083 |
| barry-far-vless | 0.255 | observe | 0 | None | 6282 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.186 | 39 | 171 | 210 |
| mheidari-all | 0.65 | 141 | 76 | 217 |
| Surfboard-tg-mixed | 0.8 | 80 | 20 | 100 |
| zhangkai | 0.909 | 20 | 2 | 22 |
| Au1rxx-base64 | 0.923 | 359 | 30 | 389 |
| tg-oneclickvpnkeys | 1.0 | 8 | 0 | 8 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16194 | yes | 4.21 | 0 |
| SoliSpirit-all | 8350 | yes | 3.39 | 0 |
| Epodonios-all | 7727 | yes | 5.64 | 0 |
| Surfboard-tg-mixed | 7291 | yes | 3.43 | 0 |
| DeltaKronecker-all | 7089 | yes | 4.82 | 0 |
| barry-far-vless | 6282 | yes | 2.56 | 0 |
| Surfboard-tg-vless | 6083 | yes | 3.06 | 0 |
| 10ium-ScrapeCategorize-Vless | 4810 | yes | 2.14 | 0 |
| mahdibland-V2RayAggregator | 4095 | yes | 1.16 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 2.65 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 210 |
| speed | 57 |
| 204 | 20 |
| cn-block | 17 |
