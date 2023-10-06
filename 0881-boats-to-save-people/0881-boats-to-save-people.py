class Solution:
    def numRescueBoats(self, peoples: List[int], limit: int) -> int:
        peoples.sort()
        l, r = 0, len(peoples) - 1
        ct = 0
        while l <= r:
            if peoples[l] + peoples[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            
            ct += 1
        return ct