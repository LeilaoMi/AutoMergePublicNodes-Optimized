# AutoNodes 每日报告

生成时间：2026-09-05 10:24:49

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 95/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 83253 |
| 去重后节点数 | 22135 |
| TCP 可达数 | 3000 |
| 真测通过数 | 504 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22135 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.6 |
| generate | 30.5 |
| geo | 1.4 |
| probe | 87.3 |
| real_test | 113.9 |
| tcp | 37.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 29 | 29 | 0 | 100.0% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 163 | 152 | 11 | 93.3% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 27 | 15 | 12 | 55.6% |
| vless | 362 | 291 | 71 | 80.4% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:TimeoutError | 22 |
| geo:ClientOSError | 15 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 11 |
| 204:ProxyError | 9 |
| geo:TimeoutError | 6 |
| speed:TimeoutError | 6 |
| 204:ClientOSError | 6 |
| speed:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| geo:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4779 |
| ConnectionRefusedError | 889 |
| gaierror | 331 |
| OSError | 19 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| Au1rxx-base64 | 0.955 | prefer | 271 | 0.886 | 1813 |
| Surfboard-tg-mixed | 0.878 | prefer | 171 | 0.801 | 7332 |
| mheidari-all | 0.862 | prefer | 108 | 0.787 | 15508 |
| DeltaKronecker-all | 0.688 | observe | 18 | 0.667 | 6212 |
| tg-oneclickvpnkeys | 0.518 | observe | 7 | 1.0 | 118 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4887 |
| Epodonios-all | 0.255 | observe | 0 | None | 7793 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

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
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.667 | 12 | 6 | 18 |
| mheidari-all | 0.787 | 85 | 23 | 108 |
| Surfboard-tg-mixed | 0.801 | 137 | 34 | 171 |
| Au1rxx-base64 | 0.886 | 240 | 31 | 271 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| tg-oneclickvpnkeys | 1.0 | 7 | 0 | 7 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15508 | yes | 3.75 | 0 |
| SoliSpirit-all | 8561 | yes | 3.38 | 0 |
| Epodonios-all | 7793 | yes | 4.22 | 0 |
| Surfboard-tg-mixed | 7332 | yes | 3.39 | 0 |
| barry-far-vless | 6302 | yes | 3.96 | 0 |
| DeltaKronecker-all | 6212 | yes | 4.6 | 0 |
| Surfboard-tg-vless | 6108 | yes | 3.18 | 0 |
| 10ium-ScrapeCategorize-Vless | 4887 | yes | 2.8 | 0 |
| mahdibland-V2RayAggregator | 4095 | yes | 1.21 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.83 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 37 |
| cn-block | 27 |
| geo | 23 |
| speed | 9 |
