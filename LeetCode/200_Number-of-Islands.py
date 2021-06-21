'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
# recursive
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            for d_i, d_j in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_i, new_j = max(min(i + d_i, m-1), 0), max(min(j + d_j, n-1), 0)
                if maps[new_i][new_j] == 0 and grid[new_i][new_j] == '1':
                    maps[new_i][new_j] = 1
                    dfs(new_i, new_j)
        m, n = len(grid), len(grid[0])
        maps = [[0 for j in range(n)] for i in range(m)]
        n_islands = 0
        for i in range(m):
            for j in range(n):
                if maps[i][j] == 0 and grid[i][j] == '1':
                    maps[i][j] = 1
                    n_islands += 1
                    dfs(i, j)
        return n_islands

# stack
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        maps = [[0 for j in range(n)] for i in range(m)]
        stack = []
        n_islands = 0
        for p in range(m*n):
            i, j = p //n, p % n
            if maps[i][j] == 1 or grid[i][j] == '0': continue
            maps[i][j] = 1
            stack.append((i, j))
            n_islands += 1
            while stack:
                top_i, top_j = stack.pop()
                for d_i, d_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_i, new_j = max(min(top_i + d_i, m-1), 0), max(min(top_j + d_j, n-1), 0)
                    if maps[new_i][new_j] == 0 and grid[new_i][new_j] == '1':
                        maps[new_i][new_j] = 1
                        stack.append((new_i, new_j))
        return n_islands
