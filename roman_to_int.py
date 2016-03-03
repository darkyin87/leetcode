def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = roman_map[s[-1]]

        for i in range(len(s) - 1):
            curr = s[i]
            next = s[i+1]
            if roman_map[curr] < roman_map[next]:
                result = result - roman_map[curr]
            else:
                result = result + roman_map[curr]

        return result
