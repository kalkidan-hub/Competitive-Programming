class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        MOD = 10**9 + 7
        
       # maintain monotonicly increasing stack
        min_stack = []
        record = {(i,elem): [1, len(arr) - i] for i, elem in enumerate(arr)} # element:[left,right]
        
        for i,elem in enumerate(arr):
            if not min_stack or min_stack[-1][1] < elem:
                if min_stack:
                    record[(i,elem)][0] = i - min_stack[-1][0] 
                min_stack.append((i, elem))
            else:
                while min_stack and min_stack[-1][1] >= elem:
                    last = min_stack.pop()
                    record[last][1] = i - last[0]
                if min_stack:
                    record[(i,elem)][0] = i - min_stack[-1][0]
                else:
                    record[(i,elem)][0] += i
                    
                min_stack.append((i, elem))
                    
        _sum = 0
        for i in record:
            _sum += i[1] * record[i][0] * record[i][1]
            
        return _sum % MOD