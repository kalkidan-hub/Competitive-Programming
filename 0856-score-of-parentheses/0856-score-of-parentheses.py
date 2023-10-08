class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score_so_far = []
        score = 0
        
        for p in s:
            if p == '(':
                score_so_far.append(score)
                score = 0
            else:
                score = score_so_far.pop() + max(score*2,1)
        
        return score