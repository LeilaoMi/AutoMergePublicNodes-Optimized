# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-14 09:40:54 |
| 运行耗时 | 229.1s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 40316 |
| 去重后节点 | 15630 |
| TCP 可达 | 1500 |
| 真实可用 | 239 |
| Verified 输出 | 239 |
| Global 输出 | 248 |
| All 输出 | 15630 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| geo | 1.2 |
| tcp | 35.7 |
| real_test | 173.4 |
| generate | 16.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 20856 |
| shadowsocks | 8250 |
| trojan | 5826 |
| vmess | 5038 |
| hysteria2 | 130 |
| shadowsocksr | 93 |
| http | 86 |
| socks | 30 |
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
| 63.23 | http | 689.8 | 912.7 | 16.53 | 0.0 | 9.62 | 18.7 | 18.38 | snakem982 | 84.239.49.219 |
| 63.21 | http | 690.0 | 896.5 | 16.53 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.166 |
| 63.12 | http | 697.2 | 914.1 | 16.29 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.49.249 |
| 63.08 | http | 697.4 | 919.8 | 16.29 | 0.0 | 9.71 | 18.7 | 18.38 | snakem982 | 84.239.49.223 |
| 63.05 | http | 695.8 | 950.3 | 16.34 | 0.0 | 9.63 | 18.7 | 18.38 | snakem982 | 84.239.49.183 |
| 62.83 | http | 704.8 | 914.3 | 16.05 | 0.0 | 9.7 | 18.7 | 18.38 | snakem982 | 84.239.49.253 |
| 62.81 | http | 701.9 | 927.7 | 16.14 | 0.0 | 9.59 | 18.7 | 18.38 | snakem982 | 84.239.49.160 |
| 62.81 | http | 705.1 | 892.5 | 16.04 | 0.0 | 9.69 | 18.7 | 18.38 | snakem982 | 84.239.49.175 |
| 62.79 | http | 705.8 | 931.7 | 16.02 | 0.0 | 9.69 | 18.7 | 18.38 | snakem982 | 84.239.14.146 |
| 62.77 | http | 707.0 | 940.2 | 15.98 | 0.0 | 9.71 | 18.7 | 18.38 | snakem982 | 84.239.49.37 |
| 62.74 | http | 707.1 | 942.6 | 15.97 | 0.0 | 9.69 | 18.7 | 18.38 | snakem982 | 84.239.49.215 |
| 62.67 | http | 708.5 | 912.6 | 15.93 | 0.0 | 9.66 | 18.7 | 18.38 | snakem982 | 84.239.49.207 |
| 62.67 | http | 709.3 | 932.3 | 15.9 | 0.0 | 9.69 | 18.7 | 18.38 | snakem982 | 84.239.49.227 |
| 62.66 | http | 707.0 | 894.0 | 15.98 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.245 |
| 62.66 | http | 709.7 | 939.6 | 15.89 | 0.0 | 9.69 | 18.7 | 18.38 | snakem982 | 84.239.49.154 |
| 62.66 | http | 710.1 | 952.5 | 15.88 | 0.0 | 9.7 | 18.7 | 18.38 | snakem982 | 84.239.49.224 |
| 62.64 | http | 709.6 | 941.9 | 15.89 | 0.0 | 9.67 | 18.7 | 18.38 | snakem982 | 84.239.49.191 |
| 62.63 | http | 711.2 | 914.6 | 15.84 | 0.0 | 9.71 | 18.7 | 18.38 | snakem982 | 84.239.14.149 |
| 62.63 | http | 712.8 | 893.0 | 15.79 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.234 |
| 62.61 | http | 708.0 | 944.2 | 15.95 | 0.0 | 9.58 | 18.7 | 18.38 | snakem982 | 84.239.49.156 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.919 | 0.935 | 46 | 52 | prefer |
| roosterkid-openproxylist-v2ray | 0.66 | 0.667 | 24 | 150 | observe |
| Au1rxx-base64 | 0.474 | 0.468 | 109 | 140 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3281 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mheidari-all | 0.247 | 0.159 | 88 | 2000 | downweight |
| Surfboard-tg-mixed | 0.219 | 0.138 | 637 | 4190 | downweight |
| Epodonios-all | 0.202 | 0.111 | 72 | 3000 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 493 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 481 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 197 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |
| Au1rxx-clash | 0.181 | None | 0 | 140 | observe |
| chromego_merge | 0.177 | None | 0 | 48 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 590 |
| 204 | ProxyError | - | 343 |
| 204 | TimeoutError | - | 103 |
| geo | status | 429 | 58 |
| geo | status | 403 | 50 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 35 |
| speed | ClientOSError | - | 18 |
| cn-block | TimeoutError | - | 12 |
| speed | TimeoutError | - | 10 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| cn-block | ProxyError | - | 5 |
| cn-block | ClientOSError | - | 5 |
| geo | ProxyError | - | 5 |
| geo | ClientOSError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 239 | - |
| global | False | 300 | 248 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
