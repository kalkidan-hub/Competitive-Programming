def reverseParentheses(s):

    stack = []
    for char in s:
        if char != ')':
            stack.append(char)
            
        else:
            temp_s = ''
            stack_last=stack.pop()
            while stack_last != '(':
                temp_s += stack_last
                stack_last = stack.pop()
            for rev_string in temp_s:
                stack.append(rev_string)
            
    return ''.join(stack)