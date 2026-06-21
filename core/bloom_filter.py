"""
轻量级布隆过滤器 (Bloom Filter)
用于在内存受限环境（如 GitHub Actions）下，对海量节点进行快速指纹去重。
相比全量 set()，可将内存占用降低 90% 以上。
"""
from __future__ import annotations
import hashlib
import math
from typing import Iterable

class BloomFilter:
    def __init__(self, expected_count: int = 100000, error_rate: float = 0.01):
        self.size = self._optimal_size(expected_count, error_rate)
        self.hash_count = self._optimal_hash_count(self.size, expected_count)
        self.bit_array = bytearray(math.ceil(self.size / 8))
        self._count = 0

    @staticmethod
    def _optimal_size(n: int, p: float) -> int:
        return int(-n * math.log(p) / (math.log(2) ** 2))

    @staticmethod
    def _optimal_hash_count(m: int, n: int) -> int:
        return max(1, int((m / n) * math.log(2)))

    def _get_bits(self, item: str) -> Iterable[int]:
        for i in range(self.hash_count):
            digest = hashlib.md5(f"{item}_{i}".encode("utf-8")).digest()
            yield int.from_bytes(digest[:4], "big") % self.size

    def add(self, item: str) -> bool:
        bits = list(self._get_bits(item))
        if all(self.bit_array[bit // 8] & (1 << (bit % 8)) for bit in bits):
            return False
        for bit in bits:
            self.bit_array[bit // 8] |= (1 << (bit % 8))
        self._count += 1
        return True

    def __contains__(self, item: str) -> bool:
        return all(self.bit_array[bit // 8] & (1 << (bit % 8)) for bit in self._get_bits(item))

    def __len__(self) -> int:
        return self._count
