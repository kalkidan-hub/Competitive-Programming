class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # maintain monotonicity, frequency and visited status
        
        stack = []
        freq = Counter(s)
        freq = {i:[freq[i],False] for i in freq}
        
        for i in s:
            if not freq[i][1]:
                if (not stack) or stack[-1] < i:
                    
                    stack.append(i)
                    freq[i][0] -= 1
                    freq[i][1] = True
                elif stack[-1] > i:

                    while stack and freq[stack[-1]][0] and stack[-1] > i:
                        freq[stack.pop()][1] = False
                    
                    stack.append(i)
                    freq[i][0] -= 1
                    freq[i][1] = True
            else:
                freq[i][0] -= 1
    
        
        
        return "".join(stack)
            