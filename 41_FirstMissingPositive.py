class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count,data = 1,{}
        for i in nums:
            if i < 0:pass
            elif i == count:
                data[i] = 1
                while data.get(count) != None:count += 1
            elif i > 0 and i != count:
                data[i] = 1
                pass        
        return count
