# AutoNodes 每日报告

生成时间：2026-08-21 13:03:08

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 99/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 95230 |
| 去重后节点数 | 24848 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1118 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24848 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.4 |
| generate | 36.0 |
| geo | 0.9 |
| probe | 63.2 |
| real_test | 191.1 |
| tcp | 38.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 20 | 20 | 0 | 100.0% |
| shadowsocks | 177 | 160 | 17 | 90.4% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 662 | 647 | 15 | 97.7% |
| vless | 264 | 174 | 90 | 65.9% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 46 |
| 204:TimeoutError | 16 |
| geo:TimeoutError | 15 |
| speed:TimeoutError | 15 |
| cn-block:TimeoutError | 12 |
| 204:ProxyError | 8 |
| speed:ClientOSError | 5 |
| cn-block:ClientOSError | 4 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4828 |
| ConnectionRefusedError | 974 |
| gaierror | 589 |
| OSError | 228 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 710 | 0.973 | 1897 |
| zhangkai | 0.997 | prefer | 111 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.903 | prefer | 111 | 0.829 | 6419 |
| mheidari-all | 0.808 | prefer | 300 | 0.73 | 22031 |
| nscl5-all | 0.391 | observe | 2 | 1.0 | 3031 |
| DeltaKronecker-all | 0.284 | observe | 6 | 0.333 | 6250 |
| tg-oneclickvpnkeys | 0.263 | observe | 1 | 1.0 | 192 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5148 |
| Epodonios-all | 0.255 | observe | 0 | None | 7104 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3985 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.333 | 2 | 4 | 6 |
| mheidari-all | 0.73 | 219 | 81 | 300 |
| Surfboard-tg-mixed | 0.829 | 92 | 19 | 111 |
| Au1rxx-base64 | 0.973 | 691 | 19 | 710 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 111 | 0 | 111 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 22031 | yes | 5.34 | 0 |
| SoliSpirit-all | 7205 | yes | 3.69 | 0 |
| Epodonios-all | 7104 | yes | 4.73 | 0 |
| Surfboard-tg-mixed | 6419 | yes | 3.52 | 0 |
| DeltaKronecker-all | 6250 | yes | 4.55 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 2.58 | 0 |
| barry-far-vless | 5444 | yes | 1.79 | 0 |
| 10ium-ScrapeCategorize-Vless | 5148 | yes | 2.18 | 0 |
| Surfboard-tg-vless | 5125 | yes | 3.16 | 0 |
| mahdibland-V2RayAggregator | 4647 | yes | 2.02 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 61 |
| 204 | 26 |
| speed | 20 |
| cn-block | 17 |
