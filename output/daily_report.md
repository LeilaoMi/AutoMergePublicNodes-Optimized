# AutoNodes Daily Report

Generated at: 2026-06-19 05:05:07

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 106/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 71770 |
| Dedup nodes | 22121 |
| TCP ok | 866 |
| Real ok | 676 |
| Verified output | 300 |
| Global output | 300 |
| All output | 22121 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.7 |
| generate | 32.6 |
| geo | 1.4 |
| probe | 92.8 |
| real_test | 173.0 |
| tcp | 64.2 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 122 | 112 | 10 | 91.8% |
| trojan | 126 | 113 | 13 | 89.7% |
| vless | 586 | 419 | 167 | 71.5% |
| vmess | 4 | 4 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| geo:TimeoutError | 72 |
| speed:ClientOSError | 51 |
| cn-block:TimeoutError | 18 |
| geo:ClientOSError | 15 |
| speed:TimeoutError | 11 |
| 204:TimeoutError | 9 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 5 |
| speed:ProxyError | 1 |
| cn-block:ClientOSError | 1 |
| cn-block:ProxyError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3329 |
| ConnectionRefusedError | 654 |
| gaierror | 361 |
| OSError | 75 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.988 | prefer | 335 | 0.91 | 4851 |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| mheidari-all | 0.848 | prefer | 269 | 0.77 | 14638 |
| Au1rxx-base64 | 0.825 | prefer | 87 | 0.828 | 127 |
| DeltaKronecker-all | 0.53 | observe | 147 | 0.449 | 7112 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4494 |
| Epodonios-all | 0.255 | observe | 0 | None | 6479 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3974 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6447 |
| Surfboard-tg-vless | 0.255 | observe | 0 | None | 3730 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 7 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 7 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 8 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.333 | 1 | 2 | 3 |
| DeltaKronecker-all | 0.449 | 66 | 81 | 147 |
| mheidari-all | 0.77 | 207 | 62 | 269 |
| Au1rxx-base64 | 0.828 | 72 | 15 | 87 |
| Surfboard-tg-mixed | 0.91 | 305 | 30 | 335 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14638 | yes | 2.78 | 0 |
| DeltaKronecker-all | 7112 | yes | 3.11 | 0 |
| Epodonios-all | 6479 | yes | 1.55 | 0 |
| SoliSpirit-all | 6447 | yes | 1.76 | 0 |
| Surfboard-tg-mixed | 4851 | yes | 1.87 | 0 |
| mahdibland-V2RayAggregator | 4615 | yes | 0.23 | 0 |
| 10ium-ScrapeCategorize-Vless | 4494 | yes | 1.11 | 0 |
| barry-far-vless | 4360 | yes | 0.95 | 0 |
| MatinGhanbari-all-sub | 3974 | yes | 1.18 | 0 |
| Surfboard-tg-vless | 3730 | yes | 1.99 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| geo | 87 |
| speed | 63 |
| 204 | 20 |
| cn-block | 20 |
