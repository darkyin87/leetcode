# 981 / 981 test cases passed.
# Status: Accepted
# Runtime: 112 ms
# Submitted: 0 minutes ago


# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

# Explanation: Maintain a dictionary of processed characters and enumerate on Input
# - if item in processed list calculate maxLen which is max between already stored max
# value and the length (currentIndex - startIndex)
# - reset the startIndex as the max between currentIndex + 1 (the next item) and startIndex
# - add the item to processed list
# - After enumeration do not forget the last step to compare the maxLen for the end of string


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        processed = {}
        maxLen = startIndex = 0;

        for idx, item in enumerate(s):
            if item in processed:
                maxLen = max(maxLen, idx - startIndex);
                startIndex = max(startIndex, processed[item] + 1);
            processed[item] = idx
        return max(maxLen, len(s) - startIndex);
