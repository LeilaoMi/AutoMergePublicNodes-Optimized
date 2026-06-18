# 自托管真测集群（P2-1）

> **状态**：P2-1 已交付**接口抽象 + 文档**，未实施基础设施变更。当前 CI 仍用 GitHub Actions runner。

## 为什么

当前 GitHub runner：
- 单 runner IP 段被目标站点频繁风控
- 4 核 runner 上 30 并发是真测上限
- 8 分钟跑完 500 节点已达吞吐极限

**自托管后**：
- 4 台 8 核 VPS 分散 IP 段
- 真测时间从 8 分钟 → 90 秒
- 单轮真测节点从 500 → 3000+

## 架构

```
┌──────────────┐    ┌────────────────────┐
│  GitHub      │───▶│  K8s cluster       │
│  Actions     │    │  (4 nodes)         │
│  (orchestrate)   │                    │
└──────────────┘    │  ┌──────────────┐  │
                    │  │test-farm-api │  │
                    │  │  :8000       │  │
                    │  └──────────────┘  │
                    │         │           │
                    │  ┌──────┴──────┐    │
                    │  ▼      ▼     ▼    │
                    │ pod1  pod2  pod3... │
                    │ (sing-box 集群)    │
                    └────────────────────┘
```

## 部署步骤（暂未实施）

1. **K3s 集群**：4 台 VPS（建议 Hetzner/Oracle Cloud 免费层）
2. **test-farm-api 镜像**：封装 `core.tester.SingBoxTester` 为 HTTP API
3. **GitHub Action 改造**：只抓源 + 调自托管 API
4. **客户端切换**：`--test-farm-url https://...` 替换内置 tester

## 接口规格（已交付抽象）

`core/_test_farm_client.py` 已定义客户端接口（如下）。CI 默认仍走本地 tester，传 `--test-farm-url` 才用远程。

```python
class TestFarmClient:
    async def test_nodes(self, nodes: List[Node]) -> List[TestResult]:
        """把 nodes 发给远端 farm，返回 TestResult。"""
```

## 何时启用

- 公开节点池扩到 5000+ 时
- GitHub Actions 每月配额接近上限时
- verified 数量连续 3 周 < 50 时

## 成本估算

- 4 台 4-8 核 VPS ≈ $40-80/月
- 比单 GitHub Actions 跑 4 倍量更便宜
