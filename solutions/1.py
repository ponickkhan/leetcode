# Two Sum

class Solution:
    def twoSum(self, nums, target):

        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

# Example

test = Solution()
nums = [2, 7, 11, 15]
target = 17
result = test.twoSum(nums,target)
print(result)
