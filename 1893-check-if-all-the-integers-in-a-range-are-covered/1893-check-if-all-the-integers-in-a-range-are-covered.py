class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums = []
        for i in ranges:
            k = i[0]
            while k <= i[1]:
                nums.append(k)
                k += 1
        
        for i in range(left,right + 1):
            if i not in nums:
                return False
        
        return True
        
    
                
            
        
        
        return 0