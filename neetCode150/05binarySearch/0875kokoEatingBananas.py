import math

# example test cases
piles1, h1 = [3, 6 ,7 ,11], 8 #k=4
piles2, h2 = [30,11,23,4,20], 5 #k=30
piles3, h3 = [30,11,23,4,20], 6 #k=23

def minEatingSpeed(piles,h):

    l = 1
    r = max(piles)

    while l <= r:
        k = (l + r) // 2
        h_temp = 0
        for pile in piles:
            h_temp += math.ceil(pile / k)

        if h_temp <= h:
            r = k - 1
        else:
            l = k + 1
    
    return k

print(minEatingSpeed(piles1, h1))
print(minEatingSpeed(piles2, h2))
print(minEatingSpeed(piles3, h3))
        

        


        







