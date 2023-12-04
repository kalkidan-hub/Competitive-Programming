class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        total = 0

        for p1,p2 in zip(points[:-1],points[1:]):
            n, m = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
            total += (min(n,m) + abs(m-n)
)
        return total