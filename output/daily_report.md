# AutoNodes Daily Report

Generated at: 2026-06-07 00:11:35

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 44/44 |
| Cleanup disable/downweight | 0/12 |
| Cleanup prefer/observe | 0/32 |
| Raw nodes | 39702 |
| Dedup nodes | 15353 |
| TCP ok | 1500 |
| Real ok | 252 |
| Verified output | 252 |
| Global output | 262 |
| All output | 15353 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 2.9 |
| generate | 25.2 |
| geo | 1.2 |
| real_test | 119.4 |
| tcp | 35.7 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| anytls | 1 | 0 | 1 | 0.0% |
| http | 23 | 7 | 16 | 30.4% |
| hysteria2 | 18 | 4 | 14 | 22.2% |
| shadowsocks | 361 | 114 | 247 | 31.6% |
| shadowsocksr | 8 | 0 | 8 | 0.0% |
| socks | 5 | 1 | 4 | 20.0% |
| trojan | 716 | 87 | 629 | 12.2% |
| tuic | 1 | 0 | 1 | 0.0% |
| vless | 351 | 32 | 319 | 9.1% |
| vmess | 16 | 7 | 9 | 43.8% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| 204:ClientOSError | 755 |
| 204:ProxyError | 304 |
| 204:TimeoutError | 65 |
| speed:TimeoutError | 57 |
| geo:status | 15 |
| cn-block:TimeoutError | 9 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: ShadowsocksR is deprecated and removed in sing-box 1.6.0 | 8 |
| speed:ClientOSError | 6 |
| cn-block:ClientOSError | 5 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: uTLS is required by reality client | 4 |
| geo:TimeoutError | 3 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ݽ5k����^�� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �׺m����k� | 2 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-bufxgub6/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-c6so1uba/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] decode config at /tmp/sb-37b0lu1n/config.json: outbounds[0].security: json: cannot unmarshal bool into Go struct field VMessOutboundOptions.security of type string | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: chacha20-poly1305 | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: �o | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: ߾��ε�g��� | 1 |
| sing-box exited 1: [31mFATAL[0m[0000] create service: initialize outbound[0]: unknown method: վ����N]k� | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 1755 |
| ConnectionRefusedError | 446 |
| gaierror | 207 |
| OSError | 29 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| roosterkid-openproxylist-v2ray | 0.673 | observe | 25 | 0.68 | 150 |
| Au1rxx-base64 | 0.546 | observe | 57 | 0.544 | 84 |
| mheidari-all | 0.436 | observe | 102 | 0.353 | 2000 |
| Surfboard-tg-mixed | 0.361 | observe | 119 | 0.277 | 4296 |
| snakem982 | 0.298 | observe | 25 | 0.28 | 47 |
| mfuu-v2ray | 0.273 | observe | 3 | 0.667 | 104 |
| Epodonios-all | 0.255 | observe | 38 | 0.158 | 3000 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3000 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3300 |
| nscl5-all | 0.245 | downweight | 6 | 0.333 | 1018 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| 10ium-HighSpeed | 0.067 | downweight | 57 | 0.018 | 0 | 839 |
| Barabama-we | 0.069 | downweight | 6 | 0.0 | 0 | 23 |
| chromego_merge | 0.092 | observe | 3 | 0.0 | 0 | 51 |
| moneyfly1-collectSub | 0.094 | downweight | 17 | 0.0 | 0 | 1164 |
| Barabama-yudou | 0.098 | downweight | 20 | 0.05 | 0 | 166 |
| abc-configs-readme-latest30 | 0.105 | observe | 2 | 0.0 | 0 | 20 |
| ermaozi | 0.105 | observe | 2 | 0.0 | 0 | 29 |
| 10ium-ScrapeCategorize-Vless | 0.112 | downweight | 29 | 0.0 | 0 | 2000 |
| ninja-vless | 0.113 | downweight | 22 | 0.0 | 0 | 1791 |
| xiaoji235-airport-v2ray-all | 0.113 | downweight | 79 | 0.076 | 0 | 661 |

## Source Cleanup Suggestions

| Bucket | Source | Score | Tested | Pass Rate | Dead | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | 10ium-HighSpeed | 0.067 | 57 | 0.018 | 0 | low score with tested >= 5 |
| downweight | Barabama-we | 0.069 | 6 | 0.0 | 0 | low score with tested >= 5 |
| downweight | moneyfly1-collectSub | 0.094 | 17 | 0.0 | 0 | low score with tested >= 5 |
| downweight | Barabama-yudou | 0.098 | 20 | 0.05 | 0 | low score with tested >= 5 |
| downweight | 10ium-ScrapeCategorize-Vless | 0.112 | 29 | 0.0 | 0 | low score with tested >= 5 |
| downweight | xiaoji235-airport-v2ray-all | 0.113 | 79 | 0.076 | 0 | low score with tested >= 5 |
| downweight | ninja-vless | 0.113 | 22 | 0.0 | 0 | low score with tested >= 5 |
| downweight | mahdibland-V2RayAggregator | 0.13 | 14 | 0.0 | 0 | low score with tested >= 5 |
| downweight | SoliSpirit-all | 0.132 | 13 | 0.0 | 0 | low score with tested >= 5 |
| downweight | ts-sf | 0.15 | 15 | 0.133 | 0 | low score with tested >= 5 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| ninja-tuic | 0.0 | 0 | 1 | 1 |
| barry-far-vless | 0.0 | 0 | 1 | 1 |
| abc-configs-readme-latest30 | 0.0 | 0 | 2 | 2 |
| ermaozi | 0.0 | 0 | 2 | 2 |
| chromego_merge | 0.0 | 0 | 3 | 3 |
| Barabama-we | 0.0 | 0 | 6 | 6 |
| SoliSpirit-all | 0.0 | 0 | 13 | 13 |
| mahdibland-V2RayAggregator | 0.0 | 0 | 14 | 14 |
| moneyfly1-collectSub | 0.0 | 0 | 17 | 17 |
| ninja-vless | 0.0 | 0 | 22 | 22 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mahdibland-V2RayAggregator | 4642 | yes | 0.75 | 0 |
| DeltaKronecker-all | 4517 | yes | 2.83 | 0 |
| Surfboard-tg-mixed | 4296 | yes | 1.58 | 0 |
| Surfboard-tg-vless | 3300 | yes | 1.67 | 0 |
| Epodonios-all | 3000 | yes | 2.55 | 0 |
| SoliSpirit-all | 3000 | yes | 2.58 | 0 |
| MatinGhanbari-all-sub | 3000 | yes | 1.37 | 0 |
| mheidari-all | 2000 | yes | 2.38 | 0 |
| 10ium-ScrapeCategorize-Vless | 2000 | yes | 1.29 | 0 |
| barry-far-vless | 2000 | yes | 1.19 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Low-pass protocols
| Protocol | Pass Rate |
| --- | --- |
| vless | 0.091 |
| anytls | 0.0 |
| shadowsocksr | 0.0 |
| tuic | 0.0 |

### Real-test error alerts
| Error | Count |
| --- | --- |
| 204 | 1124 |
| speed | 64 |
| sing-box exited 1 | 27 |
| geo | 18 |
| cn-block | 15 |
