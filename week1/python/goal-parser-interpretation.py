class Solution:
    def interpret(self, command: str) -> str:
        out = ""
        i = 0
        while i < len(command): 
            if command[i] == 'G':
               out += 'G'
               i += 1
            elif command[i:i+2] == '()':
                out += 'o'
                i += 2
            elif command[i:i+4] == '(al)':
                out += 'al'
                i += 4
        return out
    
        


            