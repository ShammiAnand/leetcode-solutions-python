"""
You have a long flowerbed in which some of the plots are planted,
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        a = 0

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            a += 1
            flowerbed[0] = 1

        if len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            a += 1
            flowerbed[0] = 1

        if (
            len(flowerbed) >= 2
            and flowerbed[len(flowerbed) - 1] == 0
            and flowerbed[len(flowerbed) - 2] == 0
        ):
            a += 1
            flowerbed[len(flowerbed) - 1] = 1

        for i in range(len(flowerbed)):
            if (
                i > 0
                and i + 1 < len(flowerbed)
                and flowerbed[i] == 0
                and flowerbed[i - 1] == 0
                and flowerbed[i + 1] == 0
            ):
                a += 1
                flowerbed[i] = 1

        return a >= n
