class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # prepare prefix_sum 
        
        pre_sum = [0]
        
        for i in nums:
            pre_sum.append(pre_sum[-1] + i) 
        # print(pre_sum)
        
        return 1 - min(pre_sum)