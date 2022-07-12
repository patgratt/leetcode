# test cases
s1, k1 = "ABAB", 2 #4
s2, k2 = "AABABBA", 1 #4


def characterReplacement(s,k):
    res = 0
    # key = char, val = count
    count = {}
    max_freq = 0

    l = 0
    # slide over right pointer, increasing our window and scanning array
    for r in range(len(s)):
        # record counts of chars in hashmap
        count[s[r]] = 1 + count.get(s[r], 0)
        # record freq of whatever char we're using as the repeating char in our window 
        max_freq = max(max_freq, count[s[r]])

        # while our window is no longer valid (we would have to do more replacements than the k we are allowed)
        while ((r - l + 1) - max_freq) > k:
            # decrement the char at our left pointer as it is no longer part of our window
            count[s[l]] -= 1
            # move the left bound of our window over
            l += 1
        # update res to be the longest valid window we've seen
        res = max(res, (r - l + 1))
    return res

print(characterReplacement(s1,k1))
print(characterReplacement(s2,k2))
