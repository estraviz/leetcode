import pytest

from solution import Solution


data = [
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),
]


@pytest.mark.parametrize(
    "x, expected", data
)
def test_reverse_integer(x, expected):
    assert Solution().reverse(x) == expected
