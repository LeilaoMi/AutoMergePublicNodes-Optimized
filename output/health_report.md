# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-09-11 04:20:01 |
| 运行耗时 | 1116.2s |
| 订阅源总数 | 107 |
| 健康订阅源 | 95 |
| 原始节点 | 83660 |
| 去重后节点 | 22960 |
| TCP 可达 | 3000 |
| 真实可用 | 539 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 22960 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.4 |
| tcp | 37.9 |
| probe | 401.0 |
| real_test | 581.7 |
| generate | 87.6 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 50810 |
| vmess | 12381 |
| shadowsocks | 9833 |
| trojan | 8157 |
| hysteria2 | 1652 |
| http | 620 |
| shadowsocksr | 128 |
| socks | 57 |
| tuic | 12 |
| hysteria | 8 |
| anytls | 2 |

## 评分权重

| 因子 | 权重 |
| --- | --- |
| latency | 25.0 |
| jitter | 15.0 |
| tcp | 10.0 |
| speed | 10.0 |
| fingerprint_resistance | 5.0 |
| protocol_history | 15.0 |
| source_history | 20.0 |

## Top 节点评分

| 评分 | 协议 | 延迟(ms) | 抖动(ms) | 延迟分 | 抖动分 | TCP分 | 协议历史分 | 来源历史分 | 来源 | 服务器 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 82.27 | vless | 240.6 | 686.4 | 22.21 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 79.141.172.154 |
| 82.2 | vless | 243.5 | 683.6 | 22.14 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 47.253.226.114 |
| 82.14 | vless | 246.0 | 668.4 | 22.08 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 137.184.218.169 |
| 81.12 | vless | 290.4 | 723.7 | 21.06 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.90 |
| 81.11 | vless | 290.6 | 655.8 | 21.05 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.184 |
| 81.01 | vless | 288.0 | 699.2 | 21.11 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 216.152.147.28 |
| 80.68 | vless | 309.1 | 649.6 | 20.62 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 47.89.186.170 |
| 80.56 | vless | 252.1 | 659.4 | 21.94 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.163 |
| 80.51 | vless | 316.5 | 855.9 | 20.45 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.15 |
| 80.33 | vless | 324.4 | 868.9 | 20.27 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.168 |
| 80.25 | shadowsocks | 244.0 | 682.4 | 22.13 | 0.0 | 10.0 | 13.32 | 18.8 | Au1rxx-base64 | 37.19.198.160 |
| 80.19 | shadowsocks | 246.7 | 687.3 | 22.07 | 0.0 | 10.0 | 13.32 | 18.8 | Au1rxx-base64 | 37.19.198.243 |
| 80.17 | vless | 331.1 | 852.0 | 20.11 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.225 |
| 80.15 | vless | 332.1 | 667.9 | 20.09 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.224 |
| 79.85 | hysteria2 | 232.5 | 637.3 | 22.4 | 0.0 | 10.0 | 9.75 | 18.8 | Au1rxx-base64 | 159.223.157.129 |
| 79.82 | vless | 346.2 | 826.3 | 19.76 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.229 |
| 79.82 | vless | 346.4 | 922.6 | 19.76 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.182 |
| 79.6 | vless | 264.3 | 698.1 | 21.66 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.212 |
| 79.45 | vless | 362.3 | 869.3 | 19.39 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.16 |
| 79.34 | vless | 366.9 | 893.3 | 19.28 | 0.0 | 10.0 | 11.26 | 18.8 | Au1rxx-base64 | 169.40.42.179 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.9 | 0.837 | 332 | 1613 | prefer |
| ermaozi | 0.813 | 0.81 | 42 | 431 | prefer |
| Surfboard-tg-mixed | 0.73 | 0.653 | 101 | 7301 | prefer |
| ermaozi-get_subscribe | 0.486 | 0.5 | 18 | 461 | observe |
| DeltaKronecker-all | 0.365 | 0.284 | 514 | 5853 | observe |
| mheidari-all | 0.305 | 0.3 | 10 | 15718 | observe |
| 10ium-HighSpeed | 0.289 | 1.0 | 1 | 839 | observe |
| tg-oneclickvpnkeys | 0.262 | 1.0 | 1 | 168 | observe |
| roosterkid-openproxylist-v2ray | 0.261 | 1.0 | 1 | 150 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4995 | observe |
| Epodonios-all | 0.255 | None | 0 | 7793 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3998 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 8799 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 5909 | observe |
| barry-far-vless | 0.255 | None | 0 | 6145 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 204 |
| speed | ClientOSError | - | 85 |
| geo | ClientOSError | - | 83 |
| speed | TimeoutError | - | 46 |
| 204 | ProxyError | - | 25 |
| cn-block | TimeoutError | - | 18 |
| cn-block | ClientOSError | - | 8 |
| 204 | TimeoutError | - | 7 |
| 204 | ClientOSError | - | 3 |
| speed | ProxyError | - | 2 |
| sing-box exited 1 |  [31mFATAL[0m[0000] start service: start inbound/socks[socks-in]: listen tcp 127.0.0.1:41389: bind: address already in use | - | 1 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
