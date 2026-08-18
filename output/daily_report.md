# AutoNodes 每日报告

生成时间：2026-08-18 01:41:26

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 80389 |
| 去重后节点数 | 22947 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1304 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22947 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.1 |
| generate | 19.4 |
| geo | 1.2 |
| probe | 70.9 |
| real_test | 261.6 |
| tcp | 36.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 126 | 126 | 0 | 100.0% |
| hysteria2 | 35 | 35 | 0 | 100.0% |
| shadowsocks | 170 | 165 | 5 | 97.1% |
| socks | 6 | 4 | 2 | 66.7% |
| trojan | 822 | 809 | 13 | 98.4% |
| tuic | 1 | 1 | 0 | 100.0% |
| vless | 340 | 161 | 179 | 47.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 88 |
| speed:TimeoutError | 50 |
| geo:ClientOSError | 24 |
| speed:ClientOSError | 14 |
| 204:TimeoutError | 6 |
| 204:ProxyError | 6 |
| cn-block:TimeoutError | 5 |
| cn-block:ClientOSError | 3 |
| 204:ClientOSError | 2 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4733 |
| ConnectionRefusedError | 937 |
| gaierror | 299 |
| OSError | 24 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 527 | 0.964 | 1475 |
| zhangkai | 0.998 | prefer | 125 | 1.0 | 159 |
| mheidari-all | 0.949 | prefer | 672 | 0.871 | 16056 |
| Surfboard-tg-mixed | 0.8 | prefer | 98 | 0.724 | 6128 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.262 | observe | 1 | 1.0 | 179 |
| DeltaKronecker-all | 0.257 | observe | 77 | 0.169 | 6368 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5085 |
| Epodonios-all | 0.255 | observe | 0 | None | 6777 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3986 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.169 | 13 | 64 | 77 |
| Surfboard-tg-mixed | 0.724 | 71 | 27 | 98 |
| mheidari-all | 0.871 | 585 | 87 | 672 |
| Au1rxx-base64 | 0.964 | 508 | 19 | 527 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 125 | 0 | 125 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16056 | yes | 3.9 | 0 |
| SoliSpirit-all | 6971 | yes | 3.2 | 0 |
| Epodonios-all | 6777 | yes | 2.51 | 0 |
| DeltaKronecker-all | 6368 | yes | 4.17 | 0 |
| Surfboard-tg-mixed | 6128 | yes | 3.18 | 0 |
| barry-far-vless | 5128 | yes | 2.09 | 0 |
| 10ium-ScrapeCategorize-Vless | 5085 | yes | 2.46 | 0 |
| Surfboard-tg-vless | 4797 | yes | 2.82 | 0 |
| mahdibland-V2RayAggregator | 4027 | yes | 0.98 | 0 |
| MatinGhanbari-all-sub | 3986 | yes | 2.53 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 112 |
| speed | 64 |
| 204 | 14 |
| cn-block | 9 |
