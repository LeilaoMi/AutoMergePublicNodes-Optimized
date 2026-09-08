# AutoNodes 每日报告

生成时间：2026-09-08 11:03:40

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 91310 |
| 去重后节点数 | 25270 |
| TCP 可达数 | 3000 |
| 真测通过数 | 563 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25270 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 47.6 |
| geo | 1.5 |
| probe | 81.6 |
| real_test | 120.0 |
| tcp | 41.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 73 | 73 | 0 | 100.0% |
| hysteria2 | 25 | 21 | 4 | 84.0% |
| shadowsocks | 179 | 163 | 16 | 91.1% |
| socks | 8 | 5 | 3 | 62.5% |
| trojan | 26 | 18 | 8 | 69.2% |
| vless | 363 | 279 | 84 | 76.9% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 24 |
| 204:TimeoutError | 23 |
| geo:ClientOSError | 15 |
| cn-block:ClientOSError | 13 |
| speed:TimeoutError | 13 |
| 204:ProxyError | 9 |
| speed:ClientOSError | 6 |
| 204:ClientOSError | 4 |
| geo:TimeoutError | 3 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5126 |
| ConnectionRefusedError | 986 |
| gaierror | 550 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| ermaozi | 1.0 | prefer | 53 | 1.0 | 450 |
| Au1rxx-base64 | 0.968 | prefer | 325 | 0.902 | 1726 |
| ermaozi-get_subscribe | 0.94 | prefer | 19 | 1.0 | 470 |
| mheidari-all | 0.852 | prefer | 77 | 0.779 | 22334 |
| Surfboard-tg-mixed | 0.762 | prefer | 190 | 0.684 | 7431 |
| DeltaKronecker-all | 0.461 | observe | 11 | 0.545 | 6097 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 212 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4657 |
| Epodonios-all | 0.255 | observe | 0 | None | 7885 |

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
| DeltaKronecker-all | 0.545 | 6 | 5 | 11 |
| Surfboard-tg-mixed | 0.684 | 130 | 60 | 190 |
| mheidari-all | 0.779 | 60 | 17 | 77 |
| Au1rxx-base64 | 0.902 | 293 | 32 | 325 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| ermaozi-get_subscribe | 1.0 | 19 | 0 | 19 |
| ermaozi | 1.0 | 53 | 0 | 53 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22334 | yes | 4.75 | 0 |
| SoliSpirit-all | 8811 | yes | 5.35 | 0 |
| Epodonios-all | 7885 | yes | 5.35 | 0 |
| Surfboard-tg-mixed | 7431 | yes | 3.91 | 0 |
| barry-far-vless | 6423 | yes | 3.36 | 0 |
| Surfboard-tg-vless | 6201 | yes | 3.57 | 0 |
| DeltaKronecker-all | 6097 | yes | 4.82 | 0 |
| 10ium-ScrapeCategorize-Vless | 4657 | yes | 2.87 | 0 |
| mahdibland-V2RayAggregator | 4209 | yes | 0.59 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 3.19 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 40 |
| 204 | 36 |
| speed | 21 |
| geo | 18 |
