# AutoNodes Daily Report

Generated at: 2026-06-19 20:03:41

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 105/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 72488 |
| Dedup nodes | 21995 |
| TCP ok | 743 |
| Real ok | 564 |
| Verified output | 300 |
| Global output | 300 |
| All output | 21995 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 2.9 |
| generate | 52.0 |
| geo | 1.3 |
| probe | 109.0 |
| real_test | 239.8 |
| tcp | 67.0 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 106 | 89 | 17 | 84.0% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 109 | 45 | 64 | 41.3% |
| vless | 496 | 398 | 98 | 80.2% |
| vmess | 3 | 3 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| speed:ClientOSError | 52 |
| cn-block:TimeoutError | 33 |
| 204:TimeoutError | 32 |
| geo:ClientOSError | 14 |
| speed:TimeoutError | 12 |
| 204:ProxyError | 10 |
| geo:TimeoutError | 9 |
| 204:ClientOSError | 6 |
| cn-block:ProxyError | 6 |
| cn-block:ClientOSError | 5 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3570 |
| ConnectionRefusedError | 671 |
| gaierror | 325 |
| OSError | 85 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Surfboard-tg-mixed | 0.899 | prefer | 357 | 0.821 | 4884 |
| mheidari-all | 0.817 | prefer | 268 | 0.739 | 14715 |
| Au1rxx-base64 | 0.717 | prefer | 26 | 0.731 | 75 |
| DeltaKronecker-all | 0.498 | observe | 65 | 0.415 | 6989 |
| nscl5-all | 0.309 | observe | 1 | 1.0 | 1360 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4458 |
| Epodonios-all | 0.255 | observe | 0 | None | 7362 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 7 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 9 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.415 | 27 | 38 | 65 |
| Au1rxx-base64 | 0.731 | 19 | 7 | 26 |
| mheidari-all | 0.739 | 198 | 70 | 268 |
| Surfboard-tg-mixed | 0.821 | 293 | 64 | 357 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14715 | yes | 1.69 | 0 |
| Epodonios-all | 7362 | yes | 1.85 | 0 |
| DeltaKronecker-all | 6989 | yes | 2.05 | 0 |
| SoliSpirit-all | 6518 | yes | 1.0 | 0 |
| Surfboard-tg-mixed | 4884 | yes | 1.13 | 0 |
| mahdibland-V2RayAggregator | 4527 | yes | 0.8 | 0 |
| 10ium-ScrapeCategorize-Vless | 4458 | yes | 1.09 | 0 |
| barry-far-vless | 4234 | yes | 0.7 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 0.86 | 0 |
| Surfboard-tg-vless | 3572 | yes | 0.97 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| speed | 64 |
| 204 | 48 |
| cn-block | 44 |
| geo | 23 |
