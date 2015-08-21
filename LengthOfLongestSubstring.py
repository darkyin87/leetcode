# Submission Details
# 981 / 981 test cases passed.
# Status: Accepted
# Runtime: 128 ms
# Submitted: 0 minutes ago


# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        processed = {}
        indexes = []
        maxLength = 0

        for letter in s:
            if letter in processed:
                for idx, item in enumerate(indexes):
                    if item == letter:
                        break
                    del processed[item]
                indexes[0:idx+1] = []


            processed[letter] = True
            indexes.append(letter)
            maxLength = max(len(processed), maxLength)

        #maxLength = max(maxLength, len(processed))
        return maxLength
