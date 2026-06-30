# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-06-30 20:08:58 |
| 运行耗时 | 201.9s |
| 订阅源总数 | 107 |
| 健康订阅源 | 103 |
| 原始节点 | 75832 |
| 去重后节点 | 23070 |
| TCP 可达 | 3000 |
| 真实可用 | 191 |
| Verified 输出 | 191 |
| Global 输出 | 197 |
| All 输出 | 23070 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 4.5 |
| geo | 1.4 |
| tcp | 30.7 |
| probe | 51.3 |
| real_test | 79.7 |
| generate | 34.3 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 42728 |
| trojan | 13038 |
| vmess | 10255 |
| shadowsocks | 9169 |
| hysteria2 | 282 |
| shadowsocksr | 158 |
| http | 135 |
| socks | 60 |
| hysteria | 6 |
| tuic | 1 |

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
| 74.58 | shadowsocks | 239.9 | 602.4 | 22.22 | 0.0 | 10.0 | 12.1 | 14.26 | mheidari-all | 198.98.53.130 |
| 74.45 | vless | 265.4 | 655.1 | 21.64 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 104.25.161.29 |
| 74.06 | vless | 264.3 | 646.9 | 21.66 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 104.17.238.33 |
| 73.67 | shadowsocks | 231.9 | 639.3 | 22.41 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 37.19.198.160 |
| 73.59 | shadowsocks | 235.5 | 654.4 | 22.33 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 37.19.198.236 |
| 73.49 | shadowsocks | 239.6 | 651.3 | 22.23 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | tinkered-pennies-puppies.freesocks.work |
| 73.08 | vless | 277.0 | 690.2 | 21.37 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 162.159.38.165 |
| 72.52 | shadowsocks | 281.7 | 783.1 | 21.26 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 37.19.198.244 |
| 71.83 | vless | 378.1 | 625.0 | 19.02 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 104.17.28.89 |
| 71.78 | vless | 376.0 | 629.9 | 19.07 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 162.159.39.247 |
| 71.7 | shadowsocks | 295.5 | 596.5 | 20.94 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 108.181.57.93 |
| 71.0 | vless | 370.8 | 601.8 | 19.19 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 162.159.44.142 |
| 69.99 | shadowsocks | 276.9 | 638.5 | 21.37 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 156.146.38.170 |
| 69.54 | vless | 361.9 | 637.6 | 19.4 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 172.64.52.55 |
| 69.03 | shadowsocks | 291.3 | 660.7 | 21.03 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 156.146.38.168 |
| 68.6 | shadowsocks | 234.8 | 645.6 | 22.34 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 37.19.198.243 |
| 68.45 | shadowsocks | 291.7 | 665.2 | 21.02 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 156.146.38.169 |
| 68.17 | shadowsocks | 318.3 | 762.0 | 20.41 | 0.0 | 10.0 | 12.1 | 13.16 | Au1rxx-base64 | 156.146.38.167 |
| 67.19 | hysteria2 | 357.3 | 697.5 | 19.51 | 0.0 | 10.0 | 11.25 | 13.16 | Au1rxx-base64 | 62.210.124.146 |
| 66.69 | vless | 380.2 | 654.6 | 18.98 | 0.0 | 10.0 | 8.79 | 15.02 | DeltaKronecker-all | 162.159.39.44 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.976 | 1.0 | 36 | 61 | prefer |
| mheidari-all | 0.88 | 0.818 | 33 | 15848 | prefer |
| Au1rxx-base64 | 0.831 | 0.852 | 27 | 83 | prefer |
| Surfboard-tg-mixed | 0.628 | 0.549 | 82 | 5645 | observe |
| Barabama-yudou | 0.318 | 1.0 | 2 | 166 | observe |
| xiaoji235-airport-v2ray-all | 0.303 | 1.0 | 1 | 1204 | observe |
| nscl5-all | 0.3 | 1.0 | 1 | 1136 | observe |
| DeltaKronecker-all | 0.267 | 0.185 | 298 | 7352 | observe |
| abc-configs-readme-latest30 | 0.256 | 1.0 | 1 | 19 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 4139 | observe |
| Epodonios-all | 0.255 | None | 0 | 6581 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3979 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6636 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4233 | observe |
| barry-far-vless | 0.255 | None | 0 | 4802 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| speed | ClientOSError | - | 193 |
| 204 | ProxyError | - | 31 |
| 204 | ClientOSError | - | 13 |
| 204 | TimeoutError | - | 12 |
| geo | TimeoutError | - | 9 |
| geo | ClientOSError | - | 8 |
| geo | ProxyError | - | 5 |
| speed | TimeoutError | - | 5 |
| cn-block | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 4 |
| cn-block | ProxyError | - | 3 |
| speed | ProxyError | - | 2 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 191 | - |
| global | False | 300 | 197 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
