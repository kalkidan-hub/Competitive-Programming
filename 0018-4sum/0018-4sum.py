class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def twoSum(lst,t):
            # assum lst is sorted
            ans = []
            l, r = 0, len(lst) - 1
            while l < r:
                if lst[l] + lst[r] < t:
                    l += 1
                elif lst[l] + lst[r] > t:
                    r -= 1
                else:
                    ans.append([lst[l], lst[r]])
                    l += 1
                    r -= 1
            return ans
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                two_sumOrest = twoSum(nums[j + 1:],target - (nums[i] + nums[j]))
                if two_sumOrest:
                    for two in two_sumOrest:
                        add = two + [nums[i],nums[j]]
                        if add not in res:
                            res.append(add)
        
        return res