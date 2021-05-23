import pytest

from solution import Solution


data = [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
]


@pytest.mark.parametrize(
    "nums, len_final_nums, final_nums", data
)
def test_remove_duplicates(nums, len_final_nums, final_nums):
    Solution().removeDuplicates(nums)
    assert len(nums) == len_final_nums
    assert nums == final_nums
