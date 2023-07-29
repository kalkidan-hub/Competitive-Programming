from collections import Counter, List
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        freq = Counter(nums)
        res = []
        try:
            where_about = nums.index(target)
        except:
            where_about = -1
        if where_about != -1:
            res = [where_about + i for i in range(freq[target])]
        
        return res