# AutoNodes 每日报告

生成时间：2026-08-30 04:53:48

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 86359 |
| 去重后节点数 | 21983 |
| TCP 可达数 | 3000 |
| 真测通过数 | 716 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21983 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 47.3 |
| geo | 1.6 |
| probe | 55.5 |
| real_test | 150.3 |
| tcp | 33.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 24 | 24 | 0 | 100.0% |
| hysteria2 | 22 | 22 | 0 | 100.0% |
| shadowsocks | 184 | 177 | 7 | 96.2% |
| socks | 4 | 3 | 1 | 75.0% |
| trojan | 12 | 7 | 5 | 58.3% |
| vless | 684 | 479 | 205 | 70.0% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 51 |
| geo:TimeoutError | 46 |
| speed:TimeoutError | 36 |
| cn-block:TimeoutError | 33 |
| 204:TimeoutError | 17 |
| speed:ClientOSError | 10 |
| cn-block:ClientOSError | 9 |
| 204:ProxyError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4258 |
| ConnectionRefusedError | 910 |
| gaierror | 422 |
| OSError | 30 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.999 | prefer | 378 | 0.929 | 1825 |
| zhangkai | 0.964 | prefer | 22 | 1.0 | 144 |
| DeltaKronecker-all | 0.955 | prefer | 30 | 0.9 | 4926 |
| Surfboard-tg-mixed | 0.824 | prefer | 209 | 0.746 | 6910 |
| mheidari-all | 0.624 | observe | 285 | 0.544 | 18105 |
| nscl5-all | 0.391 | observe | 2 | 1.0 | 4310 |
| tg-oneclickvpnkeys | 0.365 | observe | 3 | 1.0 | 169 |
| Epodonios-all | 0.255 | observe | 0 | None | 7323 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3992 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7549 |

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
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 3 | 3 |
| mheidari-all | 0.544 | 155 | 130 | 285 |
| Surfboard-tg-mixed | 0.746 | 156 | 53 | 209 |
| DeltaKronecker-all | 0.9 | 27 | 3 | 30 |
| Au1rxx-base64 | 0.929 | 351 | 27 | 378 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| tg-oneclickvpnkeys | 1.0 | 3 | 0 | 3 |
| zhangkai | 1.0 | 22 | 0 | 22 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 18105 | yes | 5.07 | 0 |
| SoliSpirit-all | 7549 | yes | 3.34 | 0 |
| Epodonios-all | 7323 | yes | 4.6 | 0 |
| Surfboard-tg-mixed | 6910 | yes | 3.43 | 0 |
| barry-far-vless | 5912 | yes | 0.82 | 0 |
| Surfboard-tg-vless | 5726 | yes | 4.29 | 0 |
| DeltaKronecker-all | 4926 | yes | 3.7 | 0 |
| 10ium-ScrapeCategorize-Vless | 4635 | yes | 2.07 | 0 |
| nscl5-all | 4310 | yes | 1.58 | 0 |
| mahdibland-V2RayAggregator | 4012 | yes | 0.3 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 99 |
| speed | 47 |
| cn-block | 45 |
| 204 | 27 |
