class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        c=0
        while((len(nums)-nums.count(0)-1)>=i):
            if nums[i]==0:
                nums.pop(i)
                c+=1
                i-=1
            i+=1
        for i in range(c):
            nums.append(0)