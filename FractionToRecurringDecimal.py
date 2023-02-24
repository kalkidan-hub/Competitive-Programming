def fractionToDecimal(numerator: int, denominator: int) -> str:
        # I think we gotta do long division, handle the negative numbers' cases as well
        if denominator == 0:
            return "undefined"
        if numerator == 0:
            return '0'
        negative = False
        if numerator < 0:
            numerator = -(numerator)
            negative = True
        if denominator < 0:
            denominator = -(denominator)
            negative = not negative


        firstPart = str(numerator//denominator)
        indexOfP = len(firstPart)
        if numerator%denominator != 0:
            firstPart += '.'
            rem = numerator%denominator
            remStory = [rem]
            while rem != 0:
                rem *= 10
                firstPart += str(rem // denominator)
                nextRem = rem%denominator
                rem = nextRem
                if nextRem in remStory:
                    repeatSince = remStory.index(nextRem)
                    
                    firstPart = firstPart[:(indexOfP + repeatSince+1)] + '(' + firstPart[(indexOfP + repeatSince+1):] + ')'
                    break
                else:
                    remStory += [nextRem]
        if negative:
            firstPart = '-' + firstPart
        return firstPart


print(fractionToDecimal(0,-5))
# fractionToDecimal(4,333)