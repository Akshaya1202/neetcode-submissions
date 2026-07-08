class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxl = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                length = length+1
                maxl = max(maxl, length)
            else:
                length = 0
        return maxl
