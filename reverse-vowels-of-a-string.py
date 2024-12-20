"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear
in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = "aeiouAEIOU"
        vowels = []
        ans = ""

        for c in s:
            if c in VOWELS:
                vowels.append(c)
        for c in s:
            if c in VOWELS:
                ans += vowels.pop()
            else:
                ans += c
        return ans
