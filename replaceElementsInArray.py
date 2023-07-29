from collections import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # thought dictionary access is better than list accessing, therefore
        
        book = dict(enumerate(nums))
        dictionarized_nums = {k:v for k,v in zip(book.values(),book.keys())}
        
        for i in operations:
            val = dictionarized_nums[i[0]]
            del dictionarized_nums[i[0]]
            dictionarized_nums[i[1]] = val
        
        final_res = sorted(dictionarized_nums, key = lambda x:dictionarized_nums[x])
        
        return final_res