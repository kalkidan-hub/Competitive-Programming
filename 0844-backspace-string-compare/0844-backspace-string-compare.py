class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        
        for i in s:
            if i == '#' and not stack_s:
                continue
            if i == '#':
                stack_s.pop()
            else:
                stack_s.append(i)
        
        for j in t:
            if j == '#' and not stack_t:
                continue
            if j == '#':
                stack_t.pop()
            else:
                stack_t.append(j)
            
        
        return "".join(stack_s) == "".join(stack_t)