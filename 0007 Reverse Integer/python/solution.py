"""Reverse Integer"""


class Solution:

    def reverse(self, x: int) -> int:
        temp = self.sign(x) * int(str(abs(x))[::-1])
        return 0 if not self.is_in_valid_range(temp) else temp

    def is_in_valid_range(self, x: int) -> bool:
        return -2 ** 31 <= x <= 2 ** 31 - 1

    def sign(self, x: int) -> int:
        return -1 if x < 0 else 1


