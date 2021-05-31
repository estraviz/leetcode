import pytest

from solution import Solution


data = [
    (121, True),
    (-121, False),
    (10, False),
    (-101, False),
]

@pytest.mark.parametrize(
    "x, expected", data
)
def test_is_palindrome(x, expected):
    assert Solution().isPalindrome(x) == expected
