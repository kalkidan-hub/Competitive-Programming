class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        n,m = len(matrix),len(matrix[0])

        curr = (0,0)
        Ii, Ij, Di, Dj = 0,1,0,0
        visited = set([(0,m),(n-1,-1),(n,m-1)])


        def where_next(Ii,Ij,Di,Dj):
            if Ij:
                Ii = 1
                Ij = 0
            elif Ii:
                Ii = 0
                Dj = 1
            elif Di:
                Di = 0
                Ij = 1
            elif Dj:
                Dj = 0
                Di = 1
            return Ii, Ij, Di, Dj
        def what_next(curr,Ii,Ij,Di,Dj):
            if Ij:
                _next = (curr[0], curr[1] + 1)
            if Ii:
                _next = (curr[0] + 1, curr[1])
            if Di:
                _next = (curr[0] - 1, curr[1])
            if Dj:
                _next = (curr[0], curr[1] - 1)
            return _next
            
        result = [] 
        while curr not in visited:
            result.append(matrix[curr[0]][curr[1]])
            _next = what_next(curr,Ii,Ij,Di,Dj)
            if _next in visited:
               
                Ii,Ij,Di,Dj = where_next(Ii,Ij,Di,Dj)
                _next = what_next(curr,Ii,Ij,Di,Dj)

            visited.add(curr)
            curr = _next

        return result

    