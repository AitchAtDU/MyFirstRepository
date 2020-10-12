#Making Linked lists using object oriented programming

class ListNode():
    def __init__(self,data,pointer):
        self.Data = data
        if pointer:
            self.Pointer = pointer
        else:
            pointer = "Null"
    
    def __str__(self):
        return self.Data

class LinkedList():
    def __init__(self,head):
        self.Head = head
        self.Tail = head
        self.Size = 0
    
    

def createLinkedList(headData):
    headNode = ListNode(headData,None)
    return LinkedList(headNode)



