def minCost(colors: str, neededTime: list[int]) -> int:
    
    res = 0
    
    i = 0
    j = 0
    while i < len(neededTime) and j < len(neededTime):
        curr_total = 0
        curr_max = 0

        while j < len(neededTime) and colors[i] == colors[j]:
            curr_total += neededTime[j]
            curr_max = max(curr_max, neededTime[j])
            j += 1

        res += curr_total - curr_max
            
    return res

# testcases
c1 = "aabaa"
t1 = [1,2,3,4,1]
print(minCost(c1,t1))
c2 = "cddcdcae"
t2 = [4,8,8,4,4,5,4,2]
print(minCost(c2,t2))