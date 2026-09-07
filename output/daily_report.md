# AutoNodes 每日报告

生成时间：2026-09-07 21:27:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/1 |
| 清理建议：优先/观察 | 5/101 |
| 原始节点数 | 84365 |
| 去重后节点数 | 22975 |
| TCP 可达数 | 3000 |
| 真测通过数 | 554 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22975 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.3 |
| generate | 41.2 |
| geo | 1.5 |
| probe | 86.0 |
| real_test | 124.8 |
| tcp | 37.4 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 16 | 14 | 2 | 87.5% |
| shadowsocks | 164 | 155 | 9 | 94.5% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 17 | 12 | 5 | 70.6% |
| vless | 418 | 345 | 73 | 82.5% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 24 |
| geo:ClientOSError | 19 |
| cn-block:TimeoutError | 16 |
| cn-block:ClientOSError | 8 |
| speed:ClientOSError | 5 |
| geo:TimeoutError | 4 |
| speed:TimeoutError | 3 |
| geo:ProxyError | 3 |
| 204:ClientOSError | 3 |
| 204:ProxyError | 2 |
| 204:ProxyConnectionError | 1 |
| speed:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4643 |
| ConnectionRefusedError | 885 |
| gaierror | 296 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 374 | 0.936 | 1688 |
| zhangkai | 0.929 | prefer | 24 | 0.958 | 144 |
| mheidari-all | 0.905 | prefer | 78 | 0.833 | 16413 |
| DeltaKronecker-all | 0.84 | prefer | 23 | 0.783 | 6417 |
| Surfboard-tg-mixed | 0.771 | prefer | 137 | 0.693 | 7444 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 196 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Epodonios-all | 0.255 | observe | 0 | None | 7899 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 8444 |

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

## 订阅源清理建议

| 分类 | 订阅源 | 评分 | 已测 | 通过率 | 连续死亡 | 原因 |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | 10ium-ScrapeCategorize-Vless | 0.153 | 5 | 0.0 | 0 | 已测数量 >= 5 且评分偏低 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 5 | 5 |
| Surfboard-tg-mixed | 0.693 | 95 | 42 | 137 |
| DeltaKronecker-all | 0.783 | 18 | 5 | 23 |
| mheidari-all | 0.833 | 65 | 13 | 78 |
| Au1rxx-base64 | 0.936 | 350 | 24 | 374 |
| zhangkai | 0.958 | 23 | 1 | 24 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16413 | yes | 5.09 | 0 |
| SoliSpirit-all | 8444 | yes | 3.41 | 0 |
| Epodonios-all | 7899 | yes | 3.21 | 0 |
| Surfboard-tg-mixed | 7444 | yes | 4.06 | 0 |
| DeltaKronecker-all | 6417 | yes | 5.48 | 0 |
| barry-far-vless | 6394 | yes | 2.78 | 0 |
| Surfboard-tg-vless | 6179 | yes | 4.63 | 0 |
| xiaoji235-airport-v2ray-all | 5750 | yes | 4.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 4650 | yes | 2.56 | 0 |
| mahdibland-V2RayAggregator | 4218 | yes | 1.47 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 30 |
| geo | 26 |
| cn-block | 25 |
| speed | 9 |
