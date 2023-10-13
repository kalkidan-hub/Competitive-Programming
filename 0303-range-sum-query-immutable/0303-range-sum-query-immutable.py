class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []
        self.prfixSum()
    def sumRange(self, left: int, right: int) -> int:
        # self.prfixSum()
        return self.prefix_sum[right+1] - self.prefix_sum[left]

    def prfixSum(self):
        self.prefix_sum.append(0)
        for i in range(len(self.nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + self.nums[i])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)