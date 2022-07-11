s1 = "pwwkew" #3 - wke
s2 = "abcabcbb" #3 - abc

def lengthOfLongestSubstring(s):
    charSet = set()
    # left pointer
    l = 0
    res = 0
    
    # right pointer continuously scanning right so use in the for loop
    for r in range(len(s)):
        # if we find a duplicate, we remove everything from the set, since we've already recorded that sequece in res
        # we now move onto the next possible sequence
        while s[r] in charSet:
            charSet.remove(s[l])
            # this fininshes by moving the left pointer over
            l += 1
        # continue to add to the set to represent a currently valid sequence if we haven't found a duplicate yet
        charSet.add(s[r])
        res = max(res, r - l + 1)
    
    return res

lengthOfLongestSubstring(s1)