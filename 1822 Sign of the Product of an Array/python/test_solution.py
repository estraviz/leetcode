import pytest

from solution import Solution


data = [
    ([-1,-2,-3,-4,3,2,1], 1),
    ([1,5,0,2,-3], 0),
    ([-1,1,-1,1,-1], -1),
]


@pytest.mark.parametrize(
    "nums, expected", data
)
def test_array_sign(nums, expected):
    solution = Solution()
    assert solution.arraySign(nums) == expected
