# AutoNodes 每日报告

生成时间：2026-06-28 19:43:19

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 76621 |
| 去重后节点数 | 23024 |
| TCP 可达数 | 3000 |
| 真测通过数 | 518 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23024 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| generate | 48.2 |
| geo | 1.4 |
| probe | 54.3 |
| real_test | 144.0 |
| tcp | 30.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 115 | 93 | 22 | 80.9% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 127 | 62 | 65 | 48.8% |
| vless | 442 | 320 | 122 | 72.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 79 |
| 204:TimeoutError | 33 |
| 204:ProxyError | 18 |
| cn-block:TimeoutError | 18 |
| geo:TimeoutError | 14 |
| speed:TimeoutError | 13 |
| 204:ClientOSError | 11 |
| geo:ClientOSError | 7 |
| cn-block:ClientOSError | 6 |
| geo:ProxyError | 5 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 3 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4244 |
| ConnectionRefusedError | 659 |
| gaierror | 240 |
| OSError | 123 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| mheidari-all | 0.844 | prefer | 295 | 0.766 | 16170 |
| Au1rxx-base64 | 0.821 | prefer | 31 | 0.839 | 82 |
| Surfboard-tg-mixed | 0.717 | prefer | 304 | 0.638 | 5276 |
| DeltaKronecker-all | 0.654 | observe | 59 | 0.576 | 6788 |
| nscl5-all | 0.302 | observe | 1 | 1.0 | 1174 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4327 |
| Epodonios-all | 0.255 | observe | 0 | None | 7727 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3984 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Parsashonam | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| Surfboard-tg-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.576 | 34 | 25 | 59 |
| Surfboard-tg-mixed | 0.638 | 194 | 110 | 304 |
| mheidari-all | 0.766 | 226 | 69 | 295 |
| Au1rxx-base64 | 0.839 | 26 | 5 | 31 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16170 | yes | 3.62 | 0 |
| Epodonios-all | 7727 | yes | 2.14 | 0 |
| SoliSpirit-all | 7087 | yes | 2.88 | 0 |
| DeltaKronecker-all | 6788 | yes | 3.74 | 0 |
| mahdibland-V2RayAggregator | 5325 | yes | 2.23 | 0 |
| Surfboard-tg-mixed | 5276 | yes | 1.6 | 0 |
| barry-far-vless | 4558 | yes | 1.29 | 0 |
| 10ium-ScrapeCategorize-Vless | 4327 | yes | 2.51 | 0 |
| MatinGhanbari-all-sub | 3984 | yes | 1.57 | 0 |
| Surfboard-tg-vless | 3784 | yes | 1.72 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 95 |
| 204 | 62 |
| cn-block | 27 |
| geo | 26 |
