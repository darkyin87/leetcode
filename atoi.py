class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        result = 0
        sign = 1
        maxint = 2**31 -1

        if len(str) == 0:
            return result

        if str[0] == '-' or str[0] == '+':
            if str[0] == '-':
                sign = -1
            str = str[1:]

        for chr in str:
            if chr >= '0' and chr <= '9':
                result = result*10 + int(chr)
            else:
                break

        result = result * sign
        if result >= maxint:
            return maxint
        if result <= (-1 * maxint) - 1:
            return (-1 * maxint) - 1
        return result

sol = Solution()
print 'Result: ', sol.myAtoi('123')
print 'Result: ', sol.myAtoi('-123')
print 'Result: ', sol.myAtoi('+123')
print 'Result: ', sol.myAtoi('0123')
print 'Result: ', sol.myAtoi('-0012a42')
print 'Result: ', sol.myAtoi('1')
