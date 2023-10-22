class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a,b):
            a,b = min(a,b), max(a,b)
            while a != 0:
                a,b = b%a, a
            
            return b
        
        ct = 0
        nums = [str(i) for i in nums]
        for j in range(len(nums)):
            for k in range(j+1,len(nums)):
                if gcd(int(nums[j][0]),int(nums[k][-1])) == 1:
                       ct += 1
        
        return ct