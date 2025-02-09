import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_explore, max_explore = 1, max(piles)
        result = max_explore
            
        while min_explore <= max_explore:
            k = (min_explore + max_explore) // 2

            total_time = 0
            for pile in piles:
                total_time += math.ceil(float(pile) / k)
            if total_time <= h:
                result = k
                max_explore = k - 1
            else:
                min_explore = k + 1

        return result
