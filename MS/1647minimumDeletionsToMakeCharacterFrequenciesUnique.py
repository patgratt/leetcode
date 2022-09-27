from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        
        res = 0
        cnt = list(Counter(s).values())
        seen = set()
        
        for x in cnt:
            while x > 0 and x in seen:
                x -= 1
                res += 1
            seen.add(x)
        
        return res