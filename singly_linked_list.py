class _Node:
    def __init__(self, item: object, next: object = None):
        self._item = item
        self._next = next

class SinglyLinkedList:
    def __init__(self):
        self._head = None
    
    def __str__(self):
        s = "head->"

        curr_node = self._head
        while curr_node is not None:
            s += f"{curr_node._item}->"
            curr_node = curr_node._next

        s += "None"
        return s

    def add_to_front(self, item: object) -> None:
        new_node = _Node(item, self._head)
        
        if self._head is None:
            self._head = new_node
        else:
            new_node._next = self._head
            self._head = new_node

        
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.add_to_front(5)
    sll.add_to_front(7)
    print(sll)