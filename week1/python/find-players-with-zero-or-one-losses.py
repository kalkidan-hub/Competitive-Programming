class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = [match[0] for match in matches]
        lose = [match[1] for match in matches]

        s_lose = Counter(lose)
        absolute_win = [w for w in win if w not in s_lose]
        one_lose = [l for l in s_lose if s_lose[l] == 1]

        def refine(l):
            l = list(set(l))
            l.sort()
            return l
            
        absolute_win, one_lose = refine(absolute_win), refine(one_lose)

        return [absolute_win,one_lose]


