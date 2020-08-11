# Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

nums = [2, 7, 11, 15]
target = 17
class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in m:
                m[num] = i
                #print(m)
            else:
                return [m[n], i]


# Example

test = Solution()
result = test.twoSum(nums,target)
print(result)
