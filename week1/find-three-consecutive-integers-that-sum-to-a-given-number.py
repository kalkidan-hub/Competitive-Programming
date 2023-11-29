class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = []
        if not num % 3:
            center = num // 3
            res = [center - 1, center, center + 1]
        
        return res