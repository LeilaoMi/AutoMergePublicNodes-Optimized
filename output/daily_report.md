# AutoNodes Daily Report

Generated at: 2026-06-20 09:34:49

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 105/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 73485 |
| Dedup nodes | 21780 |
| TCP ok | 800 |
| Real ok | 608 |
| Verified output | 300 |
| Global output | 300 |
| All output | 21780 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.2 |
| generate | 34.8 |
| geo | 1.4 |
| probe | 109.7 |
| real_test | 198.4 |
| tcp | 66.2 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 2 | 2 | 0 | 100.0% |
| shadowsocks | 106 | 92 | 14 | 86.8% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 134 | 91 | 43 | 67.9% |
| vless | 526 | 392 | 134 | 74.5% |
| vmess | 5 | 5 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| speed:ClientOSError | 49 |
| geo:TimeoutError | 29 |
| cn-block:TimeoutError | 26 |
| 204:ProxyError | 17 |
| speed:TimeoutError | 15 |
| 204:TimeoutError | 14 |
| geo:ClientOSError | 12 |
| cn-block:ClientOSError | 11 |
| 204:ClientOSError | 11 |
| speed:ProxyError | 4 |
| cn-block:ProxyError | 3 |
| geo:ProxyError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3516 |
| ConnectionRefusedError | 636 |
| gaierror | 361 |
| OSError | 87 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| mheidari-all | 0.885 | prefer | 264 | 0.807 | 14813 |
| Surfboard-tg-mixed | 0.863 | prefer | 395 | 0.785 | 5054 |
| Au1rxx-base64 | 0.815 | prefer | 35 | 0.829 | 93 |
| DeltaKronecker-all | 0.46 | observe | 77 | 0.377 | 6810 |
| nscl5-all | 0.3 | observe | 1 | 1.0 | 1126 |
| tg-LonUp_M | 0.262 | observe | 1 | 1.0 | 177 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4507 |
| Epodonios-all | 0.255 | observe | 0 | None | 7491 |
| MatinGhanbari-all-sub | 0.255 | observe | 0 | None | 3976 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| Barabama-yudou | 0.134 | observe | 1 | 0.0 | 0 | 166 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-DirectVPN | 0.175 | observe | 0 | None | 0 | 12 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| Barabama-yudou | 0.0 | 0 | 1 | 1 |
| ninja-vless | 0.0 | 0 | 1 | 1 |
| DeltaKronecker-all | 0.377 | 29 | 48 | 77 |
| Surfboard-tg-mixed | 0.785 | 310 | 85 | 395 |
| mheidari-all | 0.807 | 213 | 51 | 264 |
| Au1rxx-base64 | 0.829 | 29 | 6 | 35 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| tg-LonUp_M | 1.0 | 1 | 0 | 1 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14813 | yes | 3.17 | 0 |
| Epodonios-all | 7491 | yes | 2.18 | 0 |
| SoliSpirit-all | 6983 | yes | 2.02 | 0 |
| DeltaKronecker-all | 6810 | yes | 2.85 | 0 |
| Surfboard-tg-mixed | 5054 | yes | 2.78 | 0 |
| mahdibland-V2RayAggregator | 4516 | yes | 1.38 | 0 |
| 10ium-ScrapeCategorize-Vless | 4507 | yes | 1.18 | 0 |
| barry-far-vless | 4443 | yes | 1.02 | 0 |
| MatinGhanbari-all-sub | 3976 | yes | 1.1 | 0 |
| Surfboard-tg-vless | 3744 | yes | 1.92 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| speed | 68 |
| 204 | 42 |
| geo | 42 |
| cn-block | 40 |
