# test case
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [-3, 3, 4, -3, 1, 2]

def threeSum(nums):
    res = []
    nums.sort()

    for i, x in enumerate(nums):
        # this checks if the x value on this iteration is a duplicate, i.e. we've seen it before so we
        # don't want to waste our time checking again
        if i > 0 and x == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            curr_sum = x + nums[l] + nums[r]
            # sum is too small, increment left pointer
            if curr_sum < 0:
                l += 1
            # sum is too big, decrement right pointer
            elif curr_sum > 0:
                r -= 1
            # we found a valid threeSum
            else:
                # add all values to result array
                res.append([x, nums[l], nums[r]])
                # also need to increment left pointer to keep scan going
                l += 1
                # also need to make sure once again that we're not using a duplicate 
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

threeSum(nums1)