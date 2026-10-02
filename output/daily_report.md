# AutoNodes 每日报告

生成时间：2026-10-02 12:24:27

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 94/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 4/103 |
| 原始节点数 | 97754 |
| 去重后节点数 | 26970 |
| TCP 可达数 | 3000 |
| 真测通过数 | 392 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 26970 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 5.5 |
| generate | 71.2 |
| geo | 1.5 |
| probe | 272.6 |
| real_test | 235.5 |
| tcp | 46.3 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| anytls | 1 | 1 | 0 | 100.0% |
| http | 23 | 21 | 2 | 91.3% |
| hysteria2 | 28 | 23 | 5 | 82.1% |
| shadowsocks | 153 | 137 | 16 | 89.5% |
| socks | 3 | 1 | 2 | 33.3% |
| trojan | 17 | 13 | 4 | 76.5% |
| vless | 278 | 196 | 82 | 70.5% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| cn-block:TimeoutError | 32 |
| 204:TimeoutError | 22 |
| speed:ClientOSError | 12 |
| speed:TimeoutError | 11 |
| 204:ProxyError | 9 |
| cn-block:ClientOSError | 8 |
| geo:TimeoutError | 6 |
| 204:ClientOSError | 4 |
| cn-block:ProxyError | 2 |
| geo:ClientOSError | 2 |
| geo:ProxyError | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:44860: bind: address already in use | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 6431 |
| ConnectionRefusedError | 1138 |
| gaierror | 435 |
| OSError | 233 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.893 | prefer | 291 | 0.828 | 1673 |
| ermaozi | 0.871 | prefer | 24 | 0.875 | 618 |
| mheidari-all | 0.817 | prefer | 55 | 0.745 | 23059 |
| Surfboard-tg-mixed | 0.76 | prefer | 123 | 0.683 | 7176 |
| DeltaKronecker-all | 0.337 | observe | 7 | 0.429 | 4981 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| Pawdroid | 0.255 | observe | 1 | 1.0 | 12 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 5276 |
| Epodonios-all | 0.255 | observe | 0 | None | 7676 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3997 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| abc-configs-readme-latest30 | 0.025 | observe | 0 | None | 1 | 0 |
| mfuu-v2ray | 0.025 | observe | 0 | None | 1 | 0 |
| nscl5-all | 0.025 | observe | 0 | None | 1 | 0 |
| snakem982 | 0.025 | observe | 0 | None | 1 | 0 |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-CaV2ray | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Letiranbreath | 0.025 | observe | 0 | None | 1 | 0 |
| tg-Parsashonam | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| tg-V2RAYProxy | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.429 | 3 | 4 | 7 |
| Surfboard-tg-mixed | 0.683 | 84 | 39 | 123 |
| mheidari-all | 0.745 | 41 | 14 | 55 |
| Au1rxx-base64 | 0.828 | 241 | 50 | 291 |
| ermaozi | 0.875 | 21 | 3 | 24 |
| Pawdroid | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 23059 | yes | 4.07 | 0 |
| SoliSpirit-all | 9234 | yes | 2.78 | 0 |
| Epodonios-all | 7676 | yes | 2.78 | 0 |
| Surfboard-tg-mixed | 7176 | yes | 2.55 | 0 |
| xiaoji235-airport-v2ray-all | 6752 | yes | 2.34 | 0 |
| barry-far-vless | 6070 | yes | 2.45 | 0 |
| Surfboard-tg-vless | 5828 | yes | 3.1 | 0 |
| 10ium-ScrapeCategorize-Vless | 5276 | yes | 2.17 | 0 |
| DeltaKronecker-all | 4981 | yes | 7.5 | 0 |
| mahdibland-V2RayAggregator | 4310 | yes | 0.12 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| cn-block | 42 |
| 204 | 35 |
| speed | 23 |
| geo | 10 |
| sing-box exited 1 | 1 |
