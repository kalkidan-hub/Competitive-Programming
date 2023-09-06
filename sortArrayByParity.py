from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # using two pointer
        l, r = 0, len(nums) - 1
        
        
        
        while l <= r:
            
          
            if not nums[l] & 1:
                l += 1
            elif nums[r] & 1:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        return nums
            