import json
import sys


class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        sums = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_table.keys():
                sums.append([hash_table[diff], i])
                break
            hash_table[num] = i
        return sums[0]


def str_to_int_list(input):
    return json.loads(input)


def main():
    print(Solution().two_sum(str_to_int_list(sys.argv[1]), int(sys.argv[2])))


if __name__ == '__main__':
    main()
