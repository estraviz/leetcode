"""Sum of Unique Elements"""

from collections import Counter
from typing import List


class Solution:

    def sum_of_unique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(k for k, v in counter.items() if v == 1)
