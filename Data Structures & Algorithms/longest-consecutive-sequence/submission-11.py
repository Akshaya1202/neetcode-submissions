class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lseq = 0
        numSet = set(nums)
        for i in numSet:
            if i-1 not in numSet:
                length = 1
                while length+i in numSet:
                    length = length+1
                lseq = max(length,lseq)
        return lseq