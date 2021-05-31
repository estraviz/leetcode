import pytest

from solution import Solution, SolutionNoStringsInvolved


data = [
    (121, True),
    (-121, False),
    (10, False),
    (-101, False),
]

@pytest.mark.parametrize(
    "x, expected", data
)
def test_is_palindrome_solution_using_string_conversion(x, expected):
    assert Solution().isPalindrome(x) == expected


@pytest.mark.parametrize(
    "x, expected", data
)
def test_is_palindrome_solution_without_using_string_conversion(x, expected):
    assert SolutionNoStringsInvolved().isPalindrome(x) == expected
