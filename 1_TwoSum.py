class Solution(object):
    def twoSum(self, nums, target):
        x = []
        for i in range(len(nums)):
            if target - nums[i] in x:
                return [x.index(target - nums[i]), i]
            x.append(nums[i])
