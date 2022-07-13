class MinStack:

    def __init__(self):
        self.stack = []
        self.stackOfMins = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        # check if the val we're pushing is lower than current top of the min stack
        val = min(val, self.stackOfMins[-1] if self.stackOfMins else val)
        # push new min val to the top of the min stack
        self.stackOfMins.append(val)


    def pop(self) -> None:
        self.stack.pop()
        # have to pop off the min stack also, in case top val is min
        self.stackOfMins.pop()
        

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.stackOfMins[-1]



# MinStack object will be instantiated and called as such:
obj = MinStack()

obj.push(1)
obj.push(2)
obj.push(3)

obj.pop()

param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)