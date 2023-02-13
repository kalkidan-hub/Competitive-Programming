class Solution:
    def decodeString(self, s: str,decoded = "") -> str:
        for ind, i in enumerate(s):
            if i == '[':
                print(ind)
                numIndex = ind
                print(s[:numIndex])
                multiplier = int(s[:numIndex])
            if i == ']':
                finalIndex = ind 
                decoded += multiplier * s[numIndex:finalIndex + 1]
                break
        if ind < len(s)-1:
            self.decodeString(s[finalIndex + 1],decoded) 

        '''
        this function missed one basic property of the to be decoded string,
        which sententially is the possibility of the input might be as such [3a2[f]], here the inner should be decoded first, 
        which this code didn't handle and it seems it does't know how.         
        '''
        def decodeString(self, s:str):
            stack = []
            for c in range(len(s)):
                if s[c] != ']':
                    stack.append(s[c])
                else:
                    string = ''
                    num = ''
                    while stack[-1] != '[':
                        string = stack.pop() + string
                    stack.pop()
                    while stack and stack[-1].isdigit():
                        num = stack.pop() + num
                    stack.append(int(num) * string)
                    print(num)
            return "".join(stack)

