# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


# Note: all the odd numbers are greater than the even numbers
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return nums

        for i in range(len(nums)):
            if (i % 2 == 0 and nums[i] > nums[i+1]) or (nums[i] < nums[i+1]):
                    nums[i+1], nums[i] = nums[i], nums[i+1]

        return nums
