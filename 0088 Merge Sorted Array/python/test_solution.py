import pytest

from solution import Solution

data = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
]


@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected", data
)
def test_merge(nums1, m, nums2, n, expected):
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == expected
