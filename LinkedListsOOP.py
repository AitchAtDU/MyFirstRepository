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


