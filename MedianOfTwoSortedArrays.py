class Solution(object):

    def findKthElement(self, a, b, k):
        # print "a: ", a, "b: ", b, "k: ", k

        if len(a) > len(b):
            return self.findKthElement(b, a, k)
        if len(a) == 0:
            return b[k - 1]
        if k == 1:
            return min(a[0], b[0])

        aPos = min (len(a), k/2)
        bPos = k - aPos
        # print "aPos: ", aPos, "bPos: ", bPos
        if a[aPos - 1] <= b[bPos - 1]:
            return self.findKthElement(a[aPos::], b, k-aPos)
        else:
            return self.findKthElement(a, b[bPos::], k-bPos)


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        totalLength = len(nums1) + len(nums2)
        # if length is even, median is average of middle two elements
        # average of k and k+1 here
        k = totalLength / 2
        if totalLength % 2 == 0:
            median1 = self.findKthElement(nums1, nums2, k)
            k2 = totalLength/2 + 1
            median2 = self.findKthElement(nums1, nums2, k + 1)
            # print "median1: ", median1, " median2: ", median2
            return (median1 + median2) / 2.0
        # if length is odd, median is the middle element, (k+1)th element here
        else:
            return self.findKthElement(nums1, nums2, k+1)

sol = Solution()

# nums1 = [2,3,4,5,6]
# nums2 = [1]
# print sol.findMedianSortedArrays(nums1, nums2)
# #Ans: 3.5

nums1 = [1, 2, 4, 8, 9, 10, ]
nums2 = [3, 5, 6, 7, 8, ]
#Ans: [1,2,3,4,5,6,7,8,8,9,10] 6

print sol.findMedianSortedArrays(nums1, nums2)

nums1 = [1]
nums2 = [1]
print sol.findMedianSortedArrays(nums1, nums2)

nums1 = [2, 3]
nums2 = []
print sol.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 2]
nums2 = [1, 2]
print sol.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 1, 1]
nums2 = [1, 1, 1]
print sol.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 1, 3, 3]
nums2 = [1, 1, 3, 3]
print sol.findMedianSortedArrays(nums1, nums2)
