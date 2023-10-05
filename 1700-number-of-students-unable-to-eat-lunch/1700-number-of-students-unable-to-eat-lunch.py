class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # actually performing the operation
        st = Counter(students)
        res = len(students)
        
        while  res and (not(st[0] == 0 and sandwiches[0] == 0) and not(st[1] == 0 and sandwiches[0] == 1)):
            if students[0] == sandwiches[0]:
                res -= 1
                curr = students.pop(0)
                st[curr] -= 1
                sandwiches.pop(0)
            else:
                que_end = students.pop(0)
                students.append(que_end)
        
        return res