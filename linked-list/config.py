# helper class for all files in the folder
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # displays the object which call this method, no parameter required
    def display(self):
        curr = self
        while curr:
            print(curr.val, end="->")
            curr = curr.next
        print(curr)
    
    # this method updates the object that calls it
    def create(self, arr):
        n = len(arr)
        i = 1
        curr = self
        curr.val = arr[0]
        while i < n:
            curr.next = ListNode(arr[i])
            curr = curr.next
            i += 1

        