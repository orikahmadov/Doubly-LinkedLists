class Node:
    # Node class constructor 
    def __init__(self,data):
        self.data =  data
        self.next = None
        self.prev =  None

        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

#Class method used to add new data to the Node 
    def push(self,NewValue):
        NewNode = Node(NewValue)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
#Used for Printing the value 
    def Print(self,node):
        while node is not None:
            print(node.data),
            last  = node
            node = node.next

# Create new Head and Head will point to the node
Family =  DoublyLinkedList()
Family.Print(Family.head)
