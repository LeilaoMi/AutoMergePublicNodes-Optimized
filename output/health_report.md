# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.3.0 |
| 更新时间 | 2026-06-12 04:12:44 |
| 运行耗时 | 219.6s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 39941 |
| 去重后节点 | 15081 |
| TCP 可达 | 1500 |
| 真实可用 | 382 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 15081 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 3.2 |
| geo | 1.2 |
| tcp | 37.8 |
| real_test | 152.0 |
| generate | 25.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 20119 |
| shadowsocks | 8020 |
| trojan | 6151 |
| vmess | 5264 |
| hysteria2 | 186 |
| shadowsocksr | 89 |
| http | 86 |
| socks | 19 |
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
| 57.68 | shadowsocks | 450.3 | 194.7 | 24.3 | 7.7 | 9.85 | 5.83 | 10.0 | Au1rxx-base64 | 149.22.87.240 |
| 57.4 | vmess | 224.0 | 487.0 | 31.63 | 0.0 | 10.0 | 9.41 | 6.36 | Barabama-yudou | 82.198.246.233 |
| 57.29 | shadowsocks | 450.4 | 204.9 | 24.29 | 7.32 | 9.85 | 5.83 | 10.0 | Au1rxx-base64 | 149.22.87.241 |
| 57.24 | shadowsocks | 230.8 | 514.5 | 31.41 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 108.181.118.10 |
| 56.94 | shadowsocks | 240.1 | 475.3 | 31.11 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 173.244.56.9 |
| 56.9 | shadowsocks | 453.1 | 213.8 | 24.2 | 6.98 | 9.89 | 5.83 | 10.0 | Au1rxx-base64 | 149.22.87.204 |
| 56.72 | shadowsocks | 246.8 | 563.3 | 30.89 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 108.181.0.177 |
| 56.64 | shadowsocks | 249.3 | 570.7 | 30.81 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 216.105.168.18 |
| 56.21 | shadowsocks | 262.6 | 592.3 | 30.38 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 192.3.196.182 |
| 55.32 | shadowsocks | 290.0 | 430.1 | 29.49 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 149.22.95.183 |
| 55.1 | shadowsocks | 297.0 | 640.3 | 29.27 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 173.244.56.6 |
| 54.13 | trojan | 284.1 | 648.9 | 29.68 | 0.0 | 10.0 | 6.61 | 7.84 | Surfboard-tg-mixed | 172.235.63.252 |
| 53.78 | shadowsocks | 337.5 | 590.4 | 27.95 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 156.146.38.170 |
| 53.52 | shadowsocks | 345.7 | 615.4 | 27.69 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 156.146.38.167 |
| 53.41 | shadowsocks | 348.9 | 626.0 | 27.58 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 156.146.38.168 |
| 52.38 | shadowsocks | 380.7 | 727.3 | 26.55 | 0.0 | 10.0 | 5.83 | 10.0 | Au1rxx-base64 | 149.28.255.6 |
| 51.82 | vless | 564.0 | 194.5 | 20.61 | 7.71 | 9.86 | 3.64 | 10.0 | Au1rxx-base64 | 103.134.35.107 |
| 51.63 | shadowsocks | 207.2 | 425.2 | 32.18 | 0.0 | 10.0 | 5.83 | 3.62 | DeltaKronecker-all | 107.172.219.230 |
| 50.71 | vless | 364.6 | 785.6 | 27.07 | 0.0 | 10.0 | 3.64 | 10.0 | Au1rxx-base64 | 15.204.97.214 |
| 50.29 | vless | 555.3 | 187.2 | 20.89 | 7.98 | 9.94 | 3.64 | 7.84 | Surfboard-tg-mixed | 31.76.91.19 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.958 | 0.977 | 43 | 52 | prefer |
| Au1rxx-base64 | 0.478 | 0.473 | 91 | 121 | observe |
| roosterkid-openproxylist-v2ray | 0.446 | 0.435 | 23 | 150 | observe |
| Surfboard-tg-mixed | 0.365 | 0.285 | 734 | 4083 | observe |
| mheidari-all | 0.343 | 0.258 | 93 | 2000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3039 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| Epodonios-all | 0.247 | 0.154 | 52 | 3000 | downweight |
| 10ium-HighSpeed | 0.209 | None | 0 | 839 | observe |
| DeltaKronecker-all | 0.209 | 0.127 | 339 | 4660 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 501 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 476 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 200 | observe |
| barabama-yudou66 | 0.182 | None | 0 | 163 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 519 |
| 204 | ProxyError | - | 321 |
| 204 | TimeoutError | - | 81 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 52 |
| speed | TimeoutError | - | 44 |
| geo | status | 403 | 26 |
| speed | ClientOSError | - | 18 |
| geo | status | 429 | 16 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| cn-block | ClientOSError | - | 8 |
| cn-block | TimeoutError | - | 7 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 4 |
| geo | TimeoutError | - | 4 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unsupported flow: xtls-rprx-vision-udp443 | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] decode config at /tmp/sb-qrey53q1/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
