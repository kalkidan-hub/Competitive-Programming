class Solution:
    def compress(self, chars) -> int:
        a,b,space,count=0,0,[],0
        while b<len(chars):
            if chars[a]==chars[b]:
                b+=1
                count+=1
            elif chars[a]!=chars[b]:
                if count==1:
                    space.append(chars[a])
                else:
                    space.extend([chars[a]]+list(str(count)))
                a=b
                count=0
            # print(space)
        if count==1:
            space.append(chars[a])
        else:
            space.extend([chars[a]]+list(str(count)))
        # print(space)
            
        chars[:]=space           
        return len(chars)