class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while True:
            if not sandwiches: return 0
            if sandwiches[0] == students[0]:
                sandwiches.popleft()
                students.popleft()
            else:
                students.rotate(-1)
            count = Counter(students)
            if len(count) == 1:
                if list(dict(count).keys())[0] != sandwiches[0]:
                    return list(dict(count).values())[0]
                
            
