# AutoNodes 每日报告

生成时间：2026-09-10 04:14:57

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 87394 |
| 去重后节点数 | 23410 |
| TCP 可达数 | 3000 |
| 真测通过数 | 489 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23410 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.9 |
| generate | 36.1 |
| geo | 1.4 |
| probe | 239.7 |
| real_test | 326.9 |
| tcp | 39.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 4 | 4 | 0 | 100.0% |
| http | 48 | 31 | 17 | 64.6% |
| hysteria2 | 16 | 16 | 0 | 100.0% |
| shadowsocks | 145 | 133 | 12 | 91.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 43 | 40 | 3 | 93.0% |
| vless | 439 | 261 | 178 | 59.5% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 47 |
| speed:TimeoutError | 42 |
| geo:ClientOSError | 35 |
| speed:ClientOSError | 26 |
| 204:ProxyError | 24 |
| cn-block:ClientOSError | 16 |
| cn-block:TimeoutError | 9 |
| 204:TimeoutError | 7 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4988 |
| ConnectionRefusedError | 946 |
| gaierror | 364 |
| OSError | 245 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.984 | prefer | 297 | 0.923 | 1598 |
| Surfboard-tg-mixed | 0.894 | prefer | 41 | 0.829 | 7448 |
| ermaozi | 0.704 | prefer | 33 | 0.697 | 449 |
| mheidari-all | 0.611 | observe | 141 | 0.532 | 16259 |
| ermaozi-get_subscribe | 0.541 | observe | 17 | 0.588 | 469 |
| DeltaKronecker-all | 0.507 | observe | 148 | 0.426 | 5187 |
| xiaoji235-airport-v2ray-all | 0.492 | observe | 13 | 0.538 | 3508 |
| tg-oneclickvpnkeys | 0.317 | observe | 2 | 1.0 | 147 |
| tg-OutlineReleasedKey | 0.257 | observe | 1 | 1.0 | 53 |
| Epodonios-all | 0.255 | observe | 0 | None | 7910 |

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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 3 | 3 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.426 | 63 | 85 | 148 |
| mheidari-all | 0.532 | 75 | 66 | 141 |
| xiaoji235-airport-v2ray-all | 0.538 | 7 | 6 | 13 |
| ermaozi-get_subscribe | 0.588 | 10 | 7 | 17 |
| ermaozi | 0.697 | 23 | 10 | 33 |
| Surfboard-tg-mixed | 0.829 | 34 | 7 | 41 |
| Au1rxx-base64 | 0.923 | 274 | 23 | 297 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16259 | yes | 6.38 | 0 |
| SoliSpirit-all | 8706 | yes | 3.22 | 0 |
| Epodonios-all | 7910 | yes | 3.63 | 0 |
| Surfboard-tg-mixed | 7448 | yes | 4.05 | 0 |
| barry-far-vless | 6333 | yes | 1.95 | 0 |
| Surfboard-tg-vless | 6108 | yes | 4.27 | 0 |
| DeltaKronecker-all | 5187 | yes | 4.75 | 0 |
| 10ium-ScrapeCategorize-Vless | 4795 | yes | 2.64 | 0 |
| mahdibland-V2RayAggregator | 4247 | yes | 2.05 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 2.03 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 83 |
| speed | 68 |
| 204 | 33 |
| cn-block | 27 |
