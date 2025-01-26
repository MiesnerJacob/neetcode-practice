class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def duplicates_check(values):
            seen = set()
            for value in values:
                if value != ".":
                    if value in seen:
                        return False
                    seen.add(value)
            return True

        def valid_rows(board):
            for row in board:
                if not duplicates_check(row):
                    return False
            return True

        def valid_columns(board):
            for i in range(9):
                values = [row[i] for row in board]
                if not duplicates_check(values):
                    return False
            return True

        def valid_boxes(board):
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    values = [
                        board[r][c]
                        for r in range(box_row, box_row + 3)
                        for c in range(box_col, box_col + 3)
                    ]
                    if not duplicates_check(values):
                        return False
            return True
            

        if not valid_rows(board):
            return False
        if not valid_columns(board):
            return False
        if not valid_boxes(board):
            return False
        
        return True