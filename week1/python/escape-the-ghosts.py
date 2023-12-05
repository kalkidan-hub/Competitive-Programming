class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_dist = abs(ghost[0]-target[0]) + abs(ghost[1]-target[1])
            if ghost_dist <= dist:
                return False
        return True