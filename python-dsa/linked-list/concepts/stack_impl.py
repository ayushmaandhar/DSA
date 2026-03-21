# implementing a stack using a singly linked list
# our goal implement a class that uses a s-l-l and has the following methods
# 1) push (add new number to top of the stack)
# 2) pop (remove the top element of the stack)
# 3) top (returns the value of the last entry in the stack)

# first we need a node class to implement a singly linked-List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# now we will implement the required Stack Class

class Stack:
    def __init__(self):
        # we need a head whose next will be the top of our stack
        self.head = Node()
    
    def push(self, num):
        second = self.head.next
        new_node = Node(num, second)
        self.head.next = new_node
    
    def pop(self):
        top = self.head.next
        if top is not None:
            self.head.next = top.next
        else:
            print("Stack is empty, can't pop")
    
    def top(self):
        top = self.head.next
        if top is not None:
            return top.val
        else:
            print("Stack is empty, no element at top")
            return None

stack = Stack() # []
stack.push(1) # [1]
stack.pop() # []
stack.push(2) # [2]
stack.push(3) # [3, 2]
stack.pop() # [2]
print(stack.top())

        
        