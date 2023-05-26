from collections import defaultdict

def twoSum2(nums,target):
    book = list(enumerate(nums))
    book.sort(key=lambda s:s[1])


    lo, hi = 0, len(book) - 1
    while lo < hi and book[lo][1] + book[hi][1] != target:
        if book[lo][1] + book[hi][1] < target:
            print(lo,hi)
            lo += 1
        else:
            hi -= 1
    return (book[lo][0] , book[hi][0])

def twoSum1(nums,target):
    book = defaultdict(int)

    for i in range(len(nums)):
        complement = target - nums[i]
        print(book)
        if nums[i] in book:
            return [i,book[nums[i]]]
        book[complement] = i

twoSum1([3,2,4],6)