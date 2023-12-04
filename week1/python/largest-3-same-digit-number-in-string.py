class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num)-2):
            # print(num[i:i + 3])
            _slice = num[i:i + 3]
            if len(set(_slice)) == 1:
                if res:
                    res = _slice if int(_slice) > int(res) else res
                else:
                    res = _slice

        return res