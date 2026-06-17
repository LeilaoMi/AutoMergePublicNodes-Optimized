# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-17 11:04:56 |
| 运行耗时 | 279.6s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 43351 |
| 去重后节点 | 17819 |
| TCP 可达 | 1500 |
| 真实可用 | 258 |
| Verified 输出 | 258 |
| Global 输出 | 277 |
| All 输出 | 17819 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.4 |
| geo | 1.2 |
| tcp | 40.2 |
| real_test | 193.6 |
| generate | 41.2 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 21891 |
| shadowsocks | 8436 |
| trojan | 6933 |
| vmess | 5698 |
| hysteria2 | 167 |
| shadowsocksr | 88 |
| http | 86 |
| socks | 45 |
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
| 63.65 | http | 681.2 | 901.0 | 16.81 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.157 |
| 63.64 | http | 681.4 | 907.3 | 16.81 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.49.249 |
| 63.54 | http | 684.5 | 893.3 | 16.71 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.49.160 |
| 63.54 | http | 684.7 | 890.0 | 16.7 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.171 |
| 63.49 | http | 686.1 | 911.8 | 16.65 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.207 |
| 63.42 | http | 688.3 | 896.1 | 16.58 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.155 |
| 63.37 | http | 689.5 | 914.5 | 16.54 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.49.239 |
| 63.36 | http | 689.9 | 925.7 | 16.53 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.14.149 |
| 63.36 | http | 690.1 | 909.2 | 16.53 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.14.157 |
| 63.36 | http | 690.4 | 913.6 | 16.52 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.39 |
| 63.33 | http | 691.1 | 899.0 | 16.49 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.227 |
| 63.31 | http | 691.7 | 900.7 | 16.47 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.191 |
| 63.31 | http | 691.7 | 910.6 | 16.47 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.219 |
| 63.3 | http | 691.9 | 925.9 | 16.47 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.49.166 |
| 63.29 | http | 692.4 | 916.8 | 16.45 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.234 |
| 63.29 | http | 692.4 | 928.2 | 16.45 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.231 |
| 63.28 | http | 691.4 | 930.3 | 16.48 | 0.0 | 9.72 | 18.7 | 18.38 | snakem982 | 84.239.49.225 |
| 63.23 | http | 693.6 | 898.4 | 16.41 | 0.0 | 9.74 | 18.7 | 18.38 | snakem982 | 84.239.49.183 |
| 63.22 | http | 694.3 | 925.9 | 16.39 | 0.0 | 9.75 | 18.7 | 18.38 | snakem982 | 84.239.49.253 |
| 63.2 | http | 695.2 | 925.1 | 16.36 | 0.0 | 9.76 | 18.7 | 18.38 | snakem982 | 84.239.49.223 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.917 | 0.933 | 45 | 52 | prefer |
| Au1rxx-base64 | 0.517 | 0.512 | 80 | 109 | observe |
| roosterkid-openproxylist-v2ray | 0.47 | 0.462 | 26 | 150 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3522 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mheidari-all | 0.25 | 0.163 | 86 | 2000 | observe |
| Surfboard-tg-mixed | 0.219 | 0.138 | 789 | 4546 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 495 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 477 | observe |
| DeltaKronecker-all | 0.193 | 0.111 | 342 | 7763 | downweight |
| Epodonios-all | 0.184 | 0.0 | 2 | 3000 | observe |
| mfuu-v2ray | 0.184 | None | 0 | 231 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 197 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 510 |
| 204 | ProxyError | - | 348 |
| 204 | TimeoutError | - | 111 |
| geo | status | 429 | 83 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 58 |
| geo | status | 403 | 45 |
| cn-block | TimeoutError | - | 22 |
| speed | ClientOSError | - | 13 |
| speed | TimeoutError | - | 10 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| cn-block | ClientOSError | - | 7 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 5 |
| speed | ProxyError | - | 5 |
| geo | TimeoutError | - | 4 |
| geo | ClientOSError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 258 | - |
| global | False | 300 | 277 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
