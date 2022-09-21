# define the linked list
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

# solution
def mergeTwoLists(list1, list2):

    dummy = ListNode()
    tail = dummy

    # break when one of the lists is empty
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail = list1
    if list2:
        tail = list2

    return dummy.next

# build test cases
exlist1 = ListNode(4)
exlist1 = exlist1.push(2)
exlist1 = exlist1.push(1)
print(f"Input List1 = {exlist1.printlist()}")

exlist2 = ListNode(4)
exlist2 = exlist2.push(3)
exlist2 = exlist2.push(1)
print(f"Input List1 = {exlist2.printlist()}")

res = mergeTwoLists(exlist1, exlist2)
print(f"Output = {res.printlist()}")