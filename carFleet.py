class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorting the position given along wth the corresponding speed
        initial_posSpeed = []
        for i, j in zip(position, speed):
            initial_posSpeed += [[i,j]]
        initial_posSpeed.sort(reverse = True)
        #do time monotonicty
        max_time = (target - initial_posSpeed[0][0]) / initial_posSpeed[0][1]
        fleet = 1
        for i in range(1,len(initial_posSpeed)):
            time =  (target - initial_posSpeed[i][0]) / initial_posSpeed[i][1]
            if time > max_time:
                fleet += 1
                max_time = time

        #return fleet value
        return fleet