# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.append(0)
        n = len(nums)

        # filter out any un necessary values
        for i in range(n):
          if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0

        # make sure we set a value that is greater than the length for those
        # who values are greater than 0
        for i in range(n):
          nums[nums[i] % n] += n

        for i in range(1, n):
          if nums[i] / n == 0:
            return i

        return n

s = Solution()
print s.firstMissingPositive([0, 3])
