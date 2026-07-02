# AutoNodes 每日报告

生成时间：2026-07-02 04:06:55

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 102/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 3/104 |
| 原始节点数 | 76385 |
| 去重后节点数 | 23479 |
| TCP 可达数 | 3000 |
| 真测通过数 | 601 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 23479 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.3 |
| generate | 25.0 |
| geo | 1.3 |
| probe | 57.0 |
| real_test | 150.0 |
| tcp | 31.1 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 6 | 3 | 3 | 50.0% |
| shadowsocks | 148 | 129 | 19 | 87.2% |
| socks | 36 | 31 | 5 | 86.1% |
| trojan | 139 | 124 | 15 | 89.2% |
| vless | 731 | 272 | 459 | 37.2% |
| vmess | 6 | 6 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 197 |
| geo:TimeoutError | 155 |
| geo:ClientOSError | 61 |
| speed:TimeoutError | 41 |
| cn-block:TimeoutError | 12 |
| 204:ClientOSError | 10 |
| 204:ProxyError | 8 |
| cn-block:ClientOSError | 7 |
| 204:TimeoutError | 4 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 2 |
| geo:status | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4432 |
| ConnectionRefusedError | 693 |
| OSError | 151 |
| gaierror | 150 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | prefer | 36 | 1.0 | 61 |
| Surfboard-tg-mixed | 0.831 | prefer | 339 | 0.752 | 5684 |
| Au1rxx-base64 | 0.79 | prefer | 68 | 0.794 | 108 |
| mheidari-all | 0.56 | observe | 304 | 0.48 | 16042 |
| DeltaKronecker-all | 0.39 | observe | 350 | 0.309 | 7631 |
| nscl5-all | 0.301 | observe | 1 | 1.0 | 1162 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4308 |
| Epodonios-all | 0.255 | observe | 0 | None | 6523 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ConfigWireguard | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ShadowsocksM | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-ViProxys | 0.025 | observe | 0 | None | 1 | 0 |
| xiaoji235-airport-v2ray-all | 0.141 | observe | 3 | 0.0 | 0 | 1293 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| xiaoji235-airport-v2ray-all | 0.0 | 0 | 3 | 3 |
| DeltaKronecker-all | 0.309 | 108 | 242 | 350 |
| mheidari-all | 0.48 | 146 | 158 | 304 |
| Surfboard-tg-mixed | 0.752 | 255 | 84 | 339 |
| Au1rxx-base64 | 0.794 | 54 | 14 | 68 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 16042 | yes | 2.95 | 0 |
| DeltaKronecker-all | 7631 | yes | 3.24 | 0 |
| SoliSpirit-all | 6669 | yes | 2.3 | 0 |
| Epodonios-all | 6523 | yes | 1.6 | 0 |
| Surfboard-tg-mixed | 5684 | yes | 1.89 | 0 |
| mahdibland-V2RayAggregator | 5331 | yes | 1.68 | 0 |
| barry-far-vless | 4744 | yes | 1.39 | 0 |
| 10ium-ScrapeCategorize-Vless | 4308 | yes | 1.55 | 0 |
| Surfboard-tg-vless | 4186 | yes | 2.01 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.67 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 238 |
| geo | 220 |
| 204 | 22 |
| cn-block | 21 |
