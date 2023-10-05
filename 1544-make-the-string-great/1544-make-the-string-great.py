class Solution:
    def makeGood(self, s: str) -> str:
        goods = []
        # print(ord('a')-ord('A'))
        # print(ord('b')- ord('B'))
        
        for i in s:
            if not goods:
                goods.append(i)
            elif abs(ord(goods[-1]) - ord(i)) == 32:
                goods.pop()
            else:
                goods.append(i)
        return "".join(goods)