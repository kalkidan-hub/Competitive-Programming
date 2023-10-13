class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prf_sum = [0]
        for i in gain:
            prf_sum.append(prf_sum[-1] + i)
        return max(prf_sum)