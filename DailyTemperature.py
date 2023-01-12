class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temp) 
        for indx, i in enumerate(temp):

            if not stack:
                stack.append([indx,i])
            else:
                if stack[-1][1] >= i:
                    stack.append([indx,i])
                    

                else:
                    
                    while stack and stack[-1][1] < i :
                        stack_last = stack.pop()
                        print(stack_last)
                        res[stack_last[0]] = indx - stack_last[0]  

                    
                    stack.append([indx,i])
        return res
                       