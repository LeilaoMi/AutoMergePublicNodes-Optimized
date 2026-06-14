# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-14 14:10:42 |
| 运行耗时 | 249.6s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 40637 |
| 去重后节点 | 15778 |
| TCP 可达 | 1500 |
| 真实可用 | 234 |
| Verified 输出 | 234 |
| Global 输出 | 240 |
| All 输出 | 15778 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.3 |
| geo | 1.2 |
| tcp | 39.6 |
| real_test | 171.9 |
| generate | 33.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 21417 |
| shadowsocks | 8099 |
| trojan | 5872 |
| vmess | 4889 |
| hysteria2 | 130 |
| shadowsocksr | 92 |
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
| 61.93 | http | 729.3 | 934.8 | 15.25 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.207 |
| 61.79 | http | 733.7 | 942.0 | 15.11 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.166 |
| 61.78 | http | 733.9 | 941.0 | 15.1 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.219 |
| 61.71 | http | 736.2 | 937.9 | 15.03 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.223 |
| 61.43 | http | 741.4 | 959.5 | 14.86 | 0.0 | 9.49 | 18.7 | 18.38 | snakem982 | 84.239.49.37 |
| 61.42 | http | 744.5 | 969.2 | 14.76 | 0.0 | 9.58 | 18.7 | 18.38 | snakem982 | 84.239.49.201 |
| 61.42 | http | 744.7 | 969.2 | 14.75 | 0.0 | 9.59 | 18.7 | 18.38 | snakem982 | 84.239.49.234 |
| 61.33 | http | 744.6 | 986.1 | 14.76 | 0.0 | 9.49 | 18.7 | 18.38 | snakem982 | 84.239.49.157 |
| 61.3 | http | 748.9 | 933.1 | 14.62 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.160 |
| 61.22 | http | 751.4 | 973.3 | 14.54 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.49.164 |
| 61.2 | http | 750.4 | 944.6 | 14.57 | 0.0 | 9.55 | 18.7 | 18.38 | snakem982 | 84.239.49.225 |
| 61.2 | http | 751.9 | 929.0 | 14.52 | 0.0 | 9.6 | 18.7 | 18.38 | snakem982 | 84.239.14.149 |
| 61.19 | http | 749.2 | 952.8 | 14.61 | 0.0 | 9.5 | 18.7 | 18.38 | snakem982 | 84.239.49.171 |
| 61.14 | http | 751.7 | 960.9 | 14.53 | 0.0 | 9.53 | 18.7 | 18.38 | snakem982 | 84.239.49.191 |
| 61.12 | http | 751.5 | 987.5 | 14.54 | 0.0 | 9.5 | 18.7 | 18.38 | snakem982 | 84.239.49.176 |
| 61.09 | http | 754.4 | 952.3 | 14.44 | 0.0 | 9.57 | 18.7 | 18.38 | snakem982 | 84.239.49.249 |
| 61.07 | http | 752.9 | 964.5 | 14.49 | 0.0 | 9.5 | 18.7 | 18.38 | snakem982 | 84.239.49.154 |
| 61.03 | http | 754.9 | 967.3 | 14.42 | 0.0 | 9.53 | 18.7 | 18.38 | snakem982 | 84.239.14.159 |
| 61.02 | http | 754.9 | 975.7 | 14.42 | 0.0 | 9.52 | 18.7 | 18.38 | snakem982 | 84.239.49.155 |
| 60.88 | http | 759.2 | 975.7 | 14.28 | 0.0 | 9.52 | 18.7 | 18.38 | snakem982 | 84.239.14.154 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.898 | 0.913 | 46 | 52 | prefer |
| Au1rxx-base64 | 0.599 | 0.597 | 72 | 105 | observe |
| roosterkid-openproxylist-v2ray | 0.492 | 0.485 | 33 | 150 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3454 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mheidari-all | 0.22 | 0.132 | 91 | 2000 | downweight |
| Surfboard-tg-mixed | 0.217 | 0.136 | 686 | 4381 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 500 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 479 | observe |
| Barabama-yudou | 0.186 | 0.333 | 3 | 166 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 200 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |
| mfuu-v2ray | 0.18 | None | 0 | 118 | observe |
| Au1rxx-clash | 0.179 | None | 0 | 105 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 471 |
| 204 | ClientOSError | - | 406 |
| 204 | TimeoutError | - | 113 |
| geo | status | 429 | 75 |
| geo | status | 403 | 58 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 46 |
| cn-block | TimeoutError | - | 12 |
| speed | ClientOSError | - | 11 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 9 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| cn-block | ClientOSError | - | 6 |
| speed | TimeoutError | - | 6 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: {� | צ����� | - | 3 |
| geo | TimeoutError | - | 3 |
| geo | ProxyError | - | 3 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 239 | 234 | - |
| global | False | 248 | 240 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
