'''
In this problem we need to update the color of given pixel with gieven color, and also the adjacent pixels if they have same color
Here I am using DFS approach to solve this problem, we start at the given index and change its color and check its neighbors if any of them is same color as the original color we change its color
After changing the color we check the neighbors of current pixel if they have same color we change its color.
If none of the neighbors have the same color, we go back to parent pixel where we started. Once all the pixel values are updated recursion ends. 
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])
        dirs = [[-1,0], [1,0], [0, 1], [0, -1]]
        # saving the original color
        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        self.dfs(image, sr, sc, color, originalColor, dirs)
        return image

    def dfs(self, image, r, c, color, originalColor, dirs):
        # base: out of bound or pixel color is not same as the original clor
        if (r < 0 or c < 0 or r == len(image) or c == len(image[0]) or image[r][c] != originalColor): return
        
        # logic
        image[r][c] = color
        # finding the neighboring coordinates and calling dfs recursively
        for dir in dirs:
            newRow = r + dir[0]
            newCol = c + dir[1]
            self.dfs(image, newRow, newCol, color, originalColor, dirs)

'''
Time Complexity: O(m*n)
In worst case we iterate on each of the element in the grid once.
Space Complexity: O(m*n)
In worst case we need m*n space, space taken by recursive tree is equal to the height of the tree.
'''