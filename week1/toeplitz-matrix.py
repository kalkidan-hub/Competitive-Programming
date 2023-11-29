class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            if i == 0:
                for k in range(len(matrix[0])):
                    
                    base = matrix[i][k]
                    j,l = k,i
                    print(base)
                    while l < len(matrix) and j < len(matrix[0]):
                        if  matrix[l][j] != base:
                            return False
                        j += 1
                        l += 1
            else:
                base = matrix[i][0]
                j = 0
                l = i
                while l < len(matrix) and j < len(matrix[0]):
                        if  matrix[l][j] != base:
                            return False
                        j += 1
                        l += 1
            
        return True