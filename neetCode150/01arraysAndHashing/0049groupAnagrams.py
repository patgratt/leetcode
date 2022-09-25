from collections import defaultdict

def groupAnagrams(strs):
    # key = charCount, val = word(s)
    res = defaultdict(list)

    for word in strs:
        charCount = [0] * 26

        for letter in word:
            charCount[ord(letter) - ord('a')] += 1
        # in python lists cannot be keys but tuples can so use that instead
        res[tuple(charCount)].append(word)
    return list(res.values())



# test case
ex = ["eat","tea","tan","ate","nat","bat"] # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(ex))


# TC: O(n * m) where m is avg letters per string