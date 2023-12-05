class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = [0]*len(s)
        for i,t in zip(range(len(s)),indices):
            shuffled[t] = s[i]
        return "".join(shuffled)