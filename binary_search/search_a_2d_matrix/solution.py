from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        top = 0 
        bot = rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = matrix[(top + bot) // 2]

        left_pointer = 0
        right_pointer = len(row) - 1

        while left_pointer <= right_pointer:
            mid_pointer = (right_pointer + left_pointer) // 2

            if target > row[mid_pointer]:
                left_pointer = mid_pointer + 1
            elif target < row[mid_pointer]:
                right_pointer = mid_pointer - 1
            else:
                return True

        return False