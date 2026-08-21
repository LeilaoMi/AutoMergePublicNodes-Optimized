# AutoNodes 每日报告

生成时间：2026-08-21 07:01:45

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 100/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 94128 |
| 去重后节点数 | 24576 |
| TCP 可达数 | 3000 |
| 真测通过数 | 1153 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 24576 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.4 |
| generate | 38.1 |
| geo | 0.8 |
| probe | 68.1 |
| real_test | 206.8 |
| tcp | 38.6 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 111 | 111 | 0 | 100.0% |
| hysteria2 | 23 | 22 | 1 | 95.7% |
| shadowsocks | 194 | 184 | 10 | 94.8% |
| socks | 4 | 2 | 2 | 50.0% |
| trojan | 625 | 615 | 10 | 98.4% |
| vless | 366 | 215 | 151 | 58.7% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| geo:TimeoutError | 52 |
| speed:TimeoutError | 30 |
| geo:ClientOSError | 26 |
| 204:TimeoutError | 21 |
| cn-block:TimeoutError | 19 |
| 204:ProxyError | 10 |
| speed:ClientOSError | 9 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| cn-block:ClientOSError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4879 |
| ConnectionRefusedError | 939 |
| gaierror | 521 |
| OSError | 225 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 1.0 | prefer | 640 | 0.952 | 1607 |
| zhangkai | 0.988 | prefer | 112 | 0.991 | 144 |
| mheidari-all | 0.894 | prefer | 305 | 0.816 | 21864 |
| Surfboard-tg-mixed | 0.83 | prefer | 230 | 0.752 | 6368 |
| nscl5-all | 0.391 | observe | 2 | 1.0 | 3031 |
| roosterkid-openproxylist-v2ray | 0.317 | observe | 2 | 1.0 | 150 |
| DeltaKronecker-all | 0.296 | observe | 35 | 0.2 | 6250 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5148 |
| Epodonios-all | 0.255 | observe | 0 | None | 7077 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3988 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-An0nymousTeam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2RAYProxy | 0.136 | observe | 1 | 0.0 | 0 | 217 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.2 | 7 | 28 | 35 |
| Surfboard-tg-mixed | 0.752 | 173 | 57 | 230 |
| mheidari-all | 0.816 | 249 | 56 | 305 |
| Au1rxx-base64 | 0.952 | 609 | 31 | 640 |
| zhangkai | 0.991 | 111 | 1 | 112 |
| roosterkid-openproxylist-v2ray | 1.0 | 2 | 0 | 2 |
| nscl5-all | 1.0 | 2 | 0 | 2 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 21864 | yes | 5.12 | 0 |
| Epodonios-all | 7077 | yes | 4.51 | 0 |
| SoliSpirit-all | 7024 | yes | 5.28 | 0 |
| Surfboard-tg-mixed | 6368 | yes | 3.17 | 0 |
| DeltaKronecker-all | 6250 | yes | 5.01 | 0 |
| xiaoji235-airport-v2ray-all | 5974 | yes | 3.02 | 0 |
| barry-far-vless | 5415 | yes | 2.26 | 0 |
| 10ium-ScrapeCategorize-Vless | 5148 | yes | 2.58 | 0 |
| Surfboard-tg-vless | 5051 | yes | 3.37 | 0 |
| mahdibland-V2RayAggregator | 4647 | yes | 0.39 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| geo | 78 |
| speed | 39 |
| 204 | 35 |
| cn-block | 22 |
