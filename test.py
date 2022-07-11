# key = number we need to add up to target, value = index
def twoSum(nums, target):
        # key = number we need to add up to target, value = index
        hashmap = {}
        
        # loop thru
        for i, n in enumerate(nums):
            
            
            if n in hashmap:
                res = [i, hashmap.get(need)]
                return res
            hashmap[need] = i

nums1 = [2, 7, 11, 15]
target1 = 9

twoSum(nums1, target1)
