# AutoNodes 每日报告

生成时间：2026-08-31 22:46:01

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 96/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 78460 |
| 去重后节点数 | 22374 |
| TCP 可达数 | 3000 |
| 真测通过数 | 639 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22374 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 29.8 |
| geo | 1.4 |
| probe | 87.8 |
| real_test | 112.1 |
| tcp | 35.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 23 | 20 | 3 | 87.0% |
| hysteria2 | 26 | 26 | 0 | 100.0% |
| shadowsocks | 178 | 168 | 10 | 94.4% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 13 | 13 | 0 | 100.0% |
| vless | 473 | 407 | 66 | 86.0% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 18 |
| cn-block:TimeoutError | 15 |
| cn-block:ClientOSError | 10 |
| speed:ClientOSError | 8 |
| 204:ProxyError | 6 |
| 204:ProxyConnectionError | 5 |
| speed:TimeoutError | 5 |
| 204:ClientOSError | 4 |
| 204:TimeoutError | 4 |
| cn-block:ProxyError | 2 |
| geo:TimeoutError | 2 |
| geo:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4842 |
| ConnectionRefusedError | 932 |
| gaierror | 339 |
| OSError | 20 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.975 | prefer | 151 | 0.901 | 7016 |
| Au1rxx-base64 | 0.972 | prefer | 289 | 0.927 | 1182 |
| mheidari-all | 0.928 | prefer | 189 | 0.852 | 14929 |
| DeltaKronecker-all | 0.898 | prefer | 64 | 0.828 | 5904 |
| zhangkai | 0.852 | prefer | 24 | 0.875 | 144 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4657 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7470 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 5879 |
| barry-far-vless | 0.255 | observe | 0 | None | 6031 |

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
| Epodonios-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.828 | 53 | 11 | 64 |
| mheidari-all | 0.852 | 161 | 28 | 189 |
| zhangkai | 0.875 | 21 | 3 | 24 |
| Surfboard-tg-mixed | 0.901 | 136 | 15 | 151 |
| Au1rxx-base64 | 0.927 | 268 | 21 | 289 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14929 | yes | 4.5 | 0 |
| SoliSpirit-all | 7470 | yes | 2.95 | 0 |
| Epodonios-all | 7323 | yes | 3.2 | 0 |
| Surfboard-tg-mixed | 7016 | yes | 2.94 | 0 |
| barry-far-vless | 6031 | yes | 0.66 | 0 |
| DeltaKronecker-all | 5904 | yes | 3.33 | 0 |
| Surfboard-tg-vless | 5879 | yes | 4.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 4657 | yes | 0.42 | 0 |
| mahdibland-V2RayAggregator | 4025 | yes | 2.11 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 0.48 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 27 |
| geo | 21 |
| 204 | 19 |
| speed | 13 |
