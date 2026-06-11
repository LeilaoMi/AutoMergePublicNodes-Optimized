# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.2.0 |
| 更新时间 | 2026-06-11 23:42:36 |
| 运行耗时 | 203.8s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 39955 |
| 去重后节点 | 15027 |
| TCP 可达 | 1500 |
| 真实可用 | 301 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 15027 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.0 |
| geo | 1.2 |
| tcp | 35.8 |
| real_test | 138.6 |
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
| 57.93 | shadowsocks | 270.5 | 603.2 | Au1rxx-base64 | 37.19.198.243 |
| 57.93 | shadowsocks | 270.6 | 598.5 | Au1rxx-base64 | 37.19.198.160 |
| 57.89 | shadowsocks | 271.7 | 614.2 | Au1rxx-base64 | 37.19.198.244 |
| 56.57 | shadowsocks | 312.6 | 723.4 | Au1rxx-base64 | 37.19.198.236 |
| 55.9 | shadowsocks | 333.0 | 584.7 | Au1rxx-base64 | 156.146.38.168 |
| 55.58 | shadowsocks | 342.9 | 697.1 | Au1rxx-base64 | 149.28.255.6 |
| 55.29 | shadowsocks | 351.8 | 686.9 | Au1rxx-base64 | 156.146.38.169 |
| 55.22 | shadowsocks | 354.2 | 695.8 | Au1rxx-base64 | 156.146.38.170 |
| 54.15 | shadowsocks | 387.2 | 812.1 | Au1rxx-base64 | 107.172.250.161 |
| 54.12 | shadowsocks | 388.0 | 522.4 | Au1rxx-base64 | 173.244.56.9 |
| 53.75 | shadowsocks | 399.6 | 603.9 | Au1rxx-base64 | 108.181.0.177 |
| 53.43 | shadowsocks | 409.3 | 620.3 | Au1rxx-base64 | 108.181.118.10 |
| 52.9 | shadowsocks | 615.0 | 218.4 | Au1rxx-base64 | 149.22.87.241 |
| 52.89 | http | 1032.6 | 614.7 | snakem982 | 84.239.49.164 |
| 52.87 | shadowsocks | 426.7 | 677.2 | Au1rxx-base64 | 173.244.56.6 |
| 52.86 | http | 1030.2 | 616.8 | snakem982 | 84.239.14.159 |
| 52.69 | http | 1040.4 | 622.8 | snakem982 | 84.239.49.40 |
| 52.66 | http | 1040.8 | 620.4 | snakem982 | 84.239.49.37 |
| 52.63 | http | 1037.9 | 604.0 | snakem982 | 84.239.14.146 |
| 52.52 | http | 1045.6 | 644.6 | snakem982 | 84.239.49.156 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | 0.977 | 43 | 52 | prefer |
| Au1rxx-base64 | 0.524 | 0.521 | 71 | 88 | observe |
| roosterkid-openproxylist-v2ray | 0.329 | 0.31 | 29 | 150 | observe |
| Surfboard-tg-mixed | 0.298 | 0.217 | 741 | 4225 | observe |
| mheidari-all | 0.269 | 0.183 | 93 | 2000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3224 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| barry-far-Sub2 | 0.195 | None | 0 | 501 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 473 | observe |
| mfuu-v2ray | 0.19 | None | 0 | 387 | observe |
| Epodonios-all | 0.184 | 0.0 | 2 | 3000 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 199 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |
| Au1rxx-clash | 0.179 | None | 0 | 88 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ProxyError | - | 505 |
| 204 | ClientOSError | - | 337 |
| geo | status | 429 | 82 |
| 204 | TimeoutError | - | 67 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 54 |
| geo | status | 403 | 42 |
| speed | ClientOSError | - | 40 |
| cn-block | TimeoutError | - | 15 |
| cn-block | ClientOSError | - | 12 |
| speed | TimeoutError | - | 11 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| geo | TimeoutError | - | 5 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 3 |
| cn-block | ProxyError | - | 2 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
