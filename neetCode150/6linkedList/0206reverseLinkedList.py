# Define node for a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev