from two_sum import Solution


def test_two_sum():
    assert Solution().two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().two_sum([1, 3, 5, 7], 8) == [1, 2]
    assert Solution().two_sum([2, 7, 11, 13, 11], 22) == [2, 4]
    assert Solution().two_sum([3, 2, 3], 6) == [0, 2]
