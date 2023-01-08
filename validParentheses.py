class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        l=['(','[','{']
        i=0
        while i<len(s):
            if len(stack)==0 and s[i] not in l:
                return False

            if s[i] in l:
                stack.append(s[i])
            else:
                pop=stack.pop()
                if pop=='(' and s[i]==')':
                    pass
                elif pop=='[' and s[i]==']':
                    pass
                elif pop=='{' and s[i]=='}':
                    pass
                else: 
                    return False
            
      
            i+=1
        return len(stack)==0