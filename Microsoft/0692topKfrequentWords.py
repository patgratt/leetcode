from collections import Counter

# SOLUTION 1 - brute force solution - TC: O(nlogn) - SC: O(n)
def topKFrequent(words: list[str], k: int) -> list[str]:
    # creates hashmap, key=word, value=count
    cnt = Counter(words)
    ''' sort firstly by count in decensing order, then alphabetically,
        return only first k elements '''
    return sorted(list(cnt.keys()), key=lambda x: (-cnt[x], x))[:k]

# testcase1
words1 = ["i","love","leetcode","i","love","coding"]
k1 = 2 # ans = ["i","love"]
print(topKFrequent(words1, k1))