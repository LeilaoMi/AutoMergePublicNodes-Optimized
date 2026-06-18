# AutoNodes Daily Report

Generated at: 2026-06-18 04:04:10

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 44/44 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/40 |
| Raw nodes | 67785 |
| Dedup nodes | 22227 |
| TCP ok | 1123 |
| Real ok | 657 |
| Verified output | 300 |
| Global output | 300 |
| All output | 22227 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 3.6 |
| generate | 30.9 |
| geo | 1.3 |
| probe | 95.6 |
| real_test | 194.4 |
| tcp | 60.0 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 25 | 25 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 140 | 127 | 13 | 90.7% |
| socks | 2 | 1 | 1 | 50.0% |
| trojan | 34 | 33 | 1 | 97.1% |
| vless | 914 | 463 | 451 | 50.7% |
| vmess | 5 | 5 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| geo:TimeoutError | 215 |
| speed:ClientOSError | 125 |
| geo:ClientOSError | 36 |
| speed:TimeoutError | 34 |
| cn-block:TimeoutError | 14 |
| 204:ProxyError | 13 |
| 204:TimeoutError | 11 |
| cn-block:ClientOSError | 8 |
| 204:ClientOSError | 6 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 1 |
| speed:ProxyError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3142 |
| ConnectionRefusedError | 611 |
| gaierror | 333 |
| OSError | 59 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.966 | prefer | 25 | 1.0 | 73 |
| Surfboard-tg-mixed | 0.943 | prefer | 312 | 0.865 | 4586 |
| Au1rxx-base64 | 0.828 | prefer | 88 | 0.83 | 141 |
| mheidari-all | 0.748 | prefer | 182 | 0.67 | 13927 |
| DeltaKronecker-all | 0.403 | observe | 509 | 0.322 | 7763 |
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
| tonykong-base64 | 0.175 | observe | 0 | None | 0 | 5 |
| tonykong-clash | 0.175 | observe | 0 | None | 0 | 5 |
| Barabama-we | 0.176 | observe | 0 | None | 0 | 23 |
| Mr8AHAL | 0.176 | observe | 0 | None | 0 | 26 |
| Pawdroid | 0.176 | observe | 0 | None | 0 | 20 |
| abc-configs-readme-latest30 | 0.176 | observe | 0 | None | 0 | 22 |
| barabama-nodefree | 0.176 | observe | 0 | None | 0 | 23 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| ninja-vless | 0.0 | 0 | 4 | 4 |
| DeltaKronecker-all | 0.322 | 164 | 345 | 509 |
| mheidari-all | 0.67 | 122 | 60 | 182 |
| Au1rxx-base64 | 0.83 | 73 | 15 | 88 |
| Surfboard-tg-mixed | 0.865 | 270 | 42 | 312 |
| xiaoji235-airport-v2ray-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 25 | 0 | 25 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 13927 | yes | 3.33 | 0 |
| DeltaKronecker-all | 7763 | yes | 3.12 | 0 |
| Epodonios-all | 6401 | yes | 1.98 | 0 |
| SoliSpirit-all | 6039 | yes | 1.99 | 0 |
| Surfboard-tg-mixed | 4586 | yes | 2.12 | 0 |
| mahdibland-V2RayAggregator | 4541 | yes | 1.51 | 0 |
| 10ium-ScrapeCategorize-Vless | 4274 | yes | 1.51 | 0 |
| barry-far-vless | 4240 | yes | 1.2 | 0 |
| MatinGhanbari-all-sub | 3977 | yes | 1.51 | 0 |
| Surfboard-tg-vless | 3590 | yes | 1.75 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| geo | 253 |
| speed | 160 |
| 204 | 30 |
| cn-block | 23 |
