# AutoNodes 每日报告

生成时间：2026-08-28 10:52:38

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76338 |
| 去重后节点数 | 21064 |
| TCP 可达数 | 3000 |
| 真测通过数 | 435 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21064 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.8 |
| generate | 37.7 |
| geo | 1.4 |
| probe | 50.0 |
| real_test | 98.8 |
| tcp | 34.8 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 22 | 20 | 2 | 90.9% |
| shadowsocks | 155 | 140 | 15 | 90.3% |
| trojan | 25 | 18 | 7 | 72.0% |
| vless | 292 | 229 | 63 | 78.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 28 |
| cn-block:TimeoutError | 14 |
| geo:ClientOSError | 12 |
| 204:ProxyError | 11 |
| speed:TimeoutError | 7 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 2 |
| cn-block:ClientOSError | 2 |
| speed:ClientOSError | 1 |
| speed:ClientPayloadError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4733 |
| ConnectionRefusedError | 890 |
| gaierror | 421 |
| OSError | 21 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.966 | prefer | 307 | 0.896 | 1823 |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.839 | prefer | 114 | 0.763 | 6512 |
| mheidari-all | 0.79 | prefer | 60 | 0.717 | 14456 |
| DeltaKronecker-all | 0.37 | observe | 16 | 0.312 | 4318 |
| tg-oneclickvpnkeys | 0.362 | observe | 3 | 1.0 | 101 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4783 |
| Epodonios-all | 0.255 | observe | 0 | None | 6791 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3990 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7458 |

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
| DeltaKronecker-all | 0.312 | 5 | 11 | 16 |
| mheidari-all | 0.717 | 43 | 17 | 60 |
| Surfboard-tg-mixed | 0.763 | 87 | 27 | 114 |
| Au1rxx-base64 | 0.896 | 275 | 32 | 307 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14456 | yes | 4.6 | 0 |
| SoliSpirit-all | 7458 | yes | 4.4 | 0 |
| Epodonios-all | 6791 | yes | 4.22 | 0 |
| Surfboard-tg-mixed | 6512 | yes | 3.33 | 0 |
| barry-far-vless | 5416 | yes | 1.3 | 0 |
| Surfboard-tg-vless | 5314 | yes | 3.5 | 0 |
| 10ium-ScrapeCategorize-Vless | 4783 | yes | 1.08 | 0 |
| DeltaKronecker-all | 4318 | yes | 4.33 | 0 |
| mahdibland-V2RayAggregator | 4061 | yes | 2.78 | 0 |
| MatinGhanbari-all-sub | 3990 | yes | 0.87 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 41 |
| cn-block | 19 |
| geo | 18 |
| speed | 9 |
