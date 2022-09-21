# test case
tokens1 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] #22

def evalRPN(tokens: list[str]) -> int:
    stack = []

    for x in tokens:
        if x == "+":
            stack.append(stack.pop() + stack.pop())
        elif x == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif x == "*":
            stack.append(stack.pop() * stack.pop())
        elif x == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(x))
    return stack[0]


print(evalRPN(tokens1))