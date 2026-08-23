# AutoNodes 每日报告

生成时间：2026-08-23 12:54:29

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 5/102 |
| 原始节点数 | 77897 |
| 去重后节点数 | 21437 |
| TCP 可达数 | 3000 |
| 真测通过数 | 675 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 21437 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.2 |
| generate | 35.0 |
| geo | 1.3 |
| probe | 50.9 |
| real_test | 138.6 |
| tcp | 35.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 112 | 112 | 0 | 100.0% |
| hysteria2 | 15 | 14 | 1 | 93.3% |
| shadowsocks | 206 | 191 | 15 | 92.7% |
| socks | 3 | 2 | 1 | 66.7% |
| trojan | 43 | 35 | 8 | 81.4% |
| vless | 384 | 317 | 67 | 82.6% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 26 |
| cn-block:TimeoutError | 23 |
| 204:TimeoutError | 12 |
| cn-block:ClientOSError | 7 |
| 204:ProxyError | 7 |
| speed:ClientOSError | 6 |
| geo:ClientOSError | 4 |
| speed:TimeoutError | 3 |
| 204:ClientOSError | 2 |
| geo:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4879 |
| ConnectionRefusedError | 826 |
| gaierror | 273 |
| OSError | 17 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.997 | prefer | 112 | 1.0 | 144 |
| Au1rxx-base64 | 0.986 | prefer | 415 | 0.918 | 1745 |
| mheidari-all | 0.937 | prefer | 47 | 0.872 | 14522 |
| Surfboard-tg-mixed | 0.83 | prefer | 122 | 0.754 | 6399 |
| DeltaKronecker-all | 0.761 | prefer | 67 | 0.687 | 5415 |
| nscl5-all | 0.298 | observe | 1 | 1.0 | 1082 |
| 10ium-HighSpeed | 0.289 | observe | 1 | 1.0 | 839 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4989 |
| Epodonios-all | 0.255 | observe | 0 | None | 6941 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.687 | 46 | 21 | 67 |
| Surfboard-tg-mixed | 0.754 | 92 | 30 | 122 |
| mheidari-all | 0.872 | 41 | 6 | 47 |
| Au1rxx-base64 | 0.918 | 381 | 34 | 415 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| 10ium-HighSpeed | 1.0 | 1 | 0 | 1 |
| zhangkai | 1.0 | 112 | 0 | 112 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 14522 | yes | 2.27 | 0 |
| SoliSpirit-all | 6992 | yes | 2.15 | 0 |
| Epodonios-all | 6941 | yes | 2.43 | 0 |
| Surfboard-tg-mixed | 6399 | yes | 2.09 | 0 |
| barry-far-vless | 5469 | yes | 1.43 | 0 |
| DeltaKronecker-all | 5415 | yes | 2.59 | 0 |
| Surfboard-tg-vless | 5266 | yes | 1.92 | 0 |
| 10ium-ScrapeCategorize-Vless | 4989 | yes | 1.34 | 0 |
| mahdibland-V2RayAggregator | 4094 | yes | 0.44 | 0 |
| MatinGhanbari-all-sub | 3986 | yes | 1.59 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 31 |
| cn-block | 31 |
| 204 | 21 |
| speed | 9 |
