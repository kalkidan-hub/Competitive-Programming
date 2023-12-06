class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj = len(nums)//3
        freq = Counter(nums)
        res = []

        for num in freq:
            if freq[num] > maj:
                res.append(num)

        return res
