def wiggleSort(nums) -> None:
    nums.sort()
    mid = len(nums)//2
    
    first = nums[:mid]
    second = nums[mid:]
    # first.reverse()
    
    
    
    nums = []
    while first and second:
        nums.append(first.pop())
        nums.append(second.pop())
    if first:
        nums.append(first.pop())
    if second:
        nums.append(second.pop())
        
    print(nums) # well a working one, but not inplace operation...


def wiggleSort2(nums):
    nums_copy = nums.copy()
    nums_copy.sort()
    
    l, r = (len(nums) - 1)//2, len(nums) - 1
    
    for i in range(len(nums)):
        
        if i%2 == 0:
            nums[i] = nums_copy[l]
            l -= 1
        else:
            nums[i] = nums_copy[r]
            r -= 1