from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_rain_water = 0

        left_pointer = 0
        right_pointer = len(height) - 1

        left_high = 0
        right_high = 0

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                if height[left_pointer] >= left_high:
                    left_high = height[left_pointer]
                else:
                    trapped_rain_water += left_high - height[left_pointer]
                left_pointer += 1
            else:
                if height[right_pointer] >= right_high:
                    right_high = height[right_pointer]
                else:
                    trapped_rain_water += right_high - height[right_pointer]
                right_pointer -= 1

        return trapped_rain_water