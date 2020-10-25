import pytest
from two_sum import Solution


@pytest.mark.parametrize(
    'nums, target',
    [
        ([2, 7, 11, 15], 9)
    ]
)
def test_solution(nums, target):
    #assert Solution().two_sum([2, 7, 11, 15], 9)
    assert Solution().two_sum(nums, target)

