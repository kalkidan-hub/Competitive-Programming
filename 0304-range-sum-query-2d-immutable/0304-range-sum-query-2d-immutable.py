class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.area_sum = []
        self.areaSum()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not row1 and col1:
            res = self.area_sum[row2][col2] - self.area_sum[row2][col1-1]
        elif not col1 and row1:
            res = self.area_sum[row2][col2] - self.area_sum[row1-1][col2]
        elif not row1 and not col1:
            res = self.area_sum[row2][col2]
        else:
            res = self.area_sum[row2][col2] - self.area_sum[row1-1][col2] - self.area_sum[row2][col1-1] + self.area_sum[row1-1][col1-1]
        
        return res
    
    def areaSum(self):
        
        for row in range(len(self.matrix)):
            sum_row = []
            if row:
                sum_row.append(self.area_sum[row-1][0] + self.matrix[row][0])
                for k in range(1,len(self.matrix[row])):
                    sum_row.append(sum_row[-1]+self.matrix[row][k] + self.area_sum[row-1][k]-self.area_sum[row-1][k-1])
            else:
                sum_row.append(self.matrix[row][0])
                for k in range(1,len(self.matrix[row])):
                    sum_row.append(sum_row[-1] + self.matrix[row][k])
            self.area_sum.append(sum_row)
            
            
            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)