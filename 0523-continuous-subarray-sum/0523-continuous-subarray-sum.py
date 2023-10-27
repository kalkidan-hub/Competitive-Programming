class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        prf_sum = [0]
        for i in nums:
            prf_sum.append(prf_sum[-1] + i)
        
        _map = {0:-1}
        prf_sum = prf_sum[1:]
        
        for i in range(len(prf_sum)):
            remainder = prf_sum[i] % k
            if (remainder) in _map and (i - _map[remainder]) >= 2:
                return True
            if remainder not in _map:
                _map[remainder] = i
            