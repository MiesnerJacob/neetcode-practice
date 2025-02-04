class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = "".join([str(i) for i in digits])
        increment = int(str_digits) + 1
        return [int(i) for i in list(str(increment))]