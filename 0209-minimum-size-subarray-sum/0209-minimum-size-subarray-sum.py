class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prf_sum = [0]
        for i in nums:
            prf_sum.append(prf_sum[-1] + i)
        
        _min = float('inf')
        i, j = 0, 0
        while j < len(prf_sum):
            if prf_sum[j] - prf_sum[i] >= target:
                _min = min(_min,j - i)
                i += 1
            else:
                j += 1
        
        return 0 if _min == float('inf') else _min