# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-14 01:17:57 |
| 运行耗时 | 245.2s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 40280 |
| 去重后节点 | 15578 |
| TCP 可达 | 1500 |
| 真实可用 | 376 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 15578 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| geo | 1.2 |
| tcp | 36.5 |
| real_test | 184.7 |
| generate | 19.9 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 21047 |
| shadowsocks | 8043 |
| trojan | 5601 |
| vmess | 5251 |
| hysteria2 | 127 |
| http | 86 |
| shadowsocksr | 85 |
| socks | 33 |
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
| 63.17 | http | 683.2 | 908.3 | 16.75 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.14.146 |
| 63.16 | http | 683.5 | 910.9 | 16.74 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.253 |
| 63.14 | http | 684.0 | 901.8 | 16.72 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.156 |
| 63.13 | http | 684.4 | 904.1 | 16.71 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.14.157 |
| 63.12 | http | 684.0 | 891.0 | 16.72 | 0.0 | 9.74 | 18.7 | 17.96 | snakem982 | 84.239.49.37 |
| 63.1 | http | 685.2 | 915.0 | 16.68 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.242 |
| 63.04 | http | 686.6 | 907.1 | 16.64 | 0.0 | 9.74 | 18.7 | 17.96 | snakem982 | 84.239.14.154 |
| 63.01 | http | 688.1 | 906.7 | 16.59 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.166 |
| 62.99 | http | 688.7 | 906.7 | 16.57 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.39 |
| 62.99 | http | 688.8 | 932.7 | 16.57 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.14.159 |
| 62.96 | http | 689.4 | 894.7 | 16.55 | 0.0 | 9.75 | 18.7 | 17.96 | snakem982 | 84.239.49.160 |
| 62.89 | http | 690.5 | 908.0 | 16.51 | 0.0 | 9.72 | 18.7 | 17.96 | snakem982 | 84.239.49.42 |
| 62.89 | http | 691.7 | 892.2 | 16.47 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.154 |
| 62.85 | http | 692.2 | 927.3 | 16.46 | 0.0 | 9.73 | 18.7 | 17.96 | snakem982 | 84.239.49.214 |
| 62.84 | http | 693.4 | 906.7 | 16.42 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.249 |
| 62.83 | http | 694.0 | 922.0 | 16.4 | 0.0 | 9.77 | 18.7 | 17.96 | snakem982 | 84.239.49.219 |
| 62.81 | http | 694.0 | 913.9 | 16.4 | 0.0 | 9.75 | 18.7 | 17.96 | snakem982 | 84.239.49.224 |
| 62.79 | http | 694.5 | 931.0 | 16.38 | 0.0 | 9.75 | 18.7 | 17.96 | snakem982 | 84.239.49.239 |
| 62.78 | http | 693.9 | 915.1 | 16.4 | 0.0 | 9.72 | 18.7 | 17.96 | snakem982 | 84.239.49.207 |
| 62.77 | http | 695.5 | 903.0 | 16.35 | 0.0 | 9.76 | 18.7 | 17.96 | snakem982 | 84.239.49.175 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.938 | 0.956 | 45 | 52 | prefer |
| roosterkid-openproxylist-v2ray | 0.574 | 0.571 | 35 | 150 | observe |
| Au1rxx-base64 | 0.442 | 0.435 | 108 | 135 | observe |
| Surfboard-tg-mixed | 0.377 | 0.296 | 658 | 4199 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| mheidari-all | 0.288 | 0.202 | 104 | 2000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3299 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| DeltaKronecker-all | 0.205 | 0.123 | 342 | 4955 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 499 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 476 | observe |
| mfuu-v2ray | 0.184 | None | 0 | 224 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 199 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 400 |
| 204 | ProxyError | - | 341 |
| speed | TimeoutError | - | 95 |
| 204 | TimeoutError | - | 75 |
| geo | status | 403 | 72 |
| speed | ClientOSError | - | 52 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 35 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| cn-block | TimeoutError | - | 8 |
| cn-block | ClientOSError | - | 7 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 3 |
| geo | TimeoutError | - | 3 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: decode public_key: illegal base64 data at input byte 44 | - | 2 |
| cn-block | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 207 | 300 | - |
| global | False | 215 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
