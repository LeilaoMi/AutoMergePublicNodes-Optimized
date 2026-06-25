# AutoNodes 每日报告

生成时间：2026-06-25 04:09:11

## 摘要

| 指标 | 值 |
| --- | --- |
| 健康状态 | warning |
| 健康检查通过 | True |
| 健康源数量 | 105/107 |
| 清理建议：禁用/降权 | 0/0 |
| 清理建议：优先/观察 | 2/105 |
| 原始节点数 | 75444 |
| 去重后节点数 | 22495 |
| TCP 可达数 | 3000 |
| 真测通过数 | 521 |
| verified 输出数 | 300 |
| global 输出数 | 300 |
| all 输出数 | 22495 |
| all 输出模式 | full |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.1 |
| generate | 30.3 |
| geo | 1.4 |
| probe | 50.1 |
| real_test | 114.1 |
| tcp | 29.7 |

## 协议通过率

| 协议 | 已测 | 通过 | 失败 | 通过率 |
| --- | --- | --- | --- | --- |
| http | 36 | 36 | 0 | 100.0% |
| hysteria2 | 4 | 3 | 1 | 75.0% |
| shadowsocks | 101 | 91 | 10 | 90.1% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 182 | 146 | 36 | 80.2% |
| vless | 444 | 240 | 204 | 54.1% |
| vmess | 4 | 4 | 0 | 100.0% |

## 主要真测错误

| 错误 | 数量 |
| --- | --- |
| speed:ClientOSError | 107 |
| geo:TimeoutError | 63 |
| speed:TimeoutError | 25 |
| geo:ClientOSError | 18 |
| cn-block:TimeoutError | 12 |
| 204:ClientOSError | 10 |
| cn-block:ClientOSError | 6 |
| 204:TimeoutError | 5 |
| 204:ProxyError | 2 |
| speed:ProxyError | 1 |
| cn-block:ProxyError | 1 |
| geo:status | 1 |

## TCP 预筛选错误

| 错误 | 数量 |
| --- | --- |
| TimeoutError | 4171 |
| ConnectionRefusedError | 616 |
| gaierror | 184 |
| OSError | 105 |

## 高评分订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 解析数 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.977 | prefer | 36 | 1.0 | 82 |
| Surfboard-tg-mixed | 0.829 | prefer | 285 | 0.751 | 5184 |
| Au1rxx-base64 | 0.694 | observe | 72 | 0.694 | 119 |
| mheidari-all | 0.676 | observe | 248 | 0.597 | 15443 |
| DeltaKronecker-all | 0.631 | observe | 125 | 0.552 | 6644 |
| nscl5-all | 0.357 | observe | 2 | 1.0 | 1136 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4745 |
| Epodonios-all | 0.255 | observe | 0 | None | 7785 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3999 |

## 需关注订阅源

| 订阅源 | 评分 | 建议 | 已测 | 通过率 | 连续死亡 | 解析数 |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 10 |

## 真测通过率较低的订阅源

| 订阅源 | 通过率 | 通过 | 失败 | 已测 |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 2 | 2 |
| DeltaKronecker-all | 0.552 | 69 | 56 | 125 |
| mheidari-all | 0.597 | 148 | 100 | 248 |
| Au1rxx-base64 | 0.694 | 50 | 22 | 72 |
| Surfboard-tg-mixed | 0.751 | 214 | 71 | 285 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| nscl5-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 36 | 0 | 36 |

## 解析节点数较高的订阅源

| 订阅源 | 节点数 | 是否正常 | 耗时 | 连续死亡 |
| --- | --- | --- | --- | --- |
| mheidari-all | 15443 | yes | 3.22 | 0 |
| Epodonios-all | 7785 | yes | 1.37 | 0 |
| SoliSpirit-all | 7191 | yes | 1.7 | 0 |
| DeltaKronecker-all | 6644 | yes | 3.3 | 0 |
| Surfboard-tg-mixed | 5184 | yes | 2.01 | 0 |
| 10ium-ScrapeCategorize-Vless | 4745 | yes | 1.1 | 0 |
| mahdibland-V2RayAggregator | 4710 | yes | 0.61 | 0 |
| barry-far-vless | 4704 | yes | 1.46 | 0 |
| MatinGhanbari-all-sub | 3999 | yes | 1.3 | 0 |
| Surfboard-tg-vless | 3909 | yes | 2.34 | 0 |

## 趋势报警

无趋势报警。

## 健康报警

### 真测错误报警
| 错误 | 数量 |
| --- | --- |
| speed | 133 |
| geo | 82 |
| cn-block | 19 |
| 204 | 17 |
