class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3
        for i in nums:
            colors[i] += 1
        
        color = 0
        l = 0
        for j in colors:
            for i in range(l,l+j):
                nums[i] = color
            l += j
            color += 1
            
                
        