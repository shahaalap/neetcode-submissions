class DoublyLinkedList:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = DoublyLinkedList(), DoublyLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.count = 0
        self.capacity = capacity

        self.data = {}
        

    def movetoend(self, node):
        prevnode = node.prev
        nextnode = node.next

        prevnode.next = nextnode
        nextnode.prev = prevnode

        tailprev = self.tail.prev

        tailprev.next = node
        node.prev = tailprev
        node.next = self.tail
        self.tail.prev =  node

    def addtotail(self, node):
        tailprev = self.tail.prev

        tailprev.next = node
        node.prev = tailprev

        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        node = self.data[key]
        self.movetoend(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        node = None

        if key in self.data:
            node = self.data[key]
            node.value = value
            self.movetoend(node)
        else:
            node = DoublyLinkedList(key, value)
            self.data[key] = node
            self.count += 1
            self.addtotail(node)

        

        if self.count > self.capacity:
            nodetoberemoved = self.data[self.head.next.key]
            del self.data[self.head.next.key]
            self.count -= 1

            prev_node = nodetoberemoved.prev
            next_node = nodetoberemoved.next

            prev_node.next = next_node
            next_node.prev = prev_node

            
            


        

        

        


        
