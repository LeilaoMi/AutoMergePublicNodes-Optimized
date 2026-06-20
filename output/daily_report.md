# AutoNodes Daily Report

Generated at: 2026-06-20 14:23:35

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 104/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 73120 |
| Dedup nodes | 21770 |
| TCP ok | 793 |
| Real ok | 614 |
| Verified output | 300 |
| Global output | 300 |
| All output | 21770 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 5.0 |
| generate | 52.0 |
| geo | 1.3 |
| probe | 112.8 |
| real_test | 203.1 |
| tcp | 60.9 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 112 | 106 | 6 | 94.6% |
| trojan | 128 | 74 | 54 | 57.8% |
| vless | 521 | 402 | 119 | 77.2% |
| vmess | 5 | 5 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| speed:ClientOSError | 60 |
| cn-block:TimeoutError | 32 |
| 204:TimeoutError | 18 |
| 204:ProxyError | 16 |
| geo:TimeoutError | 14 |
| 204:ClientOSError | 10 |
| geo:ClientOSError | 9 |
| cn-block:ClientOSError | 8 |
| speed:TimeoutError | 5 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 3 |
| speed:ProxyError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3058 |
| ConnectionRefusedError | 658 |
| gaierror | 393 |
| OSError | 86 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Surfboard-tg-mixed | 0.895 | prefer | 414 | 0.816 | 4892 |
| Au1rxx-base64 | 0.816 | prefer | 30 | 0.833 | 86 |
| mheidari-all | 0.809 | prefer | 271 | 0.731 | 14626 |
| DeltaKronecker-all | 0.608 | observe | 51 | 0.529 | 6810 |
| nscl5-all | 0.3 | observe | 1 | 1.0 | 1126 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4507 |
| Epodonios-all | 0.255 | observe | 0 | None | 7484 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 7110 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| abc-configs-readme-latest30 | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.529 | 27 | 24 | 51 |
| mheidari-all | 0.731 | 198 | 73 | 271 |
| Surfboard-tg-mixed | 0.816 | 338 | 76 | 414 |
| Au1rxx-base64 | 0.833 | 25 | 5 | 30 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14626 | yes | 3.3 | 0 |
| Epodonios-all | 7484 | yes | 2.64 | 0 |
| SoliSpirit-all | 7110 | yes | 2.87 | 0 |
| DeltaKronecker-all | 6810 | yes | 3.88 | 0 |
| Surfboard-tg-mixed | 4892 | yes | 2.04 | 0 |
| barry-far-vless | 4525 | yes | 1.52 | 0 |
| mahdibland-V2RayAggregator | 4516 | yes | 1.35 | 0 |
| 10ium-ScrapeCategorize-Vless | 4507 | yes | 1.53 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 1.61 | 0 |
| Surfboard-tg-vless | 3696 | yes | 1.78 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| speed | 66 |
| 204 | 44 |
| cn-block | 43 |
| geo | 26 |
