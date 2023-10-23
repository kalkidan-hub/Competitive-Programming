class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # oddifying distance, 
        original_range = list(range(1,n+1))
        initial_distance = 2
        
        def divideByDistance(_range,distance):
            if len(_range) <= 2:
                return _range
            
            left_part = []
            right_part = []
            
            lefty = _range[0] % distance
            righty = _range[1] % distance
            for i in _range:
                if i % distance == lefty:
                    left_part.append(i)
                elif i % distance == righty:
                    right_part.append(i)
            
            return divideByDistance(left_part,distance * 2) + divideByDistance(right_part,distance * 2)
        
            
        return divideByDistance(original_range,initial_distance)
        