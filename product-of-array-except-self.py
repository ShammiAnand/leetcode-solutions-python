"""
Given an integer array nums, return an array answer
such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        for i, _ in enumerate(nums):
            prefix.append(prefix[i] * nums[i])

        for i, item in enumerate(nums[::-1]):
            suffix.append(suffix[i] * item)

        suffix = suffix[::-1]

        ans = []
        for i, item in enumerate(nums):
            ans.append(prefix[i] * suffix[i + 1])

        return ans
