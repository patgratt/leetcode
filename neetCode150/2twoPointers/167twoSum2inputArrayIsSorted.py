# optimal solution: time = O(n), mem = O(1)

# test case
nums1, target1 = [1, 3, 4, 5, 7, 11], 9  # [3, 4] (remember it's 1-indexed)

def twoSum(nums, target):

    # let's not worry about the indexing fix that at the end
    l = 0
    r = len(nums) - 1

    # while pointers haven't crossed
    while l < r:
        # we've found two numbers that add up to target, return indexes (plus 1 bc 1-indexed_)
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        # if the sum is greater than target, move right pointer left bc we wan't a smaller sum
        # takes advantage of the array being sorted
        elif nums[l] + nums[r] > target:
            r -= 1
        # if too low, shift the pointer right
        elif nums[l] + nums[r] < target:
            l += 1

print(twoSum(nums1, target1))