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

    # prints both node and node.val as list of pairs
    def printlist(self):
        temp = self
        output = []
        while temp and len(output)<10:
            pair = [temp, temp.val]
            output.append(pair)
            temp = temp.next
        return output
        print(*output, sep = "\n")

# solution
def hasCycle(head: ListNode) -> bool:
    slow = head
    fast = head
    # have to check fast.next aswell since moves by two could be one short then loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# test case for normal linked list (no cycle)
normal_ll = ListNode(-4)
normal_ll = normal_ll.push(0)
normal_ll = normal_ll.push(2)
normal_ll = normal_ll.push(3)
print(f"Input Normal Linked List: {normal_ll.printlist()}")
# output
print(f"Test output for normal_ll = {hasCycle(normal_ll)}")


# test case for linked list with cycle = True
cycle_ll = ListNode(-4)
cycle_ll = cycle_ll.push(0)
cycle_ll = cycle_ll.push(2)
cycle_ll = cycle_ll.push(3)
cycle_ll.next.next.next.next = cycle_ll.next
print(f"Input Cycle Linked List: {cycle_ll.printlist()}")
# output
print(f"Test output for cycle_ll = {hasCycle(cycle_ll)}")




