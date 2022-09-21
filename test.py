# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
    
    def push(self, val):
        newhead = ListNode(val=val)
        newhead.next = self
        self = newhead
        return self

    def printlist(self):
        temp = self
        output = []
        while temp:
            output.append(temp.val)
            temp = temp.next
        return output

# build test case
exlist1 = ListNode(-4)
exlist1 = exlist1.push(0)
exlist1 = exlist1.push(2)
exlist1 = exlist1.push(3)