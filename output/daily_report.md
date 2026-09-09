# AutoNodes 每日报告

生成时间：2026-09-09 11:14:03

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 85046 |
| 去重后节点数 | 22059 |
| TCP 可达数 | 3000 |
| 真测通过数 | 456 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22059 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.7 |
| generate | 80.2 |
| geo | 1.4 |
| probe | 230.5 |
| real_test | 277.1 |
| tcp | 36.5 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 71 | 49 | 22 | 69.0% |
| hysteria2 | 18 | 16 | 2 | 88.9% |
| shadowsocks | 146 | 136 | 10 | 93.2% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 20 | 13 | 7 | 65.0% |
| vless | 295 | 238 | 57 | 80.7% |
| vmess | 2 | 2 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| 204:ProxyError | 28 |
| 204:TimeoutError | 25 |
| geo:ClientOSError | 15 |
| cn-block:TimeoutError | 12 |
| geo:TimeoutError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 3 |
| 204:ProxyConnectionError | 2 |
| speed:TimeoutError | 2 |
| cn-block:ProxyError | 1 |
| speed:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4509 |
| ConnectionRefusedError | 885 |
| gaierror | 406 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.987 | prefer | 227 | 0.921 | 1749 |
| Surfboard-tg-mixed | 0.863 | prefer | 164 | 0.787 | 7479 |
| mheidari-all | 0.847 | prefer | 71 | 0.775 | 16452 |
| ermaozi | 0.724 | prefer | 49 | 0.714 | 442 |
| DeltaKronecker-all | 0.679 | observe | 19 | 0.632 | 5187 |
| ermaozi-get_subscribe | 0.659 | observe | 23 | 0.652 | 473 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 180 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4795 |
| Epodonios-all | 0.255 | observe | 0 | None | 7964 |
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
| DeltaKronecker-all | 0.632 | 12 | 7 | 19 |
| ermaozi-get_subscribe | 0.652 | 15 | 8 | 23 |
| ermaozi | 0.714 | 35 | 14 | 49 |
| mheidari-all | 0.775 | 55 | 16 | 71 |
| Surfboard-tg-mixed | 0.787 | 129 | 35 | 164 |
| Au1rxx-base64 | 0.921 | 209 | 18 | 227 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16452 | yes | 5.54 | 0 |
| SoliSpirit-all | 9095 | yes | 4.89 | 0 |
| Epodonios-all | 7964 | yes | 6.13 | 0 |
| Surfboard-tg-mixed | 7479 | yes | 4.73 | 0 |
| barry-far-vless | 6404 | yes | 2.87 | 0 |
| Surfboard-tg-vless | 6181 | yes | 4.39 | 0 |
| DeltaKronecker-all | 5187 | yes | 5.77 | 0 |
| 10ium-ScrapeCategorize-Vless | 4795 | yes | 3.61 | 0 |
| mahdibland-V2RayAggregator | 4219 | yes | 1.37 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 3.18 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| 204 | 58 |
| geo | 20 |
| cn-block | 17 |
| speed | 3 |
