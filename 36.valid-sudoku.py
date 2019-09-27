#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
class Solution:
    valid_nums = {'1','2','3','4','5','6','7','8','9','.'}

    def checkHorizontal(self, board):
        for row in board:
            seen_in_row = {}
            for cell in row:
                if cell in seen_in_row or cell not in self.valid_nums:
                    return False

                if cell != '.':
                    seen_in_row[cell] = None

        return True

    def checkVertical(self, board):
        for i in range(0,9):
            seen_in_col = {}
            for j in range(0,9):
                if board[j][i] in seen_in_col or board[j][i] not in self.valid_nums:
                    return False

                if board[j][i] != '.':
                    seen_in_col[board[j][i]] = None

        return True

    def checkGroups(self, board, x_of_top_left, y_of_top_left):
        seen_in_group = {}
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i+x_of_top_left][j+y_of_top_left] in seen_in_group or board[i+x_of_top_left][j+y_of_top_left] not in self.valid_nums:
                    return False

                if board[i+x_of_top_left][j+y_of_top_left] != '.':
                    seen_in_group[board[i+x_of_top_left][j+y_of_top_left]] = None

        return True        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = self.checkHorizontal(board)
        vertical = self.checkVertical(board)
        groups = 0
        groups = groups + 1 if self.checkGroups(board, 0, 0) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 3, 0) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 6, 0) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 0, 3) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 3, 3) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 6, 3) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 0, 6) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 3, 6) else groups + 0
        groups = groups + 1 if self.checkGroups(board, 6, 6) else groups + 0

        if horizontal and vertical and groups == 9:
            return True
        else:
            return False
            

