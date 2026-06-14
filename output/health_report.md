# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-14 02:31:40 |
| 运行耗时 | 222.3s |
| 订阅源总数 | 44 |
| 健康订阅源 | 44 |
| 原始节点 | 40271 |
| 去重后节点 | 15512 |
| TCP 可达 | 1500 |
| 真实可用 | 400 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 15512 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 2.9 |
| geo | 1.2 |
| tcp | 35.8 |
| real_test | 166.9 |
| generate | 15.4 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 21071 |
| shadowsocks | 8036 |
| trojan | 5585 |
| vmess | 5237 |
| hysteria2 | 127 |
| http | 86 |
| shadowsocksr | 85 |
| socks | 37 |
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
| 64.16 | http | 675.9 | 906.7 | 16.98 | 0.0 | 9.72 | 18.7 | 18.76 | snakem982 | 84.239.49.171 |
| 64.09 | http | 679.7 | 897.1 | 16.86 | 0.0 | 9.77 | 18.7 | 18.76 | snakem982 | 84.239.49.166 |
| 64.04 | http | 679.1 | 902.8 | 16.88 | 0.0 | 9.7 | 18.7 | 18.76 | snakem982 | 84.239.49.157 |
| 64.04 | http | 681.3 | 900.3 | 16.81 | 0.0 | 9.77 | 18.7 | 18.76 | snakem982 | 84.239.49.219 |
| 64.03 | http | 681.1 | 915.3 | 16.81 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.49.175 |
| 64.03 | http | 681.3 | 913.4 | 16.81 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.49.183 |
| 64.01 | http | 680.8 | 899.6 | 16.82 | 0.0 | 9.73 | 18.7 | 18.76 | snakem982 | 84.239.49.234 |
| 63.97 | http | 682.8 | 896.1 | 16.76 | 0.0 | 9.75 | 18.7 | 18.76 | snakem982 | 84.239.49.201 |
| 63.96 | http | 682.5 | 911.3 | 16.77 | 0.0 | 9.73 | 18.7 | 18.76 | snakem982 | 84.239.49.249 |
| 63.95 | http | 683.4 | 922.1 | 16.74 | 0.0 | 9.75 | 18.7 | 18.76 | snakem982 | 84.239.49.154 |
| 63.94 | http | 684.1 | 921.5 | 16.72 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.49.224 |
| 63.93 | http | 683.2 | 898.2 | 16.75 | 0.0 | 9.72 | 18.7 | 18.76 | snakem982 | 84.239.49.164 |
| 63.93 | http | 684.5 | 901.0 | 16.71 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.49.37 |
| 63.92 | http | 684.6 | 915.9 | 16.7 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.49.231 |
| 63.92 | http | 684.6 | 891.3 | 16.7 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.14.149 |
| 63.9 | http | 685.0 | 901.8 | 16.69 | 0.0 | 9.75 | 18.7 | 18.76 | snakem982 | 84.239.49.242 |
| 63.89 | http | 685.5 | 914.6 | 16.67 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.49.155 |
| 63.89 | http | 685.6 | 903.2 | 16.67 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.49.156 |
| 63.88 | http | 685.8 | 904.0 | 16.66 | 0.0 | 9.76 | 18.7 | 18.76 | snakem982 | 84.239.14.154 |
| 63.85 | http | 686.4 | 909.6 | 16.64 | 0.0 | 9.75 | 18.7 | 18.76 | snakem982 | 84.239.14.158 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.938 | 0.956 | 45 | 52 | prefer |
| roosterkid-openproxylist-v2ray | 0.582 | 0.581 | 31 | 150 | observe |
| Au1rxx-base64 | 0.481 | 0.476 | 103 | 130 | observe |
| Surfboard-tg-mixed | 0.392 | 0.312 | 664 | 4199 | observe |
| mheidari-all | 0.288 | 0.202 | 99 | 2000 | observe |
| Epodonios-all | 0.255 | None | 0 | 3000 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3000 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 3299 | observe |
| barry-far-vless | 0.255 | None | 0 | 2000 | observe |
| DeltaKronecker-all | 0.218 | 0.136 | 425 | 4955 | downweight |
| barry-far-Sub2 | 0.195 | None | 0 | 499 | observe |
| barry-far-Sub1 | 0.194 | None | 0 | 476 | observe |
| nscl5-all | 0.191 | 0.2 | 5 | 1119 | downweight |
| mfuu-v2ray | 0.184 | None | 0 | 224 | observe |
| MatinGhanbari-super-sub | 0.183 | None | 0 | 199 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| 204 | ClientOSError | - | 541 |
| 204 | ProxyError | - | 288 |
| speed | TimeoutError | - | 59 |
| geo | status | 403 | 58 |
| 204 | TimeoutError | - | 55 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | - | 33 |
| speed | ClientOSError | - | 22 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | - | 8 |
| cn-block | TimeoutError | - | 8 |
| geo | TimeoutError | - | 6 |
| geo | status | 429 | 3 |
| cn-block | ClientOSError | - | 3 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �N|smy���{�4�Ϛ�M�o��}ֻ{� | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] create service: initialize outbound[0]: decode public_key: illegal base64 data at input byte 44 | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] decode config at /tmp/sb-7308_xqo/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
