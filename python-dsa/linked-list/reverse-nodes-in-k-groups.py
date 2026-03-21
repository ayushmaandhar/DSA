from config import ListNode

head = ListNode()
head.create([2,4,5])

def sorted_string(string):
    arr = sorted(list(string))
    return "".join(arr)


print(sorted_string("anagram"))
print(sorted_string("nagaram"))





