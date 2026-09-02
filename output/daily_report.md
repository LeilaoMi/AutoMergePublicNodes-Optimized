# AutoNodes 每日报告

生成时间：2026-09-02 16:25:24

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 82564 |
| 去重后节点数 | 23518 |
| TCP 可达数 | 3000 |
| 真测通过数 | 572 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23518 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 8.2 |
| generate | 40.2 |
| geo | 1.5 |
| probe | 83.8 |
| real_test | 112.6 |
| tcp | 37.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 24 | 23 | 1 | 95.8% |
| hysteria2 | 10 | 10 | 0 | 100.0% |
| shadowsocks | 159 | 141 | 18 | 88.7% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 25 | 21 | 4 | 84.0% |
| vless | 447 | 374 | 73 | 83.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 18 |
| cn-block:TimeoutError | 17 |
| cn-block:ClientOSError | 15 |
| geo:ClientOSError | 12 |
| 204:ProxyConnectionError | 7 |
| 204:ProxyError | 7 |
| speed:ClientOSError | 6 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 5 |
| geo:TimeoutError | 4 |
| cn-block:ProxyError | 1 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4535 |
| ConnectionRefusedError | 913 |
| gaierror | 364 |
| OSError | 29 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.961 | prefer | 349 | 0.894 | 1741 |
| mheidari-all | 0.947 | prefer | 111 | 0.874 | 15532 |
| zhangkai | 0.926 | prefer | 23 | 0.957 | 144 |
| DeltaKronecker-all | 0.92 | prefer | 23 | 0.87 | 7295 |
| Surfboard-tg-mixed | 0.819 | prefer | 159 | 0.742 | 7112 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 178 |
| tg-oneclickvpnkeys | 0.259 | observe | 1 | 1.0 | 103 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 50 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4765 |
| Epodonios-all | 0.255 | observe | 0 | None | 7553 |

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
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| Surfboard-tg-mixed | 0.742 | 118 | 41 | 159 |
| DeltaKronecker-all | 0.87 | 20 | 3 | 23 |
| mheidari-all | 0.874 | 97 | 14 | 111 |
| Au1rxx-base64 | 0.894 | 312 | 37 | 349 |
| zhangkai | 0.957 | 22 | 1 | 23 |
| tg-OutlineReleasedKey | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15532 | yes | 4.89 | 0 |
| SoliSpirit-all | 7794 | yes | 2.55 | 0 |
| Epodonios-all | 7553 | yes | 5.08 | 0 |
| DeltaKronecker-all | 7295 | yes | 3.44 | 0 |
| Surfboard-tg-mixed | 7112 | yes | 3.47 | 0 |
| barry-far-vless | 6200 | yes | 2.1 | 0 |
| Surfboard-tg-vless | 5992 | yes | 3.69 | 0 |
| 10ium-ScrapeCategorize-Vless | 4765 | yes | 1.9 | 0 |
| mahdibland-V2RayAggregator | 4066 | yes | 1.98 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.19 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 37 |
| cn-block | 33 |
| geo | 17 |
| speed | 11 |
