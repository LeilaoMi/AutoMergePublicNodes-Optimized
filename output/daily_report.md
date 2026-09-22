# AutoNodes 每日报告

生成时间：2026-09-22 16:49:09

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 84229 |
| 去重后节点数 | 23642 |
| TCP 可达数 | 3000 |
| 真测通过数 | 405 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23642 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 9.5 |
| generate | 28.1 |
| geo | 1.4 |
| probe | 258.1 |
| real_test | 179.4 |
| tcp | 38.9 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 30 | 22 | 8 | 73.3% |
| hysteria2 | 15 | 12 | 3 | 80.0% |
| shadowsocks | 162 | 151 | 11 | 93.2% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 14 | 7 | 7 | 50.0% |
| vless | 357 | 212 | 145 | 59.4% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 54 |
| geo:ClientOSError | 34 |
| 204:TimeoutError | 22 |
| 204:ProxyError | 15 |
| cn-block:TimeoutError | 14 |
| cn-block:ClientOSError | 12 |
| geo:TimeoutError | 8 |
| speed:TimeoutError | 6 |
| cn-block:ProxyError | 4 |
| 204:ClientOSError | 4 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41535: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5593 |
| ConnectionRefusedError | 835 |
| gaierror | 278 |
| OSError | 16 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.924 | prefer | 296 | 0.858 | 1703 |
| DeltaKronecker-all | 0.83 | prefer | 30 | 0.767 | 6324 |
| ermaozi | 0.763 | prefer | 26 | 0.769 | 325 |
| mheidari-all | 0.642 | observe | 71 | 0.563 | 16289 |
| Surfboard-tg-mixed | 0.511 | observe | 151 | 0.43 | 7076 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| tg-oneclickvpnkeys | 0.26 | observe | 1 | 1.0 | 132 |
| Epodonios-all | 0.255 | observe | 0 | None | 7611 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3996 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9154 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-abc_configs | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ernoxin_shop | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 1 | 1 |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| ermaozi-get_subscribe | 0.333 | 1 | 2 | 3 |
| Surfboard-tg-mixed | 0.43 | 65 | 86 | 151 |
| mheidari-all | 0.563 | 40 | 31 | 71 |
| DeltaKronecker-all | 0.767 | 23 | 7 | 30 |
| ermaozi | 0.769 | 20 | 6 | 26 |
| Au1rxx-base64 | 0.858 | 254 | 42 | 296 |
| tg-oneclickvpnkeys | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16289 | yes | 3.45 | 0 |
| SoliSpirit-all | 9154 | yes | 3.71 | 0 |
| Epodonios-all | 7611 | yes | 3.61 | 0 |
| Surfboard-tg-mixed | 7076 | yes | 3.09 | 0 |
| DeltaKronecker-all | 6324 | yes | 3.23 | 0 |
| barry-far-vless | 6010 | yes | 1.76 | 0 |
| Surfboard-tg-vless | 5712 | yes | 2.74 | 0 |
| 10ium-ScrapeCategorize-Vless | 4915 | yes | 1.38 | 0 |
| mahdibland-V2RayAggregator | 4344 | yes | 1.25 | 0 |
| xiaoji235-airport-v2ray-all | 4242 | yes | 2.86 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 60 |
| geo | 44 |
| 204 | 41 |
| cn-block | 30 |
| sing-box exited 1 | 1 |
