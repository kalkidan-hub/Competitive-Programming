class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # collect indexes of offending parenthesis, 
        stack = []
        for i in enumerate(s):
            if stack and i[1] == ')' and stack[-1][1] == '(':
                stack.pop()
            else:
                stack.append(i)
        
        # iterate over the offendigs to find the longest
        len_long = 0
        if not stack:
            return len(s)
        else:
            len_long = len(s) - stack[-1][0] - 1
            while len(stack) != 1:
                len_long = max(len_long,stack[-1][0] - stack[-2][0] - 1)
                stack.pop()
            
            len_long = max(len_long,stack[-1][0])
                
        
            
        return len_long