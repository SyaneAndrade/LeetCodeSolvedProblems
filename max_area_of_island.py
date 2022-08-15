"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1

"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        size_row = len(grid)
        size_col = len(grid[0])
        area = 0
        max_area = 0
        for i in range(0, size_row):
            for j in range(0, size_col):
                if(grid[i][j]):
                    area = self.calculateArea(grid, i ,j)
                    max_area = max(area, max_area)
        return max_area
        
    def calculateArea(self, grid, i, j):
        size_row = len(grid)
        size_col = len(grid[0])
        if ((i< 0) or (j < 0) or 
            (i >= size_row) or 
            (j >= size_col) or 
            (grid[i][j] == 0)):
            return 0
        if grid[i][j]:
            grid[i][j] = 0
            return (1 + 
                    self.calculateArea(grid, i, j-1) + 
                    self.calculateArea(grid, i, j + 1) + 
                    self.calculateArea(grid, i - 1, j) + 
                    self.calculateArea(grid, i + 1, j))

sol = Solution()
# grid = [[0,0,0,0,0,0,0,0]]
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(sol.maxAreaOfIsland(grid))