"""
[v2.9] 联邦式测试网络 (Federated Test Network)

支持多个节点贡献者协同测试，构建分布式节点质量评估网络。

核心功能:
1. 节点注册 - 注册测试节点和贡献者
2. 任务分发 - 将测试任务分配给各贡献者
3. 结果聚合 - 合并多方测试结果
4. 信誉系统 - 评估贡献者的可靠性
"""
from __future__ import annotations

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from collections import defaultdict
import json
import hashlib
import logging
import time
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class Contributor:
    """测试贡献者"""
    id: str  # 贡献者ID
    name: str
    region: str  # 所在地区
    capabilities: List[str] = field(default_factory=list)  # 支持的测试能力
    reliability_score: float = 1.0  # 信誉分 (0-1)
    total_tests: int = 0
    successful_tests: int = 0
    last_active: float = 0.0
    registered_at: float = field(default_factory=time.time)


@dataclass
class TestTask:
    """测试任务"""
    task_id: str
    node_fingerprints: List[str]
    assigned_to: str  # contributor id
    status: str = "pending"  # pending / assigned / completed / failed
    created_at: float = field(default_factory=time.time)
    completed_at: float = 0.0
    results: Dict = field(default_factory=dict)


@dataclass
class FederatedReport:
    """联邦测试报告"""
    total_contributors: int = 0
    active_contributors: int = 0
    total_tasks: int = 0
    completed_tasks: int = 0
    coverage_ratio: float = 0.0  # 测试覆盖率
    region_coverage: Dict[str, int] = field(default_factory=dict)
    contributor_rankings: List[Dict] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class FederatedTestNetwork:
    """联邦式测试网络"""

    MAX_CONTRIBUTORS = 100
    MAX_TASKS = 1000
    RELIABILITY_DECAY = 0.95  # 长时间不活跃信誉衰减
    ACTIVE_THRESHOLD = 3600 * 24 * 7  # 7天内活跃算活跃

    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = storage_path
        self.contributors: Dict[str, Contributor] = {}
        self.tasks: List[TestTask] = []
        self.results: Dict[str, List[Dict]] = defaultdict(list)  # fp -> [test_results]
        if storage_path:
            self._load_state()

    def register_contributor(
        self,
        contributor_id: str,
        name: str,
        region: str,
        capabilities: Optional[List[str]] = None,
    ) -> Contributor:
        """注册测试贡献者"""
        if contributor_id in self.contributors:
            contributor = self.contributors[contributor_id]
            contributor.last_active = time.time()
            if capabilities:
                contributor.capabilities = capabilities
            logger.info(f"更新贡献者: {name} ({region})")
        else:
            contributor = Contributor(
                id=contributor_id,
                name=name,
                region=region,
                capabilities=capabilities or ["basic"],
                last_active=time.time(),
            )
            self.contributors[contributor_id] = contributor
            logger.info(f"注册新贡献者: {name} ({region})")

        if self.storage_path:
            self._save_state()
        return contributor

    def create_test_tasks(
        self,
        node_fingerprints: List[str],
        batch_size: int = 50,
    ) -> List[TestTask]:
        """创建测试任务并分配给贡献者"""
        active = self._get_active_contributors()
        if not active:
            logger.warning("无活跃贡献者，无法创建测试任务")
            return []

        tasks = []
        # 分批
        for i in range(0, len(node_fingerprints), batch_size):
            batch = node_fingerprints[i:i + batch_size]
            task_id = hashlib.md5(
                f"{time.time()}-{i}".encode()
            ).hexdigest()[:12]

            # 轮询分配
            contributor = active[len(tasks) % len(active)]
            task = TestTask(
                task_id=task_id,
                node_fingerprints=batch,
                assigned_to=contributor.id,
                status="assigned",
            )
            tasks.append(task)
            self.tasks.append(task)

        # 限制任务数
        if len(self.tasks) > self.MAX_TASKS:
            self.tasks = self.tasks[-self.MAX_TASKS:]

        if self.storage_path:
            self._save_state()

        logger.info(f"创建 {len(tasks)} 个测试任务，分配给 {len(active)} 个贡献者")
        return tasks

    def submit_results(
        self,
        contributor_id: str,
        task_id: str,
        results: Dict[str, Dict],
    ) -> bool:
        """提交测试结果"""
        task = None
        for t in self.tasks:
            if t.task_id == task_id:
                task = t
                break

        if not task:
            logger.warning(f"未找到任务: {task_id}")
            return False

        if task.assigned_to != contributor_id:
            logger.warning(f"任务 {task_id} 未分配给 {contributor_id}")
            return False

        # 更新任务状态
        task.status = "completed"
        task.completed_at = time.time()
        task.results = results

        # 聚合结果
        for fp, result_data in results.items():
            self.results[fp].append({
                "contributor_id": contributor_id,
                "task_id": task_id,
                "result": result_data,
                "timestamp": time.time(),
            })
            # 限制每个节点的结果数
            if len(self.results[fp]) > 20:
                self.results[fp] = self.results[fp][-20:]

        # 更新贡献者信誉
        if contributor_id in self.contributors:
            c = self.contributors[contributor_id]
            c.total_tests += len(results)
            c.successful_tests += sum(
                1 for r in results.values() if r.get("success", False)
            )
            c.last_active = time.time()

        if self.storage_path:
            self._save_state()

        return True

    def get_aggregated_results(self, fp: str) -> Dict:
        """获取某节点的聚合测试结果"""
        entries = self.results.get(fp, [])
        if not entries:
            return {}

        # 聚合统计
        latencies = []
        successes = 0
        for e in entries:
            r = e.get("result", {})
            if r.get("success", False):
                successes += 1
            lat = r.get("latency_ms", 0)
            if lat > 0:
                latencies.append(lat)

        return {
            "total_tests": len(entries),
            "success_rate": successes / len(entries) if entries else 0,
            "avg_latency_ms": sum(latencies) / len(latencies) if latencies else 0,
            "min_latency_ms": min(latencies) if latencies else 0,
            "max_latency_ms": max(latencies) if latencies else 0,
            "contributors": list(set(e["contributor_id"] for e in entries)),
        }

    def generate_report(self) -> FederatedReport:
        """生成联邦测试报告"""
        report = FederatedReport()
        report.total_contributors = len(self.contributors)

        now = time.time()
        report.active_contributors = sum(
            1 for c in self.contributors.values()
            if now - c.last_active < self.ACTIVE_THRESHOLD
        )

        report.total_tasks = len(self.tasks)
        report.completed_tasks = sum(1 for t in self.tasks if t.status == "completed")

        # 地区覆盖
        region_count = defaultdict(int)
        for c in self.contributors.values():
            region_count[c.region] += 1
        report.region_coverage = dict(region_count)

        # 测试覆盖率
        total_nodes = len(set(fp for t in self.tasks for fp in t.node_fingerprints))
        tested_nodes = len(set(
            fp for t in self.tasks if t.status == "completed" for fp in t.node_fingerprints
        ))
        report.coverage_ratio = tested_nodes / total_nodes if total_nodes > 0 else 0

        # 贡献者排名
        rankings = sorted(
            self.contributors.values(),
            key=lambda c: c.reliability_score * c.successful_tests,
            reverse=True,
        )
        report.contributor_rankings = [
            {
                "id": c.id,
                "name": c.name,
                "region": c.region,
                "reliability": round(c.reliability_score, 2),
                "tests": c.total_tests,
                "success_rate": round(
                    c.successful_tests / c.total_tests, 2
                ) if c.total_tests > 0 else 0,
            }
            for c in rankings[:10]
        ]

        return report

    def _get_active_contributors(self) -> List[Contributor]:
        """获取活跃贡献者"""
        now = time.time()
        return [
            c for c in self.contributors.values()
            if now - c.last_active < self.ACTIVE_THRESHOLD
        ]

    def _load_state(self):
        """从文件加载状态"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            # 恢复贡献者
            for cid, cdata in data.get("contributors", {}).items():
                self.contributors[cid] = Contributor(
                    id=cid,
                    name=cdata.get("name", ""),
                    region=cdata.get("region", ""),
                    capabilities=cdata.get("capabilities", []),
                    reliability_score=cdata.get("reliability_score", 1.0),
                    total_tests=cdata.get("total_tests", 0),
                    successful_tests=cdata.get("successful_tests", 0),
                    last_active=cdata.get("last_active", 0),
                    registered_at=cdata.get("registered_at", time.time()),
                )
            # 恢复结果
            for fp, entries in data.get("results", {}).items():
                self.results[fp] = entries[-20:]
        except Exception as e:
            logger.warning(f"加载联邦网络状态失败: {e}")

    def _save_state(self):
        """保存状态到文件"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {
                "contributors": {
                    cid: {
                        "name": c.name,
                        "region": c.region,
                        "capabilities": c.capabilities,
                        "reliability_score": c.reliability_score,
                        "total_tests": c.total_tests,
                        "successful_tests": c.successful_tests,
                        "last_active": c.last_active,
                        "registered_at": c.registered_at,
                    }
                    for cid, c in self.contributors.items()
                },
                "results": {
                    fp: entries[-20:]
                    for fp, entries in self.results.items()
                },
            }
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning(f"保存联邦网络状态失败: {e}")
