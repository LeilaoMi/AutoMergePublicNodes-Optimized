# Security Policy

## 本仓库做了什么

`AutoMergePublicNodes-Optimized` 是一个**公开订阅源聚合 + 真测 + 重新分发**的工具。我们：

- **不存储任何用户流量**。所有真测目标都是公开测速/解锁检测站（youtube/generate_204, cloudflare, www.cloudflare.com/cdn-cgi/trace, baidu/robots.txt 等）。
- **不记录任何用户行为**。本仓库不收集订阅者的 IP、访问时间、使用习惯。
- **不代理任何用户流量**。本仓库的 CI 只跑真测流水线，不提供任何"代理服务"。

## 公开节点的风险（给订阅者）

- 公开节点**稳定性不可控**。本仓库只做"测试当下可用"，不保证后续可用。
- 公开节点**可能被记录访问日志**。敏感流量不应通过本仓库的订阅。
- 公开节点**可能违反当地法规**。请自行评估合规风险。

## 如何报告安全问题

发现安全漏洞（例如：源码注入、Token 泄露、恶意源）请：
1. **不要**直接开公开 Issue
2. 邮件联系维护者（见仓库顶部）
3. 我们会在 48 小时内确认

## 反滥用措施（CI 侧）

- 所有真测并发受 `asyncio.Semaphore` 门控（探活 100 并发、真测 50 并发），避免对目标站点造成压力
- TCP 预筛 + 轻量探活 + 完整真测三层过滤，避免无意义请求
- `tools/audit_sources.py` 在流水线起始阶段对订阅源做健康审计，识别死源并自动禁用
- `core/filtering.py` 的 SSRF 防投毒：拦截指向私有地址 / 云元数据端点的恶意节点
- `tools/import_contract.py` 在 CI 阶段检查导入契约，防止悬空 import 破坏构建

## 第三方镜像与订阅

- 本仓库仅在 GitHub 主仓 + jsDelivr CDN 公开分发
- 其他第三方镜像**未经验证**，可能篡改订阅内容
- 推荐使用 jsDelivr 链接：`https://cdn.jsdelivr.net/gh/LeilaoMi/AutoMergePublicNodes-Optimized@main/output/verified.txt`

## 已知免责

本仓库仅供**学习与研究**使用。使用者应自行承担合规与安全责任。
