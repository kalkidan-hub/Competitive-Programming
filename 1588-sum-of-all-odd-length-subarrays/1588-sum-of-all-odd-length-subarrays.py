class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prf_sum = [0]
        
        for i in arr:
            prf_sum.append(prf_sum[-1] + i)
            
        _sum = 0
        inc = 3
        
        while inc <= len(arr):
            for j in range(len(prf_sum) - inc):
                _sum += prf_sum[j + inc] - prf_sum[j] 
            
            inc += 2
        
        return _sum + prf_sum[-1]