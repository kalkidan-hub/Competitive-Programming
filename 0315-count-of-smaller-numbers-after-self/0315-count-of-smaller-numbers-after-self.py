class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def bin_insertion(controller, val, start, end):
            if start == end:
                if val <= controller[start]:
                    return start, 0
                else:
                    return start + 1, 1
            if start > end:
                return start, 0
            mid = (start + end) // 2
            if controller[mid] < val:
                pos, count = bin_insertion(controller, val, mid + 1, end)
                return pos, count + mid - start + 1
            else:
                pos, count = bin_insertion(controller, val, start, mid - 1)
                return pos, count

        res = []
        controller = []

        for num in reversed(nums):
            _where, count = bin_insertion(controller, num, 0, len(controller) - 1)
            controller.insert(_where, num)
            res.append(count)

        return list(reversed(res))