class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        
        ans = len(nums) + 1
        window = 0
        l = 0
        for r in range(len(nums)):
            window += nums[r]
            
            while l <= r and total - window < x:
                window -= nums[l]
                l += 1
            if total - window == x:
                ans = min(ans,len(nums) - (r - l  + 1))
        
        return -1 if ans > len(nums) else ans