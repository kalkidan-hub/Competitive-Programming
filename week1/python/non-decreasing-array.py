class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        fall,idx = 0,0
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                fall += 1
                idx = i + 1

        if fall == 1 and 1 < idx < len(nums) - 1:
            return nums[idx-1] <= nums[idx + 1] or nums[idx-2] <= nums[idx]
        return fall <= 1