"""[P2-1] 自托管真测集群客户端接口（未启用，参见 docs/test-farm-setup.md）。

仅作为接口抽象，不实际调用任何远程服务。生产启用时把
HTTP client 替换为真实实现即可，不影响 main.py 调用方。
"""
from __future__ import annotations

from typing import Any, Dict, List

from core.parser import Node
from core.tester import TestResult


class TestFarmClient:
    """自托管真测集群 HTTP 客户端接口。

    生产使用：
        client = TestFarmClient(base_url="https://test-farm.internal:8000", api_key="...")
        results = await client.test_nodes(nodes)

    当前状态：接口定义，main.py 不调用。传 --test-farm-url 才走远程。
    """

    def __init__(self, base_url: str, api_key: str = "", timeout: float = 600.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    async def test_nodes(self, nodes: List[Node]) -> List[TestResult]:
        """远程测试节点。

        实际实现：POST {base_url}/test, body={nodes: [...]}
        返回 TestResult list。
        """
        raise NotImplementedError(
            "[P2-1] TestFarmClient 接口已定义但未实施；"
            "请参考 docs/test-farm-setup.md 部署 K8s 集群后启用。"
        )

    async def health_check(self) -> Dict[str, Any]:
        """检查 farm 集群健康状态。"""
        raise NotImplementedError(
            "[P2-1] TestFarmClient 接口已定义但未实施。"
        )
