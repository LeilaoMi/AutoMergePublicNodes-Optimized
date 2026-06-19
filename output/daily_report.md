# AutoNodes Daily Report

Generated at: 2026-06-19 10:54:46

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 106/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 72574 |
| Dedup nodes | 21825 |
| TCP ok | 698 |
| Real ok | 544 |
| Verified output | 300 |
| Global output | 300 |
| All output | 21825 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.9 |
| generate | 69.3 |
| geo | 1.3 |
| probe | 104.4 |
| real_test | 202.2 |
| tcp | 66.0 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 110 | 102 | 8 | 92.7% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 75 | 54 | 21 | 72.0% |
| vless | 480 | 355 | 125 | 74.0% |
| vmess | 4 | 4 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| cn-block:TimeoutError | 37 |
| speed:ClientOSError | 36 |
| 204:TimeoutError | 24 |
| geo:TimeoutError | 15 |
| 204:ProxyError | 15 |
| speed:TimeoutError | 11 |
| geo:ClientOSError | 8 |
| speed:ProxyError | 5 |
| geo:ProxyError | 2 |
| cn-block:ClientOSError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3454 |
| ConnectionRefusedError | 648 |
| gaierror | 339 |
| OSError | 84 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Au1rxx-base64 | 0.916 | prefer | 77 | 0.922 | 121 |
| mheidari-all | 0.865 | prefer | 259 | 0.788 | 15002 |
| Surfboard-tg-mixed | 0.832 | prefer | 272 | 0.754 | 4682 |
| DeltaKronecker-all | 0.68 | observe | 63 | 0.603 | 6989 |
| Barabama-yudou | 0.262 | observe | 1 | 1.0 | 166 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4458 |
| Epodonios-all | 0.255 | observe | 0 | None | 7124 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3975 |
| SoliSpirit-all | 0.255 | observe | 0 | None | 6752 |

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
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.603 | 38 | 25 | 63 |
| Surfboard-tg-mixed | 0.754 | 205 | 67 | 272 |
| mheidari-all | 0.788 | 204 | 55 | 259 |
| Au1rxx-base64 | 0.922 | 71 | 6 | 77 |
| Barabama-yudou | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 15002 | yes | 3.38 | 0 |
| Epodonios-all | 7124 | yes | 0.94 | 0 |
| DeltaKronecker-all | 6989 | yes | 2.79 | 0 |
| SoliSpirit-all | 6752 | yes | 1.98 | 0 |
| Surfboard-tg-mixed | 4682 | yes | 1.61 | 0 |
| mahdibland-V2RayAggregator | 4527 | yes | 0.26 | 0 |
| 10ium-ScrapeCategorize-Vless | 4458 | yes | 1.66 | 0 |
| barry-far-vless | 4215 | yes | 1.5 | 0 |
| MatinGhanbari-all-sub | 3975 | yes | 1.76 | 0 |
| Surfboard-tg-vless | 3547 | yes | 1.72 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| speed | 52 |
| 204 | 39 |
| cn-block | 38 |
| geo | 25 |
