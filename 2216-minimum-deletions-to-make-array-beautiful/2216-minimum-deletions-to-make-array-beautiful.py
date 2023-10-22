class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        s_last = None
        s_len = 0
        ct = 0
        for i in range(len(nums)):
            
            if s_len & 1 and s_last == nums[i]:
                ct += 1
            else:
                s_last = nums[i]
                s_len += 1
                
        return ct if not s_len & 1 else ct + 1