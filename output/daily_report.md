# AutoNodes 每日报告

生成时间：2026-09-22 11:29:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 97/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 1/106 |
| 原始节点数 | 91703 |
| 去重后节点数 | 25251 |
| TCP 可达数 | 3000 |
| 真测通过数 | 413 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 25251 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 10.4 |
| generate | 148.0 |
| geo | 1.5 |
| probe | 257.5 |
| real_test | 198.2 |
| tcp | 42.2 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 37 | 23 | 14 | 62.2% |
| hysteria2 | 17 | 16 | 1 | 94.1% |
| shadowsocks | 154 | 143 | 11 | 92.9% |
| socks | 4 | 1 | 3 | 25.0% |
| trojan | 16 | 5 | 11 | 31.2% |
| vless | 455 | 223 | 232 | 49.0% |
| vmess | 1 | 1 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:ClientOSError | 70 |
| geo:ClientOSError | 54 |
| speed:ClientOSError | 35 |
| 204:ProxyError | 27 |
| cn-block:TimeoutError | 25 |
| geo:TimeoutError | 25 |
| 204:TimeoutError | 19 |
| speed:TimeoutError | 11 |
| 204:ClientOSError | 3 |
| cn-block:ProxyError | 2 |
| speed:ProxyError | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 5737 |
| ConnectionRefusedError | 937 |
| gaierror | 384 |
| OSError | 234 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.904 | prefer | 295 | 0.841 | 1630 |
| ermaozi | 0.643 | observe | 33 | 0.636 | 369 |
| Surfboard-tg-mixed | 0.593 | observe | 150 | 0.513 | 7157 |
| mheidari-all | 0.406 | observe | 188 | 0.324 | 19835 |
| DeltaKronecker-all | 0.305 | observe | 10 | 0.3 | 6324 |
| xiaoji235-airport-v2ray-all | 0.287 | observe | 2 | 0.5 | 4242 |
| ermaozi-get_subscribe | 0.256 | observe | 4 | 0.5 | 393 |
| Epodonios-all | 0.255 | observe | 0 | None | 7495 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3995 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 9028 |

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
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.3 | 3 | 7 | 10 |
| mheidari-all | 0.324 | 61 | 127 | 188 |
| xiaoji235-airport-v2ray-all | 0.5 | 1 | 1 | 2 |
| ermaozi-get_subscribe | 0.5 | 2 | 2 | 4 |
| Surfboard-tg-mixed | 0.513 | 77 | 73 | 150 |
| ermaozi | 0.636 | 21 | 12 | 33 |
| Au1rxx-base64 | 0.841 | 248 | 47 | 295 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 19835 | yes | 4.96 | 0 |
| SoliSpirit-all | 9028 | yes | 3.32 | 0 |
| Epodonios-all | 7495 | yes | 3.42 | 0 |
| Surfboard-tg-mixed | 7157 | yes | 3.87 | 0 |
| DeltaKronecker-all | 6324 | yes | 2.16 | 0 |
| barry-far-vless | 5817 | yes | 2.38 | 0 |
| Surfboard-tg-vless | 5792 | yes | 5.9 | 0 |
| 10ium-ScrapeCategorize-Vless | 4915 | yes | 2.59 | 0 |
| mahdibland-V2RayAggregator | 4344 | yes | 3.13 | 0 |
| xiaoji235-airport-v2ray-all | 4242 | yes | 1.37 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 97 |
| geo | 79 |
| 204 | 49 |
| speed | 47 |
