class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {j:i for i,j in enumerate(nums)}
        
        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in d and d[remainder] != index:
                return sorted([index, d[remainder]])
        
        return None