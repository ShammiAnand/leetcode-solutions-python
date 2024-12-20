"""
For two strings s and t, we say "t divides s"
if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2,
return the largest string x such that x divides both str1 and str2.
"""


class Solution:
    def _does_divide(self, s: str, t: str) -> bool:
        """checks if t divides s"""
        if len(s) % len(t) == 0:
            q = int(len(s) / len(t))
            return t * q == s

        return False

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_len = min(len(str1), len(str2))

        ans = ""
        for i in range(1, min_len + 1):
            if str1[:i] == str2[:i]:
                if self._does_divide(str1, str1[:i]) and self._does_divide(
                    str2, str2[:i]
                ):
                    ans = str1[:i]
        return ans
