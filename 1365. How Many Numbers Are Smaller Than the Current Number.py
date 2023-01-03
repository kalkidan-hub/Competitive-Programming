class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lstCount=[]
        for i in nums:
            ct=0
            for j in nums:
                if j<i:
                    ct+=1
            lstCount+=[ct]
        return lstCount