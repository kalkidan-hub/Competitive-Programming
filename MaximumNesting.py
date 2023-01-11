def maxNestingDepth(s: str) -> int:
    #Given a VPS represented as string s, return the maximum nesting depth of 
    """
    "(1)+((2))+(((3)))"
    s = [((]
    depth = 1,2 3

    "(1+(2*3)+((8)/4))+1"



    #"((1*(5+6))*(8/6))"
    """
    """  
    stack = []
    ct = 0
    maxDepth = 0
    justPop = None
    for i in s:
        if i == '(':
            if justPop:
                maxDepth += len(stack)
            stack.append(i)
            ct = 0
            justPop = False
            
        elif i == ')':
            justPop = True
            stack.pop()
            ct += 1
            
        maxDepth = max(maxDepth, ct)

    print (maxDepth)

    return maxDepth
"""
    open = 0
    max_depth = 0
    for char in s:
        if char == '(':
            open += 1
        elif char == ')':
            open -= 1 
        max_depth = max(max_depth,open)
    return max_depth
# print(maxNestingDepth("(1+(2*3)+((8)/4))+1"))