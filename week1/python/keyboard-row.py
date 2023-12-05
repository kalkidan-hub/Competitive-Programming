class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        one_row = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        one_line = []
        
        for word in words:
            word_low = word.lower()
            for row in one_row:
                if all(w in row for w in word_low):
                    one_line.append(word)
                    break

        return one_line