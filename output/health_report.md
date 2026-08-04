# AutoNodes 健康报告

## 总览

| 指标 | 数值 |
| --- | --- |
| 版本 | 2.4.0 |
| 更新时间 | 2026-08-04 03:18:36 |
| 运行耗时 | 315.5s |
| 订阅源总数 | 107 |
| 健康订阅源 | 101 |
| 原始节点 | 85773 |
| 去重后节点 | 24690 |
| TCP 可达 | 3000 |
| 真实可用 | 739 |
| Verified 输出 | 300 |
| Global 输出 | 300 |
| All 输出 | 24690 |

## 阶段耗时

| 阶段 | 秒 |
| --- | --- |
| fetch | 6.6 |
| geo | 1.4 |
| tcp | 36.6 |
| probe | 59.0 |
| real_test | 175.9 |
| generate | 36.0 |

## 协议分布

| 协议 | 数量 |
| --- | --- |
| vless | 52095 |
| vmess | 12956 |
| shadowsocks | 10211 |
| trojan | 9245 |
| hysteria2 | 1003 |
| socks | 76 |
| http | 76 |
| shadowsocksr | 73 |
| hysteria | 18 |
| tuic | 10 |
| anytls | 10 |

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
| 80.39 | hysteria2 | 234.4 | 638.0 | 22.35 | 0.0 | 10.0 | 13.5 | 15.64 | Au1rxx-base64 | 159.223.157.129 |
| 80.3 | hysteria2 | 242.7 | 673.3 | 22.16 | 0.0 | 10.0 | 13.5 | 15.64 | Au1rxx-base64 | 138.124.68.188 |
| 79.46 | hysteria2 | 247.8 | 685.6 | 22.04 | 0.0 | 9.28 | 13.5 | 15.64 | Au1rxx-base64 | usa1.spectrumproxy.shop |
| 78.66 | trojan | 252.7 | 691.1 | 21.93 | 0.0 | 10.0 | 14.09 | 15.64 | Au1rxx-base64 | 153.75.250.171 |
| 76.06 | shadowsocks | 222.5 | 604.5 | 22.63 | 0.0 | 10.0 | 11.79 | 15.64 | Au1rxx-base64 | 198.98.53.130 |
| 75.96 | shadowsocks | 226.5 | 626.0 | 22.53 | 0.0 | 10.0 | 11.79 | 15.64 | Au1rxx-base64 | 37.19.198.160 |
| 75.89 | shadowsocks | 229.6 | 626.9 | 22.46 | 0.0 | 10.0 | 11.79 | 15.64 | Au1rxx-base64 | 37.19.198.244 |
| 75.87 | shadowsocks | 230.8 | 639.0 | 22.44 | 0.0 | 10.0 | 11.79 | 15.64 | Au1rxx-base64 | 37.19.198.236 |
| 75.78 | vless | 241.7 | 673.5 | 22.18 | 0.0 | 10.0 | 7.96 | 15.64 | Au1rxx-base64 | 47.89.186.170 |
| 75.76 | shadowsocks | 235.4 | 645.6 | 22.33 | 0.0 | 10.0 | 11.79 | 15.64 | Au1rxx-base64 | 37.19.198.243 |
| 74.86 | shadowsocks | 252.5 | 691.3 | 21.93 | 0.0 | 10.0 | 11.79 | 15.64 | Au1rxx-base64 | 68.168.222.210 |
| 74.86 | vless | 281.4 | 740.6 | 21.26 | 0.0 | 10.0 | 7.96 | 15.64 | Au1rxx-base64 | 169.40.42.212 |
| 74.03 | http | 394.6 | 718.4 | 18.64 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.218 |
| 73.94 | http | 368.4 | 665.3 | 19.25 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.211 |
| 73.88 | vless | 324.0 | 889.4 | 20.28 | 0.0 | 10.0 | 7.96 | 15.64 | Au1rxx-base64 | 159.89.87.21 |
| 73.62 | vless | 335.1 | 914.2 | 20.02 | 0.0 | 10.0 | 7.96 | 15.64 | Au1rxx-base64 | 167.17.69.171 |
| 73.52 | http | 397.5 | 777.3 | 18.58 | 0.0 | 10.0 | 14.78 | 19.78 | zhangkai | 138.199.35.216 |
| 73.39 | vless | 345.3 | 943.1 | 19.79 | 0.0 | 10.0 | 7.96 | 15.64 | Au1rxx-base64 | 169.40.42.179 |
| 73.08 | vless | 358.4 | 853.3 | 19.48 | 0.0 | 10.0 | 7.96 | 15.64 | Au1rxx-base64 | 169.40.42.184 |
| 73.06 | vless | 289.8 | 717.4 | 21.07 | 0.0 | 10.0 | 7.96 | 15.64 | Au1rxx-base64 | 169.40.42.16 |

## 来源质量排行

| 来源 | 评分 | 通过率 | 测试数 | 解析节点 | 建议 |
| --- | --- | --- | --- | --- | --- |
| zhangkai | 0.989 | 1.0 | 67 | 92 | prefer |
| Au1rxx-base64 | 0.941 | 0.875 | 631 | 1681 | prefer |
| Surfboard-tg-mixed | 0.584 | 0.504 | 127 | 5262 | observe |
| tg-OutlineReleasedKey | 0.257 | 1.0 | 1 | 57 | observe |
| 10ium-ScrapeCategorize-Vless | 0.255 | None | 0 | 5285 | observe |
| Epodonios-all | 0.255 | None | 0 | 5848 | observe |
| MatinGhanbari-all-sub | 0.255 | None | 0 | 3997 | observe |
| SoliSpirit-all | 0.255 | None | 0 | 6833 | observe |
| Surfboard-tg-vless | 0.255 | None | 0 | 4123 | observe |
| barry-far-vless | 0.255 | None | 0 | 4484 | observe |
| mahdibland-V2RayAggregator | 0.255 | None | 0 | 5152 | observe |
| xiaoji235-airport-v2ray-all | 0.255 | None | 0 | 5127 | observe |
| mheidari-all | 0.254 | 0.172 | 291 | 19963 | observe |
| Au1rxx-clash | 0.242 | None | 0 | 1682 | observe |
| nscl5-all | 0.226 | None | 0 | 1267 | observe |

## 真实测试失败原因

| 目标 | 原因 | 状态/值 | 数量 |
| --- | --- | --- | --- |
| geo | TimeoutError | - | 181 |
| speed | TimeoutError | - | 83 |
| speed | ClientOSError | - | 62 |
| geo | ClientOSError | - | 59 |
| cn-block | TimeoutError | - | 22 |
| 204 | ProxyError | - | 6 |
| 204 | ClientOSError | - | 6 |
| 204 | TimeoutError | - | 5 |
| cn-block | ClientOSError | - | 2 |
| cn-block | ProxyError | - | 1 |
| geo | ProxyError | - | 1 |

## 输出保护

| 前缀 | 是否保留旧输出 | 上一轮数量 | 本轮建议数量 | 保护比例 |
| --- | --- | --- | --- | --- |
| verified | False | 300 | 300 | - |
| global | False | 300 | 300 | - |

---

此文件由 `core.report.write_health_report()` 自动生成。
