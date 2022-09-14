def generateParentheses(n):

    # this stack will be used to build up possible combos
    stack = []
    # res stack that we'll return
    res = []

    # recursive function
    def backtrack(openN, closedN):
        # base case, we have a "well formed parentheses"
        if openN == closedN == n:
            res.append("".join(stack))

        # we still have room to add an open
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        # we still have room to add closed
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0,0)
    return res

print(generateParentheses(3))