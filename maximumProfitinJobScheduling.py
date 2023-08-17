class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = list(zip(startTime,endTime,profit))
        jobs.sort()
        
        @lru_cache(None)
        def dp(ind):
            if ind == n: 
                return 0
            next_job_at = ind + 1
            while next_job_at < n and jobs[next_job_at][0] < jobs[ind][1]:
                next_job_at += 1
            one = jobs[ind][2] + dp(next_job_at)
            two = dp(ind + 1)
            
            return max(one,two)
        return dp(0)