# test cases
n1 = 19 # true
n2 = 2 # false


def isHappy(n: int) -> bool:
    # create hashset
    visit = set()

    while n not in visit:
        visit.add(n)
        # compute cycle
        n = sumOfSquares(n)

        if n == 1:
            return True

    return False


def sumOfSquares(n: int) -> int:
    output = 0
    # while n > 0
    while n:
        # this gets us the ones digit
        digit = n % 10
        # square it
        digit = digit ** 2
        output += digit
        # this eliminates the ones place, continue loop
        n = n // 10
    return output

#print(isHappy(n1))
print(isHappy(n2))

