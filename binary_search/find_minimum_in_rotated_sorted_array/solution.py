from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:
            mid_pointer = (right_pointer + left_pointer) // 2

            if nums[mid_pointer] > nums[right_pointer]:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer

        return nums[left_pointer]