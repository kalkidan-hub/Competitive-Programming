class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums = sorted(nums,key=lambda x:x[1])
        intersection = [0]*(nums[-1][1] + 2)
        
        for i in nums:
            intersection[i[0]] += 1
            intersection[i[1] + 1] -= 1
        for j in range(1,len(intersection)):
            intersection[j] += intersection[j-1]
        
        
        _intsec = 0
        for k in intersection:
            if k:  
                _intsec += 1 
        return _intsec