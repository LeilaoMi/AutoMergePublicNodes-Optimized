"""
[v2.8] 开放 API 平台 (Open API Platform)

提供标准化的 API 接口，支持外部系统查询节点数据、提交反馈、获取推荐。

核心功能:
1. API 端点定义 - 标准化的 RESTful API 端点
2. 认证管理 - API Key 管理和权限控制
3. 速率限制 - 防止滥用
4. 响应格式 - 统一的 JSON 响应格式
5. API 文档生成 - 自动生成 API 文档
"""
from __future__ import annotations

from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, field
from collections import defaultdict
import json
import hashlib
import logging
import time
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class APIKey:
    """API Key"""
    key: str
    name: str
    permissions: List[str] = field(default_factory=list)  # read / write / admin
    created_at: float = field(default_factory=time.time)
    last_used: float = 0.0
    rate_limit: int = 100  # 每分钟请求上限
    request_count: int = 0
    is_active: bool = True


@dataclass
class APIRequest:
    """API 请求"""
    method: str
    endpoint: str
    params: Dict = field(default_factory=dict)
    body: Dict = field(default_factory=dict)
    api_key: str = ""
    timestamp: float = field(default_factory=time.time)
    client_ip: str = ""


@dataclass
class APIResponse:
    """API 响应"""
    status_code: int = 200
    data: Any = None
    message: str = "success"
    error: str = ""
    timestamp: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))
    request_id: str = ""

    def to_dict(self) -> Dict:
        return {
            "status_code": self.status_code,
            "data": self.data,
            "message": self.message,
            "error": self.error,
            "timestamp": self.timestamp,
            "request_id": self.request_id,
        }


@dataclass
class APIEndpoint:
    """API 端点定义"""
    method: str  # GET / POST / PUT / DELETE
    path: str
    description: str
    parameters: List[Dict] = field(default_factory=list)
    response_example: Dict = field(default_factory=dict)
    permission: str = "read"  # read / write / admin
    rate_limit: int = 100


class OpenAPIPlatform:
    """开放 API 平台"""

    # 预定义的 API 端点
    ENDPOINTS = [
        APIEndpoint(
            method="GET",
            path="/api/v1/nodes",
            description="获取节点列表（支持过滤和排序）",
            parameters=[
                {"name": "protocol", "type": "string", "required": False, "description": "协议类型过滤"},
                {"name": "region", "type": "string", "required": False, "description": "地区过滤"},
                {"name": "min_score", "type": "number", "required": False, "description": "最低评分"},
                {"name": "limit", "type": "integer", "required": False, "description": "返回数量上限", "default": 50},
                {"name": "sort_by", "type": "string", "required": False, "description": "排序字段: score/latency/speed", "default": "score"},
            ],
            response_example={"nodes": [{"tag": "...", "server": "...", "score": 85.2}]},
            permission="read",
        ),
        APIEndpoint(
            method="GET",
            path="/api/v1/nodes/{fingerprint}",
            description="获取单个节点详情",
            parameters=[
                {"name": "fingerprint", "type": "string", "required": True, "description": "节点指纹"},
            ],
            response_example={"node": {"tag": "...", "score": 85.2, "stats": {}}},
            permission="read",
        ),
        APIEndpoint(
            method="GET",
            path="/api/v1/stats",
            description="获取系统运行统计",
            parameters=[],
            response_example={"total_nodes": 100, "pass_rate": 0.85},
            permission="read",
        ),
        APIEndpoint(
            method="GET",
            path="/api/v1/recommend",
            description="获取个性化推荐节点",
            parameters=[
                {"name": "use_case", "type": "string", "required": False, "description": "使用场景: streaming/gaming/download/work"},
                {"name": "user_id", "type": "string", "required": False, "description": "用户ID（用于个性化推荐）"},
                {"name": "limit", "type": "integer", "required": False, "description": "返回数量", "default": 10},
            ],
            response_example={"recommendations": [{"node": {}, "reason": "..."}]},
            permission="read",
        ),
        APIEndpoint(
            method="GET",
            path="/api/v1/quality-map",
            description="获取节点质量地图数据",
            parameters=[
                {"name": "group_by", "type": "string", "required": False, "description": "分组维度: region/protocol", "default": "region"},
            ],
            response_example={"regions": [{"region": "US", "avg_score": 80}]},
            permission="read",
        ),
        APIEndpoint(
            method="POST",
            path="/api/v1/feedback",
            description="提交节点使用反馈",
            parameters=[
                {"name": "node_fingerprint", "type": "string", "required": True, "description": "节点指纹"},
                {"name": "rating", "type": "integer", "required": True, "description": "评分 1-5"},
                {"name": "comment", "type": "string", "required": False, "description": "评论"},
            ],
            response_example={"status": "received"},
            permission="write",
        ),
        APIEndpoint(
            method="POST",
            path="/api/v1/nodes/submit",
            description="提交新节点到社区",
            parameters=[
                {"name": "node_url", "type": "string", "required": True, "description": "节点链接"},
                {"name": "protocol", "type": "string", "required": True, "description": "协议类型"},
                {"name": "region", "type": "string", "required": True, "description": "地区"},
            ],
            response_example={"submission_id": "abc123", "status": "pending"},
            permission="write",
        ),
        APIEndpoint(
            method="GET",
            path="/api/v1/health",
            description="健康检查",
            parameters=[],
            response_example={"status": "ok", "version": "2.8.0"},
            permission="read",
            rate_limit=600,
        ),
    ]

    def __init__(self, storage_path: Optional[str] = None):
        self.storage_path = storage_path
        self.api_keys: Dict[str, APIKey] = {}
        self.request_log: List[Dict] = []
        self.rate_limits: Dict[str, List[float]] = defaultdict(list)  # key -> [timestamps]
        self.feedback: List[Dict] = []
        if storage_path:
            self._load_state()

    def create_api_key(
        self,
        name: str,
        permissions: Optional[List[str]] = None,
        rate_limit: int = 100,
    ) -> APIKey:
        """创建 API Key"""
        raw_key = hashlib.sha256(
            f"{name}-{time.time()}-{id(self)}".encode()
        ).hexdigest()[:32]

        key = APIKey(
            key=raw_key,
            name=name,
            permissions=permissions or ["read"],
            rate_limit=rate_limit,
        )
        self.api_keys[raw_key] = key

        if self.storage_path:
            self._save_state()

        logger.info(f"创建 API Key: {name} ({raw_key[:8]}...)")
        return key

    def validate_request(self, request: APIRequest) -> Optional[APIResponse]:
        """验证 API 请求（认证 + 速率限制）"""
        # 健康检查不需要认证
        if request.endpoint == "/api/v1/health":
            return None

        # 检查 API Key
        if not request.api_key:
            return APIResponse(
                status_code=401,
                message="unauthorized",
                error="缺少 API Key",
            )

        key_obj = self.api_keys.get(request.api_key)
        if not key_obj:
            return APIResponse(
                status_code=401,
                message="unauthorized",
                error="无效的 API Key",
            )

        if not key_obj.is_active:
            return APIResponse(
                status_code=403,
                message="forbidden",
                error="API Key 已被禁用",
            )

        # 检查权限
        endpoint = self._find_endpoint(request.method, request.endpoint)
        if endpoint:
            if endpoint.permission not in key_obj.permissions and "admin" not in key_obj.permissions:
                return APIResponse(
                    status_code=403,
                    message="forbidden",
                    error=f"需要 {endpoint.permission} 权限",
                )

        # 速率限制
        now = time.time()
        window_key = request.api_key
        # 清理过期的请求记录 (1分钟窗口)
        self.rate_limits[window_key] = [
            t for t in self.rate_limits[window_key] if now - t < 60
        ]
        limit = endpoint.rate_limit if endpoint else key_obj.rate_limit
        if len(self.rate_limits[window_key]) >= limit:
            return APIResponse(
                status_code=429,
                message="rate_limited",
                error=f"请求频率超限 ({limit}/min)",
            )

        self.rate_limits[window_key].append(now)
        key_obj.last_used = now
        key_obj.request_count += 1

        return None  # 验证通过

    def handle_request(self, request: APIRequest) -> APIResponse:
        """处理 API 请求"""
        # 验证
        error = self.validate_request(request)
        if error:
            return error

        # 路由
        endpoint_path = request.endpoint
        method = request.method.upper()

        try:
            if endpoint_path == "/api/v1/health":
                return self._handle_health()
            elif endpoint_path == "/api/v1/stats":
                return self._handle_stats(request)
            elif endpoint_path.startswith("/api/v1/nodes/") and method == "GET":
                fp = endpoint_path.split("/")[-1]
                return self._handle_node_detail(fp)
            elif endpoint_path == "/api/v1/nodes" and method == "GET":
                return self._handle_nodes_list(request)
            elif endpoint_path == "/api/v1/recommend":
                return self._handle_recommend(request)
            elif endpoint_path == "/api/v1/quality-map":
                return self._handle_quality_map(request)
            elif endpoint_path == "/api/v1/feedback" and method == "POST":
                return self._handle_feedback(request)
            elif endpoint_path == "/api/v1/nodes/submit" and method == "POST":
                return self._handle_submit_node(request)
            else:
                return APIResponse(
                    status_code=404,
                    message="not_found",
                    error=f"未找到端点: {method} {endpoint_path}",
                )
        except Exception as e:
            logger.error(f"API 请求处理失败: {e}")
            return APIResponse(
                status_code=500,
                message="internal_error",
                error=str(e),
            )

    def _handle_health(self) -> APIResponse:
        return APIResponse(
            data={"status": "ok", "version": "2.8.0", "uptime": "running"},
        )

    def _handle_stats(self, request: APIRequest) -> APIResponse:
        """返回占位统计 — 实际由 main.py 注入真实数据"""
        return APIResponse(
            data={"message": "stats endpoint ready, data injected by pipeline"},
        )

    def _handle_node_detail(self, fingerprint: str) -> APIResponse:
        return APIResponse(
            data={"fingerprint": fingerprint, "message": "detail lookup ready"},
        )

    def _handle_nodes_list(self, request: APIRequest) -> APIResponse:
        return APIResponse(
            data={"nodes": [], "total": 0, "filters": request.params},
        )

    def _handle_recommend(self, request: APIRequest) -> APIResponse:
        return APIResponse(
            data={"recommendations": [], "use_case": request.params.get("use_case", "work")},
        )

    def _handle_quality_map(self, request: APIRequest) -> APIResponse:
        return APIResponse(
            data={"group_by": request.params.get("group_by", "region"), "data": {}},
        )

    def _handle_feedback(self, request: APIRequest) -> APIResponse:
        fb = {
            "node_fingerprint": request.body.get("node_fingerprint", ""),
            "rating": request.body.get("rating", 0),
            "comment": request.body.get("comment", ""),
            "timestamp": time.time(),
            "api_key": request.api_key[:8] + "...",
        }
        self.feedback.append(fb)
        if len(self.feedback) > 5000:
            self.feedback = self.feedback[-5000:]
        if self.storage_path:
            self._save_state()
        return APIResponse(data={"status": "received", "feedback_id": len(self.feedback)})

    def _handle_submit_node(self, request: APIRequest) -> APIResponse:
        sub_id = hashlib.md5(
            f"{request.body.get('node_url', '')}-{time.time()}".encode()
        ).hexdigest()[:12]
        return APIResponse(
            data={"submission_id": sub_id, "status": "pending"},
        )

    def _find_endpoint(self, method: str, path: str) -> Optional[APIEndpoint]:
        for ep in self.ENDPOINTS:
            if ep.method == method.upper() and ep.path == path:
                return ep
            # 处理路径参数 (如 /api/v1/nodes/{fingerprint})
            if ep.method == method.upper() and "{" in ep.path:
                base = ep.path.split("{")[0].rstrip("/")
                if path.startswith(base) and path != base:
                    return ep
        return None

    def generate_api_docs(self) -> Dict:
        """生成 API 文档"""
        docs = {
            "title": "AutoNodes Open API",
            "version": "2.8.0",
            "base_url": "https://api.autonodes.example.com",
            "authentication": {
                "type": "api_key",
                "header": "X-API-Key",
                "description": "在请求头中添加 X-API-Key 进行认证",
            },
            "endpoints": [],
        }

        for ep in self.ENDPOINTS:
            docs["endpoints"].append({
                "method": ep.method,
                "path": ep.path,
                "description": ep.description,
                "parameters": [
                    {
                        "name": p["name"],
                        "type": p["type"],
                        "required": p.get("required", False),
                        "description": p.get("description", ""),
                        "default": p.get("default"),
                    }
                    for p in ep.parameters
                ],
                "response_example": ep.response_example,
                "permission": ep.permission,
                "rate_limit": f"{ep.rate_limit}/min",
            })

        return docs

    def save_api_docs(self, output_dir: str):
        """保存 API 文档到文件"""
        docs = self.generate_api_docs()
        path = Path(output_dir) / "api_docs.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
        logger.info(f"API 文档已保存: {path}")

    def get_api_summary(self) -> Dict:
        """获取 API 平台摘要"""
        active_keys = sum(1 for k in self.api_keys.values() if k.is_active)
        total_requests = sum(k.request_count for k in self.api_keys.values())
        return {
            "total_endpoints": len(self.ENDPOINTS),
            "active_api_keys": active_keys,
            "total_requests": total_requests,
            "total_feedback": len(self.feedback),
        }

    def _load_state(self):
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            for key_str, kdata in data.get("api_keys", {}).items():
                self.api_keys[key_str] = APIKey(
                    key=key_str,
                    name=kdata.get("name", ""),
                    permissions=kdata.get("permissions", ["read"]),
                    created_at=kdata.get("created_at", time.time()),
                    last_used=kdata.get("last_used", 0),
                    rate_limit=kdata.get("rate_limit", 100),
                    request_count=kdata.get("request_count", 0),
                    is_active=kdata.get("is_active", True),
                )
            self.feedback = data.get("feedback", [])[-5000:]
        except Exception as e:
            logger.warning(f"加载 API 平台状态失败: {e}")

    def _save_state(self):
        if not self.storage_path:
            return
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {
                "api_keys": {
                    k: {
                        "name": v.name,
                        "permissions": v.permissions,
                        "created_at": v.created_at,
                        "last_used": v.last_used,
                        "rate_limit": v.rate_limit,
                        "request_count": v.request_count,
                        "is_active": v.is_active,
                    }
                    for k, v in self.api_keys.items()
                },
                "feedback": self.feedback[-5000:],
            }
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            logger.warning(f"保存 API 平台状态失败: {e}")
