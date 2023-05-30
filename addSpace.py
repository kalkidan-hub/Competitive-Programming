from collections import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        spaces = [0] + spaces
        for i in range(len(spaces)-1):
            words.append(s[spaces[i]:spaces[i+1]])
        words.append(s[spaces[i + 1]:])
        print(words)  
        return ' '.join(words)