class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res, after,piv = [],[],[]
        for num in nums:
            if num < pivot:
                res.append(num)
            elif num == pivot:
                piv.append(num)
            else:
                after.append(num)
            
        while piv:
            res.append(piv.pop())
        while after:
            res.append(after.pop(0))
        
        return res

