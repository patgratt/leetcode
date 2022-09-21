# implement the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp

    # prints current linked list in the form of a python list
    def printlist(self):
        temp = self.head
        output = []
        while temp:
            output.append(temp.val)
            temp = temp.next
        return output
    
    def reverseIterative(self, head):
        # solution uses three pointers, assume input = [1->2->3->null]
        prev = None # prev->null
        curr = head # curr->head (1)
        while curr: # we've reached the end of the list when curr->null
            temp = curr.next # temp->2, temp->3, temp->null
            # reverse step
            curr.next = prev # 1<-2, 2<-3, 3<-null
            prev = curr # prev->1, prev->2, prev->3
            curr = temp # curr->2, curr->3, curr->null, done
        return prev


    def reverseRecursive(self, head):
        # base case, if head is empty then we're looking at an empty list
        if not head: # this is only gonna execute if the test case they give us is trying to trick us by just giving us empty list
            return None
        newHead = head # since this executes each recursive call, it will save at the end of the list, which is the new head
        # this is really the base case, if this condition is false we're at the end of the list and it won't execute
        if head.next:
            newHead = self.reverseRecursive(head.next) # recursively call on the next node until we've reached the end
            head.next.next = head # reverse step
        head.next = None # after each recursive call sets 3->null, 2->null, 1->null, done

        return newHead

# ITERATIVE

# create example input linked list (test case)
my_ll = LinkedList()
my_ll.push(3)
my_ll.push(2)
my_ll.push(1)
print(f"Input Iterative = {my_ll.printlist()}")

# reverse iterative 
my_ll.head = my_ll.reverseIterative(my_ll.head)
print(f"Output Iterative = {my_ll.printlist()}")

# RECURSIVE

# create example input linked list (test case)
my_ll = LinkedList()
my_ll.push(3)
my_ll.push(2)
my_ll.push(1)
print(f"Input Recursive = {my_ll.printlist()}")

# reverse recursive
my_ll.head = my_ll.reverseRecursive(my_ll.head)
print(f"Output Recursive = {my_ll.printlist()}")