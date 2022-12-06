class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            j=nums2.index(i)
            ct=0
            for k in nums2[j:]:
                if k>i:
                    if ct==0:
                        ans+=[k]
                        ct+=1
            if ct==0:
                ans+=[-1]
      
        return ans

