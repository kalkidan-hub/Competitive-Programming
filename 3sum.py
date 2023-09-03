class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        
        res = []
        visited = set()
        for i in range(len(nums)-1):
            if nums[i] in visited: continue
            left, right = i + 1, len(nums)-1
            
            while left < right:
                
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == 0:
                    res.append([nums[i] ,nums[left],nums[right]])
                    
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                    right -= 1
                else:
                    if curr_sum < 0:
                        left += 1
                    else:
                        right -= 1
            visited.add(nums[i])                      
        
        return res
                