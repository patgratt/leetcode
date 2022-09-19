allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]

def countConsistentStrings(allowed, words):
    allowed = set(allowed)
    count = 0

    for word in words:
        for letter in word:
            if letter not in allowed:
                count += 1
                break
    
    return len(words) - count

print(countConsistentStrings(allowed1, words1))



