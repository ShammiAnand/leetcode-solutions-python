"""
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other,
append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        ans = ""

        for a, b in zip(word1, word2):
            ans += a + b

        if len(word1) != min_len:
            ans += word1[min_len:]

        if len(word2) != min_len:
            ans += word2[min_len:]

        return ans
