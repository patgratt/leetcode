target1 = 12
position1 = [10, 8, 0, 5, 3]
speed1 = [2, 4, 1, 1, 3]

def carFleet(target, position, speed):
    # create array of pairs from input arrays in from of [ [p, s] ]
    # this python zip function creates an iterator that pairs together two or more paramets 
    pair = [ [p, s] for p, s in zip(position, speed)]

    stack = []

    # sort our list of pairs, then iteratre thru them backwards
    # sorted function will sort by the first value in the pair
    for p, s in sorted(pair)[::-1]:
        # calculate time to finish and append to stack
        stack.append((target - p) / s)
        # check if stack has at least 2 cars, if not there's no need to compare
        # then, if time to finish for car2 (top of stack) is less than car1, pop it off
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


print(carFleet(target1, position1, speed1))
