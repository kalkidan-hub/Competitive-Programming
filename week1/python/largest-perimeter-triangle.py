class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_perimeter = 0

        for i in range(len(nums)-3,-1,-1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                max_perimeter = nums[i] + nums[i + 1] + nums[i + 2]
                break

        return max_perimeter