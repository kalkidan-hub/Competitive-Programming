from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        
        maxHeap = [[-ct,char] for char, ct in freq.items()]
        heapq.heapify(maxHeap)
        
        
        
        if -maxHeap[0][0] > ((len(s) + 1)/2) :
            return ""
        
        res = ""
        while len(maxHeap) >= 2:
            ct1, char1 = heapq.heappop(maxHeap)
            ct2, char2 = heapq.heappop(maxHeap)
            
            res += char1 + char2
            
            if ct1 + 1:
                heapq.heappush(maxHeap,[ct1 + 1,char1])
            if ct2 + 1:
                heapq.heappush(maxHeap, [ct2 + 1,char2])
        if maxHeap:
            res += maxHeap[0][1]
            
                    
        return res