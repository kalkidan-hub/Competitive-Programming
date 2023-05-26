def missingNumber(nums: list[int]) -> int:
        checker = [0]*(len(nums) + 1)
        for i in nums:
            checker[i] = 'P'
        for j in range(len(checker)):
            if checker[j] == 0:
                return j