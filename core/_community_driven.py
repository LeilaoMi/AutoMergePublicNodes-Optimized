"""
[v2.9] 社区驱动系统 (Community Driven System)

支持社区贡献节点、评审质量、投票排名。

核心功能:
1. 贡献管理 - 接收和验证社区提交的节点
2. 质量评审 - 社区成员对节点进行评审打分
3. 投票排名 - 基于社区投票的节点排名
4. 贡献者激励 - 追踪贡献者贡献并给予信誉奖励
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
class NodeSubmission:
    """社区节点提交"""
    submission_id: str
    submitter_id: str
    node_url: str  # 节点订阅链接或原始节点
    protocol: str
    region: str
    description: str = ""
    status: str = "pending"  # pending / approved / rejected / expired
    submitted_at: float = field(default_factory=time.time)
    reviewed_at: float = 0.0
    votes_up: int = 0
    votes_down: int = 0
    quality_score: float = 0.0  # 综合质量分


@dataclass
class CommunityMember:
    """社区成员"""
    member_id: str
    name: str
    reputation: float = 1.0  # 信誉分
    total_submissions: int = 0
    approved_submissions: int = 0
    total_reviews: int = 0
    joined_at: float = field(default_factory=time.time)


@dataclass
class CommunityReport:
    """社区报告"""
    total_members: int = 0
    total_submissions: int = 0
    approved_submissions: int = 0
    pending_submissions: int = 0
    top_contributors: List[Dict] = field(default_factory=list)
    top_rated_nodes: List[Dict] = field(default_factory=list)
    recent_activity: List[Dict] = field(default_factory=list)
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))


class CommunityDrivenSystem:
    """社区驱动系统"""

    MAX_SUBMISSIONS = 2000
    MAX_MEMBERS = 500
    MIN_REPUTATION_TO_SUBMIT = 0.5
    APPROVAL_THRESHOLD = 0.6  # 60%投票通过即批准

    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = storage_path
        self.members: Dict[str, CommunityMember] = {}
        self.submissions: List[NodeSubmission] = []
        if storage_path:
            self._load_state()

    def register_member(self, member_id: str, name: str) -> CommunityMember:
        """注册社区成员"""
        if member_id in self.members:
            return self.members[member_id]

        member = CommunityMember(member_id=member_id, name=name)
        self.members[member_id] = member
        if self.storage_path:
            self._save_state()
        return member

    def submit_node(
        self,
        submitter_id: str,
        node_url: str,
        protocol: str,
        region: str,
        description: str = "",
    ) -> Optional[NodeSubmission]:
        """提交新节点"""
        if submitter_id not in self.members:
            logger.warning(f"未注册成员: {submitter_id}")
            return None

        member = self.members[submitter_id]
        if member.reputation < self.MIN_REPUTATION_TO_SUBMIT:
            logger.warning(f"成员 {submitter_id} 信誉不足，无法提交")
            return None

        sub_id = hashlib.md5(
            f"{submitter_id}-{node_url}-{time.time()}".encode()
        ).hexdigest()[:12]

        submission = NodeSubmission(
            submission_id=sub_id,
            submitter_id=submitter_id,
            node_url=node_url,
            protocol=protocol,
            region=region,
            description=description,
        )
        self.submissions.append(submission)
        member.total_submissions += 1

        if len(self.submissions) > self.MAX_SUBMISSIONS:
            self.submissions = self.submissions[-self.MAX_SUBMISSIONS:]

        if self.storage_path:
            self._save_state()

        logger.info(f"新节点提交: {sub_id} by {submitter_id}")
        return submission

    def vote_submission(
        self,
        member_id: str,
        submission_id: str,
        vote_up: bool,
    ) -> bool:
        """对提交投票"""
        sub = self._find_submission(submission_id)
        if not sub:
            return False

        if vote_up:
            sub.votes_up += 1
        else:
            sub.votes_down += 1

        # 更新成员评审计数
        if member_id in self.members:
            self.members[member_id].total_reviews += 1

        # 检查是否达到批准/拒绝阈值
        self._check_submission_status(sub)

        if self.storage_path:
            self._save_state()
        return True

    def review_submission(
        self,
        submission_id: str,
        quality_score: float,
        status: str = "approved",
    ) -> bool:
        """评审提交(管理员或自动化)"""
        sub = self._find_submission(submission_id)
        if not sub:
            return False

        sub.quality_score = quality_score
        sub.status = status
        sub.reviewed_at = time.time()

        # 更新提交者信誉
        if sub.submitter_id in self.members:
            member = self.members[sub.submitter_id]
            if status == "approved":
                member.approved_submissions += 1
                member.reputation = min(5.0, member.reputation + 0.1)
            else:
                member.reputation = max(0.0, member.reputation - 0.05)

        if self.storage_path:
            self._save_state()
        return True

    def get_approved_nodes(self) -> List[Dict]:
        """获取所有已批准的节点"""
        approved = [
            {
                "submission_id": s.submission_id,
                "node_url": s.node_url,
                "protocol": s.protocol,
                "region": s.region,
                "quality_score": s.quality_score,
                "votes_up": s.votes_up,
                "votes_down": s.votes_down,
                "submitter": s.submitter_id,
            }
            for s in self.submissions if s.status == "approved"
        ]
        approved.sort(key=lambda x: x["quality_score"], reverse=True)
        return approved

    def generate_report(self) -> CommunityReport:
        """生成社区报告"""
        report = CommunityReport()
        report.total_members = len(self.members)
        report.total_submissions = len(self.submissions)
        report.approved_submissions = sum(
            1 for s in self.submissions if s.status == "approved"
        )
        report.pending_submissions = sum(
            1 for s in self.submissions if s.status == "pending"
        )

        # 顶级贡献者
        sorted_members = sorted(
            self.members.values(),
            key=lambda m: m.approved_submissions * m.reputation,
            reverse=True,
        )
        report.top_contributors = [
            {
                "id": m.member_id,
                "name": m.name,
                "reputation": round(m.reputation, 2),
                "approved": m.approved_submissions,
                "total": m.total_submissions,
            }
            for m in sorted_members[:10]
        ]

        # 顶级节点
        sorted_subs = sorted(
            [s for s in self.submissions if s.status == "approved"],
            key=lambda s: s.quality_score,
            reverse=True,
        )
        report.top_rated_nodes = [
            {
                "id": s.submission_id,
                "protocol": s.protocol,
                "region": s.region,
                "score": round(s.quality_score, 2),
                "votes": s.votes_up - s.votes_down,
            }
            for s in sorted_subs[:10]
        ]

        # 最近活动
        recent = sorted(
            self.submissions,
            key=lambda s: s.submitted_at,
            reverse=True,
        )[:10]
        report.recent_activity = [
            {
                "id": s.submission_id,
                "submitter": s.submitter_id,
                "status": s.status,
                "protocol": s.protocol,
                "timestamp": s.submitted_at,
            }
            for s in recent
        ]

        return report

    def _find_submission(self, submission_id: str) -> Optional[NodeSubmission]:
        """查找提交"""
        for s in self.submissions:
            if s.submission_id == submission_id:
                return s
        return None

    def _check_submission_status(self, sub: NodeSubmission):
        """检查提交状态是否应该变更"""
        total_votes = sub.votes_up + sub.votes_down
        if total_votes < 3:
            return

        approval_ratio = sub.votes_up / total_votes
        if approval_ratio >= self.APPROVAL_THRESHOLD:
            sub.status = "approved"
            sub.reviewed_at = time.time()
            sub.quality_score = approval_ratio * 100
        elif approval_ratio < (1 - self.APPROVAL_THRESHOLD) and total_votes >= 5:
            sub.status = "rejected"
            sub.reviewed_at = time.time()

    def _load_state(self):
        """加载状态"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            for mid, mdata in data.get("members", {}).items():
                self.members[mid] = CommunityMember(
                    member_id=mid,
                    name=mdata.get("name", ""),
                    reputation=mdata.get("reputation", 1.0),
                    total_submissions=mdata.get("total_submissions", 0),
                    approved_submissions=mdata.get("approved_submissions", 0),
                    total_reviews=mdata.get("total_reviews", 0),
                    joined_at=mdata.get("joined_at", time.time()),
                )
            for sdata in data.get("submissions", []):
                self.submissions.append(NodeSubmission(
                    submission_id=sdata.get("submission_id", ""),
                    submitter_id=sdata.get("submitter_id", ""),
                    node_url=sdata.get("node_url", ""),
                    protocol=sdata.get("protocol", ""),
                    region=sdata.get("region", ""),
                    description=sdata.get("description", ""),
                    status=sdata.get("status", "pending"),
                    submitted_at=sdata.get("submitted_at", time.time()),
                    reviewed_at=sdata.get("reviewed_at", 0),
                    votes_up=sdata.get("votes_up", 0),
                    votes_down=sdata.get("votes_down", 0),
                    quality_score=sdata.get("quality_score", 0),
                ))
        except Exception as e:
            logger.warning(f"加载社区状态失败: {e}")

    def _save_state(self):
        """保存状态"""
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {
                "members": {
                    mid: {
                        "name": m.name,
                        "reputation": m.reputation,
                        "total_submissions": m.total_submissions,
                        "approved_submissions": m.approved_submissions,
                        "total_reviews": m.total_reviews,
                        "joined_at": m.joined_at,
                    }
                    for mid, m in self.members.items()
                },
                "submissions": [
                    {
                        "submission_id": s.submission_id,
                        "submitter_id": s.submitter_id,
                        "node_url": s.node_url,
                        "protocol": s.protocol,
                        "region": s.region,
                        "description": s.description,
                        "status": s.status,
                        "submitted_at": s.submitted_at,
                        "reviewed_at": s.reviewed_at,
                        "votes_up": s.votes_up,
                        "votes_down": s.votes_down,
                        "quality_score": s.quality_score,
                    }
                    for s in self.submissions
                ],
            }
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning(f"保存社区状态失败: {e}")
