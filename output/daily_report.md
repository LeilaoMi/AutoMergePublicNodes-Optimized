# AutoNodes 每日报告

生成时间：2026-10-08 23:20:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 2/104 |
| 原始节点数 | 98866 |
| 去重后节点数 | 27653 |
| TCP 可达数 | 3000 |
| 真测通过数 | 401 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 27653 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 12.0 |
| generate | 76.2 |
| geo | 1.5 |
| probe | 245.3 |
| real_test | 241.2 |
| tcp | 47.0 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 5 | 1 | 4 | 20.0% |
| http | 22 | 15 | 7 | 68.2% |
| hysteria2 | 18 | 18 | 0 | 100.0% |
| shadowsocks | 110 | 106 | 4 | 96.4% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 66 | 65 | 1 | 98.5% |
| vless | 241 | 194 | 47 | 80.5% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 16 |
| speed:ClientOSError | 10 |
| geo:ClientOSError | 8 |
| 204:ProxyConnectionError | 7 |
| 204:TimeoutError | 7 |
| speed:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| geo:TimeoutError | 2 |
| cn-block:ProxyError | 1 |
| 204:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6598 |
| ConnectionRefusedError | 1011 |
| gaierror | 415 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.966 | prefer | 344 | 0.895 | 1827 |
| mheidari-all | 0.901 | prefer | 76 | 0.829 | 23588 |
| zhangkai | 0.672 | observe | 22 | 0.682 | 144 |
| DeltaKronecker-all | 0.57 | observe | 11 | 0.727 | 5197 |
| Surfboard-tg-mixed | 0.48 | observe | 4 | 1.0 | 7092 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5081 |
| Epodonios-all | 0.255 | observe | 0 | None | 7650 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ermaozi-get_subscribe | 0.168 | 5 | 0.2 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.2 | 1 | 4 | 5 |
| zhangkai | 0.682 | 15 | 7 | 22 |
| DeltaKronecker-all | 0.727 | 8 | 3 | 11 |
| mheidari-all | 0.829 | 63 | 13 | 76 |
| Au1rxx-base64 | 0.895 | 308 | 36 | 344 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Surfboard-tg-mixed | 1.0 | 4 | 0 | 4 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23588 | yes | 7.33 | 0 |
| SoliSpirit-all | 10086 | yes | 4.78 | 0 |
| Epodonios-all | 7650 | yes | 5.89 | 0 |
| Surfboard-tg-mixed | 7092 | yes | 2.8 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 3.93 | 0 |
| barry-far-vless | 5923 | yes | 3.18 | 0 |
| Surfboard-tg-vless | 5580 | yes | 6.11 | 0 |
| DeltaKronecker-all | 5197 | yes | 7.4 | 0 |
| 10ium-ScrapeCategorize-Vless | 5081 | yes | 1.29 | 0 |
| mahdibland-V2RayAggregator | 4362 | yes | 1.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 21 |
| 204 | 18 |
| speed | 15 |
| geo | 10 |
