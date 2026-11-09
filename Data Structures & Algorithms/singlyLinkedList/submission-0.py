from typing import List

class LinkedList:

    def __init__(self, data=None):
        self.data = data
        self.nxt = None
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        count = 0

        while temp:
            if count == index:
                return temp.data
            temp = temp.nxt
            count += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = LinkedList(val)
        new_node.nxt = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = LinkedList(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.nxt:
            temp = temp.nxt

        temp.nxt = new_node

    def remove(self, index: int) -> bool:
        if self.head is None or index < 0:
            return False

        if index == 0:
            self.head = self.head.nxt
            return True

        temp = self.head
        count = 0

        while temp.nxt:
            if count == index - 1:
                temp.nxt = temp.nxt.nxt
                return True

            temp = temp.nxt
            count += 1

        return False

    def getValues(self) -> List[int]:
        result = []
        temp = self.head

        while temp:
            result.append(temp.data)
            temp = temp.nxt

        return result
