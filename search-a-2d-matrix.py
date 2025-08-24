"""
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_search(items: list[int], target: int) -> bool:
            left, right = 0, len(items) - 1
            while left <= right:
                mid = (left + right) // 2
                if items[mid] == target:
                    return True
                elif items[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        def flat_list_from(matrix: list[list[int]]) -> list[int]:
            flat = []
            for i in matrix:
                flat.extend(i)

            return flat

        return binary_search(flat_list_from(matrix), target)
