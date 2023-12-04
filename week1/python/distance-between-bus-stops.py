class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start,destination),max(start,destination)
        direct_dist = sum(distance[start:destination])
        return min(direct_dist, sum(distance) - direct_dist)
        