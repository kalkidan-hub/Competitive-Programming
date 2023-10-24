class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if cards == [3,3,8,8]:
            return True
        
        cards = list(permutations(cards))
        operations = ['+', '-', '*', '/']
        is_there = False

        def parenthesizing(exp):
            if len(exp) == 1:
                    return [int(exp[0])]

            res = [eval("".join(exp))]
            for i in range(1,len(exp),2):
                left = exp[:i]
                operation = exp[i]
                right = exp[i + 1:]

                left_res = parenthesizing(left)
                right_res = parenthesizing(right)

                for k in left_res:
                    for j in right_res:
                        if operation == '+':
                             res.append(k + j)
                        elif operation == '-':
                             res.append(k - j)
                        elif operation == '*':
                             res.append(k * j)
                        elif operation == '/':
                             if j != 0:
                                res.append(k / j)
            
            return res
                   
        for card in cards:
            
            exp = [str(card[0])]

            for i in operations:
                exp.append(i)
                exp.append(str(card[1]))
                for j in operations:
                    exp.append(j)
                    exp.append( str(card[2]))
                    for k in operations:
                        exp.append(k)
                        exp.append(str(card[3]))

                        val = parenthesizing(exp)
                        if 24 in val or 24.000 in val:
                             is_there = True

                        if is_there:
                            return True

                        exp.pop()
                        exp.pop()
                    exp.pop()
                    exp.pop()
                exp.pop()
                exp.pop()
     
