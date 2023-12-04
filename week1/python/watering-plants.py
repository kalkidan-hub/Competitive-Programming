class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        steps = 0
        i = 0
        
        while i < len(plants):
            if plants[i] > cap:
                cap = capacity
                steps += (2 * i)
            
            cap -= plants[i]
            steps += 1

            i += 1
        return steps
