"""9. Palindrome Number"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class SolutionNoStringsInvolved:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        temp = x
        while temp >= 10:
            rem = temp % 10
            digits.append(rem)
            temp = (temp - rem) // 10
        digits.append(temp)
        return x == sum(digit * 10**i for i, digit in enumerate(digits[::-1]))
