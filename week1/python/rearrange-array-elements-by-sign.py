class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg,res = [],[],[]

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        for p,n in zip(pos,neg):
            res.append(p)
            res.append(n)
        
        return res 