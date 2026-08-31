# AutoNodes 每日报告

生成时间：2026-08-31 04:57:22

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 78971 |
| 去重后节点数 | 21904 |
| TCP 可达数 | 3000 |
| 真测通过数 | 638 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21904 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.0 |
| generate | 24.6 |
| geo | 1.6 |
| probe | 82.5 |
| real_test | 141.4 |
| tcp | 35.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 22 | 1 | 95.7% |
| hysteria2 | 14 | 14 | 0 | 100.0% |
| shadowsocks | 148 | 145 | 3 | 98.0% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 45 | 33 | 12 | 73.3% |
| vless | 646 | 418 | 228 | 64.7% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 103 |
| geo:ClientOSError | 56 |
| speed:TimeoutError | 17 |
| 204:ProxyError | 16 |
| cn-block:TimeoutError | 15 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 11 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| cn-block:ClientOSError | 3 |
| speed:ProxyError | 2 |
| 204:ProxyConnectionError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4968 |
| ConnectionRefusedError | 871 |
| gaierror | 292 |
| OSError | 18 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.998 | prefer | 307 | 0.928 | 1804 |
| zhangkai | 0.929 | prefer | 24 | 0.958 | 144 |
| Surfboard-tg-mixed | 0.815 | prefer | 217 | 0.737 | 6765 |
| DeltaKronecker-all | 0.578 | observe | 325 | 0.498 | 5576 |
| mheidari-all | 0.568 | observe | 8 | 0.875 | 14559 |
| Epodonios-all | 0.335 | observe | 1 | 1.0 | 7271 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4762 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7850 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5673 |

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
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.498 | 162 | 163 | 325 |
| Surfboard-tg-mixed | 0.737 | 160 | 57 | 217 |
| mheidari-all | 0.875 | 7 | 1 | 8 |
| Au1rxx-base64 | 0.928 | 285 | 22 | 307 |
| zhangkai | 0.958 | 23 | 1 | 24 |
| Epodonios-all | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14559 | yes | 4.74 | 0 |
| SoliSpirit-all | 7850 | yes | 4.08 | 0 |
| Epodonios-all | 7271 | yes | 1.4 | 0 |
| Surfboard-tg-mixed | 6765 | yes | 3.16 | 0 |
| barry-far-vless | 5858 | yes | 1.71 | 0 |
| Surfboard-tg-vless | 5673 | yes | 3.32 | 0 |
| DeltaKronecker-all | 5576 | yes | 3.87 | 0 |
| 10ium-ScrapeCategorize-Vless | 4762 | yes | 2.26 | 0 |
| mahdibland-V2RayAggregator | 4041 | yes | 1.46 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 2.32 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 159 |
| speed | 33 |
| 204 | 32 |
| cn-block | 21 |
