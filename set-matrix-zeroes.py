"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        z_rows, z_cols = set(), set()
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == 0:
                    z_rows.add(i)
                    z_cols.add(j)

        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if i in z_rows or j in z_cols:
                    matrix[i][j] = 0


# if __name__ == "__main__":
#     sol = Solution()
#     input = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
#     print("input ", input)
#     sol.setZeroes(input)
#     print("output ", input)
