class Solution:
    def average(self, salary: List[int]) -> float:
        _min = min(salary)
        _max = max(salary)
        total = 0

        for sal in salary:
            if sal != _min and sal != _max:
                total += sal
        average = total/(len(salary)-2)

        return average
            


