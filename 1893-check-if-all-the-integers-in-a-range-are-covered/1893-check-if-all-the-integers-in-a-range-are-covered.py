class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        _map = [0]*60
        
        for i in ranges:
            _map[i[0]] += 1
            _map[i[1] + 1] -= 1
        
        for k in range(1,len(_map)):
            _map[k] += _map[k-1]
        
        if _map[left:right + 1]:
            return min(_map[left:right + 1]) >= 1
        