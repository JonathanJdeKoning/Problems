class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.h = SortedList()
        self.tasks = {}
        for uid, tid, p in tasks:
            self.h.add((p, tid, uid))
            self.tasks[tid] = (p,uid)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.h.add((priority, taskId, userId))
        self.tasks[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        oldp, olduid = self.tasks[taskId]
        self.h.discard((oldp, taskId, olduid))
        self.tasks[taskId] = (newPriority, olduid)
        self.h.add((newPriority, taskId, olduid))
        

    def rmv(self, taskId: int) -> None:
        p, u = self.tasks[taskId]
        self.h.discard((p, taskId, u))
        del self.tasks[taskId]

    def execTop(self) -> int:
        if not self.h: return -1
            
        p, tid, uid = self.h.pop()
        return uid

        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()