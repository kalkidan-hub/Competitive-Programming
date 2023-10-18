class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        total = 0
        for i in w:
            total += i
            self.w.append(total)
        self.total = total
    def pickIndex(self) -> int:
        rnd = random.randint(1,self.total)
        for idx, weight in enumerate(self.w):
            if rnd <= weight:
                return idx
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()