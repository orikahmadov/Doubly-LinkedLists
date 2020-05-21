class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None
        self.prev =  None

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def push(self,NewValue):
        NewNode = Node(NewValue)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def Print(self,node):
        while node is not None:
            print(node.data),
            last  = node
            node = node.next


Family =  DoublyLinkedList()
Family.push("Sadig Ahmadov")
Family.push("Orkhan Ahmadov")
Family.push("Sanan Ahmadov")

Family.Print(Family.head)