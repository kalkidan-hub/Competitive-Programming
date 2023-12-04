class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count = 0
        max_one = 0

        for num in nums:
            if num == 0:
                max_one = max(max_one,curr_count)
                curr_count = 0
            else:
                curr_count += 1
        
        return max(max_one,curr_count)