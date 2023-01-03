class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

'''
# Solution 1
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2

            if remaining in seen: #3
                return [i, seen[remaining]]  #4
            else:
                seen[value] = i  #5
'''