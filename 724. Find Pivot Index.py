class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        val = -1
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                val = i
                break
        return val


'''
# Solution 1
class Solution(object):
    def pivotIndex(self, nums):
        leftSum, rightSum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            rightSum -= ele
            if leftSum == rightSum:
                return idx 
            leftSum += ele
        return -1

# Solution 2
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total= sum(nums)
        temp = 0
        for i in range(len(nums)):
            if(nums[i] == total - 2*temp): 
                return i
            temp += nums[i]
        return -1
'''