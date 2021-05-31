import pytest

from solution import Solution

data = [
    ("thequickbrownfoxjumpsoverthelazydog", True),
    ("leetcode", False),
]


@pytest.mark.parametrize(
    "sentence, expected", data
)
def test_if_pangram(sentence, expected):
    assert Solution().checkIfPangram(sentence) == expected
