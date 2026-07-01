class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.ll = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.ll
        for i in range(index):
            curr = curr.next
        return curr.val

    def insertHead(self, val: int) -> None:
        self.ll = Node(val, self.ll)
        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.ll = Node(val)
            self.size += 1
            return
        # traverse self.size - 1 times
        curr = self.ll
        for i in range(self.size - 1):
            curr = curr.next
        curr.next = Node(val)
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.ll = self.ll.next
            self.size -= 1
            return True
        # traverse index - 1 times
        new_head = self.ll
        new_curr = new_head
        old_curr = self.ll
        for i in range(index - 1):
            new_curr = new_curr.next
            old_curr = old_curr.next
        old_curr = old_curr.next
        new_curr.next = old_curr.next
        self.ll = new_head
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        ans = [0] * self.size
        curr = self.ll
        for i in range(self.size):
            ans[i] = curr.val
            curr = curr.next
        return ans
