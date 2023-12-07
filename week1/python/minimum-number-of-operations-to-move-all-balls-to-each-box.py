class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indices = [i for i in range(len(boxes)) if boxes[i] == '1']
        res = []

        for k in range(len(boxes)):
            val = sum([abs(k-idx) for idx in indices])
            res.append(val)

        return res