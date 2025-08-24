"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        def _get_list_for_row_num(row_num: int) -> list[int]:
            return [1] * row_num

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        resp = [[1], [1, 1]]

        for i in range(3, numRows + 1):
            temp = _get_list_for_row_num(i)

            for j, _ in enumerate(temp):
                if j - 1 >= 0 and j < len(resp[-1]):
                    temp[j] = resp[-1][j - 1] + resp[-1][j]

            resp.append(temp)

        return resp


# if __name__ == "__main__":
#     sol = Solution()
#     input = 5
#     print("input ", input)
#     output = sol.generate(input)
#     print("output ", output)
#     assert output == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
