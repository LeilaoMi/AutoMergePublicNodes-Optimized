"""
高并发端口池与信号量门控
替代原有基于多进程的 ProcessPoolGate，专为 asyncio 和 sing-box 探针设计。
确保在 100+ 并发探活时，端口不冲突、内存不溢出。
"""
from __future__ import annotations
import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator

class PortPool:
    def __init__(self, start_port: int, pool_size: int):
        self._available: asyncio.Queue[int] = asyncio.Queue()
        for p in range(start_port, start_port + pool_size):
            self._available.put_nowait(p)

    @asynccontextmanager
    async def acquire(self) -> AsyncIterator[int]:
        port = await self._available.get()
        try:
            yield port
        finally:
            await self._available.put(port)

class ConcurrencyGate:
    def __init__(self, max_concurrency: int, start_port: int = 10000):
        self._semaphore = asyncio.Semaphore(max_concurrency)
        self._port_pool = PortPool(start_port, max_concurrency)

    @asynccontextmanager
    async def acquire(self) -> AsyncIterator[int]:
        async with self._semaphore:
            async with self._port_pool.acquire() as port:
                yield port
