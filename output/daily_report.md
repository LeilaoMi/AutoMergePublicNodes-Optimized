# AutoNodes 每日报告

生成时间：2026-08-27 22:08:41

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 87058 |
| 去重后节点数 | 23525 |
| TCP 可达数 | 3000 |
| 真测通过数 | 482 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23525 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.9 |
| generate | 40.0 |
| geo | 1.5 |
| probe | 47.3 |
| real_test | 90.3 |
| tcp | 39.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 22 | 22 | 0 | 100.0% |
| hysteria2 | 25 | 23 | 2 | 92.0% |
| shadowsocks | 184 | 165 | 19 | 89.7% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 20 | 19 | 1 | 95.0% |
| vless | 316 | 247 | 69 | 78.2% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:ClientOSError | 35 |
| 204:TimeoutError | 16 |
| cn-block:TimeoutError | 11 |
| speed:ClientOSError | 9 |
| speed:TimeoutError | 7 |
| 204:ClientOSError | 5 |
| cn-block:ProxyError | 4 |
| cn-block:ClientOSError | 2 |
| 204:ProxyError | 2 |
| geo:TimeoutError | 2 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5343 |
| ConnectionRefusedError | 966 |
| gaierror | 394 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 303 | 0.944 | 1622 |
| zhangkai | 0.966 | prefer | 23 | 1.0 | 144 |
| Surfboard-tg-mixed | 0.868 | prefer | 149 | 0.792 | 6577 |
| mheidari-all | 0.622 | observe | 94 | 0.543 | 19755 |
| DeltaKronecker-all | 0.391 | observe | 2 | 1.0 | 4318 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4783 |
| Epodonios-all | 0.255 | observe | 0 | None | 6955 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3991 |

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
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| mheidari-all | 0.543 | 51 | 43 | 94 |
| Surfboard-tg-mixed | 0.792 | 118 | 31 | 149 |
| Au1rxx-base64 | 0.944 | 286 | 17 | 303 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| DeltaKronecker-all | 1.0 | 2 | 0 | 2 |
| zhangkai | 1.0 | 23 | 0 | 23 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19755 | yes | 4.45 | 0 |
| SoliSpirit-all | 7129 | yes | 3.37 | 0 |
| Epodonios-all | 6955 | yes | 2.51 | 0 |
| Surfboard-tg-mixed | 6577 | yes | 3.07 | 0 |
| barry-far-vless | 5568 | yes | 1.16 | 0 |
| xiaoji235-airport-v2ray-all | 5418 | yes | 2.64 | 0 |
| Surfboard-tg-vless | 5393 | yes | 3.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4783 | yes | 1.35 | 0 |
| DeltaKronecker-all | 4318 | yes | 4.98 | 0 |
| mahdibland-V2RayAggregator | 4019 | yes | 0.6 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 37 |
| 204 | 23 |
| cn-block | 17 |
| speed | 16 |
