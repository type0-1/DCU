def reverse(nums):
    if len(nums) == 0:
        return nums
    return [nums[-1]] + reverse(nums[:-1])