# AutoNodes Daily Report

Generated at: 2026-06-18 15:45:29

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 106/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 5/102 |
| Raw nodes | 70175 |
| Dedup nodes | 21946 |
| TCP ok | 719 |
| Real ok | 586 |
| Verified output | 300 |
| Global output | 300 |
| All output | 21946 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.7 |
| generate | 51.6 |
| geo | 1.3 |
| probe | 93.1 |
| real_test | 176.9 |
| tcp | 61.8 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 4 | 4 | 0 | 100.0% |
| shadowsocks | 121 | 106 | 15 | 87.6% |
| socks | 17 | 14 | 3 | 82.4% |
| trojan | 96 | 57 | 39 | 59.4% |
| vless | 449 | 373 | 76 | 83.1% |
| vmess | 7 | 7 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| cn-block:TimeoutError | 26 |
| speed:ClientOSError | 24 |
| 204:ProxyError | 17 |
| 204:TimeoutError | 15 |
| cn-block:ProxyError | 12 |
| cn-block:ClientOSError | 10 |
| geo:ClientOSError | 10 |
| speed:TimeoutError | 10 |
| geo:ProxyError | 4 |
| speed:ProxyError | 3 |
| geo:TimeoutError | 1 |
| 204:ClientOSError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3205 |
| ConnectionRefusedError | 640 |
| gaierror | 351 |
| OSError | 62 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Au1rxx-base64 | 0.922 | prefer | 82 | 0.927 | 133 |
| Surfboard-tg-mixed | 0.906 | prefer | 325 | 0.828 | 4764 |
| mheidari-all | 0.85 | prefer | 228 | 0.772 | 14064 |
| DeltaKronecker-all | 0.729 | prefer | 55 | 0.655 | 7112 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| xiaoji235-airport-v2ray-all | 0.289 | observe | 1 | 1.0 | 847 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 174 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4494 |
| Epodonios-all | 0.255 | observe | 0 | None | 6309 |

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
| DeltaKronecker-all | 0.655 | 36 | 19 | 55 |
| mheidari-all | 0.772 | 176 | 52 | 228 |
| Surfboard-tg-mixed | 0.828 | 269 | 56 | 325 |
| Au1rxx-base64 | 0.927 | 76 | 6 | 82 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14064 | yes | 2.74 | 0 |
| DeltaKronecker-all | 7112 | yes | 3.11 | 0 |
| Epodonios-all | 6309 | yes | 0.66 | 0 |
| SoliSpirit-all | 5844 | yes | 1.84 | 0 |
| Surfboard-tg-mixed | 4764 | yes | 2.46 | 0 |
| mahdibland-V2RayAggregator | 4615 | yes | 1.71 | 0 |
| 10ium-ScrapeCategorize-Vless | 4494 | yes | 1.5 | 0 |
| barry-far-vless | 4375 | yes | 2.45 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.62 | 0 |
| Surfboard-tg-vless | 3752 | yes | 1.65 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| cn-block | 48 |
| speed | 37 |
| 204 | 33 |
| geo | 15 |
