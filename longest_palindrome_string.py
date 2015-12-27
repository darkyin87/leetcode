class Solution(object):
    def expandAroundCenter(self, input, l, r):
        length = len(input)
        while l >= 0 and r < length and input[l] == input[r]:
            l = l-1
            r = r+1
        # print 'range: ', l+1, r-1-l
        return input[l+1:r]
    
    def longestPalindrome(self, input):
        length = len(input)
        if length == 0:
            return ''
        longest = input[0:1]
        for i in range(0, length):
            p1 = self.expandAroundCenter(input, i, i)
            if (len(p1) > len(longest)):
                longest = p1
            # print 'p1: ', p1, i
            p2 = self.expandAroundCenter(input, i, i+1)
            if (len(p2) > len(longest)):
                longest = p2
            # print 'p2: ', p2, i
        return longest
