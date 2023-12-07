class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        remain = n%7
        total = ((7 + weeks) * weeks * 7) /2
        total += ((2*(weeks + 1) + remain - 1)*remain)/2

        return int(total)
