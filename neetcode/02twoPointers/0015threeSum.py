def threeSum(nums):

    res = []
    nums.sort()
    
    for i in range(len(nums)):
        ''' this checks if the num on this iteration is a duplicate, i.e. we've 
            seen it before so we don't want to waste our time checking again '''
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_sum = (nums[i] + nums[l] + nums[r])
            # sum is too small, increment left pointer
            if curr_sum < 0:
                l += 1
            # sum is too small, increment left pointer
            elif curr_sum > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                # keep scan going, could be another valid 3sum using this num
                l += 1
                # also need to make sure once again that we're not using a duplicate 
                #while nums[l] == nums[l - 1] and l < r:
                #       l += 1
    return res

# test cases
testcase1 = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]
print(threeSum(testcase1))

testcase2 = [0,0,0,0] # [0,0,0,0]
print(threeSum(testcase2))

# TC: O(nlogn) + O(n^2) = O(n^2)