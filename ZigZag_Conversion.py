class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
    
        gap = (numRows -1 ) * 2
        result = ""
    
        for row in range(0, numRows):
            offset = gap - (row * 2)
            currPos = row
            while currPos < len(s):
                if offset != 0:
                    result += s[currPos]
                    currPos = currPos + offset
                offset = gap - offset
        return result
