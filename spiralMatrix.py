class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def helper(start_row, end_row, start_col, end_col):
            if start_row > end_row or start_col > end_col:
                return []

            result = []
            for i in range(start_col, end_col + 1):
                result.append(matrix[start_row][i])

            for i in range(start_row + 1, end_row + 1):
                result.append(matrix[i][end_col])

            if start_row != end_row:
                for i in range(end_col - 1, start_col - 1, -1):
                    result.append(matrix[end_row][i])

            if start_col != end_col:
                for i in range(end_row - 1, start_row, -1):
                    result.append(matrix[i][start_col])

            result += helper(start_row + 1, end_row - 1, start_col + 1, end_col - 1)
            return result
        return helper(0, len(matrix) - 1, 0, len(matrix[0]) - 1)