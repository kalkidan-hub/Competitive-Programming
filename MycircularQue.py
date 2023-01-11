class MyCircularDeque:
  
    def __init__(self, k: int):
        self.deque = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.isEmpty():
            self.deque += [value]
            return True
        
        if len(self.deque) < self.size:
            for i in range(len(self.deque)):
                curr = self.deque[i]
                self.deque[i] = value
                value = curr
            self.deque += [value]
            return True
        elif self.isFull():
            return False
    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.size:
            self.deque += [value]
            return True
        return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque = self.deque[1:]
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque = self.deque[:len(self.deque)-1]

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.deque[-1]
            

    def isEmpty(self) -> bool:
        if len(self.deque) == 0:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.deque) == self.size:
            return True
        return False




if __name__ == "__main__":
    def printRes(lst1,lst2):
        obj = MyCircularDeque(lst2[0][0])
        result = [None]
        for i in range(1,len(lst1)):
            if lst1[i] == "insertFront":
                result += [obj.insertFront(lst2[i][0])]
            elif lst1[i] == "insertLast":
                result += [obj.insertLast(lst2[i][0])]
            elif lst1[i] == "deleteFront":
                result +=  [obj.deleteFront()]
            elif lst1[i] == "deleteLast":
                result +=  [obj.deleteLast()]
            elif lst1[i] == "getRear":
                result +=  [obj.getRear()]
            elif lst1[i] == "isEmpty":
                result +=  [obj.isEmpty()]
            elif lst1[i] == "isFull":
                result +=  [obj.isFull()]
        print(result)
            
   



