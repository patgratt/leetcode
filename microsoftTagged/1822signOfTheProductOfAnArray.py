# my solution

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if self.prod(nums) > 0:
            return 1
        elif self.prod(nums) < 0:
            return -1
        else:
            return 0
            
    def prod(self, nums):
        p = 1
        for x in nums:
            p *= x
        return p

# testcase
solution = Solution()
print(solution.arraySign([-1,-2,-3,-4,3,2,1])) # 1

# better solution
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        ans = 1
        for x in nums: 
            if x == 0: return 0 
            if x < 0: ans *= -1
        return ans 

# testcase
solution = Solution()
print(solution.arraySign([-1,-2,-3,-4,3,2,1])) # 1