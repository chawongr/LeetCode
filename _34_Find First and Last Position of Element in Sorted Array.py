class Solution(object):
    def searchRange(self, nums, target):
        first,last = -1,-1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:first = i
                last = i
        return [first, last]
