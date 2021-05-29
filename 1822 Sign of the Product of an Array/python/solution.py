"""1822. Sign of the Product of an Array"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = sum(1 for x in nums if x < 0)
        zeroes = any(True for x in nums if x == 0)
        return 0 if zeroes else -1 if negatives % 2 == 1 else 1
