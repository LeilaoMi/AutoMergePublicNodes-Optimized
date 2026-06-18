# AutoNodes Daily Report

Generated at: 2026-06-18 05:07:10

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 107/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 70294 |
| Dedup nodes | 22593 |
| TCP ok | 786 |
| Real ok | 636 |
| Verified output | 300 |
| Global output | 300 |
| All output | 22593 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.8 |
| generate | 33.3 |
| geo | 1.3 |
| probe | 100.0 |
| real_test | 37.0 |
| tcp | 58.4 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 132 | 129 | 3 | 97.7% |
| socks | 2 | 2 | 0 | 100.0% |
| trojan | 129 | 108 | 21 | 83.7% |
| vless | 490 | 364 | 126 | 74.3% |
| vmess | 5 | 5 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| geo:TimeoutError | 53 |
| speed:ClientOSError | 36 |
| general:unknown | 27 |
| geo:ClientOSError | 13 |
| speed:TimeoutError | 8 |
| cn-block:ClientOSError | 4 |
| 204:TimeoutError | 4 |
| 204:ProxyError | 4 |
| cn-block:TimeoutError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3046 |
| ConnectionRefusedError | 649 |
| gaierror | 412 |
| OSError | 65 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| Surfboard-tg-mixed | 0.985 | prefer | 344 | 0.907 | 4586 |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Au1rxx-base64 | 0.866 | prefer | 77 | 0.87 | 126 |
| mheidari-all | 0.856 | prefer | 212 | 0.778 | 13927 |
| DeltaKronecker-all | 0.608 | observe | 121 | 0.529 | 7763 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.289 | observe | 1 | 1.0 | 847 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4274 |
| Epodonios-all | 0.255 | observe | 0 | None | 6401 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3977 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| ninja-vless | 0.152 | observe | 4 | 0.0 | 0 | 1791 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 7 |
| tg-AzadNet | 0.175 | observe | 0 | None | 0 | 3 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |
| tg-ISVvpn | 0.175 | observe | 0 | None | 0 | 8 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.529 | 64 | 57 | 121 |
| mheidari-all | 0.778 | 165 | 47 | 212 |
| Au1rxx-base64 | 0.87 | 67 | 10 | 77 |
| Surfboard-tg-mixed | 0.907 | 312 | 32 | 344 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 13927 | yes | 3.35 | 0 |
| DeltaKronecker-all | 7763 | yes | 3.41 | 0 |
| Epodonios-all | 6401 | yes | 2.05 | 0 |
| SoliSpirit-all | 5959 | yes | 1.53 | 0 |
| Surfboard-tg-mixed | 4586 | yes | 2.19 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 1.54 | 0 |
| 10ium-ScrapeCategorize-Vless | 4274 | yes | 1.21 | 0 |
| barry-far-vless | 4240 | yes | 1.03 | 0 |
| MatinGhanbari-all-sub | 3977 | yes | 1.28 | 0 |
| Surfboard-tg-vless | 3590 | yes | 1.76 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| geo | 66 |
| speed | 44 |
| general | 27 |
| 204 | 8 |
| cn-block | 5 |
