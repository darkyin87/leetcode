class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        life = [[1 for x in range(n)] for y in range(m)]

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                min_life = 1
                if row < m - 1:
                    min_life = min(life[row + 1][col], life[row][col+1]) if col < n - 1 else life[row+1][col]
                elif col < n - 1:
                    min_life = life[row][col + 1]
                life[row][col] = max(min_life - dungeon[row][col], 1)
        return life[0][0]

# dungeon = [[100]]
# sol = Solution()
# print sol.calculateMinimumHP(dungeon)

# dungeon = [[-100]]
# sol = Solution()
# print sol.calculateMinimumHP(dungeon)

# dungeon = [[0]]
# sol = Solution()
# print sol.calculateMinimumHP(dungeon)


# dungeon = [[0 , 0]]
# sol = Solution()
# print sol.calculateMinimumHP(dungeon)

# dungeon = [[0 , -3]]
# sol = Solution()
# print sol.calculateMinimumHP(dungeon)

# dungeon = [[0,5],[-2,-3]]
# sol = Solution()
# print sol.calculateMinimumHP(dungeon)


# dungeon = [[1,-2,3],[2,-2,-2]]
# sol = Solution()
# print sol.calculateMinimumHP(dungeon)
