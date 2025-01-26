from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left_pointer = index + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                three_sum = value + nums[left_pointer] + nums[right_pointer]

                if three_sum < 0:
                    left_pointer += 1
                elif three_sum > 0:
                    right_pointer -= 1
                else:
                    output.append([value, nums[left_pointer], nums[right_pointer]])

                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                        right_pointer -= 1

                    left_pointer += 1
                    right_pointer -= 1

        return output