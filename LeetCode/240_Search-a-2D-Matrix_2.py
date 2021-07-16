'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        queue = deque([[0, n-1]])
        if matrix[0][n-1] == target: return True
        visited[0][n-1] = 1
        while queue:
            mx, my = queue.popleft()
            if matrix[mx][my] == target: return True
            if matrix[mx][my] > target:
                my -= 1
            else:
                mx += 1
            mx, my = min(max(mx, 0), m-1), min(max(my, 0), n-1)
            if not visited[mx][my]:
                visited[mx][my] = 1
                queue.append([mx, my])
        return False
