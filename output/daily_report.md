# AutoNodes Daily Report

Generated at: 2026-06-20 04:19:08

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 105/107 |
| Cleanup disable/downweight | 0/1 |
| Cleanup prefer/observe | 4/102 |
| Raw nodes | 73021 |
| Dedup nodes | 22102 |
| TCP ok | 935 |
| Real ok | 710 |
| Verified output | 300 |
| Global output | 300 |
| All output | 22102 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.1 |
| generate | 36.3 |
| geo | 1.3 |
| probe | 97.0 |
| real_test | 202.7 |
| tcp | 65.4 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 125 | 119 | 6 | 95.2% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 132 | 106 | 26 | 80.3% |
| vless | 645 | 452 | 193 | 70.1% |
| vmess | 3 | 3 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| geo:TimeoutError | 82 |
| speed:ClientOSError | 59 |
| geo:ClientOSError | 16 |
| 204:ClientOSError | 16 |
| cn-block:TimeoutError | 15 |
| 204:TimeoutError | 11 |
| speed:TimeoutError | 9 |
| 204:ProxyError | 8 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 2 |
| speed:ProxyError | 1 |
| cn-block:ProxyError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3315 |
| ConnectionRefusedError | 671 |
| gaierror | 414 |
| OSError | 90 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Au1rxx-base64 | 0.958 | prefer | 20 | 1.0 | 98 |
| Surfboard-tg-mixed | 0.913 | prefer | 429 | 0.834 | 5022 |
| mheidari-all | 0.854 | prefer | 335 | 0.776 | 14629 |
| DeltaKronecker-all | 0.48 | observe | 108 | 0.398 | 6989 |
| xiaoji235-airport-v2ray-all | 0.292 | observe | 1 | 1.0 | 913 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| roosterkid-openproxylist-v2ray | 0.261 | observe | 1 | 1.0 | 150 |
| Epodonios-all | 0.255 | observe | 0 | None | 7454 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3978 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-configfa | 0.085 | observe | 4 | 0.0 | 0 | 129 |
| ninja-vless | 0.136 | downweight | 7 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## Source Cleanup Suggestions

| Bucket | Source | Score | Tested | Pass Rate | Dead | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| downweight | ninja-vless | 0.136 | 7 | 0.0 | 0 | low score with tested >= 5 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| 10ium-ScrapeCategorize-Vless | 0.0 | 0 | 2 | 2 |
| tg-configfa | 0.0 | 0 | 4 | 4 |
| ninja-vless | 0.0 | 0 | 7 | 7 |
| DeltaKronecker-all | 0.398 | 43 | 65 | 108 |
| nscl5-all | 0.5 | 1 | 1 | 2 |
| mheidari-all | 0.776 | 260 | 75 | 335 |
| Surfboard-tg-mixed | 0.834 | 358 | 71 | 429 |
| roosterkid-openproxylist-v2ray | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14629 | yes | 3.14 | 0 |
| Epodonios-all | 7454 | yes | 1.88 | 0 |
| DeltaKronecker-all | 6989 | yes | 3.05 | 0 |
| SoliSpirit-all | 6672 | yes | 1.42 | 0 |
| Surfboard-tg-mixed | 5022 | yes | 2.01 | 0 |
| mahdibland-V2RayAggregator | 4527 | yes | 1.42 | 0 |
| 10ium-ScrapeCategorize-Vless | 4458 | yes | 1.11 | 0 |
| barry-far-vless | 4406 | yes | 0.84 | 0 |
| MatinGhanbari-all-sub | 3978 | yes | 1.2 | 0 |
| Surfboard-tg-vless | 3739 | yes | 2.28 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| geo | 100 |
| speed | 69 |
| 204 | 35 |
| cn-block | 21 |
