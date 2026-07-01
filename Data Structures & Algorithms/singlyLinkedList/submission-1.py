class LinkedList:
    
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.arr[index]

    def insertHead(self, val: int) -> None:
        self.size += 1
        new_arr = [0] * self.size
        new_arr[0] = val
        for i in range(self.size - 1):
            new_arr[i + 1] = self.arr[i]
        self.arr = new_arr

    def insertTail(self, val: int) -> None:
        self.size += 1
        new_arr = [0] * self.size
        for i in range(self.size - 1):
            new_arr[i] = self.arr[i]
        new_arr[self.size - 1] = val
        self.arr = new_arr

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        self.size -= 1
        new_arr = [0] * self.size
        for i in range(index):
            new_arr[i] = self.arr[i]
        for i in range(index + 1, self.size + 1):
            new_arr[i - 1] = self.arr[i]
        self.arr = new_arr
        return True

    def getValues(self) -> List[int]:
        return self.arr
        
