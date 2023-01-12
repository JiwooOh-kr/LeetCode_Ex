class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_val = 0
        sum_ls = []
        for num in nums:
            sum_val += num
            sum_ls.append(sum_val)
        return sum_ls

'''
# Solution 1
def runningSum(self, nums):
    i = 1
    while i<len(nums):
        nums[i]+=nums[i-1]
        i+=1
    return nums
'''