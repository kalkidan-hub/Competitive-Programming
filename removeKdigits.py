def removeKdigits(num: str, k: int) -> str:
    m_stack = []
    for i in num:
        i = int(i)
        if not m_stack or m_stack[-1] < i:
            m_stack.append(i)
        else:
            while (m_stack and m_stack[-1] > i) and k != 0:
                m_stack.pop()
                k -= 1
            m_stack.append(i)
    res = "".join([str(i) for i in m_stack])
    res = res[:len(res)-k].lstrip('0')
    return '0' if not res else res

# print(removeKdigits("1173",2))
