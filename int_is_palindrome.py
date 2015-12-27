class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            # Negative number cannot be palindrome
            return False

        elif x > 0 and x % 10 == 0:
            return False

        reverse = 0
        while x >= reverse:
            reverse = (reverse * 10) + (x % 10)
            # print x, reverse
            if x == reverse:
                return True
            x = int (x / 10)
            if x == reverse:
                return True
        return input == reverse


sol = Solution()
print 'Result: ', sol.isPalindrome(10)
print 'Result: ', sol.isPalindrome(-1)
print 'Result: ', sol.isPalindrome(-123)
print 'Result: ', sol.isPalindrome(12321)
print 'Result: ', sol.isPalindrome(01234)
print 'Result: ', sol.isPalindrome(1221)
print 'Result: ', sol.isPalindrome(1)
print 'Result: ', sol.isPalindrome(0)
