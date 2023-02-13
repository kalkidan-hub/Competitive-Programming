import collections
import sys
class Solution:
    ## a solution with an inefficient performance time
    def shortestSubarray0(self, nums, k: int) -> int:
        if len(nums) == 0 and k != 0:
            return -1
        summ = 0
        subarray = []
        
        for i in nums:

                summ += i 
                if summ < k:
                    subarray += [i]
                    
                    continue
                else:
                    subarray += [i]
                    break
        kk = sum(subarray)
        if kk < k:
            return -1
        else:
            while kk > k:
                if kk - subarray[0] >= k:
                    subarray = subarray[1:]
                kk = sum(subarray) 
            return len(subarray)
    def shortestSubarray(self, nums, k: int) -> int:
        sums = [0] * (len(nums)+1)
        for i in range(1,(len(nums)+1)):
            sums[i] = nums[i-1] + sums[i-1]       
        ## produces cumulative sum of the nums array
        result = sys.maxsize
        q = collections.deque()
        for right, s in enumerate(sums):
            while q and s <= sums[q[-1]]:
                q.pop()
            while q and s - sums[q[0]] >= k:
                result = min(result,right-q.popleft())
            q.append(right)
        if result == sys.maxsize: return -1
        return result


