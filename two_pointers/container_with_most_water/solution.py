class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        left_pointer = 0
        right_pointer = len(heights) - 1

        while left_pointer < right_pointer:
            water_amount = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            if water_amount > max_water:
                max_water = water_amount

            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water