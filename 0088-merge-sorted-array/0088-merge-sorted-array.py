class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # append nums2 to nums1, 
        
        for i in range(m,m+n):
            nums1[i] = nums2[i - m]
        
        l, r,ct = 0, m, 0
        while r < (m + n):
            if nums1[l] >= nums1[r]:
                nums1[l], nums1[r] = nums1[r], nums1[l]
                ct += 1
            if l == r:
                r += 1
                l -= ct
                ct = 0
            l += 1
         