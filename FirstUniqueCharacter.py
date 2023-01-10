def firstUniqChar(s: str) -> int:
        reapChar=[]
        for i in range(len(s)):
            currChar=s[i]
            flag = True
            if currChar in reapChar:
                flag = False
                
            else:
                for j in range(i+1,len(s)):
                    if currChar == s[j]:
                        reapChar += [currChar]
                        flag = False
                        break
            if flag: 
                return i
        if flag == False:
            return -1


        