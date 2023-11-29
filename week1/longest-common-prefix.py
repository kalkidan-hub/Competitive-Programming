class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        upto = 200
        for st in strs:
            upto = min(upto,len(st)) 

        res = ""
        for i in range(upto):

            if all(st[i] == strs[0][i] for st in strs):
                res += st[i]
            else:
                break
        
        return res