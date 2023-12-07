class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = set()
        for ran in ranges:
            cover.update(list(range(ran[0],ran[1]+1)))
        
        for i in range(left,right+1):
            if i not in cover:
                return False
        return True
