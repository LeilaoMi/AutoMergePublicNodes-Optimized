# 订阅源清理建议

生成时间：2026-06-09 20:12:57

本报告默认只读。修改 `config/sources.yaml` 前请人工复核。

## 摘要

| 分类 | 数量 |
| --- | --- |
| disable | 0 |
| downweight | 13 |
| prefer | 1 |
| observe | 30 |

## 建议禁用

无记录。

## 建议降权

| 订阅源 | 评分 | 已测 | 通过率 | 解析数 | 连续死亡 | 原因 | URL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ts-sf | 0.059 | 10 | 0.0 | 59 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/ts-sf/fly/main/clash |
| moneyfly1-collectSub | 0.069 | 43 | 0.0 | 1164 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/moneyfly1/collectSub/refs/heads/main/config_all_merged_nodes.txt |
| xiaoji235-airport-v2ray-all | 0.082 | 11 | 0.0 | 678 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt |
| 10ium-HighSpeed | 0.102 | 6 | 0.0 | 839 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/10ium/free-config/refs/heads/main/HighSpeed.txt |
| Surfboard-tg-vless | 0.109 | 103 | 0.019 | 3238 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/vless |
| SoliSpirit-all | 0.117 | 25 | 0.0 | 3000 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/all_configs.txt |
| ninja-vless | 0.123 | 13 | 0.0 | 1791 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/vless.txt |
| 10ium-ScrapeCategorize-Vless | 0.129 | 15 | 0.0 | 2000 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/Vless.txt |
| mahdibland-V2RayAggregator | 0.148 | 6 | 0.0 | 4536 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt |
| DeltaKronecker-all | 0.154 | 269 | 0.071 | 4764 | 0 | 已测数量 >= 5 且评分偏低 | https://github.com/Delta-Kronecker/V2ray-Config/raw/refs/heads/main/config/all_configs.txt |
| nscl5-all | 0.177 | 6 | 0.167 | 1026 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/nscl5/5/refs/heads/main/configs/all.txt |
| chromego_merge | 0.195 | 7 | 0.286 | 55 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml |
| Surfboard-tg-mixed | 0.244 | 743 | 0.163 | 4132 | 0 | 已测数量 >= 5 且评分偏低 | https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed |

## 建议优先保留

| 订阅源 | 评分 | 已测 | 通过率 | 解析数 | 连续死亡 | 原因 | URL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| snakem982 | 0.821 | 53 | 0.83 | 61 | 0 | 源评分较高 | https://raw.githubusercontent.com/snakem982/proxypool/main/source/clash-meta.yaml |

## 继续观察

| 订阅源 | 评分 | 已测 | 通过率 | 解析数 | 连续死亡 | 原因 | URL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Au1rxx-base64 | 0.528 | 59 | 0.525 | 93 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/main/output/v2ray-base64.txt |
| Au1rxx-clash | 0.179 | 0 | None | 93 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Au1rxx/free-vpn-subscriptions/main/output/clash.yaml |
| Barabama-we | 0.128 | 1 | 0.0 | 23 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt |
| Barabama-yudou | 0.087 | 4 | 0.0 | 166 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt |
| Epodonios-all | 0.207 | 1 | 0.0 | 3000 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt |
| MatinGhanbari-all-sub | 0.255 | 0 | None | 3000 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/refs/heads/main/subscriptions/v2ray/all_sub.txt |
| MatinGhanbari-super-sub | 0.183 | 0 | None | 200 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/refs/heads/main/subscriptions/v2ray/super-sub.txt |
| Mr8AHAL | 0.176 | 0 | None | 26 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Mr8AHAL/v2ray/main/SERVER.txt |
| Pawdroid | 0.175 | 0 | None | 7 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub |
| abc-configs-readme-latest30 | 0.269 | 3 | 0.667 | 20 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/FreeFolksOn/abc-configs-free-vpn-proxy-list/main/README.md |
| barabama-nodefree | 0.176 | 0 | None | 23 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.yaml |
| barabama-yudou66 | 0.182 | 0 | None | 163 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.yaml |
| barry-far-Sub1 | 0.194 | 0 | None | 476 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub1.txt |
| barry-far-Sub2 | 0.195 | 0 | None | 498 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt |
| barry-far-vless | 0.255 | 0 | None | 2000 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt |
| ermaozi | 0.176 | 0 | None | 29 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt |
| ermaozi-get_subscribe | 0.176 | 0 | None | 29 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml |
| freefq | 0.176 | 0 | None | 14 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/freefq/free/master/v2 |
| mfuu-v2ray | 0.184 | 0 | None | 225 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/mfuu/v2ray/master/v2ray |
| mheidari-all | 0.286 | 100 | 0.2 | 2000 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/mheidari98/.proxy/main/all |
| ninja-hy2 | 0.175 | 0 | None | 3 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/hysteria.txt |
| ninja-tuic | 0.128 | 1 | 0.0 | 1 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/ninjastrikers/v2ray-configs/main/splitted/tuic.txt |
| peasoft-NoMoreWalls | 0.176 | 0 | None | 37 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml |
| ripaojiedian-freenode | 0.176 | 0 | None | 15 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash |
| roosterkid-openproxylist-v2ray | 0.441 | 21 | 0.429 | 150 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt |
| tonykong-base64 | 0.175 | 0 | None | 5 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/tonykongcn/free-vpn-subscriptions/main/output/v2ray-base64.txt |
| tonykong-clash | 0.175 | 0 | None | 5 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/tonykongcn/free-vpn-subscriptions/main/output/clash.yaml |
| ts-sf-Fly | 0.177 | 0 | None | 60 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/ts-sf/Fly/main/v2 |
| vxiaov | 0.176 | 0 | None | 28 | 0 | 证据不足或评分中性 | https://cdn.jsdelivr.net/gh/vxiaov/free_proxies@main/clash/clash.provider.yaml |
| zhangkai | 0.177 | 0 | None | 61 | 0 | 证据不足或评分中性 | https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml |
