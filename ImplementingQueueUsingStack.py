class MyQueue:

    def __init__(self):
        self.queue=[]

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if len(self.queue)>=1:
            if len(self.queue)==1:
                the_peek=self.queue[0]
                self.queue=[]
                return the_peek
            the_peek=self.queue[0]
            self.queue=self.queue[1:]
            return the_peek
    def peek(self) -> int:
        if len(self.queue)>=1:
            return self.queue[0]
            

    def empty(self) -> bool:
        return (len(self.queue)==0)



def the_queue(operations:list,myQueue:list):
    list_result=[]
    q=MyQueue()
    for i in range(len(operations)):
        if operations[i]=='MyQueue':
            list_result+=[None]
        elif operations[i]=='push':
            q.push(myQueue[i][0])
            list_result+=[None]
        elif operations[i]=='pop':
            # q.pop()
            list_result+=[q.pop()]
        elif operations[i]=='peek':
            list_result+=[q.peek()]
        elif operations[i]=='empty':
            list_result+=[q.empty()]


    return list_result

