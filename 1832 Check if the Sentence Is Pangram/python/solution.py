"""1832. Check if the Sentence Is Pangram"""

from collections import Counter
from string import ascii_lowercase as chars


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return True if len(Counter(sentence.lower())) == len(chars) else False
