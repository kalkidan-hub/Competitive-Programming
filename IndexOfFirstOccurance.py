def strStr(haystack: str, needle: str) -> int:
    
        i = j = 0
        

        while i < len(haystack) and j < (len(needle)):
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - j + 1
            else:
                j = 0
                
            i += 1        
        
        else:
            return -1

# amended
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack) + 1 - len(needle)):
            
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1

