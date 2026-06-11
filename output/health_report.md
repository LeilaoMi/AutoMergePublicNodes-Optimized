# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.2.0 |
| 更新时间 | 2026-06-11 23:46:52 |
| 运行耗时 | 204.1s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 39955 |
| 去重后节点 | 15027 |
| TCP 可达 | 1500 |
| 真实可用 | 325 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 15027 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| geo | 1.1 |
| tcp | 35.8 |
| real_test | 139.1 |
| generate | 25.1 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 20391 |
| shadowsocks | 7985 |
| trojan | 6037 |
| vmess | 5130 |
| hysteria2 | 184 |
| shadowsocksr | 90 |
| http | 86 |
| socks | 41 |
| hysteria | 6 |
| anytls | 4 |
| tuic | 1 |

## Top 节点评分

| 评分 | 协议 | 延迟(ms) | 抖动(ms) | 来源 | 服务器 |
| --- | --- | --- | --- | --- | --- |
| 56.99 | shadowsocks | 253.9 | 602.9 | Au1rxx-base64 | 37.19.198.160 |
| 56.88 | shadowsocks | 257.3 | 612.6 | Au1rxx-base64 | 37.19.198.244 |
| 56.33 | shadowsocks | 274.2 | 584.5 | Au1rxx-base64 | 37.19.198.243 |
| 55.31 | shadowsocks | 305.7 | 754.5 | Au1rxx-base64 | 37.19.198.236 |
| 54.78 | shadowsocks | 321.9 | 597.1 | Au1rxx-base64 | 156.146.38.170 |
| 54.76 | shadowsocks | 322.7 | 603.1 | Au1rxx-base64 | 156.146.38.169 |
| 54.69 | shadowsocks | 324.8 | 596.4 | Au1rxx-base64 | 156.146.38.167 |
| 54.29 | http | 992.4 | 615.4 | snakem982 | 84.239.49.155 |
| 54.2 | http | 995.3 | 619.0 | snakem982 | 84.239.49.156 |
| 54.03 | http | 1000.5 | 642.5 | snakem982 | 84.239.49.154 |
| 54.0 | http | 1001.5 | 631.4 | snakem982 | 84.239.49.39 |
| 53.99 | http | 1001.6 | 627.2 | snakem982 | 84.239.49.164 |
| 53.99 | http | 1001.8 | 626.1 | snakem982 | 84.239.49.171 |
| 53.97 | http | 1002.4 | 626.7 | snakem982 | 84.239.49.166 |
| 53.96 | http | 1002.7 | 621.4 | snakem982 | 84.239.49.160 |
| 53.95 | http | 1002.7 | 620.1 | snakem982 | 84.239.49.254 |
| 53.95 | http | 1003.2 | 621.2 | snakem982 | 84.239.49.242 |
| 53.91 | http | 1004.1 | 623.1 | snakem982 | 84.239.49.175 |
| 53.83 | http | 1006.6 | 607.0 | snakem982 | 84.239.49.223 |
| 53.81 | http | 1007.3 | 612.0 | snakem982 | 84.239.14.154 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | 0.977 | 43 | 52 | prefer |
| Au1rxx-base64 | 0.553 | 0.551 | 69 | 88 | observe |
| Surfboard-tg-mixed | 0.308 | 0.227 | 717 | 4225 | observe |
| roosterkid-openproxylist-v2ray | 0.306 | 0.286 | 28 | 150 | observe |
| mheidari-all | 0.282 | 0.196 | 92 | 2000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3224 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| DeltaKronecker-all | 0.2 | 0.119 | 463 | 4660 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 501 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 473 | observe |
| mfuu-v2ray | 0.19 | None | 0 | 387 | observe |
| Barabama-yudou | 0.186 | 0.333 | 3 | 166 | observe |
| Epodonios-all | 0.184 | 0.0 | 2 | 3000 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 199 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 506 |
| 204 | ProxyError | - | 365 |
| geo | status | 429 | 73 |
| 204 | TimeoutError | - | 69 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 52 |
| geo | status | 403 | 38 |
| cn-block | TimeoutError | - | 16 |
| cn-block | ClientOSError | - | 11 |
| speed | ClientOSError | - | 9 |
| speed | TimeoutError | - | 9 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 3 |
| geo | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] decode config at /tmp/sb-p3ai_8oq/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | - | 1 |
| sing-box exited 1 |  [31mFATAL[0m[0000] decode config at /tmp/sb-6ftjci7x/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
