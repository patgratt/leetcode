def dailyTemperatures(temperatures):
    # initialize res array with default values of zero
    res = [0] * len(temperatures)

    stack = [] # pair: [temp, index]

    # iteratre thru temperatures array
    for i, t in enumerate(temperatures):
        # while stack is not empty and the temp we're checking is greater than the temp on the top of the stack
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t, i])
    return res

temp1 = [73,74,75,71,69,72,76,73] # output = [1,1,4,2,1,1,0,0])
print(dailyTemperatures(temp1)) 