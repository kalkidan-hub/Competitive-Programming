class Solution: 
    def select(self, arr, i):
        # code here 
        min_val, idx = arr[i], i
        for k in range(i+1,len(arr)):
            if arr[k] <= min_val:
                min_val, idx = arr[k], k
        return idx
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            selected = self.select(arr,i)
            arr[i], arr[selected] = arr[selected], arr[i]
        
        return arr