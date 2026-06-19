# AutoNodes Daily Report

Generated at: 2026-06-19 15:39:38

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 105/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 5/102 |
| Raw nodes | 73391 |
| Dedup nodes | 22037 |
| TCP ok | 771 |
| Real ok | 647 |
| Verified output | 300 |
| Global output | 300 |
| All output | 22037 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 5.5 |
| generate | 35.3 |
| geo | 1.3 |
| probe | 101.4 |
| real_test | 222.5 |
| tcp | 67.5 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 103 | 94 | 9 | 91.3% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 108 | 75 | 33 | 69.4% |
| vless | 527 | 445 | 82 | 84.4% |
| vmess | 3 | 3 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| speed:ClientOSError | 34 |
| cn-block:TimeoutError | 23 |
| 204:ProxyError | 16 |
| 204:TimeoutError | 12 |
| speed:TimeoutError | 7 |
| geo:TimeoutError | 6 |
| cn-block:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| geo:ClientOSError | 5 |
| 204:ClientOSError | 5 |
| geo:ProxyError | 4 |
| speed:ProxyError | 2 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3774 |
| ConnectionRefusedError | 661 |
| gaierror | 306 |
| OSError | 84 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| mheidari-all | 0.919 | prefer | 284 | 0.842 | 14955 |
| Surfboard-tg-mixed | 0.918 | prefer | 388 | 0.84 | 4956 |
| Au1rxx-base64 | 0.837 | prefer | 28 | 0.857 | 85 |
| DeltaKronecker-all | 0.776 | prefer | 44 | 0.705 | 6989 |
| nscl5-all | 0.309 | observe | 1 | 1.0 | 1360 |
| xiaoji235-airport-v2ray-all | 0.289 | observe | 1 | 1.0 | 844 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4458 |
| Epodonios-all | 0.255 | observe | 0 | None | 7116 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3981 |

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
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.705 | 31 | 13 | 44 |
| Surfboard-tg-mixed | 0.84 | 326 | 62 | 388 |
| mheidari-all | 0.842 | 239 | 45 | 284 |
| Au1rxx-base64 | 0.857 | 24 | 4 | 28 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14955 | yes | 3.21 | 0 |
| SoliSpirit-all | 7256 | yes | 3.26 | 0 |
| Epodonios-all | 7116 | yes | 2.55 | 0 |
| DeltaKronecker-all | 6989 | yes | 4.22 | 0 |
| Surfboard-tg-mixed | 4956 | yes | 0.38 | 0 |
| mahdibland-V2RayAggregator | 4527 | yes | 0.14 | 0 |
| 10ium-ScrapeCategorize-Vless | 4458 | yes | 1.83 | 0 |
| barry-far-vless | 4206 | yes | 1.02 | 0 |
| MatinGhanbari-all-sub | 3981 | yes | 1.12 | 0 |
| Surfboard-tg-vless | 3736 | yes | 2.02 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| speed | 43 |
| 204 | 33 |
| cn-block | 33 |
| geo | 15 |
