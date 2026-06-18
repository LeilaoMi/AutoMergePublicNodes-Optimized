# AutoNodes Daily Report

Generated at: 2026-06-18 10:45:33

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 107/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 70128 |
| Dedup nodes | 21724 |
| TCP ok | 690 |
| Real ok | 543 |
| Verified output | 300 |
| Global output | 300 |
| All output | 21724 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 3.3 |
| generate | 28.8 |
| geo | 1.2 |
| probe | 104.8 |
| real_test | 169.2 |
| tcp | 59.6 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 114 | 96 | 18 | 84.2% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 85 | 46 | 39 | 54.1% |
| vless | 457 | 367 | 90 | 80.3% |
| vmess | 6 | 6 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| 204:TimeoutError | 37 |
| speed:ClientOSError | 31 |
| cn-block:TimeoutError | 25 |
| geo:TimeoutError | 15 |
| speed:TimeoutError | 10 |
| geo:ClientOSError | 9 |
| 204:ClientOSError | 6 |
| 204:ProxyError | 5 |
| cn-block:ClientOSError | 5 |
| geo:ProxyError | 3 |
| cn-block:ProxyError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3027 |
| ConnectionRefusedError | 649 |
| gaierror | 379 |
| OSError | 61 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Surfboard-tg-mixed | 0.894 | prefer | 326 | 0.816 | 4615 |
| Au1rxx-base64 | 0.887 | prefer | 58 | 0.897 | 96 |
| mheidari-all | 0.816 | prefer | 225 | 0.738 | 14164 |
| DeltaKronecker-all | 0.673 | observe | 52 | 0.596 | 7112 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.297 | observe | 1 | 1.0 | 1044 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4494 |
| Epodonios-all | 0.255 | observe | 0 | None | 6424 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3985 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 7 |
| tg-AzadNet | 0.175 | observe | 0 | None | 0 | 3 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 7 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |
| tg-GrizzlyVPN | 0.175 | observe | 0 | None | 0 | 1 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.596 | 31 | 21 | 52 |
| mheidari-all | 0.738 | 166 | 59 | 225 |
| Surfboard-tg-mixed | 0.816 | 266 | 60 | 326 |
| Au1rxx-base64 | 0.897 | 52 | 6 | 58 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14164 | yes | 2.31 | 0 |
| DeltaKronecker-all | 7112 | yes | 2.37 | 0 |
| Epodonios-all | 6424 | yes | 1.29 | 0 |
| SoliSpirit-all | 6163 | yes | 1.73 | 0 |
| Surfboard-tg-mixed | 4615 | yes | 1.49 | 0 |
| mahdibland-V2RayAggregator | 4615 | yes | 0.36 | 0 |
| 10ium-ScrapeCategorize-Vless | 4494 | yes | 1.39 | 0 |
| barry-far-vless | 4217 | yes | 0.7 | 0 |
| MatinGhanbari-all-sub | 3985 | yes | 1.58 | 0 |
| Surfboard-tg-vless | 3599 | yes | 1.37 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| 204 | 48 |
| speed | 41 |
| cn-block | 31 |
| geo | 27 |
