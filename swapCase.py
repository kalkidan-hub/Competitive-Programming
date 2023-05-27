def swapCase(s):
    res = ''

    for i in s:
        o = ord(i)

        if o >= 97 and o <= 122:
            i = chr(o -32)
        elif(o >= 65 and o <= 91) :
            i = chr(o + 32)
        res += i
    return res

print(swapCase('''HackerRank.com presents "Pythonist 2".'''))