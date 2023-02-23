def plusOne(digits):
    if digits[-1] != 9:
            digits[-1] += 1
            return digits
    if digits[-1] == 9:
        if len(digits) == 1:
            return [1,0]
        return plusOne(digits[:-1]) + [0]
 

print(plusOne([4,9]))
