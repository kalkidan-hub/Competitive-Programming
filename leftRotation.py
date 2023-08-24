def rotateLeft(d, arr):
    # Write your code here
    d %= len(arr)
    idx = len(arr) - d - 1
    arr.reverse()
    
    arr = arr[idx::-1] + arr[:idx:-1]
    return arr

print(rotateLeft(2,[1,2,3,4,5]))