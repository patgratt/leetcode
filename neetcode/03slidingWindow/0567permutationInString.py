# test cases
#s1a, s2a = "ab", "eidbaooo" #true
#s1b, s2b = "ab", "eidboaoo" #false
s1c, s2c = "abc", "baxyzabc" #true

def checkInclusion(s1: str, s2: str) -> bool:
    # quick possibility check, len(s2) has to be >= len(s1) for a valid permutation to exist
    if len(s1) > len(s2):
                return False
    # initialize count arrays
    s1Count, s2Count = [0] * 26, [0] * 26
    # increment arrays, indices will represent chars with a having i=0 and z having i=25
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    matches = 0
    # check overall char count arrays and record matches 
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord("a")
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        index = ord(s2[l]) - ord("a")
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1
    return matches == 26

print(checkInclusion(s1c, s2c))