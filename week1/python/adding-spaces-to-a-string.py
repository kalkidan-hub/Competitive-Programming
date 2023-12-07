class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        idx = 0
        for space in spaces:
            s = s[:space + idx] + ' ' + s[space + idx:]
            idx += 1
        return s