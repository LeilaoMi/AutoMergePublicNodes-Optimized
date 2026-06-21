# AutoNodes Daily Report

Generated at: 2026-06-21 10:05:49

## Summary

| Metric | Value |
| --- | --- |
| Health status | warning |
| Health ok | True |
| Sources healthy | 104/107 |
| Cleanup disable/downweight | 0/0 |
| Cleanup prefer/observe | 4/103 |
| Raw nodes | 73085 |
| Dedup nodes | 21857 |
| TCP ok | 796 |
| Real ok | 601 |
| Verified output | 300 |
| Global output | 300 |
| All output | 21857 |
| All output mode | full |

## Stage Durations

| Stage | Seconds |
| --- | --- |
| fetch | 4.8 |
| generate | 64.4 |
| geo | 1.3 |
| probe | 110.6 |
| real_test | 185.2 |
| tcp | 62.9 |

## Protocol Pass Rate

| Protocol | Tested | Passed | Failed | Pass Rate |
| --- | --- | --- | --- | --- |
| http | 69 | 69 | 0 | 100.0% |
| hysteria2 | 3 | 3 | 0 | 100.0% |
| shadowsocks | 114 | 95 | 19 | 83.3% |
| socks | 1 | 1 | 0 | 100.0% |
| trojan | 99 | 51 | 48 | 51.5% |
| vless | 506 | 378 | 128 | 74.7% |
| vmess | 4 | 4 | 0 | 100.0% |

## Main Real-Test Errors

| Error | Count |
| --- | --- |
| speed:ClientOSError | 64 |
| 204:TimeoutError | 28 |
| 204:ProxyError | 27 |
| geo:TimeoutError | 21 |
| cn-block:TimeoutError | 20 |
| cn-block:ClientOSError | 9 |
| speed:TimeoutError | 9 |
| geo:ClientOSError | 7 |
| speed:ProxyError | 5 |
| geo:ProxyError | 2 |
| cn-block:ProxyError | 2 |
| 204:ClientOSError | 1 |

## TCP Precheck Errors

| Error | Count |
| --- | --- |
| TimeoutError | 3096 |
| ConnectionRefusedError | 652 |
| gaierror | 373 |
| OSError | 108 |

## Best Sources By Score

| Source | Score | Recommendation | Tested | Pass Rate | Parsed |
| --- | --- | --- | --- | --- | --- |
| snakem982 | 0.991 | prefer | 69 | 1.0 | 131 |
| Au1rxx-base64 | 0.897 | prefer | 35 | 0.914 | 138 |
| mheidari-all | 0.858 | prefer | 291 | 0.78 | 14998 |
| Surfboard-tg-mixed | 0.84 | prefer | 332 | 0.762 | 4684 |
| DeltaKronecker-all | 0.334 | observe | 65 | 0.246 | 6748 |
| Barabama-yudou | 0.318 | observe | 2 | 1.0 | 166 |
| nscl5-all | 0.303 | observe | 1 | 1.0 | 1204 |
| abc-configs-readme-latest30 | 0.256 | observe | 1 | 1.0 | 26 |
| 10ium-ScrapeCategorize-Vless | 0.255 | observe | 0 | None | 4494 |
| Epodonios-all | 0.255 | observe | 0 | None | 7269 |

## Sources Needing Attention

| Source | Score | Recommendation | Tested | Pass Rate | Dead | Parsed |
| --- | --- | --- | --- | --- | --- | --- |
| tg-AzadNet | 0.025 | observe | 0 | None | 1 | 0 |
| tg-V2rayngVpn | 0.025 | observe | 0 | None | 1 | 0 |
| tg-shadowproxy66 | 0.025 | observe | 0 | None | 1 | 0 |
| ninja-hy2 | 0.175 | observe | 0 | None | 0 | 3 |
| ninja-tuic | 0.175 | observe | 0 | None | 0 | 1 |
| tg-Ahmedhamoomi_Servers | 0.175 | observe | 0 | None | 0 | 2 |
| tg-ArV2ray | 0.175 | observe | 0 | None | 0 | 6 |
| tg-BESTFORBEST66 | 0.175 | observe | 0 | None | 0 | 8 |
| tg-CaV2ray | 0.175 | observe | 0 | None | 0 | 12 |
| tg-ConfigWireguard | 0.175 | observe | 0 | None | 0 | 5 |

## Worst Sources By Real-Test Pass Rate

| Source | Pass Rate | Passed | Failed | Tested |
| --- | --- | --- | --- | --- |
| DeltaKronecker-all | 0.246 | 16 | 49 | 65 |
| Surfboard-tg-mixed | 0.762 | 253 | 79 | 332 |
| mheidari-all | 0.78 | 227 | 64 | 291 |
| Au1rxx-base64 | 0.914 | 32 | 3 | 35 |
| abc-configs-readme-latest30 | 1.0 | 1 | 0 | 1 |
| nscl5-all | 1.0 | 1 | 0 | 1 |
| Barabama-yudou | 1.0 | 2 | 0 | 2 |
| snakem982 | 1.0 | 69 | 0 | 69 |

## Top Sources By Parsed Nodes

| Source | Nodes | OK | Duration | Consecutive Dead |
| --- | --- | --- | --- | --- |
| mheidari-all | 14998 | yes | 3.18 | 0 |
| Epodonios-all | 7269 | yes | 2.21 | 0 |
| SoliSpirit-all | 7017 | yes | 1.4 | 0 |
| DeltaKronecker-all | 6748 | yes | 2.95 | 0 |
| Surfboard-tg-mixed | 4684 | yes | 1.72 | 0 |
| mahdibland-V2RayAggregator | 4510 | yes | 1.48 | 0 |
| 10ium-ScrapeCategorize-Vless | 4494 | yes | 0.97 | 0 |
| barry-far-vless | 4394 | yes | 1.1 | 0 |
| MatinGhanbari-all-sub | 3997 | yes | 1.17 | 0 |
| Surfboard-tg-vless | 3546 | yes | 1.89 | 0 |

## Trend Alerts

No trend alerts.

## Health Alerts

### Real-test error alerts
| Error | Count |
| --- | --- |
| speed | 78 |
| 204 | 56 |
| cn-block | 31 |
| geo | 30 |
