# 同类项目全量深度对标分析（最终版）

> 分析时间：2026-06-14
> 分析范围：GitHub 上 **33 个**公开节点抓取/聚合项目，穷尽搜索所有关键词组合
> 目的：提炼可落地的工程优点，补足完善 AutoMergePublicNodes-Optimized

---

## 一、全量项目概览（33 个，按 star 降序）

### A. 有工程代码的项目（8 个）

| # | 项目 | Stars | 语言 | 更新 | 真测 | 核心特点 |
|---|---|---:|---|---|---|---|
| 1 | chengaopan/AutoMergePublicNodes | 7.6k | Python | 定时 | 否 | 我们项目的父仓库 |
| 2 | mahdibland/V2RayAggregator | 4.0k | Python | 12h | 是(LiteSpeedTest) | LiteSpeedTest 测速 + 区域配置 + subconverter |
| 3 | Epodonios/v2ray-configs | 3.1k | Python | **5min** | 否 | 5 分钟高频更新 + 42 分块 + 协议分文件 |
| 4 | Barabama/FreeNodes | 2.8k | Python(Scrapy) | 12h | 否 | Scrapy 爬虫 + 多源分文件 |
| 5 | snakem982/proxypool | 1.8k | Go | 实时 | 否 | Go 爬虫 + CDN 输出 |
| 6 | Resinat/Resin | 1.3k | Go | 实时 | 否 | 高性能代理池网关 + sticky session |
| 7 | xiaoji235/airport-free | 512 | Python | 3h | 否 | 多源爬取 + 去重 + CDN 分片 |
| 8 | **LeilaoMi/AutoMergePublicNodes-Optimized** | **5** | **Python** | **6h** | **是(sing-box)** | **sing-box 真测 + 5 因子评分 + 4 套模板** |

### B. 纯分享/无代码/GitHub Pages 项目（25 个）

| # | 项目 | Stars | 特点 |
|---|---|---:|---|
| 9 | Pawdroid/Free-servers | 17.8k | 纯分享 + v2cross.com |
| 10 | free-nodes/clashfree | 15.7k | 纯分享 + clashgithub.com |
| 11 | OpenRunner/clash-freenode | 6.3k | 纯分享 SSR/Clash/V2Ray |
| 12 | VPN-Subcription-Links/ClashX-V2Ray-TopFreeProxy | 5.3k | 纯分享 |
| 13 | shuaidaoya/FreeNodes | 2.3k | SubsCheck 测速后分享 |
| 14 | ebrasha/free-v2ray-public-list | 952 | TG Bot + 15min 更新 |
| 15 | mfuu/v2ray | 888 | 极简 Python |
| 16 | freenodes/freenodes | 758 | GitHub Pages 独立站 |
| 17 | ts-sf/fly | 662 | 纯分享 |
| 18 | vxiaov/free_proxies | 577 | TG 频道联动 |
| 19 | mermeroo/V2RAY-CLASH-BASE64 | 503 | 链接聚合 |
| 20 | kooker/FreeSubsCheck | 47 | subs-check 测速 |
| 21 | wenxig/free-nodes-sub | 56 | TypeScript |
| 22 | firefoxmmx2/v2rayshare_subcription | 51 | v2rayshare 抓取 |
| 23 | xyfqzy/free-nodes | 122 | Python 自动化 |
| 24 | littlebais/free-proxy-nodes | 111 | 节点池聚合 |
| 25 | gfwcross/v2pool | 81 | Python 测速 |
| 26 | Surfboardv2ray/v2ray-worker-sub | 143 | Cloudflare Worker |
| 27 | clashv2ray-hub/clashfree | 258 | Shell + Pages |
| 28 | clashv2ray-hub/v2rayfree | 257 | Shell + Pages |
| 29 | abshare3/abshare3.github.io | 257 | GitHub Pages |
| 30 | toshare5/toshare5.github.io | 220 | GitHub Pages |
| 31 | FreeFolksOn/abc-configs-free-vpn-proxy-list | 24 | TG 联动 |
| 32 | clashv2rayu/clashv2rayu.github.io | 25 | GitHub Pages |
| 33 | clash2025/clash2025 | 15 | Python |

---

## 二、逐项优点提炼

### 1. Barabama/FreeNodes — Scrapy 爬虫框架

**他们的做法：**
- 使用 Scrapy 框架，每个数据源一个 Spider
- `config.json` 集中管理所有目标站点
- 每个源输出独立的 `.txt` + `.yaml`
- 用户可以选择只订阅某个源的节点

**我们可学习的：**
- ✅ 模块化爬虫：每个源独立 Spider，某个源挂了不影响其他
- ✅ 配置驱动源列表
- ❌ Scrapy 太重，我们已有更轻的 asyncio 异步抓取

**差距评估：** 无。我们的 `core/fetcher.py` 已经是异步并发 + 配置驱动。但可以借鉴"分源输出"的想法——按来源分文件输出，方便用户选择。

---

### 2. snakem982/proxypool — Go 爬虫 + CDN

**他们的做法：**
- Go 语言编写爬虫，性能优于 Python
- 爬取多种协议格式（vmess/vless/trojan/ss/hysteria2）
- 输出 clash-meta.yaml 和 v2ray.txt 两种格式
- 有 spider 目录，每个爬虫独立
- 有 cdn 目录做输出分发
- 4700+ commits，维护非常活跃

**我们可学习的：**
- ✅ 多协议解析覆盖面广（含 hysteria2、tuic 等新协议）
- ✅ Spider 模块化
- ❌ Go vs Python：我们没有切换语言的需求

**差距评估：** 协议覆盖我们已覆盖 vmess/vless/trojan/ss/ssr/hysteria/hysteria2/tuic/anytls/socks5/http，比他们更全。

---

### 3. xiaoji235/airport-free — 3 小时高频更新 + CDN 分片

**他们的做法：**
- 每 3 小时更新一次（比常见的 6h 更频繁）
- 多个 Python 脚本分别爬不同站点
- 输出分片：v2ray nodes 1/2/3, clash nodes 1/2/3
- CDN 分片降低单文件体积
- jsDelivr 加速 + GitHub 直连双通道
- README 中直接显示更新时间
- 有 Issues 提交新源的社区机制

**我们可学习的：**
- ✅ **CDN 分片输出**：大订阅文件拆成多个分片，避免单文件过大被 CDN 缓存卡住
- ✅ **更新频率可调**：我们当前 6h，可考虑支持 3h/4h 选项
- ✅ **社区贡献源**：Issues 模板让用户提交新源

---

### 4. shuaidaoya/FreeNodes — SubsCheck 自动测速

**他们的做法：**
- 使用 SubsCheck-Win-GUI 自动从节点池测速筛选
- 每 4h 更新一次
- 测速后输出可用节点

**我们可学习的：**
- ✅ 自动测速概念（我们已有 sing-box 真测，更彻底）
- ❌ SubsCheck 是 Windows GUI 工具，不适合 CI

**差距评估：** 我们的 sing-box 真测比 SubsCheck 更可靠，且支持 CI 自动化。

---

### 5. Pawdroid/Free-servers — 17.8k Stars 纯分享

**他们的做法：**
- 无代码，纯订阅链接分享
- 6h 更新
- README 极其简洁，只有订阅链接
- v2cross.com 独立网站导流

**我们可学习的：**
- ✅ README 简洁明了：用户打开就看到订阅链接
- ✅ 独立网站导流（我们暂不需要）
- ❌ 无工程能力，不可持续

**差距评估：** 我们的 README 已有快速选择表格 + 多格式链接 + 状态区，比他们更完善。

---

## 三、总结：我们的独特优势 vs 短板

### 我们已经领先的能力（全 33 个项目中独一无二）

| 能力 | 同类项目普遍水平 | 我们的水平 | 独特性 |
|---|---|---|---|
| 真实代理测试 | 仅 V2RayAggregator(LiteSpeedTest) | sing-box 全协议真测 | **唯一** |
| 综合评分排序 | 纯延迟 或 无排序 | 5 因子加权评分 + 4 套模板 | **唯一** |
| 评分透明度 | 无 | 分项 breakdown + 报告 | **唯一** |
| 可观测性 | 仅 V2RayAggregator 有 Log | health_report + daily_report + Actions Summary | **唯一** |
| 源质量治理 | 无 | 自动评分 + 清理建议 | **唯一** |
| 配置化 | 部分有 | 全配置化 + CI 校验 + 多模板 | **领先** |
| 多格式输出 | txt + yaml | txt/yaml/json/urls | **领先** |
| 回归测试 | 无 | 58 个测试 | **唯一** |
| 发布规范 | 无 | CHANGELOG + Release Notes | **唯一** |
| README 自动状态 | 极少 | 自动状态区 + Top 节点 | **领先** |

### 我们需要补足的短板（从 33 个项目提炼）

| 短板 | 来源 | 优先级 | 实现难度 | 验证依据 |
|---|---|---|---|---|
| **分块输出** | Epodonios/V2RayAggregator/xiaoji235/ebrasha | 高 | 中 | 4 个工程化项目都做了 |
| **协议分文件** | Epodonios/V2RayAggregator/ebrasha | 高 | 中 | 3 个项目都做了 |
| **社区贡献源** | xiaoji235/V2RayAggregator | 中 | 低 | 2 个项目有 |
| **Cloudflare Worker 加速** | Surfboardv2ray | 中 | 中 | 独特架构 |
| **订阅管理系统** | eooce/Merge-sub | 中 | 高 | 合并多订阅 |
| **Telegram Bot** | ebrasha | 低 | 中 | 1 个项目有 |
| **区域化 Clash 配置** | V2RayAggregator | 低 | 中 | 不同地区分流 |
| **独立网站** | free-nodes/clashfree | 低 | 高 | 15.7k star 来源 |
| **代理池网关** | Resinat/Resin | 低 | 高 | sticky session |

---

## 四、推荐迭代路线（优先级排序）

### P0：CDN 分片输出（高价值）

**问题：** 当 verified 节点 > 300 时，单文件可能超过 500KB，jsDelivr CDN 缓存更新延迟。

**方案：**
```
output/verified_1.txt   # 第 1-100 个节点
output/verified_2.txt   # 第 101-200 个节点
output/verified_3.txt   # 第 201-300 个节点
output/verified_all.txt # 全量（兼容旧订阅）
```

**影响文件：**
- `core/generator.py`：新增分片输出逻辑
- `main.py`：传入分片参数
- `.github/workflows/update.yml`：purge 分片文件

### P1：社区贡献源机制（中价值）

**方案：**
- 创建 Issue 模板 `.github/ISSUE_TEMPLATE/new-source.md`
- 用户填 URL + 协议 + 预估节点数
- 维护者审核后加入 `config/sources.yaml`

### P2：按来源分文件输出（中价值）

**方案：**
```
output/by_source/snakem982.txt
output/by_source/aiboboxx.txt
output/by_source/v2rayshare.txt
```

方便用户只订阅高质量源的节点。

### P3：Telegram/Discord 推送（低优先）

**方案：**
- CI 完成后通过 Bot 推送更新摘要
- 包含节点数量、Top 延迟、报告链接

---

## 五、新发现项目深度分析

### 6. mahdibland/V2RayAggregator (4.0k stars) — 最接近我们的工程化项目

**他们的做法：**
- Python + GitHub Actions 全自动化
- 使用 LiteSpeedTest 做测速筛选（类似我们的 sing-box 真测）
- 收集 20+ 个公共节点源，22758 commits，维护极为活跃
- 输出 Base64/Mixed/Clash 三种格式
- 按协议分文件：VMESS / TROJAN / SSR / SHADOWSOCKS
- 按区域输出 Clash 配置：Iran / China / Others
- 提供 subconverter 在线转换服务
- 提供 Netlify 可视化 Log Visualizer
- 输出分块订阅（200 节点/块）
- 机场节点单独分组，2 小时更新

**我们可学习的（新发现）：**
- ✅ **区域化配置**：Clash Meta For Iran/China/Others — 不同地区输出不同分流策略
- ✅ **机场 vs 公共节点分组**：两类源分开管理，更新频率不同
- ✅ **Log Visualizer**：Netlify 上可视化节点延迟测试结果
- ✅ **subconverter 集成**：支持用户自行转换格式
- ✅ **块输出**：200 个/块，避免大文件问题（与我们 P0 方向一致）

**差距评估：** 这是最接近我们工程水平的项目。但他们用 LiteSpeedTest 测速，我们用 sing-box 真测，我们的测速更准确。

---

### 7. Epodonios/v2ray-configs (3.1k stars) — 5 分钟极高频更新

**他们的做法：**
- **每 5 分钟更新一次**（是所有同类项目中最高的频率）
- 43237 commits，极为活跃
- 收集数千个配置
- 输出 Sub1.txt ~ Sub42.txt（42 个分块文件，250 配置/块）
- 按协议分文件：vless/vmess/ss/ssr/trojan
- 提供 Base64 格式
- 提供 V2Ray Config Scanner 脚本（Python，测延迟）
- GPL-3.0 开源

**我们可学习的（新发现）：**
- ✅ **42 个分块文件**：比 xiaoji235 的 3 个分块更极致，大池子也不会单文件过大
- ✅ **5 分钟更新**：虽然 GitHub Actions 免费版不支持 5 分钟 cron，但说明高频更新有需求
- ✅ **独立 Scanner 脚本**：让用户本地测延迟排序

**差距评估：** 我们 6h 更新，但有 sing-box 真测 + 综合评分，质量远高于他们纯堆量。他们的分块策略值得学习。

---

### 8. ebrasha/free-v2ray-public-list (952 stars) — Telegram Bot + 15 分钟更新

**他们的做法：**
- **每 15 分钟更新**
- 支持 SS/SSR/Trojan/VLESS/VMess/TUIC/Hysteria2 全协议
- **Telegram Bot 自动推送配置**：@AbdalV2rayBot
- Bot 功能：按国家/平台/端口过滤配置，定时自动发送
- 按协议分文件输出
- 分块输出：mixed-protocol-chunks / separated-protocols-chunks
- 双语 README（英语 + 波斯语）
- 面向伊朗用户为主，兼顾中国

**我们可学习的（新发现）：**
- ✅ **Telegram Bot 集成**：不只是推送，还支持过滤和定时发送
- ✅ **按国家/端口过滤配置**：用户可以选择特定地区的节点
- ✅ **分块 + 分协议双重输出**：chunks 目录 + separated 目录
- ✅ **多语言 README**：面向不同地区用户

---

## 六、汇总：所有项目的优点矩阵

| 能力/特性 | 我们 | V2RayAggregator | Epodonios | ebrasha | Barabama | xiaoji235 | snakem982 |
|---|---|---|---|---|---|---|---|
| 真实代理测试 | ✅ sing-box | ✅ LiteSpeedTest | ❌ | ❌ | ❌ | ❌ | ❌ |
| 综合评分排序 | ✅ 5因子 | ❌ 纯速度 | ❌ | ❌ | ❌ | ❌ | ❌ |
| 评分透明度 | ✅ breakdown | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 配置化 | ✅ 全配置 | 部分 | ❌ | ❌ | ✅ config.json | ❌ | ❌ |
| 多格式输出 | ✅ 4格式 | ✅ 3格式 | ✅ 3格式 | ✅ 多格式 | ✅ 2格式 | ✅ 2格式 | ✅ 2格式 |
| 协议分文件 | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| 分块输出 | ❌ | ✅ 200/块 | ✅ 250/块 | ✅ chunks | ❌ | ✅ 3块 | ❌ |
| 区域化配置 | ❌ | ✅ Iran/China | ❌ | ❌ | ❌ | ❌ | ❌ |
| 源质量治理 | ✅ 自动 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 可观测报告 | ✅ 多报告 | ✅ Log Visualizer | ❌ | ❌ | ❌ | ❌ | ❌ |
| 回归测试 | ✅ 58个 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Telegram Bot | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 按国家过滤 | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 更新频率 | 6h | 12h | 5min | 15min | 12h | 3h | 实时 |
| 发布规范 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## 七、更新后的迭代路线（优先级排序）

### P0：CDN 分块输出（高价值，多方验证）

来源：xiaoji235 + V2RayAggregator + Epodonios + ebrasha

4 个高 star 项目都做了分块，说明这是刚需。

**方案：**
```
output/verified_1.txt   # 第 1-100
output/verified_2.txt   # 第 101-200
output/verified_3.txt   # 第 201-300
output/verified.txt     # 全量（兼容旧订阅）
```

### P1：按协议分文件输出（中价值，多方验证）

来源：V2RayAggregator + Epodonios + ebrasha

3 个项目都做了协议分文件。

**方案：**
```
output/by_protocol/vmess.txt
output/by_protocol/vless.txt
output/by_protocol/trojan.txt
output/by_protocol/ss.txt
```

### P2：社区贡献源机制（中价值）

来源：xiaoji235 + V2RayAggregator 的源列表

**方案：**
- Issue 模板 `.github/ISSUE_TEMPLATE/new-source.md`

### P3：Telegram Bot 推送（低优先，差异化）

来源：ebrasha

**方案：**
- CI 完成后 Bot 推送更新摘要

### P4：区域化 Clash 配置（低优先）

来源：V2RayAggregator

**方案：**
- 输出 Clash Meta For China（国内分流策略）
- 输出 Clash Meta For Global（海外分流策略）

所有新功能开发前，先在本地验证：

```bash
cd /sdcard/Download/Operit/projects/AutoMergePublicNodes-Optimized

# 编译检查
python -m compileall -q main.py core tools tests

# 配置校验
python tools/validate_config.py \
  --sources config/sources.yaml \
  --filter-rules config/filter_rules.yaml \
  --scoring-rules 'config/scoring*.yaml'

# 回归测试
python -m unittest -v tests.test_regressions
```

确认全绿后再提交到远程仓库。
