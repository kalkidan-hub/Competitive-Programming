class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res_s = ""
        alter = True
        for i in range(0,len(s),k):
            if alter:
                res_s += s[i:i+k][::-1]
            else:
                res_s += s[i:i+k]
            alter = not alter
            
        
        return res_s
    