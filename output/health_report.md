# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.3.0 |
| 更新时间 | 2026-06-12 10:19:49 |
| 运行耗时 | 216.0s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 40228 |
| 去重后节点 | 15001 |
| TCP 可达 | 1500 |
| 真实可用 | 272 |
| Verified 输出 | 272 |
| Global 输出 | 286 |
| All 输出 | 15001 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.8 |
| geo | 1.2 |
| tcp | 34.8 |
| real_test | 150.1 |
| generate | 27.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 20462 |
| shadowsocks | 8024 |
| trojan | 6256 |
| vmess | 5085 |
| hysteria2 | 188 |
| shadowsocksr | 97 |
| http | 86 |
| socks | 23 |
| hysteria | 6 |
| tuic | 1 |

## 评分权重

| 因子 | 权重 |
| --- | --- |
| latency | 35.0 |
| jitter | 15.0 |
| tcp | 10.0 |
| protocol_history | 20.0 |
| source_history | 20.0 |

## Top 节点评分

| 评分 | 协议 | 延迟(ms) | 抖动(ms) | 延迟分 | 抖动分 | TCP分 | 协议历史分 | 来源历史分 | 来源 | 服务器 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56.89 | shadowsocks | 255.5 | 611.6 | 30.61 | 0.0 | 10.0 | 6.72 | 9.56 | Au1rxx-base64 | 37.19.198.160 |
| 56.22 | shadowsocks | 276.1 | 677.5 | 29.94 | 0.0 | 10.0 | 6.72 | 9.56 | Au1rxx-base64 | 37.19.198.236 |
| 55.88 | shadowsocks | 286.5 | 577.2 | 29.6 | 0.0 | 10.0 | 6.72 | 9.56 | Au1rxx-base64 | 37.19.198.243 |
| 55.77 | shadowsocks | 290.1 | 708.2 | 29.49 | 0.0 | 10.0 | 6.72 | 9.56 | Au1rxx-base64 | 37.19.198.244 |
| 54.79 | shadowsocks | 320.3 | 579.1 | 28.51 | 0.0 | 10.0 | 6.72 | 9.56 | Au1rxx-base64 | 156.146.38.169 |
| 54.67 | shadowsocks | 324.1 | 595.2 | 28.39 | 0.0 | 10.0 | 6.72 | 9.56 | Au1rxx-base64 | 156.146.38.167 |
| 54.63 | http | 983.6 | 594.7 | 7.01 | 0.0 | 9.76 | 18.7 | 19.16 | snakem982 | 84.239.49.224 |
| 54.57 | http | 985.6 | 614.8 | 6.95 | 0.0 | 9.76 | 18.7 | 19.16 | snakem982 | 84.239.49.201 |
| 54.48 | http | 988.4 | 597.0 | 6.86 | 0.0 | 9.76 | 18.7 | 19.16 | snakem982 | 84.239.49.164 |
| 54.4 | http | 990.8 | 600.8 | 6.78 | 0.0 | 9.76 | 18.7 | 19.16 | snakem982 | 84.239.49.225 |
| 54.3 | http | 994.3 | 601.5 | 6.67 | 0.0 | 9.77 | 18.7 | 19.16 | snakem982 | 84.239.49.42 |
| 54.29 | http | 992.9 | 638.5 | 6.71 | 0.0 | 9.72 | 18.7 | 19.16 | snakem982 | 84.239.49.39 |
| 54.28 | shadowsocks | 266.3 | 628.4 | 30.26 | 0.0 | 10.0 | 6.72 | 7.3 | Surfboard-tg-mixed | 45.55.40.127 |
| 54.21 | http | 993.9 | 654.2 | 6.68 | 0.0 | 9.67 | 18.7 | 19.16 | snakem982 | 84.239.49.166 |
| 54.18 | http | 997.4 | 637.9 | 6.56 | 0.0 | 9.76 | 18.7 | 19.16 | snakem982 | 84.239.14.152 |
| 54.15 | http | 998.6 | 580.8 | 6.53 | 0.0 | 9.76 | 18.7 | 19.16 | snakem982 | 84.239.49.227 |
| 54.07 | http | 999.2 | 611.4 | 6.51 | 0.0 | 9.7 | 18.7 | 19.16 | snakem982 | 84.239.49.176 |
| 54.06 | http | 1001.2 | 629.2 | 6.44 | 0.0 | 9.76 | 18.7 | 19.16 | snakem982 | 84.239.49.183 |
| 54.05 | http | 1002.0 | 590.6 | 6.42 | 0.0 | 9.77 | 18.7 | 19.16 | snakem982 | 84.239.49.171 |
| 54.02 | shadowsocks | 343.9 | 555.8 | 27.74 | 0.0 | 10.0 | 6.72 | 9.56 | Au1rxx-base64 | 156.146.38.170 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | 0.977 | 43 | 52 | prefer |
| Au1rxx-base64 | 0.531 | 0.527 | 74 | 106 | observe |
| mheidari-all | 0.28 | 0.194 | 93 | 2000 | observe |
| Surfboard-tg-mixed | 0.26 | 0.179 | 726 | 4171 | observe |
| roosterkid-openproxylist-v2ray | 0.256 | 0.227 | 22 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3165 | observe |
| barry-far-Sub2 | 0.195 | None | 0 | 494 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 476 | observe |
| mfuu-v2ray | 0.191 | None | 0 | 390 | observe |
| Barabama-yudou | 0.186 | 0.333 | 3 | 166 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 199 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |
| barry-far-vless | 0.181 | 0.071 | 14 | 2000 | downweight |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 488 |
| 204 | ClientOSError | - | 379 |
| 204 | TimeoutError | - | 112 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 57 |
| speed | ClientOSError | - | 43 |
| geo | status | 429 | 41 |
| geo | status | 403 | 30 |
| cn-block | TimeoutError | - | 19 |
| speed | TimeoutError | - | 14 |
| cn-block | ClientOSError | - | 13 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 3 |
| geo | ClientOSError | - | 3 |
| cn-block | ProxyError | - | 3 |
| geo | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 272 | - |
| global | False | 300 | 286 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
