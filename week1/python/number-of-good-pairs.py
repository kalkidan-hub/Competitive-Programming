class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        good_pair = 0
        for val in freq:
            if freq[val] > 1:
                good_pair += math.factorial(freq[val])//(math.factorial(freq[val]-2)*2)
            
        return good_pair