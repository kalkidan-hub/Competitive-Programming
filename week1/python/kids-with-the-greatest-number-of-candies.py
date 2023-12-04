class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_so_far = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= max_so_far:
                res.append(True)
            else:
                res.append(False)
        
        return res
        