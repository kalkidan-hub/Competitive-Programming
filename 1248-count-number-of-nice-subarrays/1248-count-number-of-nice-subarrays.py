class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [i%2 for i in nums]
        ct = 0
        _dic = {0:1}
        prf_sum = [0]
        for i in nums:
            prf_sum.append(prf_sum[-1] + i)
            if prf_sum[-1] - k in _dic:
                ct += _dic[prf_sum[-1] - k]
            if prf_sum[-1] in _dic:
                _dic[prf_sum[-1]] += 1
            else:
                 _dic[prf_sum[-1]] = 1
        
        return ct