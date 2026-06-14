# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-14 19:32:57 |
| 运行耗时 | 274.6s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 41035 |
| 去重后节点 | 15688 |
| TCP 可达 | 1500 |
| 真实可用 | 214 |
| Verified 输出 | 214 |
| Global 输出 | 219 |
| All 输出 | 15688 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| geo | 1.3 |
| tcp | 39.2 |
| real_test | 193.2 |
| generate | 37.7 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 21848 |
| shadowsocks | 7982 |
| trojan | 5745 |
| vmess | 5085 |
| hysteria2 | 145 |
| shadowsocksr | 88 |
| http | 86 |
| socks | 49 |
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
| 61.17 | http | 740.0 | 970.2 | 14.91 | 0.0 | 9.6 | 18.7 | 17.96 | snakem982 | 84.239.49.157 |
| 61.0 | http | 743.2 | 946.5 | 14.8 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.14.152 |
| 60.96 | http | 744.6 | 988.4 | 14.76 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.14.159 |
| 60.85 | http | 748.3 | 972.8 | 14.64 | 0.0 | 9.55 | 18.7 | 17.96 | snakem982 | 84.239.49.40 |
| 60.79 | http | 749.7 | 973.2 | 14.59 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.49.156 |
| 60.74 | http | 750.4 | 951.9 | 14.57 | 0.0 | 9.51 | 18.7 | 17.96 | snakem982 | 84.239.49.224 |
| 60.73 | http | 751.1 | 964.3 | 14.55 | 0.0 | 9.52 | 18.7 | 17.96 | snakem982 | 84.239.49.231 |
| 60.72 | http | 751.6 | 923.7 | 14.53 | 0.0 | 9.53 | 18.7 | 17.96 | snakem982 | 84.239.49.227 |
| 60.71 | http | 751.5 | 973.9 | 14.54 | 0.0 | 9.51 | 18.7 | 17.96 | snakem982 | 84.239.14.157 |
| 60.67 | http | 746.4 | 955.9 | 14.7 | 0.0 | 9.31 | 18.7 | 17.96 | snakem982 | 84.239.49.171 |
| 60.58 | http | 756.5 | 974.3 | 14.37 | 0.0 | 9.55 | 18.7 | 17.96 | snakem982 | 84.239.49.42 |
| 60.54 | http | 757.6 | 978.0 | 14.34 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.14.154 |
| 60.48 | http | 759.2 | 996.5 | 14.28 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.49.201 |
| 60.46 | http | 761.1 | 979.4 | 14.22 | 0.0 | 9.58 | 18.7 | 17.96 | snakem982 | 84.239.14.158 |
| 60.45 | http | 760.2 | 974.2 | 14.25 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.49.245 |
| 60.43 | http | 753.7 | 966.9 | 14.46 | 0.0 | 9.31 | 18.7 | 17.96 | snakem982 | 84.239.49.155 |
| 60.41 | http | 759.9 | 996.9 | 14.26 | 0.0 | 9.49 | 18.7 | 17.96 | snakem982 | 84.239.49.225 |
| 60.39 | http | 760.3 | 957.0 | 14.25 | 0.0 | 9.48 | 18.7 | 17.96 | snakem982 | 84.239.49.37 |
| 60.39 | http | 762.1 | 958.5 | 14.19 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.49.253 |
| 60.36 | http | 762.9 | 972.4 | 14.16 | 0.0 | 9.54 | 18.7 | 17.96 | snakem982 | 84.239.49.175 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.917 | 0.933 | 45 | 52 | prefer |
| Au1rxx-base64 | 0.578 | 0.575 | 87 | 122 | observe |
| roosterkid-openproxylist-v2ray | 0.32 | 0.303 | 33 | 150 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3622 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| mheidari-all | 0.218 | 0.13 | 92 | 2000 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 500 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 477 | observe |
| Surfboard-tg-mixed | 0.193 | 0.112 | 759 | 4520 | downweight |
| mfuu-v2ray | 0.183 | None | 0 | 202 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |
| nscl5-all | 0.181 | 0.167 | 6 | 1123 | downweight |
| Au1rxx-clash | 0.18 | None | 0 | 122 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 489 |
| 204 | ClientOSError | - | 375 |
| 204 | TimeoutError | - | 184 |
| geo | status | 429 | 62 |
| geo | status | 403 | 44 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 42 |
| cn-block | TimeoutError | - | 22 |
| speed | ClientOSError | - | 13 |
| speed | TimeoutError | - | 13 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| geo | TimeoutError | - | 6 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 4 |
| cn-block | ClientOSError | - | 4 |
| speed | ClientPayloadError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] decode config at /tmp/sb-6we7hjom/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 234 | 214 | - |
| global | False | 240 | 219 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
