# AutoNodes 每日报告

生成时间：2026-08-29 16:36:21

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78465 |
| 去重后节点数 | 21216 |
| TCP 可达数 | 3000 |
| 真测通过数 | 618 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21216 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.2 |
| generate | 46.5 |
| geo | 1.3 |
| probe | 52.2 |
| real_test | 120.1 |
| tcp | 34.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 26 | 26 | 0 | 100.0% |
| hysteria2 | 22 | 22 | 0 | 100.0% |
| shadowsocks | 184 | 175 | 9 | 95.1% |
| socks | 7 | 5 | 2 | 71.4% |
| trojan | 30 | 22 | 8 | 73.3% |
| vless | 429 | 365 | 64 | 85.1% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 21 |
| cn-block:TimeoutError | 17 |
| speed:TimeoutError | 8 |
| geo:ClientOSError | 7 |
| speed:ClientOSError | 7 |
| 204:ProxyError | 6 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 4 |
| geo:TimeoutError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 2 |
| speed:ClientPayloadError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4644 |
| ConnectionRefusedError | 866 |
| gaierror | 410 |
| OSError | 23 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.995 | prefer | 372 | 0.925 | 1807 |
| Surfboard-tg-mixed | 0.955 | prefer | 78 | 0.885 | 6877 |
| zhangkai | 0.929 | prefer | 24 | 0.958 | 144 |
| mheidari-all | 0.895 | prefer | 79 | 0.823 | 14622 |
| DeltaKronecker-all | 0.865 | prefer | 142 | 0.789 | 4926 |
| tg-oneclickvpnkeys | 0.364 | observe | 3 | 1.0 | 155 |
| nscl5-all | 0.283 | observe | 1 | 1.0 | 700 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4635 |
| Epodonios-all | 0.255 | observe | 0 | None | 7290 |

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
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.789 | 112 | 30 | 142 |
| mheidari-all | 0.823 | 65 | 14 | 79 |
| Surfboard-tg-mixed | 0.885 | 69 | 9 | 78 |
| Au1rxx-base64 | 0.925 | 344 | 28 | 372 |
| zhangkai | 0.958 | 23 | 1 | 24 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14622 | yes | 3.78 | 0 |
| SoliSpirit-all | 7426 | yes | 3.11 | 0 |
| Epodonios-all | 7290 | yes | 0.52 | 0 |
| Surfboard-tg-mixed | 6877 | yes | 4.01 | 0 |
| barry-far-vless | 5725 | yes | 2.17 | 0 |
| Surfboard-tg-vless | 5686 | yes | 3.26 | 0 |
| DeltaKronecker-all | 4926 | yes | 3.88 | 0 |
| 10ium-ScrapeCategorize-Vless | 4635 | yes | 2.56 | 0 |
| mahdibland-V2RayAggregator | 4012 | yes | 1.47 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.02 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 31 |
| cn-block | 22 |
| speed | 18 |
| geo | 12 |
