class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prf_sum = [0]
        
        for i in nums:
            prf_sum.append(prf_sum[-1] + i)
        
        ans = [len(nums)]*len(queries)
        queries = [(queries[i],i) for i in range(len(queries))]
        queries.sort()
        
        one,two = 0,0
        while one < len(prf_sum) and two < len(queries):
            if prf_sum[one] > queries[two][0]:
                ans[queries[two][1]] = one - 1
                two += 1
            else:
                one += 1
            
        
        return ans