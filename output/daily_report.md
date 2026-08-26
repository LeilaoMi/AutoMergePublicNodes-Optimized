# AutoNodes 每日报告

生成时间：2026-08-26 19:57:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 89577 |
| 去重后节点数 | 24385 |
| TCP 可达数 | 3000 |
| 真测通过数 | 455 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24385 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 35.4 |
| geo | 1.4 |
| probe | 51.6 |
| real_test | 106.4 |
| tcp | 39.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 26 | 23 | 3 | 88.5% |
| shadowsocks | 122 | 108 | 14 | 88.5% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 17 | 16 | 1 | 94.1% |
| vless | 391 | 282 | 109 | 72.1% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:TimeoutError | 35 |
| cn-block:TimeoutError | 22 |
| 204:TimeoutError | 19 |
| geo:ClientOSError | 17 |
| 204:ProxyError | 13 |
| speed:ClientOSError | 11 |
| geo:TimeoutError | 5 |
| cn-block:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5339 |
| ConnectionRefusedError | 965 |
| gaierror | 384 |
| OSError | 236 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.966 | prefer | 350 | 0.889 | 1979 |
| zhangkai | 0.926 | prefer | 23 | 0.957 | 144 |
| Surfboard-tg-mixed | 0.757 | prefer | 122 | 0.68 | 6645 |
| DeltaKronecker-all | 0.509 | observe | 68 | 0.426 | 6107 |
| mheidari-all | 0.46 | observe | 17 | 0.412 | 19290 |
| tg-oneclickvpnkeys | 0.319 | observe | 2 | 1.0 | 205 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4825 |
| Epodonios-all | 0.255 | observe | 0 | None | 7011 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| mheidari-all | 0.412 | 7 | 10 | 17 |
| DeltaKronecker-all | 0.426 | 29 | 39 | 68 |
| Surfboard-tg-mixed | 0.68 | 83 | 39 | 122 |
| Au1rxx-base64 | 0.889 | 311 | 39 | 350 |
| zhangkai | 0.957 | 22 | 1 | 23 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19290 | yes | 4.37 | 0 |
| SoliSpirit-all | 7313 | yes | 3.06 | 0 |
| Epodonios-all | 7011 | yes | 2.53 | 0 |
| Surfboard-tg-mixed | 6645 | yes | 2.71 | 0 |
| DeltaKronecker-all | 6107 | yes | 4.41 | 0 |
| barry-far-vless | 5698 | yes | 2.83 | 0 |
| Surfboard-tg-vless | 5444 | yes | 3.5 | 0 |
| xiaoji235-airport-v2ray-all | 5418 | yes | 2.33 | 0 |
| 10ium-ScrapeCategorize-Vless | 4825 | yes | 2.47 | 0 |
| mahdibland-V2RayAggregator | 4011 | yes | 0.99 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 46 |
| 204 | 33 |
| cn-block | 27 |
| geo | 22 |
