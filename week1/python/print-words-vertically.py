class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        out_len = 0
        for word in words:
            if len(word) > out_len:
                out_len = len(word)
        output = ['' for _ in range(out_len)]
        for i in range(out_len):
            for w in words:
                if i < len(w):

                    output[i] += w[i]
                else:
                    output[i] += " "

        return [out.rstrip() for out in output]