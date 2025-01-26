class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            pointer_sum = numbers[left_pointer] + numbers[right_pointer]
            if pointer_sum > target:
                right_pointer -= 1
            elif pointer_sum < target:
                left_pointer += 1
            elif pointer_sum == target:
                return [left_pointer + 1, right_pointer + 1]
        
        return [None, None]