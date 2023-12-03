class Solution:
    def freqAlphabets(self, s: str) -> str:
        number_to_letter = { i - ord('a') + 1: chr(i) for i in range(ord('a'), ord('z') + 1)}
        nums = []
        for n in s:
            if n == '#':
                dg1 = nums.pop()
                dg2 = nums.pop()
                nums.append(dg2 + dg1)
            else:
                nums.append(n)

        return "".join([number_to_letter[int(num)] for num in nums])
