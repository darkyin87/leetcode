# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


# Maintain a list of processed items in a dict with its index being the value
# and the item being the key, this makes the solution O(n) instead of O(n^2)


# Submission Details
# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 40 ms


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        processed = {}
        index = 1
        for num in nums:
            diff = target - num
            if diff in processed and processed[diff] < index:
                return [processed[diff], index]

            processed[num] = index
            index += 1
