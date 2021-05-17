import pytest

from solution import Solution


data = [
    ([1, 2, 3, 2], 4),
    ([1, 1, 1, 1, 1], 0),
    ([1, 2, 3, 4, 5], 15),
]


@pytest.mark.parametrize(
    "nums, expected", data
)
def test_sum_of_unique_numbers(nums, expected):
    assert Solution().sum_of_unique(nums) == expected
