from typing import List

# O(n^2) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_1, value_1 in enumerate(nums):
            for index_2, value_2 in enumerate(nums[index_1 + 1:], start=index_1 + 1):
                if value_1 + value_2 == target:
                    return [index_1, index_2]


# O(n) solution two-pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, value in enumerate(nums):
            nums_map[value] = index
        
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in nums_map and nums_map[remainder] != index:
                return sorted([index, nums_map[remainder]])

# O(n) solution one-pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in nums_map:
                return sorted([index, nums_map[remainder]])
            nums_map[value] = index