class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        idx_sum = len(list1) + len(list2)

        for i in range(len(list1)):
            if list1[i] in list2:
                idx_sum_n = i + list2.index(list1[i])
                if idx_sum_n == idx_sum:
                    res.append(list1[i])
                elif idx_sum_n < idx_sum:
                    idx_sum = idx_sum_n
                    while res:
                        res.pop()
                    res.append(list1[i])
      
        return res
