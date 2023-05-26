from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        for j in t:
            d[j] -= 1
        
        return all(e == 0 for e in list(d.values()))