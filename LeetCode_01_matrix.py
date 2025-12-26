'''
In this problem we need to find the distance of nearest 0 to 1.
Here I am running DFS for every cell which has value as 1 to find nearest 0, and updating the resultant matrix with distance values.
Using these neighboring result values, we compute the next neighboring values distance.
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None or len(mat) == 0: return mat
        self.m = len(mat)
        self.n = len(mat[0])
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.result = [[0]* self.n for _ in range(self.m)]
        # looping through each cell
        for i in range(self.m):
            for j in range(self.n):
                if mat[i][j] == 1:
                    self.result[i][j] = self.dfs(mat, i, j)
        
        return self.result
        
    def dfs(self, mat, i, j):
        # base: if any immediate neighbor is 0, update the distance to 1 and stop recursion
        if i > 0 and mat[i-1][j] == 0:
            return 1
        if i < self.m-1 and mat[i+1][j] == 0:
            return 1
        if j > 0 and mat[i][j-1] == 0:
            return 1
        if j < self.n-1 and mat[i][j+1] == 0:
            return 1
        
        # taking the distances of 4 directions(represnting infinity)
        top, left, bottom, right = 9999, 9999, 9999, 9999
        # here we are going top-down, so if the top values are already calculated we can reuse them
        # top
        if i > 0 and self.result[i-1][j] != 0:
            top = self.result[i-1][j]
        # left
        if j > 0 and self.result[i][j-1] != 0:
            left = self.result[i][j-1]
        
        # for right and bottom we are computing using DFS
        # right
        if j < self.n-1:
            if self.result[i][j+1] == 0:
                self.result[i][j+1] = self.dfs(mat, i, j+1)
            right = self.result[i][j+1]
        # bottom
        if i < self.m-1:
            if self.result[i+1][j] == 0:
                self.result[i+1][j] = self.dfs(mat, i+1, j)
            bottom = self.result[i+1][j]
        
        return 1+ min(top, min(left, min(bottom, right)))

'''
Time Complexity: O(m*n)
In worst case if all the cells are 1, time taken to go through each cell is m*n
Space Complexity: O(m*n)
In worst case if all the cells are 1, maximum stack space used by the tree is m*n
'''