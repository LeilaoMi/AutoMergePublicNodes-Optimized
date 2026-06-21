# AutoNodes Daily Report

Generated at: 2026-06-21 20:00:23

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 105/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 72909 |
| Dedup nodes | 22018 |
| TCP ok | 845 |
| Real ok | 622 |
| Verified output | 300 |
| Global output | 300 |
| All output | 22018 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.9 |
| generate | 41.1 |
| geo | 1.4 |
| probe | 120.3 |
| real_test | 267.0 |
| tcp | 62.5 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 69 | 69 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 114 | 93 | 21 | 81.6% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 87 | 27 | 60 | 31.0% |
| vless | 568 | 426 | 142 | 75.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| 204:TimeoutError | 85 |
| speed:ClientOSError | 44 |
| cn-block:TimeoutError | 26 |
| geo:TimeoutError | 16 |
| 204:ProxyError | 14 |
| speed:TimeoutError | 14 |
| geo:ClientOSError | 8 |
| 204:ClientOSError | 7 |
| cn-block:ProxyError | 4 |
| cn-block:ClientOSError | 3 |
| geo:ProxyError | 2 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3260 |
| ConnectionRefusedError | 638 |
| gaierror | 383 |
| OSError | 109 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | prefer | 69 | 1.0 | 131 |
| Au1rxx-base64 | 0.885 | prefer | 89 | 0.888 | 138 |
| mheidari-all | 0.818 | prefer | 284 | 0.739 | 14833 |
| Surfboard-tg-mixed | 0.759 | prefer | 350 | 0.68 | 4837 |
| DeltaKronecker-all | 0.549 | observe | 47 | 0.468 | 6748 |
| SoliSpirit-all | 0.391 | observe | 2 | 1.0 | 6721 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4494 |
| Epodonios-all | 0.255 | observe | 0 | None | 7211 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3998 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-LonUp_M | 0.135 | observe | 1 | 0.0 | 0 | 178 |
| Pawdroid | 0.175 | observe | 0 | None | 0 | 11 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| nscl5-all | 0.0 | 0 | 1 | 1 |
| tg-LonUp_M | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.468 | 22 | 25 | 47 |
| Surfboard-tg-mixed | 0.68 | 238 | 112 | 350 |
| mheidari-all | 0.739 | 210 | 74 | 284 |
| Au1rxx-base64 | 0.888 | 79 | 10 | 89 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| SoliSpirit-all | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 69 | 0 | 69 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14833 | yes | 3.7 | 0 |
| Epodonios-all | 7211 | yes | 2.28 | 0 |
| DeltaKronecker-all | 6748 | yes | 3.67 | 0 |
| SoliSpirit-all | 6721 | yes | 1.6 | 0 |
| Surfboard-tg-mixed | 4837 | yes | 2.01 | 0 |
| barry-far-vless | 4563 | yes | 1.25 | 0 |
| mahdibland-V2RayAggregator | 4505 | yes | 0.34 | 0 |
| 10ium-ScrapeCategorize-Vless | 4494 | yes | 1.08 | 0 |
| MatinGhanbari-all-sub | 3998 | yes | 1.32 | 0 |
| Surfboard-tg-vless | 3719 | yes | 2.58 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| 204 | 106 |
| speed | 58 |
| cn-block | 33 |
| geo | 26 |
